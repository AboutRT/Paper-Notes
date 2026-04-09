<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**🧪 ICML2025** · 共 **19** 篇

**[A Generalizable Physics-Enhanced State Space Model for Long-Term Dynamics Forecasting in Complex Environments](a_generalizable_physics-enhanced_state_space_model_for_long-term_dynamics_foreca.md)**

:   提出 Phy-SSM，将部分已知的物理知识融入深度状态空间模型（SSM），通过动力学分解（已知/未知矩阵）和物理状态正则化，实现对噪声大、不规则采样数据的长期动力学精准预测与外推。

**[AAAR-1.0: Assessing AI's Potential to Assist Research](aaar-10_assessing_ais_potential_to_assist_research.md)**

:   提出 AAAR-1.0 基准，通过公式推断、实验设计、论文弱点发现、审稿质量鉴别四个专家级任务，系统评估 LLM 辅助科研的真实能力，揭示当前模型在深度研究任务上仍有显著不足。

**[Beyond CVaR: Leveraging Static Spectral Risk Measures for Enhanced Decision-Making in Distributional Reinforcement Learning](beyond_cvar_leveraging_static_spectral_risk_measures_for_enhanced_decision-makin.md)**

:   提出首个在分布式 RL 框架内优化一般静态谱风险度量（SRM）的算法，超越了仅限于简单 CVaR 的现有方法，通过利用回报分布实现闭式外层优化和中间风险度量的时间分解，在多种风险设置中超越现有风险敏感 DRL 模型。

**[Doubly Robust Fusion of Many Treatments for Policy Learning](doubly_robust_fusion_of_many_treatments_for_policy_learning.md)**

:   提出校准加权治疗融合（Calibration-Weighted Treatment Fusion）方法，通过双重稳健地合并具有相似效果的治疗组来降低动作空间维度，使得现有多臂策略学习方法（如策略树）可高效应用于大量治疗选项的个体化推荐场景。

**[Efficient Logit-based Knowledge Distillation of Deep Spiking Neural Networks for Full-Range Timestep Deployment](efficient_logit-based_knowledge_distillation_of_deep_spiking_neural_networks_for.md)**

:   提出一种时间维度解耦的 logit 蒸馏框架，利用 SNN 固有的时空特性，将训练目标分解到每个时间步，实现单模型在全范围推理时间步上的高性能部署，无需为不同时间步重新训练。

**[Enhancing Decision-Making of Large Language Models via Actor-Critic](enhancing_decision-making_of_large_language_models_via_actor-critic.md)**

:   提出 LAC（LLM-based Actor-Critic）框架，通过 token logits 的正/负结果概率比构建 Q 函数（Critic），并用 KL 约束闭式解实现无梯度策略优化（Actor），在 ALFWorld、BabyAI-Text、WebShop 三个基准上用 7B/8B 模型超越 GPT-4 + ReAct。

**[Enhancing Parallelism in Decentralized Stochastic Convex Optimization](enhancing_parallelism_in_decentralized_stochastic_convex_optimization.md)**

:   提出 Decentralized Anytime SGD (DAT-SGD)，通过在渐变平均查询点上计算梯度来缓解共识距离偏差，将去中心化随机凸优化的并行度上界从 $\mathcal{O}(\rho^{1/2} N^{1/4})$ 提升至 $\mathcal{O}(\rho \sqrt{N})$，在高连通拓扑下首次匹配中心化学习的速率。

**[Erwin: A Tree-based Hierarchical Transformer for Large-scale Physical Systems](erwin_a_tree-based_hierarchical_transformer_for_large-scale_physical_systems.md)**

:   提出 Erwin，一种基于 ball tree 分层结构的 Transformer 架构，通过将注意力计算限制在固定大小的局部球区域内，实现线性时间复杂度，同时通过渐进式粗化/细化和跨球交互机制捕获多尺度特征，在宇宙学、分子动力学、PDE 求解和粒子流体动力学多个领域达到 SOTA。

**[From Logits to Hierarchies: Hierarchical Clustering made Simple](from_logits_to_hierarchies_hierarchical_clustering_made_simple.md)**

:   提出 L2H（Logits to Hierarchies）算法，仅利用预训练平面聚类模型的 logits 输出，通过掩码 softmax 和迭代合并策略，在无需微调的情况下构建高质量层次聚类，大幅超越专用深度层次聚类模型，且在 ImageNet 规模数据集上 CPU 运行不到一分钟。

**[Generative Social Choice: The Next Generation](generative_social_choice_the_next_generation.md)**

:   将生成式社会选择框架扩展至带成本/预算约束和近似查询的场景，提出 DemocraticProcess 算法并给出近乎最优的近似比例代表性理论保证，实现了实用系统 PROSE（基于 GPT-4o）在药物评论和城市治理数据集上验证有效性。

**[KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment](kelps_a_framework_for_verified_multi-language_autoformalization_via_semantic-syn.md)**

:   提出基于断言逻辑的中间表示——知识方程(Knowledge Equation)，实现自然语言数学命题到多种形式语言(Lean4/Coq/Isabelle)的规则化翻译，在 MiniF2F 上 pass@1 句法准确率达 88.9%，超越 DeepSeek-V3 和 Herald。

**[Log-Sum-Exponential Estimator For Off-Policy Evaluation And Learning](log-sum-exponential_estimator_for_off-policy_evaluation_and_learning.md)**

:   提出基于 log-sum-exponential (LSE) 算子的新型非线性估计器，用于离线策略评估与学习，在重尾奖励和噪声倾向分数场景下显著降低方差并提供理论保证。

**[Provably Improving Generalization of Few-Shot Models with Synthetic Data](provably_improving_generalization_of_few-shot_models_with_synthetic_data.md)**

:   提出一个理论框架量化合成数据与真实数据的分布差异对少样本分类泛化能力的影响，并基于该理论设计了联合优化数据划分与模型训练的算法，在10个基准数据集上超越SOTA。

**[SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability](saebench_a_comprehensive_benchmark_for_sparse_autoencoders_in_language_model_int.md)**

:   提出 SAEBench——一个包含 8 项评估指标的综合基准，系统评测稀疏自编码器（SAE）在语言模型可解释性中的表现，揭示了代理指标（稀疏-保真度）与下游任务性能之间的严重脱节。

**[Semantic Shift Estimation via Dual-Projection and Classifier Reconstruction for Exemplar-Free Class-Incremental Learning](semantic_shift_estimation_via_dual-projection_and_classifier_reconstruction_for_.md)**

:   提出 DPCR 方法，通过双投影（任务级 TSSP + 类别级 CIP）估计语义漂移，并用岭回归无BP地重建分类器，同时解决无样例类增量学习中的语义漂移和决策偏差问题，在多个基准上超越 SOTA。

**[Sparse Spectral Training and Inference on Euclidean and Hyperbolic Neural Networks](sparse_spectral_training_and_inference_on_euclidean_and_hyperbolic_neural_networ.md)**

:   提出 Sparse Spectral Training (SST)，通过在谱域上每步更新全部奇异值、按奇异值大小多项式采样选择性更新奇异向量，并周期性 re-SVD 保持正交性，实现接近全秩训练的预训练效果，同时显存开销与 LoRA 相当。

**[TabFlex: Scaling Tabular Learning to Millions with Linear Attention](tabflex_scaling_tabular_learning_to_millions_with_linear_attention.md)**

:   用线性注意力替换 TabPFN 中的 softmax 注意力，将表格分类的 ICL 方法从小数据集扩展到百万级样本，实现 2× 以上加速且性能不降。

**[Validating Mechanistic Interpretations: An Axiomatic Approach](validating_mechanistic_interpretations_an_axiomatic_approach.md)**

:   借鉴程序分析中抽象解释的思想，提出一组公理化框架来形式化定义和验证神经网络的机制解释（mechanistic interpretation），并在 2-SAT 求解器和模加法两个案例中验证了该框架的有效性。

**[VisionTS: Visual Masked Autoencoders Are Free-Lunch Zero-Shot Time Series Forecasters](visionts_visual_masked_autoencoders_are_free-lunch_zero-shot_time_series_forecas.md)**

:   将时间序列重构为图像，利用 ImageNet 预训练的 MAE（Masked Autoencoder）在**零样本**设置下进行时序预测，无需任何时序数据训练即可匹敌甚至超越专门的时序基础模型。
