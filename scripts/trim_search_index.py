#!/usr/bin/env python3
"""
后处理 mkdocs build 生成的 search_index.json，大幅精简索引以降低浏览器内存占用。

问题：12K 论文页面 × body text → 200+ MB JSON → lunr 内存索引 ~450 MB。
方案 v3：
  1. 去掉所有 body text
  2. text 字段只保留非会议标签（会议名已在 URL 路径中，lunr 会索引 location）
  3. 不注入双语同义词（改为客户端查询展开，见 main.html 中的 JS）
  4. 目标：lunr 内存 < 50 MB

用法: python scripts/trim_search_index.py [site_dir]
"""
import json
import re
import sys
from pathlib import Path

# 会议名模式，用于从 tags 中过滤掉会议标签（已在 URL 路径中，冗余索引）
_CONF_PATTERN = re.compile(
    r'^(ICLR|CVPR|ACL|NeurIPS|AAAI|ECCV|ICCV|ICML|EMNLP|NAACL)\s*\d{4}$',
    re.IGNORECASE,
)


def main():
    site_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("site")
    index_path = site_dir / "search" / "search_index.json"

    if not index_path.exists():
        print(f"ERROR: {index_path} not found")
        sys.exit(1)

    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    original_size = index_path.stat().st_size
    original_count = len(data["docs"])

    # 将同一页面的多个 section 合并为一个文档
    pages = {}  # location_base -> merged doc
    for doc in data["docs"]:
        loc = doc.get("location", "")
        base = loc.split("#")[0] if "#" in loc else loc
        title = doc.get("title", "").strip()
        tags = doc.get("tags", [])

        # Skip index/home pages
        base_clean = base.rstrip("/")
        if base_clean == "" or base_clean.count("/") < 2 or base_clean.endswith("index"):
            continue

        if base not in pages:
            pages[base] = {
                "location": base if base else loc,
                "title": title,
                "text": "",
                "_tags": set(),
            }
        else:
            merged = pages[base]
            if not merged["title"] and title:
                merged["title"] = title

        if tags:
            pages[base]["_tags"].update(tags)

    # 构建 text 字段：清空 body text，仅靠 title 搜索
    # tags 保留在 doc 中供 MkDocs UI 显示，但不放入 text 以减少 lunr 索引体积
    # (30K unique tags → 太多 tokens → lunr 倒排索引 100MB+)
    # 双语搜索通过客户端 Worker 拦截实现
    conf_removed = 0
    for doc in pages.values():
        all_tags = list(doc.pop("_tags"))
        # 过滤掉会议名标签
        filtered_tags = []
        for tag in all_tags:
            if _CONF_PATTERN.match(tag.strip()):
                conf_removed += 1
            else:
                filtered_tags.append(tag)

        if filtered_tags:
            doc["tags"] = filtered_tags
        # text 设为空，搜索仅匹配 title（lunr 也索引 title 字段）
        doc["text"] = ""

    data["docs"] = list(pages.values())

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    new_size = index_path.stat().st_size
    print(f"  ✓ search_index.json: {original_size/1024/1024:.2f} MB → {new_size/1024/1024:.2f} MB")
    print(f"    merged sections: {original_count} → {len(data['docs'])} docs")
    print(f"    removed {conf_removed} conference name tags (redundant with URL)")
    print(f"    bilingual search: handled client-side (no synonyms in index)")


if __name__ == "__main__":
    main()
