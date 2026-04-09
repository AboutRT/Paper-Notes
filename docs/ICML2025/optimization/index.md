<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📐 优化/理论

**🧪 ICML2025** · 共 **42** 篇

**[A Generalization Result for Convergence in Learning-to-Optimize](a_generalization_result_for_convergence_in_learning-to-optimize.md)**

:   提出一个概率框架，将 PAC-Bayesian 泛化理论与变分分析中的 Kurdyka-Łojasiewicz (KL) 收敛定理相结合，首次在不限制学习算法设计的前提下，以高概率证明了学习型优化算法收敛到临界点。

**[A Unified View on Learning Unnormalized Distributions via Noise-Contrastive Estimation](a_unified_view_on_learning_unnormalized_distributions_via_noise-contrastive_esti.md)**

:   通过f-NCE框架的两个变体（alpha-CentNCE和f-CondNCE）统一了学习非归一化分布的多种方法（MLE/MC-MLE/pseudo-likelihood/ISO等），发现f-CondNCE与score matching的真实关系，并为指数族建立首个有限样本收敛保证。

**[Adjustment for Confounding using Pre-Trained Representations](adjustment_for_confounding_using_pre-trained_representations.md)**

:   本文研究如何利用预训练神经网络的隐表示来调整非表格数据（如图像、文本）中的混杂因素，形式化了表示充分性条件，证明了稀疏性/可加性假设在可逆线性变换（ILT）下不成立，并基于低内在维度和层次组合模型建立了深度网络的收敛速率理论，从而保证 DML 框架下 ATE 估计的有效推断。

**[AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](advprompter_fast_adaptive_adversarial_prompting_for_llms.md)**

:   提出 AdvPrompter——用一个 LLM（AdvPrompter）在秒级速度内为目标 LLM 生成人类可读的对抗提示后缀，通过交替优化算法训练，在 AdvBench 和 HarmBench 上实现高攻击成功率，且可迁移到闭源黑盒 LLM，同时展示了用生成的对抗后缀进行对抗训练以增强目标 LLM 鲁棒性的策略。

**[Benefits Of Early Stopping In Gradient Descent For Overparameterized Logistic Re](benefits_of_early_stopping_in_gradient_descent_for_overparameterized_logistic_re.md)**

:   在过参数化逻辑回归中，理论证明了早停梯度下降（early-stopped GD）相比渐近 GD 具有统计优势：早停 GD 是校准且一致的，而渐近 GD 的 logistic risk 趋于无穷且校准误差不消失；同时建立了早停与 $\ell_2$ 正则化之间的定量联系。

**[Beyond Self-Repellent Kernels: History-Driven Target Towards Efficient Nonlinear MCMC on General Graphs](beyond_self-repellent_kernels_history-driven_target_towards_efficient_nonlinear_.md)**

:   提出 History-Driven Target (HDT) 框架，通过修改目标分布（而非转移核）将自排斥机制嵌入任意 MCMC 采样器，在保持 O(1/α) 方差缩减的同时解决了 SRRW 的计算开销大、仅限可逆链、内存占用高三大问题。

**[Can Transformers Learn Full Bayesian Inference In Context?](can_transformers_learn_full_bayesian_inference_in_context.md)**

:   证明 Transformer 可以在上下文中执行完整的贝叶斯推断——通过在合成数据上预训练一个编码器-解码器架构（TabPFN 编码器 + 扩散 Transformer 解码器），模型在部署时无需参数更新即可为 GLM、混合高斯模型等统计模型生成与 HMC 质量媲美的后验样本。

**[Clipping Improves Adam-Norm and AdaGrad-Norm when the Noise Is Heavy-Tailed](clipping_improves_adam-norm_and_adagrad-norm_when_the_noise_is_heavy-tailed.md)**

:   证明了 AdaGrad/Adam 在重尾噪声下的高概率收敛可能很差（依赖置信水平的多项式），并证明梯度裁剪可以修复这个问题——Clip-AdaGrad-Norm 和 Clip-Adam-Norm 在重尾噪声下实现了对置信水平的对数多项式依赖的高概率收敛界，扩展到延迟步长版本。

