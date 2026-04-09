<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎁 推荐系统

**🧪 ICML2025** · 共 **5** 篇

**[Deprecating Benchmarks: Criteria and Framework](deprecating_benchmarks_criteria_and_framework.md)**

:   提出了一套判断 AI 基准何时应被废弃的 **7 项标准** 和一个包含评估-报告-通知三阶段的 **废弃框架**，并以 EU AI Office 为例给出了制度化落地方案。

**[ELMO: Efficiency via Low-precision and Peak Memory Optimization in Large Output Spaces](elmo_efficiency_via_low-precision_and_peak_memory_optimization_in_large_output_s.md)**

:   提出 ELMO 框架，通过纯 BFloat16/Float8 低精度训练结合梯度融合、分块策略等峰值显存优化，将 300 万标签的 XMC 模型训练显存从 39.7 GiB 降至 6.6 GiB，且不损失分类精度。

**[How to Set AdamW's Weight Decay as You Scale Model and Dataset Size](how_to_set_adamws_weight_decay_as_you_scale_model_and_dataset_size.md)**

:   将 AdamW 的权重更新解释为指数移动平均（EMA），揭示了 EMA 时间尺度 $\tau = 1/(\eta\lambda)$ 是核心超参数，其以 epoch 为单位的最优值在模型和数据集规模变化时保持稳定，从而给出了 weight decay 随规模缩放的明确规则。

**[New Interaction Paradigm for Complex EDA Software Leveraging GPT](new_interaction_paradigm_for_complex_eda_software_leveraging_gpt.md)**

:   提出 SmartonAI 系统，将大语言模型（LLM）和检索增强生成（RAG）集成到 EDA 工具 KiCad 中，通过自然语言交互实现任务分解、文档检索和智能插件推荐与执行，大幅降低复杂工程软件的学习门槛。

**[QuRe: Query-Relevant Retrieval through Hard Negative Sampling in Composed Image Retrieval](qure_query-relevant_retrieval_through_hard_negative_sampling_in_composed_image_r.md)**

:   提出 QuRe，通过基于相关性分数陡降的硬负样本采样策略和奖励模型优化目标，在组合图像检索(CIR)中同时召回目标图像和其他相关图像，从而提升用户满意度。
