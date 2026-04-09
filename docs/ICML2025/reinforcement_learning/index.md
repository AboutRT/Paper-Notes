<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎮 强化学习

**🧪 ICML2025** · 共 **51** 篇

**[A Theoretical Study of (Hyper) Self-Attention through the Lens of Interactions](a_theoretical_study_of_hyper_self-attention_through_the_lens_of_interactions_rep.md)**

:   从"交互实体"视角统一分析自注意力，证明单层线性SA能高效表示/学习/泛化成对交互函数（含OOD长度泛化），并提出HyperFeatureAttention和HyperAttention分别捕获特征级耦合交互和高阶多实体交互。

**[Adversarial Cooperative Rationalization: The Risk of Spurious Correlations in Even Clean Datasets](adversarial_cooperative_rationalization_the_risk_of_spurious_correlations_in_eve.md)**

:   揭示协作理据化框架（RNP）中的隐蔽缺陷——即使在干净数据集上，生成器的采样偏差也会引入理据与标签间的虚假相关，提出对抗检测+指令干预方法，在文本和图分类上显著超越现有方法。

**[BEAVER: Building Environments with Assessable Variation for Evaluating Multi-Objective Reinforcement Learning](beaver_building_environments_with_assessable_variation_for_evaluating_multi-obje.md)**

:   提出 BEAVER 基准——一个支持多目标和泛化评估的建筑能源管理 RL 环境，将问题形式化为多目标上下文 MDP（MOC-MDP），评估现有 MORL 方法在热对流差异和气候变化下的泛化能力。

**[Benchmarking Quantum Reinforcement Learning](benchmarking_quantum_reinforcement_learning.md)**

:   提出量子强化学习（QRL）的严格基准测试方法论——基于样本复杂度的统计估计器和统计显著性定义的"超越"概念，在新设计的 6G 波束管理环境上进行迄今最大规模（100 seeds）的 QRL vs 经典 RL 比较，发现先前关于 QRL 优越性的声称需要更审慎看待。

**[Beyond The Rainbow: High Performance Deep Reinforcement Learning on a Desktop PC](beyond_the_rainbow_high_performance_deep_reinforcement_learning_on_a_desktop_pc.md)**

:   提出 BTR（Beyond The Rainbow）——整合 6 项 RL 改进到 Rainbow DQN 中，在单台桌面 PC 上 12 小时内训练 Atari-60 达到 IQM 7.4（Rainbow 为 1.9），并首次成功训练智能体玩马里奥银河、马里奥赛车和真人快打等 3D 游戏。

**[BRITE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](brite_bootstrapping_reinforced_thinking_process_to_enhance_language_model_reason.md)**

:   提出 BRITE——通过自举（bootstrapping）方式迭代收集和强化 LLM 的中间思维过程，结合过程级奖励模型和 PPO 训练，持续提升 LLM 在数学推理等任务上的表现。

**[Conceptual Belief-Informed Reinforcement Learning](conceptual_belief-informed_reinforcement_learning.md)**

:   提出 HI-RL（Human Intelligence-RL）——将认知科学中的概念抽象和概率先验信念机制引入 RL，从经验中提取高层概念并构建概念关联的自适应先验来指导值函数/策略更新，作为算法无关插件一致提升 DQN/PPO/SAC/TD3 的样本效率。

**[Controlling Underestimation Bias in Constrained Reinforcement Learning for Safe Exploration](controlling_underestimation_bias_in_constrained_reinforcement_learning_for_safe_.md)**

:   提出 MICE（Memory-driven Intrinsic Cost Estimation）——通过闪光灯记忆机制存储历史高代价状态，构建内在代价信号来纠正代价值函数的低估偏差，在约束 RL 的训练过程中显著减少约束违反次数。

**[Counterfactual Effect Decomposition in Multi-Agent Sequential Decision Making](counterfactual_effect_decomposition_in_multi-agent_sequential_decision_making.md)**

:   提出一种双层因果分解框架，将多智能体序列决策中某动作的总反事实效应（TCFE）系统地分解为"通过智能体行为传播的效应"（tot-ASE）和"通过状态转移传播的效应"（r-SSE），并分别用 Shapley 值和内在因果贡献（ICC）进一步归因到每个智能体和每个状态变量。

**[Decoding Rewards in Competitive Games: Inverse Game Theory with Entropy Regularization](decoding_rewards_in_competitive_games_inverse_game_theory_with_entropy_regulariz.md)**

:   提出基于熵正则化的零和博弈逆问题统一框架，利用 Quantal Response Equilibrium (QRE) 在线性假设下建立奖励函数的可辨识性条件，并给出从观测动作恢复奖励函数的置信集构造算法，附带 $\mathcal{O}(T^{-1/2})$ 收敛速率保证。

