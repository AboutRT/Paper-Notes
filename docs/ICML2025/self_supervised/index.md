<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🔄 自监督/表示学习

**🧪 ICML2025** · 共 **15** 篇

**[A Bayesian Model Selection Criterion for Selecting Pretraining Checkpoints](a_bayesian_model_selection_criterion_for_selecting_pretraining_checkpoints.md)**

:   引入"下游自由能"作为预训练检查点的贝叶斯模型选择准则——衡量检查点附近参数空间中适合下游任务的参数浓度，并证明可仅用预训练数据近似（预训练自由能），为选择最优检查点提供理论指导。

**[AdaWorld: Learning Adaptable World Models with Latent Actions](adaworld_learning_adaptable_world_models_with_latent_actions.md)**

:   提出 AdaWorld——通过从视频中自监督提取潜在动作（latent actions）进行动作感知预训练，构建高度可适应的世界模型，支持零样本动作迁移和少量交互快速适应新环境。

**[Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](alpha-sql_zero-shot_text-to-sql_using_monte_carlo_tree_search.md)**

:   Alpha-SQL 将零样本 Text-to-SQL 建模为树搜索问题，通过蒙特卡洛树搜索 (MCTS) 框架结合 LLM-as-Action-Model 和自监督奖励函数，无需微调即可在 BIRD 数据集上以 32B 开源模型达到 69.7% 执行精度，超越基于 GPT-4o 的零样本 SOTA 2.5 个百分点。

**[Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions](beyond_sensor_data_foundation_models_of_behavioral_data_from_wearables_improve_h.md)**

:   在 162K 个体的 25 亿小时可穿戴行为数据上训练基础模型（WBM），系统优化不规则采样行为数据的 tokenizer 和架构，在 57 项健康检测任务上展示强大表现，特别在行为驱动任务（如睡眠预测）上表现突出。

**[Clustering Properties of Self-Supervised Learning](clustering_properties_of_self-supervised_learning.md)**

:   从理论角度分析自监督学习（SSL）表示的聚类性质，证明 SSL 方法（对比学习、正则化方法等）在优化充分时会产生具有聚类结构的表示——类内紧凑、类间分离，连接了 SSL 与有监督学习中的神经塌缩现象。

**[Foundation Model Insights and a Multi-Model Approach for Superior Fine-Grained One-shot Subset Selection](foundation_model_insights_and_a_multi-model_approach_for_superior_fine-grained_o.md)**

:   本文系统研究了基础模型（FM）替代传统信息提取器（IE）用于子集选择的优劣，发现 FM 在细粒度数据集上显著优于传统 IE，并提出 RAM-APL 方法，利用多个 FM（DINOv2 + CLIP）从类内和类间两个维度联合衡量样本重要性，在三个细粒度数据集上达到 SOTA。

**[Generalization Analysis for Supervised Contrastive Representation Learning under Non-IID Settings](generalization_analysis_for_supervised_contrastive_representation_learning_under.md)**

:   本文首次在非独立同分布（non-IID）条件下为监督对比表征学习（CRL）建立了泛化界，利用 U-统计量分解技术处理训练元组重叠样本的依赖性问题，给出了以标记样本数 $N$ 为自变量的 excess risk 收敛速率。

**[Griffin: Towards a Graph-Centric Relational Database Foundation Model](griffin_towards_a_graph-centric_relational_database_foundation_model.md)**

:   Griffin 是首个面向关系数据库（RDB）的基础模型，通过将多表结构转化为异构图，结合统一编码器/解码器、交叉注意力和层级聚合的 MPNN，在 150M+ 行数据上进行自监督掩码补全预训练 + 联合 SFT，实现跨数据库、跨域、跨任务的泛化预测。

**[MTL-UE: Learning to Learn Nothing for Multi-Task Learning](mtl-ue_learning_to_learn_nothing_for_multi-task_learning.md)**

:   提出 MTL-UE，首个针对多任务学习数据的不可学习样本框架，通过编码器-解码器注入类别先验嵌入并结合任务内/任务间嵌入正则化，有效保护 MTL 和 STL 模型免受未授权训练。

**[Neighbour-Driven Gaussian Process Variational Autoencoders for Scalable Structured Latent Modelling](neighbour-driven_gaussian_process_variational_autoencoders_for_scalable_structur.md)**

:   提出两种基于最近邻的高斯过程先验近似方法（HPA 和 SPA），将近邻驱动的稀疏性引入 GPVAE 的潜空间推断，在保留关键潜变量依赖的同时实现可扩展的 mini-batch 训练，避免了对大量诱导点或受限核函数的依赖。

**[PDE-Transformer: Efficient and Versatile Transformers for Physics Simulations](pde-transformer_efficient_and_versatile_transformers_for_physics_simulations.md)**

:   提出 PDE-Transformer，一种面向物理模拟的改进 Transformer 架构，通过分离通道嵌入、移位窗口注意力和多尺度 U 形结构，在 16 种 PDE 类型上超越现有 SOTA，并展现出强大的下游任务迁移能力。

**[Promoting Ensemble Diversity with Interactive Bayesian Distributional Robustness for Fine-tuning Foundation Models](promoting_ensemble_diversity_with_interactive_bayesian_distributional_robustness.md)**

:   提出 IBDR 框架，在贝叶斯推断中建模粒子间交互以促进集成多样性，结合 Wasserstein 分布鲁棒优化提供理论保证，在 VTAB-1K 和常识推理任务上显著优于现有方法。

**[Proxy-FDA: Proxy-based Feature Distribution Alignment for Fine-tuning Vision Foundation Models without Forgetting](proxy-fda_proxy-based_feature_distribution_alignment_for_fine-tuning_vision_foun.md)**

:   提出 Proxy-FDA，通过基于最近邻图的特征分布对齐（FDA）和动态生成的代理特征（Proxy），在微调视觉基础模型时显式保留特征邻域结构中的丰富知识，大幅减少概念遗忘。

**[Test-Time Canonicalization by Foundation Models for Robust Perception](test-time_canonicalization_by_foundation_models_for_robust_perception.md)**

:   提出 FoCal 框架，在推理阶段利用 CLIP 和 Stable Diffusion 的视觉先验，通过"变换-排序"策略将输入图像变换为最具视觉典型性的版本，无需重训练即可提升模型对视角、光照、旋转等变换的鲁棒性。

**[Update Your Transformer to the Latest Release: Re-Basin of Task Vectors](update_your_transformer_to_the_latest_release_re-basin_of_task_vectors.md)**

:   提出 TransFusion，一种专为 Transformer 设计的两级权重置换方法（头间+头内），实现将旧模型的微调知识（任务向量）免数据免训练地迁移至新版基础模型。