**[Compelling ReLU Networks to Exhibit Exponentially Many Linear Regions at Initialization and During Training](compelling_relu_networks_to_exhibit_exponentially_many_linear_regions_at_initial.md)**

:   提出一种基于非对称三角波的 ReLU 网络重参数化方法，使深度为 $d$ 的 4 神经元宽网络在初始化时即产生 $2^d$ 个线性区域，并在预训练中保持该指数级表达能力，在一维函数逼近任务上将误差降低了 **3 个数量级**。

**[Constant Stepsize Local GD for Logistic Regression: Acceleration by Instability](constant_stepsize_local_gd_for_logistic_regression_acceleration_by_instability.md)**

:   证明了 Local GD 在分布式逻辑回归问题上可以使用**任意正步长** $\eta > 0$ 收敛，且通过允许初始不稳定阶段的非单调目标下降，可实现比现有凸优化最坏情况下界更快的 $\widetilde{\mathcal{O}}(M/(\gamma^5 R^2))$ 收敛速率。

**[Efficient Curvature-Aware Hypergradient Approximation For Bilevel Optimization](efficient_curvature-aware_hypergradient_approximation_for_bilevel_optimization.md)**

:   提出 NBO 框架，利用双层优化中超梯度的内在结构（下层问题求解与 Hessian 逆向量积共享同一 Hessian），通过非精确 Newton 方法高效融合曲率信息来逼近超梯度，在确定性场景下将梯度计算复杂度相比 SOTA 改善了 $\kappa \log \kappa$ 倍。

**[Emergence in Non-Neural Models: Grokking Modular Arithmetic via Average Gradient Outer Product](emergence_in_non-neural_models_grokking_modular_arithmetic_via_average_gradient_.md)**

:   本文证明 grokking（延迟泛化）现象并非神经网络或梯度下降特有，而是源于**任务相关特征的逐步学习**——利用非神经网络的 Recursive Feature Machines (RFM) 在核机器上复现了模算术的 grokking，揭示分块循环（block-circulant）特征矩阵是泛化的核心。

**[FedSWA: Improving Generalization in Federated Learning with Highly Heterogeneous Data via Momentum-Based Stochastic Controlled Weight Averaging](fedswa_improving_generalization_in_federated_learning_with_highly_heterogeneous_.md)**

:   针对高数据异质性下 FedSAM 泛化失败的问题，提出 FedSWA（周期学习率 + EMA 聚合）和 FedMoSWA（动量方差缩减控制变量），在理论和实验上均证明优于 FedSAM 及其变体，在 CIFAR-100 Dirichlet-0.1 上比 FedSAM 高出 21.8% 准确率。

**[Flexible Tails for Normalizing Flows](flexible_tails_for_normalizing_flows.md)**

:   提出 Tail Transform Flow (TTF)，在 normalizing flow 的**最后一层**添加基于互补误差函数的非 Lipschitz 变换，将高斯尾部转换为可调权重的重尾分布，避免了使用重尾基分布导致的神经网络优化困难问题。

**[GCAL: Adapting Graph Models to Evolving Domain Shifts](gcal_adapting_graph_models_to_evolving_domain_shifts.md)**

:   提出 Graph Continual Adaptive Learning (GCAL)，通过"适应+生成记忆"双层优化策略，在图模型面对持续演变的 OOD 图序列时，利用信息最大化进行无监督域适应，同时基于信息瓶颈理论设计变分记忆图生成模块来压缩历史图知识，有效缓解灾难性遗忘。

**[Generalization and Robustness of the Tilted Empirical Risk](generalization_and_robustness_of_the_tilted_empirical_risk.md)**