**[Demystifying the Paradox of Importance Sampling with an Estimated History-Dependent Behavior Policy in Off-Policy Evaluation](demystifying_the_paradox_of_importance_sampling_with_an_estimated_history-depend.md)**

:   本文从理论上揭示了"在 OPE 中使用估计的历史依赖行为策略比使用真实行为策略反而更好"这一悖论的根本原因——估计行为策略隐式地将 IS 估计器投影到更约束的空间，降低渐近方差但增加有限样本偏差。

**[Diving into Self-Evolving Training for Multimodal Reasoning](diving_into_self-evolving_training_for_multimodal_reasoning.md)**

:   通过强化学习视角重新审视多模态推理中的自演化训练（Self-Evolving Training），系统性地分析训练方法、奖励模型和提示变体三大关键因素，并提出基于 Reward-Pass@K 的自适应温度调节机制来缓解训练饱和问题，最终形成 M-STaR 框架，在多个基准上取得一致提升。

**[Embedding Safety into RL: A New Take on Trust Region Methods](embedding_safety_into_rl_a_new_take_on_trust_region_methods.md)**

:   提出 C-TRPO 算法，通过修改策略空间的几何结构（在 KL 散度中嵌入约束感知的障碍项），使信赖域天然只包含安全策略，从而在训练全程保障约束满足，同时保持与 SOTA 相当的回报性能。

**[Enhancing Cooperative Multi-Agent Reinforcement Learning with State Modelling and Adversarial Exploration](enhancing_cooperative_multi-agent_reinforcement_learning_with_state_modelling_an.md)**

:   提出 SMPE² 算法，通过变分推断学习有意义的状态信念表示并结合对抗式内在探索，在部分可观测的合作多智能体环境中显著提升协调能力，在 MPE、LBF、RWARE 三个基准上超越 SOTA。

**[Ergodic Generative Flows](ergodic_generative_flows.md)**

:   提出 Ergodic Generative Flows (EGFs)，通过有限个全局微分同胚构建生成流，利用遍历性 (ergodicity) 保证通用性，并设计 KL-weakFM 损失实现无需独立奖励模型的模仿学习训练，在 NASA 地球科学数据集上以 30 倍更小的模型超越基线。

**[EVOLvE: Evaluating and Optimizing LLMs For In-Context Exploration](evolve_evaluating_and_optimizing_llms_for_in-context_exploration.md)**

:   提出 BanditBench 基准和三种增强策略（推理时算法引导、Few-shot 示范、Oracle 行为微调），系统评估并改善 LLM 在 bandit 环境中的上下文探索能力，使小模型通过算法蒸馏超越大模型。

**[Exploring Large Action Sets with Hyperspherical Embeddings using von Mises-Fisher Sampling](exploring_large_action_sets_with_hyperspherical_embeddings_using_von_mises-fishe.md)**

:   提出 vMF-exp，通过在超球面上采样 von Mises-Fisher 分布向量再做最近邻检索，实现对大规模动作集（百万级）的可扩展探索，理论证明在均匀分布假设下渐近等价于 Boltzmann 探索，并成功部署于 Deezer 音乐推荐系统。

**[Extreme Value Policy Optimization for Safe Reinforcement Learning](extreme_value_policy_optimization_for_safe_reinforcement_learning.md)**

:   提出 EVO 算法，将极值理论 (EVT) 引入约束强化学习，用广义 Pareto 分布 (GPD) 建模代价尾部的极端样本，并设计极端分位数约束与极端优先回放机制，在训练中实现零约束违反的同时保持竞争性策略性能。

**[Fast and Robust: Task Sampling with Posterior and Diversity Synergies for Adaptive Decision-Makers in Randomized Environments](fast_and_robust_task_sampling_with_posterior_and_diversity_synergies_for_adaptiv.md)**

:   提出 PDTS（Posterior and Diversity Synergized Task Sampling），将鲁棒主动任务采样建模为无穷臂老虎机问题，通过后验采样替代 UCB 并引入多样性正则化，以极简实现在 Domain Randomization 和 Meta-RL 中达到接近最坏情况的鲁棒适应性能。

**[Flow of Reasoning: Training LLMs for Divergent Reasoning with Minimal Examples](flow_of_reasoning_training_llms_for_divergent_reasoning_with_minimal_examples.md)**

:   提出 Flow of Reasoning (FoR)，将多步 LLM 推理建模为 DAG 上的马尔可夫流，借助 GFlowNet 的轨迹平衡目标微调 LLM，使其仅用极少训练样本（如15个）即可采样出概率正比于奖励的多条高质量且多样化的推理路径。

