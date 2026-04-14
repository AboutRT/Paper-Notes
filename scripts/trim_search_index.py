#!/usr/bin/env python3
"""
后处理 mkdocs build 生成的 search_index.json，大幅精简索引以降低浏览器内存占用。

问题：12K 论文页面 × 500 chars body → 14 MB JSON → lunr 内存索引 ~450 MB。
方案：只保留 title + tags，去掉所有 body text → ~1-2 MB JSON → lunr ~30 MB。
增强：注入中英文双语同义词，搜索"目标检测"也能匹配"object detection"。

用法: python scripts/trim_search_index.py [site_dir]
"""
import json
import re
import sys
from pathlib import Path

# ── 中英文双语映射（从 src/translate_tags.py 的 TAG_MAPPING 中提取并去重）──
# 格式：小写英文 → 中文。运行时会自动构建反向映射。
# 只保留有实际中文翻译的条目（排除保持原样的如 "training-free" → "training-free"）
_EN_TO_ZH: dict[str, str] = {
    # 学习范式
    "in-context learning": "上下文学习",
    "continual learning": "持续学习",
    "curriculum learning": "课程学习",
    "few-shot learning": "小样本学习",
    "few-shot": "小样本",
    "zero-shot": "零样本",
    "zero-shot generalization": "零样本泛化",
    "zero-shot learning": "零样本学习",
    "meta-learning": "元学习",
    "imitation learning": "模仿学习",
    "online learning": "在线学习",
    "active learning": "主动学习",
    "self-training": "自训练",
    "self-supervised": "自监督",
    "self-supervised learning": "自监督学习",
    "self-distillation": "自蒸馏",
    "multi-task learning": "多任务学习",
    "transfer learning": "迁移学习",
    "representation learning": "表示学习",
    "feature learning": "特征学习",
    "deep learning": "深度学习",
    "offline rl": "离线强化学习",
    "reinforcement learning": "强化学习",
    "contrastive learning": "对比学习",
    "knowledge distillation": "知识蒸馏",
    "semi-supervised learning": "半监督学习",
    "semi-supervised": "半监督",
    "unsupervised learning": "无监督学习",
    "federated learning": "联邦学习",
    # 训练/优化
    "fine-tuning": "微调",
    "pre-training": "预训练",
    "instruction tuning": "指令微调",
    "regularization": "正则化",
    "data selection": "数据选择",
    "data efficiency": "数据效率",
    "data curation": "数据整理",
    "dataset": "数据集",
    "dataset distillation": "数据集蒸馏",
    "synthetic data": "合成数据",
    "data attribution": "数据归因",
    "data augmentation": "数据增强",
    "training dynamics": "训练动态",
    "gradient flow": "梯度流",
    "gradient projection": "梯度投影",
    "bilevel optimization": "双层优化",
    "multi-objective optimization": "多目标优化",
    # 推理/思维链
    "reasoning": "推理",
    "reasoning efficiency": "推理效率",
    "inference efficiency": "推理效率",
    "spatial reasoning": "空间推理",
    "compositional reasoning": "组合推理",
    "counterfactual reasoning": "反事实推理",
    "visual reasoning": "视觉推理",
    "overthinking": "过度思考",
    "test-time scaling": "测试时缩放",
    "test-time compute": "测试时计算",
    "test-time adaptation": "测试时自适应",
    "inference-time scaling": "推理时缩放",
    "self-correction": "自我纠正",
    "self-consistency": "自一致性",
    "self-reflection": "自我反思",
    "self-improvement": "自我改进",
    "length generalization": "长度泛化",
    # LLM 相关
    "hallucination": "幻觉",
    "hallucination detection": "幻觉检测",
    "jailbreak": "越狱攻击",
    "jailbreak defense": "越狱防御",
    "safety alignment": "安全对齐",
    "alignment": "对齐",
    "reward model": "奖励模型",
    "process reward model": "过程奖励模型",
    "reward hacking": "奖励篡改",
    "red teaming": "红队测试",
    "instruction following": "指令遵循",
    "preference optimization": "偏好优化",
    "preference learning": "偏好学习",
    "speculative decoding": "推测解码",
    "long context": "长上下文",
    "knowledge editing": "知识编辑",
    "knowledge conflict": "知识冲突",
    "knowledge graph": "知识图谱",
    "model merging": "模型合并",
    "model editing": "模型编辑",
    "model collapse": "模型崩溃",
    "function calling": "函数调用",
    "tool use": "工具使用",
    "code generation": "代码生成",
    "text generation": "文本生成",
    "inference-time alignment": "推理时对齐",
    "content moderation": "内容审核",
    # Agent
    "multi-agent": "多智能体",
    "multi-agent system": "多智能体系统",
    "embodied ai": "具身智能",
    "embodied agent": "具身智能体",
    # 多模态/视觉
    "visual grounding": "视觉定位",
    "text-to-image": "文生图",
    "text-to-3d": "文生3D",
    "video generation": "视频生成",
    "video qa": "视频问答",
    "novel view synthesis": "新视角合成",
    "differentiable rendering": "可微渲染",
    "dynamic scenes": "动态场景",
    "egocentric vision": "第一人称视觉",
    "egocentric video": "第一人称视频",
    "motion generation": "运动生成",
    "stereo matching": "立体匹配",
    "autoregressive generation": "自回归生成",
    "autoregressive": "自回归",
    "temporal consistency": "时序一致性",
    "representation alignment": "表示对齐",
    "semantic alignment": "语义对齐",
    "missing modality": "缺失模态",
    "modality imbalance": "模态不平衡",
    "token merging": "令牌合并",
    "token reduction": "令牌缩减",
    "token efficiency": "令牌效率",
    # 安全/鲁棒/隐私
    "robustness": "鲁棒性",
    "adversarial robustness": "对抗鲁棒性",
    "adversarial attack": "对抗攻击",
    "adversarial examples": "对抗样本",
    "adversarial training": "对抗训练",
    "privacy": "隐私",
    "differential privacy": "差分隐私",
    "fairness": "公平性",
    "debiasing": "去偏",
    "bias mitigation": "偏差缓解",
    "gender bias": "性别偏差",
    "watermarking": "水印",
    # 可解释性
    "interpretability": "可解释性",
    "mechanistic interpretability": "机制可解释性",
    "explainability": "可解释性",
    "circuit discovery": "电路发现",
    "calibration": "校准",
    "confidence calibration": "置信度校准",
    # 数学/统计
    "generalization": "泛化",
    "distribution shift": "分布偏移",
    "distribution matching": "分布匹配",
    "optimal transport": "最优传输",
    "information bottleneck": "信息瓶颈",
    "information theory": "信息论",
    "mutual information": "互信息",
    "variational inference": "变分推断",
    "conformal prediction": "共形预测",
    "importance sampling": "重要性采样",
    "sample complexity": "样本复杂度",
    "sample efficiency": "样本效率",
    "uncertainty": "不确定性",
    "uncertainty estimation": "不确定性估计",
    "uncertainty quantification": "不确定性量化",
    "anomaly detection": "异常检测",
    "hypothesis testing": "假设检验",
    "score matching": "分数匹配",
    "influence function": "影响函数",
    "policy gradient": "策略梯度",
    "scalability": "可扩展性",
    "communication efficiency": "通信效率",
    "memorization": "记忆",
    "domain generalization": "领域泛化",
    # 模型架构
    "foundation model": "基础模型",
    "vision foundation model": "视觉基础模型",
    "generative model": "生成模型",
    "language model": "语言模型",
    "world model": "世界模型",
    "unified model": "统一模型",
    "concept bottleneck model": "概念瓶颈模型",
    "plug-and-play": "即插即用",
    "speech language model": "语音语言模型",
    # CV 任务
    "object detection": "目标检测",
    "3d object detection": "3D 目标检测",
    "semantic segmentation": "语义分割",
    "instance segmentation": "实例分割",
    "panoptic segmentation": "全景分割",
    "image segmentation": "图像分割",
    "point cloud": "点云",
    "depth estimation": "深度估计",
    "optical flow": "光流",
    "pose estimation": "姿态估计",
    "image restoration": "图像复原",
    "image generation": "图像生成",
    "image editing": "图像编辑",
    "image classification": "图像分类",
    "super-resolution": "超分辨率",
    "image super-resolution": "图像超分辨率",
    "video understanding": "视频理解",
    "action recognition": "动作识别",
    "visual question answering": "视觉问答",
    "image captioning": "图像描述",
    "text-to-video": "文生视频",
    "text-to-speech": "文本转语音",
    "speech recognition": "语音识别",
    "video editing": "视频编辑",
    "image inpainting": "图像修复",
    "denoising": "去噪",
    "change detection": "变化检测",
    "face recognition": "人脸识别",
    # 应用
    "autonomous driving": "自动驾驶",
    "remote sensing": "遥感",
    "robotic manipulation": "机器人操作",
    "sim-to-real": "仿真到现实",
    "machine translation": "机器翻译",
    "tabular data": "表格数据",
    "time series forecasting": "时间序列预测",
    "dense retrieval": "稠密检索",
    "medical image": "医学图像",
    "medical imaging": "医学影像",
    "motion planning": "运动规划",
    "trajectory prediction": "轨迹预测",
    # 压缩
    "model compression": "模型压缩",
    "model pruning": "模型剪枝",
    "quantization": "量化",
    "parameter-efficient fine-tuning": "参数高效微调",
    "parameter efficiency": "参数效率",
    # NLP
    "multilingual": "多语言",
    "cross-lingual transfer": "跨语言迁移",
    "cross-lingual": "跨语言",
    "text embedding": "文本嵌入",
    "multi-turn dialogue": "多轮对话",
    "multi-hop qa": "多跳问答",
    "question answering": "问答",
    "named entity recognition": "命名实体识别",
    "sentiment analysis": "情感分析",
    "text classification": "文本分类",
    "document understanding": "文档理解",
    "information extraction": "信息抽取",
    "relation extraction": "关系抽取",
    # 其他
    "domain adaptation": "域适应",
    "multi-modal": "多模态",
    "multi-modal learning": "多模态学习",
    "multimodal learning": "多模态学习",
    "cross-modal": "跨模态",
    "scene understanding": "场景理解",
    "scene generation": "场景生成",
    "point cloud completion": "点云补全",
    "graph neural network": "图神经网络",
    "neural architecture search": "神经架构搜索",
    "reward shaping": "奖励塑形",
    "label noise": "标签噪声",
    "noisy labels": "噪声标签",
    "out-of-distribution": "分布外",
    "open-vocabulary": "开放词汇",
    "visual localization": "视觉定位",
    "place recognition": "地点识别",
    "feature extraction": "特征提取",
    "feature alignment": "特征对齐",
    "feature fusion": "特征融合",
    "catastrophic forgetting": "灾难性遗忘",
    "survey": "综述",
    "evaluation": "评估",
    "personalization": "个性化",
    "diversity": "多样性",
    "causal inference": "因果推理",
    "causal discovery": "因果发现",
    "diffusion model": "扩散模型",
    "attention mechanism": "注意力机制",
    "one-step generation": "一步生成",
    "few-step generation": "少步生成",
    "low-resource": "低资源",
    "copyright protection": "版权保护",
    "deepfake detection": "深度伪造检测",
    "moment retrieval": "时刻检索",
    "event camera": "事件相机",
    "beam search": "束搜索",
    "weak-to-strong generalization": "弱到强泛化",
    "probabilistic forecasting": "概率预测",
    "inverse problems": "逆问题",
}