:   本文为负倾斜参数(γ<0)下的 Tilted Empirical Risk (TER) 提供了系统性的泛化误差上下界和鲁棒性保证，在损失函数无界但具有有界 (1+ε) 阶矩条件下，通过均匀方法和信息论方法建立了 $O(n^{-\epsilon/(1+\epsilon)})$ 的收敛速率，并给出了数据驱动的倾斜参数选择方案。

**[Global Convergence and Rich Feature Learning in $L$-Layer Infinite-Width Neural Networks under $\mu$P Parametrization](global_convergence_and_rich_feature_learning_in_l-layer_infinite-width_neural_ne.md)**

:   证明了在 $\mu$P (Maximal Update Parametrization) 下，$L$ 层无限宽 MLP 用 SGD 训练时，各层特征在整个训练过程中保持线性独立且发生实质性演化，从而保证训练收敛点必为全局最小值——首次同时解决"丰富特征学习"和"全局收敛"两个理论目标。

**[Grokking at the Edge of Linear Separability](grokking_at_the_edge_of_linear_separability.md)**

:   在最简单的逻辑回归二分类任务中揭示了 grokking（延迟泛化）的根本原因：当数据维度与样本数之比 $\lambda = d/N$ 接近临界点 $\lambda_c = 1/2$ 时，训练动力学会在过拟合解附近停留任意长时间后才收敛到泛化解，类似于物理学中的"临界减速"现象。

**[How Transformers Learn Regular Language Recognition: A Theoretical Study on Training Dynamics and Implicit Bias](how_transformers_learn_regular_language_recognition_a_theoretical_study_on_train.md)**

:   从理论上刻画了一层 Transformer 学习 "even pairs" 和 "parity check" 两类正则语言识别任务时的两阶段训练动力学，证明了线性层在梯度下降下隐式收敛到最大间隔超平面，并揭示了 CoT 在解决 parity 问题中的关键作用。

**[Improved Last-Iterate Convergence of Shuffling Gradient Methods for Nonsmooth Convex Optimization](improved_last-iterate_convergence_of_shuffling_gradient_methods_for_nonsmooth_co.md)**

:   首次证明RR和SS在非光滑（强）凸有限和优化中，last-iterate收敛率严格优于Proximal GD，达到近似最优的O(1/(n^{1/4}sqrt(K)))，匹配下界。

**[Improved Sample Complexity for Private Nonsmooth Nonconvex Optimization](improved_sample_complexity_for_private_nonsmooth_nonconvex_optimization.md)**

:   在差分隐私约束下研究非光滑非凸（NSNC）随机优化，通过改进梯度估计器的有效灵敏度，将已知最优样本复杂度降低了 $\Omega(\sqrt{d})$ 倍，并首次证明 Goldstein 稳定性可从经验损失泛化到总体损失。

**[Incremental Gradient Descent with Small Epoch Counts is Surprisingly Slow on Ill-Conditioned Problems](incremental_gradient_descent_with_small_epoch_counts_is_surprisingly_slow_on_ill.md)**

:   揭示IGD（确定性排列SGD）在小epoch情形(K<kappa)的令人惊讶的慢收敛：即使所有组件强凸仍无法快于均匀SGD；非凸组件导致指数级退化。

**[Integer Programming for Generalized Causal Bootstrap Designs](integer_programming_for_generalized_causal_bootstrap_designs.md)**

:   提出基于整数规划（IP）数值求解最不利 copula 的方法，将因果 bootstrap 的设计不确定性量化从"完全随机化 + 均值差估计量"推广到任意已知概率分配与线性/二次处理估计量，并证明渐近有效性。

**[Interior-Point Vanishing Problem in Semidefinite Relaxations for Neural Network Verification](interior-point_vanishing_problem_in_semidefinite_relaxations_for_neural_network_.md)**

:   本文首次识别了SDP松弛用于深度神经网络验证时的"内点消失"(interior-point vanishing)问题——随着网络深度增加，SDP问题丧失严格可行性导致数值不稳定和求解失败——并提出五种缓解方法，其中B-Remove（移除层边界约束）最有效，解决了88%原本无法求解的问题。