**[Graph-Assisted Stitching for Offline Hierarchical Reinforcement Learning](graph-assisted_stitching_for_offline_hierarchical_reinforcement_learning.md)**

:   提出 Graph-Assisted Stitching (GAS) 框架，用基于图搜索的子目标选择替代显式高层策略学习，通过时间距离表示 (TDR) 空间中的聚类构图与最短路径规划，在离线 HRL 中实现高效的跨轨迹拼接，在最具挑战的 antmaze-giant-stitch 任务上从前 SOTA 的 1.0 飙升至 88.3。

**[Graph-Supported Dynamic Algorithm Configuration for Multi-Objective Combinatorial Optimization](graph-supported_dynamic_algorithm_configuration_for_multi-objective_combinatoria.md)**

:   提出 GS-MODAC，利用 GNN 将目标空间中的解映射为图结构来学习状态表征，结合 PPO 实现对多目标进化算法（MOEA）参数的动态配置，在调度和路由两类 NP-hard 组合优化问题上超越静态和已有 DRL 方法，并展现出跨问题规模和目标数量的泛化能力。

**[Heterogeneous Data Game: Characterizing the Model Competition Across Multiple Data Sources](heterogeneous_data_game_characterizing_the_model_competition_across_multiple_dat.md)**

:   提出"异构数据博弈"框架分析多ML模型提供者在异构数据源上的竞争，揭示三种PNE模式（不存在/同质化/异质化），给出不同选择模型和市场结构下PNE存在性的充分必要条件。

**[Hierarchical Reinforcement Learning with Targeted Causal Interventions](hierarchical_reinforcement_learning_with_targeted_causal_interventions.md)**

:   提出 HRC 框架，将层次强化学习中的子目标关系建模为因果图，通过因果发现算法学习子目标结构，并基于因果效应优先级进行**定向干预**，显著降低长时域稀疏奖励任务的训练代价。

**[KEA: Keeping Exploration Alive by Proactively Coordinating Exploration Strategies](kea_keeping_exploration_alive_by_proactively_coordinating_exploration_strategies.md)**

:   提出 KEA 方法，通过引入标准智能体与新颖性增强智能体的动态切换机制，主动协调不同探索策略，解决 SAC 与新颖性探索结合时因策略交互导致的冗余采样和低效探索问题。

**[Large Language Model (LLM)-enabled In-context Learning for Wireless Network Optimization](large_language_model_llm-enabled_in-context_learning_for_wireless_network_optimi.md)**

:   提出基于 LLM 上下文学习（In-context Learning）的基站功率控制算法，通过自然语言任务描述和经验池驱动的示例选择，在不更新模型参数的条件下达到接近传统深度强化学习的性能。

**[Learning Mean Field Control On Sparse Graphs](learning_mean_field_control_on_sparse_graphs.md)**

:   提出 Local Weak Mean Field Control (LWMFC) 框架，利用局部弱收敛理论将平均场控制扩展到幂律系数 γ>2 的极稀疏图上，配合两系统近似与可扩展 RL 算法，在合成和真实网络上大幅超越基于 Lp graphon 和 graphex 的方法。

**[Learning Progress Driven Multi-Agent Curriculum](learning_progress_driven_multi-agent_curriculum.md)**

:   提出 SPMARL，以基于 TD 误差的学习进度（而非回报）驱动智能体数量的自适应课程分布，解决多智能体稀疏奖励任务中回报估计高方差与信用分配困难两大问题。

**[Learning to Incentivize in Repeated Principal-Agent Problems with Adversarial Agent Arrivals](learning_to_incentivize_in_repeated_principal-agent_problems_with_adversarial_ag.md)**

:   首次研究 agent 以对抗顺序到达的重复 principal-agent 问题，在 greedy 和 smooth 两种响应模型下分别给出了紧的 regret 上下界，核心思路是将激励设计问题规约为对抗线性 bandit。

**[Learning to Trust Bellman Updates: Selective State-Adaptive Regularization for Offline RL](learning_to_trust_bellman_updates_selective_state-adaptive_regularization_for_of.md)**

:   提出选择性状态自适应正则化（SSAR），用神经网络为每个状态动态生成正则化系数，并仅在高质量动作上施加约束，统一了CQL（值正则化）和TD3+BC（策略约束）两大离线RL范式，在D4RL离线和O2O场景均大幅超越基线。

**[Leveraging Skills from Unlabeled Prior Data for Efficient Online Exploration](leveraging_skills_from_unlabeled_prior_data_for_efficient_online_exploration.md)**

