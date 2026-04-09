<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📡 信号/通信

**🧪 ICML2025** · 共 **2** 篇

**[Reward-Augmented Data Enhances Direct Preference Alignment of LLMs](reward-augmented_data_enhances_direct_preference_alignment_of_llms.md)**

:   提出一种**奖励增强的数据重标注方法**，通过将偏好对条件化于奖励分数构建扩增数据集，使DPO能感知回复质量全谱，缓解高质量rejected回复被遗忘和低质量chosen回复被盲目学习的问题，在多个基准上一致性大幅提升DPO性能。

**[SepLLM: Accelerate Large Language Models by Compressing One Segment into One Separator](sepllm_accelerate_large_language_models_by_compressing_one_segment_into_one_sepa.md)**

:   SepLLM 发现分隔符 token（标点等）在注意力中占据主导地位，提出将文本段信息压缩到分隔符 token 中，通过数据依赖的稀疏注意力掩码仅保留 Initial + Separator + Neighboring tokens 的 KV cache，实现 50%+ 的 KV cache 压缩且性能几乎无损。