**[Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](learning_to_plan_reason_for_evaluation_with_thinking-llm-as-a-judge.md)**

:   提出 EvalPlanner，通过将 LLM-as-a-Judge 的推理过程解耦为"评估计划生成"和"计划执行"两个阶段，并在自训练循环中用 DPO 迭代优化计划与执行的偏好对，在 RewardBench 上以仅 22K 合成偏好对达到 93.9 的生成式奖励模型新 SOTA。

**[MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines](metaagent_automatically_constructing_multi-agent_systems_based_on_finite_state_m.md)**

:   提出 MetaAgent，一个基于有限状态机（FSM）的框架，给定任务描述即可自动设计多智能体系统，无需外部训练数据，支持工具调用和状态回溯，在文本任务、ML 任务和软件开发任务上超越现有自动设计方法并逼近人工设计系统性能。

**[Nonparametric Teaching for Graph Property Learners](nonparametric_teaching_for_graph_property_learners.md)**

:   提出 GraNT 范式，将非参数教学理论拓展到图属性学习场景，通过贪心选择"预测偏差最大"的图样本子集来加速 GCN 训练，在保持泛化性能的同时将训练时间缩减 30%–47%。

**[On Understanding Attention-Based In-Context Learning for Categorical Data](on_understanding_attention-based_in-context_learning_for_categorical_data.md)**

:   将 Transformer 的 in-context learning (ICL) 从实值输出推广到**分类数据**（categorical outcomes），证明一种交替使用 self-attention 和 cross-attention 的架构可以**精确实现**多步函数梯度下降（functional GD），并在理论上证明该 GD 参数构型是注意力模型损失函数的驻点。

**[Optimization over Sparse Support-Preserving Sets: Two-Step Projection with Global Optimality Guarantees](optimization_over_sparse_support-preserving_sets_two-step_projection_with_global.md)**

:   针对带有额外支撑保持约束的稀疏优化问题，提出两步投影IHT算法（先硬阈值再投影凸集），在RSC/RSS条件下给出全局目标值保证（无系统误差），揭示稀疏度松弛与次优性间的新trade-off。

**[POPri: Private Federated Learning using Preference-Optimized Synthetic Data](popri_private_federated_learning_using_preference-optimized_synthetic_data.md)**

:   将差分隐私联邦学习中的合成数据生成问题重新建模为 LLM 策略优化（DPO）问题，利用客户端 DP 反馈构建偏好对来微调 LLM，比传统 Private Evolution 提升更大——在 ε=1 下将隐私-性能差距缩小 58%。

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](provable_in-context_vector_arithmetic_via_retrieving_task_concepts.md)**

:   本文从优化理论角度证明：带残差连接和层归一化的非线性 Transformer 经梯度下降在 QA 数据上训练后，能通过向量加法（task vector + query）完成事实召回型 ICL 任务，且在 ICL 数据上训练反而会导致低层特征的有害记忆。

**[Quantum Optimization via Gradient-Based Hamiltonian Descent](quantum_optimization_via_gradient-based_hamiltonian_descent.md)**

:   将梯度信息融入量子哈密顿下降 (QHD) 框架，提出 gradient-based QHD，在凸和非凸优化中均实现了比原始 QHD 及经典方法（NAG、SGDM）快至少一个数量级的收敛速度和更高的全局最优命中概率。

**[Random Feature Representation Boosting](random_feature_representation_boosting.md)**

:   提出 RFRBoost，利用梯度表示提升（gradient representation boosting）理论构建深层残差随机特征神经网络，在 MSE 损失下获得封闭解，在一般损失下化归为二次约束最小二乘问题，在表格数据上显著超越单层 RFNN 与端到端训练的 MLP ResNet。

**[Revisiting Unbiased Implicit Variational Inference](revisiting_unbiased_implicit_variational_inference.md)**