:   提出 SUPE 方法，将无标签离线轨迹数据"用两次"——既用于 VAE 技能预训练，又通过 UCB 伪标签转化为高层 off-policy 数据加速在线探索，在 42 个稀疏奖励任务上全面超越已有方法。

**[Lineflow A Framework To Learn Active Control Of Production Lines](lineflow_a_framework_to_learn_active_control_of_production_lines.md)**

:   提出 LineFlow，一个可扩展的开源 Python 框架，用于模拟任意复杂度的生产线并训练 RL 智能体进行主动产线控制（自适应路由、工人重分配、调度等），同时给出了若干子问题的数学最优解作为基准。

**[Maximum Total Correlation Reinforcement Learning](maximum_total_correlation_reinforcement_learning.md)**

:   提出最大化轨迹总相关（Total Correlation）作为 RL 的归纳偏置，鼓励策略产生简单、可压缩的轨迹，从而在不牺牲任务性能的前提下显著提升对观测噪声、动作噪声和动力学变化的零样本鲁棒性。

**[Meta-Black-Box-Optimization through Offline Q-function Learning (Q-Mamba)](meta-black-box-optimization_through_offline_q-function_learning.md)**

:   提出 Q-Mamba，首个离线 MetaBBO 框架，通过 Q 函数分解 + 保守 Q 学习 + Mamba 架构，在不到在线方法一半训练预算下达到可比甚至更优的 BBO 算法配置性能。

**[Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn](mitigating_plasticity_loss_in_continual_reinforcement_learning_by_reducing_churn.md)**

:   通过 NTK 矩阵建立可塑性丧失 (plasticity loss) 与 churn（批外数据输出漂移）之间的因果联系，提出 C-CHAIN 方法在持续 RL 训练中持续抑制 churn，从而缓解可塑性丧失，在 24 个持续 RL 环境上超越已有基线。

**[Non-stationary Online Learning for Curved Losses: Improved Dynamic Regret via Mixability](non-stationary_online_learning_for_curved_losses_improved_dynamic_regret_via_mix.md)**

:   利用 mixability（可混合性）概念替代传统 KKT 分析，提出基于指数权重+fixed-share更新的连续空间在线学习框架，将弯曲损失函数（squared/logistic loss）的动态遗憾中对维度 $d$ 的依赖从 $O(d^{10/3})$ 大幅改进至 $O(d)$。

**[Of Mice And Machines A Comparison Of Learning Between Real World Mice And Rl Age](of_mice_and_machines_a_comparison_of_learning_between_real_world_mice_and_rl_age.md)**

:   系统比较真实小鼠与RL智能体在捕食者-猎物迷宫中的行为差异，发现RL缺乏自我保护本能，提出创伤启发安全缓冲（TISB）和方差惩罚TD学习（VP-TDMPC-2）两种机制，将智能体与小鼠的状态访问重叠率从20.9%提升至86.1%。

**[Online Pre-Training for Offline-to-Online Reinforcement Learning](online_pre-training_for_offline-to-online_reinforcement_learning.md)**

:   提出 OPT 方法，在离线预训练和在线微调之间引入"在线预训练"阶段，通过新增一个独立值函数并用元适应目标训练，解决离线预训练智能体因值估计不准而导致在线微调性能下降的问题，在 D4RL 基准上平均提升约 30%。

**[Pessimism Principle Can Be Effective: Towards a Framework for Zero-Shot Transfer RL](pessimism_principle_can_be_effective_towards_a_framework_for_zero-shot_transfer_.md)**

:   提出基于悲观主义原则的迁移RL框架：用鲁棒MDP构建目标域性能保守下界作为代理目标优化，设计Averaged Operator和Minimal Pessimism两种代理及分布式算法，确保安全迁移并避免负迁移。

**[Principal-Agent Bandit Games with Self-Interested and Exploratory Learning Agents](principal-agent_bandit_games_with_self-interested_and_exploratory_learning_agent.md)**

:   本文研究重复委托-代理赌臂博弈中，代理基于经验均值做决策（而非已知真实均值）且可能随机探索时，如何设计委托人的激励算法使后悔界达到 $\tilde{O}(\sqrt{T})$ 或 $\tilde{O}(T^{2/3})$，显著优于先前 $\tilde{O}(T^{11/12})$ 的结果。

**[Revise Learning To Refine At Test-Time Via Intrinsic Self-Verification](revise_learning_to_refine_at_test-time_via_intrinsic_self-verification.md)**

