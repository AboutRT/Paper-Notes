<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚡ LLM 效率

**🧪 ICML2025** · 共 **15** 篇

**[Addressing Imbalanced Domain-Incremental Learning through Dual-Balance Collaborative Experts (DCE)](addressing_imbalanced_domain-incremental_learning_through_dual-balance_collabora.md)**

:   DCE 提出频率感知专家组 + 动态专家选择器的双阶段训练框架，同时解决域增量学习中域内类别不平衡和跨域类别分布偏移两个难题，在四个 benchmark 上达到 SOTA。

**[Autonomy-of-Experts Models (AoE)](autonomy-of-experts_models.md)**

:   AoE 提出让 MoE 中的 expert 基于自身内部激活范数自主决定是否处理输入（而非由外部 router 决定），通过低秩权重分解降低预计算开销，在 700M-4B 参数语言模型预训练中超越传统 MoE。

**[CostFilter-AD: Enhancing Anomaly Detection through Matching Cost Filtering](costfilter-ad_enhancing_anomaly_detection_through_matching_cost_filtering.md)**

:   将立体匹配/光流估计中的**代价体滤波（cost volume filtering）**思想引入无监督异常检测（UAD），构造输入与模板之间的匹配代价体，并通过3D U-Net 加双流注意力引导进行去噪滤波，作为通用后处理插件可同时提升重建型和嵌入型 UAD 方法的性能，在 MVTec-AD 和 VisA 上取得 SOTA。

**[Curse of High Dimensionality Issue in Transformer for Long-context Modeling](curse_of_high_dimensionality_issue_in_transformer_for_long-context_modeling.md)**

:   本文从监督学习视角重新审视序列建模中的注意力冗余问题，提出了 Dynamic Group Attention (DGA) 机制，通过将不重要的 token 动态分组聚合来减少注意力计算中的冗余，在保持竞争性能的同时大幅降低推理延迟（LLaMA2-7B 在 16K 上下文下推理速度提升 2.42 倍）。

**[Curvature Enhanced Data Augmentation for Regression](curvature_enhanced_data_augmentation_for_regression.md)**

:   提出 CEMS（Curvature-Enhanced Manifold Sampling），利用数据流形的二阶近似（曲率信息）生成合成样本，用于回归任务的数据增强，在分布内和分布外场景均取得 SOTA 或接近 SOTA 的性能。

**[EasyInv: Toward Fast and Better DDIM Inversion](easyinv_toward_fast_and_better_ddim_inversion.md)**

:   提出 EasyInv，通过在反演过程中周期性地将当前 latent 状态与前一步 latent 状态加权聚合（类卡尔曼滤波），增强初始 latent 的影响力、抑制噪声累积误差，在不需要迭代优化的前提下达到与迭代方法相当甚至更好的反演质量，同时推理速度提升约 3 倍。

**[Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](efficient_length-generalizable_attention_via_causal_retrieval_for_long-context_l.md)**

:   本文提出 Grouped Cross-Attention (GCA) 机制，将 chunk 级别的因果检索（causal retrieval）集成到注意力中实现端到端可学习的检索器，构建的 Differentiable Retrieval-based Transformer (DRT) 在 16M 上下文的 passkey 检索测试中达到近乎完美的准确率，实现了训练长度 1000 倍的长度泛化。

**[Ladder Residual: Parallelism-Aware Architecture for Accelerating Large Model Inference](ladder-residual_parallelism-aware_architecture_for_accelerating_large_model_infe.md)**

:   本文提出 Ladder Residual，一种简单的架构修改——将每个模块的输入从上一层的输出改为上上层的输出（错位残差），使模块计算与 AllReduce 通信解耦，从而实现通信与计算的重叠，在 70B 模型 8 卡 TP 推理中实现 29% 的端到端加速，且模型性能与标准 Transformer 持平。

**[Long-Short Alignment for Effective Long-Context Modeling in LLMs](long-short_alignment_for_effective_long-context_modeling_in_llms.md)**

:   本文从模型输出分布的角度提出长度泛化的新视角——长短对齐 (Long-Short Alignment)，指出不同长度输入的输出分布一致性是长度泛化的关键因素，提出 Long-Short Misalignment 度量并将其作为训练正则项，在合成任务和自然语言任务上均显著提升长上下文建模能力。

**[NExtLong: Toward Effective Long-Context Training without Long Documents](nextlong_toward_effective_long-context_training_without_long_documents.md)**

:   本文提出 NExtLong 框架，通过将文档分割为 meta-chunk 并在 chunk 之间插入从预训练语料检索的硬负例干扰文本来合成长上下文训练数据，迫使模型区分长距离依赖信息和干扰内容，在 HELMET 和 RULER 基准上比此前最佳的长上下文合成方法 Quest 平均提升 7.33%。

**[Online Sparsification of Bipartite-Like Clusters in Graphs](online_sparsification_of_bipartite-like_clusters_in_graphs.md)**

:   提出了一种**近线性时间的在线图稀疏化算法**，能在保留图的二部图式聚类（bipartite-like clusters）结构的前提下，将边数压缩到 $\widetilde{O}(n)$，同时适用于无向图和有向图，显著加速现有聚类算法。

**[PENCIL: Long Thoughts with Short Memory](pencil_long_thoughts_with_short_memory.md)**

:   提出 **PENCIL**（PENCIL ENables Context-efficient Inference and Learning），在自回归生成过程中引入受函数调用栈启发的**归约规则（reduction rule）**，递归地清除不再需要的中间推理步骤，使LLM能以多项式级上下文长度解决本需指数级上下文的计算难题。

**[Ranked Entropy Minimization for Continual Test-Time Adaptation](ranked_entropy_minimization_for_continual_test-time_adaptation.md)**

:   提出 Ranked Entropy Minimization (REM)，通过渐进式遮挡策略构建预测难度的显式排序结构，结合遮挡一致性损失和熵排序损失，解决了熵最小化方法在持续测试时自适应(CTTA)中的模型崩塌问题，同时保持了计算效率。

**[RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](rapid_long-context_inference_with_retrieval-augmented_speculative_decoding.md)**

:   提出 RAPID，将 RAG 与 Speculative Decoding 结合：用 RAG drafter（在短检索上下文上运行的 LLM）为长上下文目标 LLM 生成候选 token，并通过推理时知识迁移增强目标分布，在长上下文推理中同时实现 >2× 加速和生成质量提升。

**[Retraining-Free Merging of Sparse MoE via Hierarchical Clustering](retraining-free_merging_of_sparse_moe_via_hierarchical_clustering.md)**

:   提出 HC-SMoE，一种基于专家输出层次聚类的无需重训练专家合并框架，通过输出相似度度量和层次聚类实现 SMoE 模型的高效压缩，在 Qwen 和 Mixtral 上分别实现 25%-50% 的专家参数缩减并保持优越性能。