:   重新审视被认为"不实用"的无偏隐式变分推断（UIVI），用重要性采样替代其内部 MCMC 循环，并通过最小化期望前向 KL 散度无偏地学习最优提议分布，在标准 SIVI 基准上达到或超越 SOTA。

**[SDP-CROWN: Efficient Bound Propagation for Neural Network Verification with Tightness of Semidefinite Programming](sdp-crown_efficient_bound_propagation_for_neural_network_verification_with_tight.md)**

:   提出 SDP-CROWN，将半定规划（SDP）松弛的紧致性融入线性界传播框架，每层仅增加一个参数 λ，便可在 ℓ₂ 扰动下将验证松弛度最多收紧 √n 倍，同时保持与 α-CROWN 同级的可扩展性。

**[Statistical and Computational Guarantees of Kernel Max-Sliced Wasserstein Distances](statistical_and_computational_guarantees_of_kernel_max-sliced_wasserstein_distan.md)**

:   本文为 Kernel Max-Sliced (KMS) Wasserstein 距离提供了**尖锐的有限样本统计保证**（无维度依赖、收敛速率 $n^{-1/(2p)}$）和**计算保证**（证明精确计算是 NP-hard 后提出高效的半定松弛 SDR 及一阶算法），并在高维两样本检验、人体活动检测和生成建模上验证了优越性能。

**[Synonymous Variational Inference for Perceptual Image Compression](synonymous_variational_inference_for_perceptual_image_compression.md)**

:   基于语义信息论中的同义性视角，提出同义变分推断 (SVI) 方法，从理论上证明感知图像压缩的优化方向是率-失真-感知三元权衡，并设计渐进式同义图像压缩 (SIC) 编解码器，单模型即可覆盖多码率多感知质量级别。

**[Tilted Sharpness-Aware Minimization](tilted_sharpness-aware_minimization.md)**

:   提出 Tilted SAM (TSAM)，利用指数倾斜 (exponential tilting) 将 SAM 的 min-max 目标平滑化为对邻域内多个局部解按损失值加权的软优化，理论上更平滑、更偏好平坦极小值，实验在图像和文本任务上一致优于 SAM 及其变体。

**[Training Dynamics of In-Context Learning in Linear Attention](training_dynamics_of_in-context_learning_in_linear_attention.md)**

:   本文完整刻画了多头线性注意力在梯度流训练中获取 ICL 能力的动态过程：merged KQ 参数化呈现单次突变式 loss 下降，而 separate KQ 参数化则展现 saddle-to-saddle 逐步学习主成分回归的阶梯式训练动态。

**[Transformative Or Conservative Conservation Laws For Resnets And Transformers](transformative_or_conservative_conservation_laws_for_resnets_and_transformers.md)**

:   系统推导并证明了卷积 ResNet 和 Transformer 等现代架构在梯度流训练动态下的守恒律，揭示残差连接不改变守恒律、块级守恒律等价于孤立块的守恒律，并证明离散 SGD 下守恒误差为 $O(\text{step-size}^2)$。

**[Understanding Sharpness Dynamics in NN Training with a Minimalist Example: The Effects of Dataset Difficulty, Depth, Stochasticity, and More](understanding_sharpness_dynamics_in_nn_training_with_a_minimalist_example_the_ef.md)**

:   提出用"每层单神经元的深度线性网络"作为极简模型，系统性地研究 progressive sharpening 和 edge of stability 现象，引入 dataset difficulty $Q$ 概念并推导了 sharpness 在全局最优处的上下界，理论分析了数据规模、网络深度、batch size 和学习率对 sharpness 动态的影响机制。

**[Understanding the Statistical Accuracy-Communication Trade-off in Personalized Federated Learning with Minimax Guarantees](understanding_the_statistical_accuracy-communication_trade-off_in_personalized_f.md)**

:   本文首次定量刻画了个性化联邦学习中个性化程度 $\lambda$ 如何同时影响统计精度和通信效率，建立了 minimax 最优统计速率，并提出 FedCLUP 算法实现了统计-通信的最优权衡。