# 构建双向映射（中→英 + 英→中），用于给 tags/title 注入同义词
_BILINGUAL: dict[str, str] = {}
for _en, _zh in _EN_TO_ZH.items():
    if _en.lower() != _zh.lower():  # 排除保持原文的条目
        _BILINGUAL[_en.lower()] = _zh
        _BILINGUAL[_zh] = _en.lower()


def get_synonyms(text: str) -> list[str]:
    """为给定文本查找双语同义词。返回所有匹配到的对应语言词汇。"""
    synonyms = []
    text_lower = text.lower().strip()
    # 精确匹配
    if text_lower in _BILINGUAL:
        synonyms.append(_BILINGUAL[text_lower])
    return synonyms


def extract_conference_field(location: str) -> str:
    """从 URL 路径提取会议和领域信息作为可搜索文本。"""
    # location format: CONF/field/paper_name/
    parts = location.strip("/").split("/")
    if len(parts) >= 2:
        conf = parts[0].replace("_", " ")
        field = parts[1].replace("_", " ")
        return f"{conf} {field}"
    return ""


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

    # 将同一页面的多个 section 合并为一个文档，只保留 title + tags + 双语同义词
    pages = {}  # location_base -> merged doc
    for doc in data["docs"]:
        loc = doc.get("location", "")
        base = loc.split("#")[0] if "#" in loc else loc
        title = doc.get("title", "").strip()
        tags = doc.get("tags", [])

        # Skip index pages entirely
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
            if tags:
                pages[base]["tags"] = tags
        else:
            merged = pages[base]
            if not merged["title"] and title:
                merged["title"] = title

        # 收集所有 tags
        if tags:
            pages[base]["_tags"].update(tags)

    # 构建每个文档的 searchable text：会议+领域 + tags + 同义词
    synonym_count = 0
    for doc in pages.values():
        all_tags = list(doc.pop("_tags"))
        if all_tags:
            doc["tags"] = all_tags

        parts = []
        # 会议+领域
        meta = extract_conference_field(doc["location"])
        if meta:
            parts.append(meta)

        # tags 原文
        if all_tags:
            parts.extend(all_tags)

        # 为每个 tag 注入双语同义词
        seen_synonyms = set()
        for tag in all_tags:
            for syn in get_synonyms(tag):
                if syn not in seen_synonyms:
                    seen_synonyms.add(syn)
                    parts.append(syn)
                    synonym_count += 1

        # 为 title 中的关键短语注入同义词
        title_lower = doc["title"].lower()
        for en, zh in _EN_TO_ZH.items():
            if en in title_lower and zh not in seen_synonyms:
                seen_synonyms.add(zh)
                parts.append(zh)
                synonym_count += 1

        doc["text"] = " ".join(parts)

    data["docs"] = list(pages.values())

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    new_size = index_path.stat().st_size
    print(f"  ✓ search_index.json: {original_size/1024/1024:.2f} MB → {new_size/1024/1024:.2f} MB")
    print(f"    merged sections: {original_count} → {len(data['docs'])} docs")
    print(f"    injected {synonym_count} bilingual synonyms (中↔英)")


if __name__ == "__main__":
    main()
