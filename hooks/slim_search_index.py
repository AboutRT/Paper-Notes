"""Post-build hook: slim down search_index.json for fast client-side search.

Strategy:
  1. Merge section-level entries (#anchor) into their parent page entry,
     keeping only one doc per page with a combined title.
  2. Clear all 'text' fields (title-only indexing).

This reduces ~230k entries / 262MB to ~13k entries / ~1-2MB.
"""

import json
import os
from collections import OrderedDict


def on_post_build(config, **kwargs):
    index_path = os.path.join(config["site_dir"], "search", "search_index.json")
    if not os.path.exists(index_path):
        return

    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = data.get("docs", [])
    if not docs:
        return

    original_count = len(docs)

    # Group docs by base page (location without #fragment)
    pages = OrderedDict()  # base_loc -> merged doc
    for doc in docs:
        loc = doc.get("location", "")
        base = loc.split("#")[0]

        if base not in pages:
            # First entry for this page: use as the base doc
            pages[base] = {
                "location": base,
                "title": doc.get("title", ""),
                "text": "",
            }
        else:
            # Subsequent section entry: append title if meaningful and short enough
            section_title = doc.get("title", "").strip()
            existing_title = pages[base]["title"]
            if (
                section_title
                and section_title not in existing_title
                and len(existing_title) < 300
            ):
                pages[base]["title"] += " | " + section_title

    slim_docs = list(pages.values())

    data["docs"] = slim_docs

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    new_size = os.path.getsize(index_path)
    print(
        f"[slim_search_index] {original_count} -> {len(slim_docs)} entries, "
        f"index size: {new_size / 1024 / 1024:.1f} MB"
    )