:   提出 ReVISE 框架，通过引入 `[refine]` 特殊 token 和两阶段课程学习（先学自验证、再学自纠错），使 LLM 在推理时能内省式地验证并修正自身推理轨迹，无需外部验证器或复杂 RL 训练。

**[Reward-free World Models for Online Imitation Learning](reward-free_world_models_for_online_imitation_learning.md)**

:   提出 IQ-MPC，一种无需显式奖励建模的世界模型在线模仿学习方法，通过逆软Q学习在潜空间中联合学习动态模型与Q函数，利用 MPPI 规划实现对高维观测和复杂动力学任务的稳定专家级模仿。

**[Robot-Gated Interactive Imitation Learning with Adaptive Intervention Mechanism](robot-gated_interactive_imitation_learning_with_adaptive_intervention_mechanism.md)**

:   提出自适应干预机制 AIM，通过学习代理 Q 函数模拟人类干预决策，让机器人主动请求专家帮助，相比不确定性基线 Thrifty-DAgger 在人类接管成本和学习效率上提升 40%。

**[Robust Noise Attenuation via Adaptive Pooling of Transformer Outputs](robust_noise_attenuation_via_adaptive_pooling_of_transformer_outputs.md)**

:   本文将 Transformer 输出的池化操作形式化为向量量化问题，证明 AvgPool 和 MaxPool 在信噪比 (SNR) 变化时存在性能崩溃风险，并提出基于交叉注意力的自适应池化方法 (AdaPool)，在理论上可在任意 SNR 下逼近信号最优量化器，在 RL、关系推理和视觉任务中均表现出优越的鲁棒性。

**[Safety Certificate against Latent Variables with Partially Unidentifiable Dynamics](safety_certificate_against_latent_variables_with_partially_unidentifiable_dynami.md)**

:   提出基于概率空间不变性条件的安全证书设计方法，利用因果强化学习从含潜变量的离线数据中学习边际化 Q 函数，在离线与在线统计分布不一致的情况下仍能保证长期安全性，并证明了安全动作的持续可行性。

**[SENSEI: Semantic Exploration Guided by Foundation Models to Learn Versatile World Models](sensei_semantic_exploration_guided_by_foundation_models_to_learn_versatile_world.md)**

:   提出 SENSEI 框架：利用 VLM 成对比较观测图像的"有趣程度"，蒸馏出语义内在奖励，再与集成不确定性驱动的新颖性奖励结合，通过世界模型实现语义有意义的无任务探索，并显著加速下游任务学习。

**[Solving Zero-Sum Convex Markov Games](solving_zero-sum_convex_markov_games.md)**

:   本文首次为两人零和凸马尔可夫博弈（cMG）中的独立策略梯度方法提供了全局收敛到Nash均衡的理论保证，通过非凸正则化将问题化归为非凸-pPL min-max优化，并设计了嵌套/交替策略梯度算法。

**[The Sample Complexity of Online Strategic Decision Making with Information Asymmetry and Knowledge Transportability](the_sample_complexity_of_online_strategic_decision_making_with_information_asymm.md)**

:   在信息不对称（代理拥有隐私类型和动作作为混淆变量）且需要跨分布知识迁移的在线强化学习场景中，提出基于非参数工具变量（NPIV）方法的模型算法 OPME，证明以 $\tilde{O}(1/\epsilon^2)$ 样本复杂度学得 $\epsilon$-最优策略，并匹配对应下界。

**[VinePPO: Refining Credit Assignment in RL Training of LLMs](vineppo_refining_credit_assignment_in_rl_training_of_llms.md)**

:   VinePPO 利用语言环境可从任意中间状态重置的特性，用蒙特卡洛 (MC) rollout 替换 PPO 中的 value network 进行无偏值估计，在数学推理任务上以更少的墙钟时间（最高 3 倍加速）超越 PPO/GRPO/RLOO 的峰值性能，并展现出更强的泛化斜率。

**[Wasserstein Policy Optimization](wasserstein_policy_optimization.md)**

:   提出 Wasserstein Policy Optimization (WPO)，将最优传输理论中的 Wasserstein 梯度流投影到参数空间，得到一种兼具确定性策略梯度（DPG）利用动作值梯度和经典随机策略梯度（SPG）支持任意分布的闭式更新规则，无需重参数化技巧。

**[Zero-Shot Generalization of Vision-Based RL Without Data Augmentation](zero-shot_generalization_of_vision-based_rl_without_data_augmentation.md)**

:   提出 ALDA（Associative Latent DisentAnglement），通过解耦表示学习+联想记忆机制实现视觉RL在未见环境中的零样本泛化，无需数据增强即可媲美使用千万级外部数据的方法。
