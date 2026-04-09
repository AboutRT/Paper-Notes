<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎮 强化学习

**🔬 ICLR2026** · 共 **80** 篇

**[AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](abstral_augmenting_llms_reasoning_by_reinforcing_abstract_thinking.md)**

:   提出 AbstRaL，通过强化学习教 LLM 学习推理问题的数学抽象（将具体数字/名称替换为符号变量、提取通用公式），然后用符号求解器推导答案，在 GSM 扰动 benchmark 上几乎完全消除了分布偏移导致的性能下降，并在 OOD 数学/通用推理任务上也有隐式提升。

**[APPLE: Toward General Active Perception via Reinforcement Learning](apple_toward_general_active_perception_via_reinforcement_learning.md)**

:   提出APPLE——一种结合强化学习与监督学习的通用主动感知框架，将主动感知建模为POMDP，奖励函数设计为RL奖励减去预测损失，梯度自然分解为策略梯度和预测损失梯度两部分，基于off-policy算法（SAC/CrossQ）和共享ViViT骨干网络，在5个不同任务基准上验证通用性，其中CrossQ变体无需逐任务调参且训练效率提高53%。

**[ARM-FM: Automated Reward Machines via Foundation Models for Compositional Reinforcement Learning](arm-fm_automated_reward_machines_via_foundation_models_for_compositional_reinfor.md)**

:   提出ARM-FM框架，利用基础模型（GPT-4o等）从自然语言任务描述自动生成语言对齐奖励机器（LARM）——包括自动机结构、可执行标签函数和每个状态的自然语言描述——为RL agent提供组合式密集奖励信号，在MiniGrid/Craftium(3D Minecraft)/Meta-World等环境中解决标准RL完全无法学习的稀疏奖励长程任务，并实现零样本任务泛化。

**[Autoqd Automatic Discovery Of Diverse Behaviors With Quality-Diversity Optimizat](autoqd_automatic_discovery_of_diverse_behaviors_with_quality-diversity_optimizat.md)**

:   提出 AutoQD，利用占用度量 (occupancy measure) 的随机 Fourier 特征嵌入自动生成行为描述子 (behavioral descriptor)，替代传统 QD 优化中的手工设计描述子，在 6 个连续控制任务上展现了强大的多样化策略发现能力。

**[Autotool Automatic Scaling Of Tool-Use Capabilities In Rl Via Decoupled Entropy ](autotool_automatic_scaling_of_tool-use_capabilities_in_rl_via_decoupled_entropy_.md)**

:   提出解耦自适应熵约束 (Decoupled Adaptive Entropy Constraints) 的强化学习策略，使 LLM 在工具调用任务中根据问题难度自动切换长/短推理模式，在提升 9.8% 准确率的同时减少约 81% 的推理 token 开销。

**[AWM: Accurate Weight-Matrix Fingerprint for Large Language Models](awm_accurate_weight-matrix_fingerprint_for_large_language_models.md)**

:   提出 AWM，一种无需训练的 LLM 权重矩阵指纹方法，利用线性分配问题（LAP）恢复嵌入层的置换和符号翻转，再用无偏 CKA 消除 Q/K 矩阵的正交变换影响，在 150 对 LLM 上实现完美 AUC（1.0），对 SFT、持续预训练（5.5T token）、RL、多模态扩展、剪枝、upcycling 六类后训练均鲁棒，30 秒内完成。

**[BA-MCTS: Bayes Adaptive Monte Carlo Tree Search for Offline Model-based RL](bayes_adaptive_monte_carlo_tree_search_for_offline_model-based_reinforcement_lea.md)**

:   首次将贝叶斯自适应 MDP（BAMDP）引入离线模型基 RL，提出 Continuous BAMCP 解决连续状态/动作空间的贝叶斯规划，结合悲观奖励惩罚和搜索基策略迭代（"RL + Search"范式），在 D4RL 12 个任务上显著超越 19 个基线（Cohen's $d > 1.8$），并成功应用于核聚变 tokamak 控制。

**[Boolean Satisfiability via Imitation Learning](boolean_satisfiability_via_imitation_learning.md)**

:   提出 ImitSAT，首个基于模仿学习的 CDCL 求解器分支策略：通过将求解器运行压缩为无冲突的 KeyTrace 专家序列，将分支决策建模为前缀条件的自回归预测任务，以少量查询预算显著减少传播次数和求解时间，并在结构化 SAT 问题上展现良好泛化能力。

**[Breaking Barriers: Do Reinforcement Post Training Gains Transfer To Unseen Domains?](breaking_barriers_do_reinforcement_post_training_gains_transfer_to_unseen_domain.md)**

:   通过观察性研究（18 个开源 RPT 模型）和干预性研究（单域 GRPO 训练），系统揭示了强化后训练（RPT/RLVR）的泛化局限：RPT 在训练域内提升显著，但跨域泛化不一致——结构化域（数学↔代码）可互相迁移，但无法泛化到非结构化域（法律/金融/医疗），且这一结论跨算法、模型规模和训练步数保持一致。

**[Breaking the SFT Plateau: Multimodal Structured Reinforcement Learning for Chart-to-Code Generation](breaking_the_sft_plateau_multimodal_structured_reinforcement_learning_for_chart-.md)**

:   针对图表到代码生成任务中SFT的性能瓶颈问题，提出多模态结构化强化学习（MSRL），通过文本+视觉双层奖励函数和两阶段RL策略，在ChartMimic和ReachQA上分别提升6.2%和9.9%的高层指标，达到开源SOTA并媲美GPT-4o。

**[Chain-of-Context Learning: Dynamic Constraint Understanding for Multi-Task VRPs](chain-of-context_learning_dynamic_constraint_understanding_for_multi-task_vrps.md)**

:   提出 Chain-of-Context Learning (CCL)，通过 Relevance-Guided Context Reformulation（RGCR，自适应聚合约束信息构建上下文）和 Trajectory-Shared Node Re-embedding（TSNR，跨轨迹共享节点更新避免冗余计算）实现逐步动态的约束感知解码，在 48 种 VRP 变体（16 分布内 + 32 分布外）上全面超越现有方法。

**[Co-rewarding: Stable Self-supervised RL for Eliciting Reasoning in Large Language Models](co-rewarding_stable_self-supervised_rl_for_eliciting_reasoning_in_large_language.md)**

:   Co-rewarding 提出自监督 RL 框架，通过数据侧（对比改写问题的跨视角一致性）和模型侧（EMA 教师模型提供伪标签）两种互补监督方式，解决自奖励 RL 中的训练崩溃问题，在无人工标签条件下多项数学推理基准上达到甚至超过 RLVR（有标签）的性能。

**[Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning](continuous-time_value_iteration_for_multi-agent_reinforcement_learning.md)**

:   提出 VIP（Value Iteration via PINN）框架，首次将物理信息神经网络（PINN）用于求解连续时间多智能体强化学习中的 HJB 偏微分方程，并引入 Value Gradient Iteration（VGI）模块迭代精炼价值梯度，在连续时间 MPE 和 MuJoCo 多智能体任务上始终优于离散时间和连续时间基线。

**[Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning](controllable_exploration_in_hybrid-policy_rlvr_for_multi-modal_reasoning.md)**

:   CalibRL 将专家数据重新定义为分布校准基线（而非严格模仿目标），通过 LeakyReLU 不对称激活 + 优势加权实现对 MLLM 推理训练中探索-利用平衡的精细控制，解决 RLVR 中的熵崩溃问题，在几何推理等任务上大幅超越 GRPO/DAPO。

**[Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets](cross-embodiment_offline_reinforcement_learning_for_heterogeneous_robot_datasets.md)**

:   系统研究跨形态离线 RL 预训练范式，发现次优数据比例和机器人多样性增加时梯度冲突导致负迁移，提出基于形态图距离的 Embodiment Grouping（EG）策略将机器人按形态聚类后分组更新 actor，在 16 种机器人平台的 locomotion benchmark 上显著缓解负迁移（70% 次优数据集上 IQL+EG 比 IQL 提升 34%）。

**[CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning](cuda-l1_improving_cuda_optimization_via_contrastive_reinforcement_learning.md)**

:   提出 CUDA-L1，一个基于对比强化学习（Contrastive RL）的三阶段流水线框架，将初始 CUDA 能力较弱的 LLM 训练为高效的 CUDA 优化器，在 KernelBench 的 250 个 CUDA 内核上实现平均 3.12× 加速，峰值达 120×，并可跨 GPU 架构迁移。

**[Deep SPI: Safe Policy Improvement via World Models](deep_spi_safe_policy_improvement_via_world_models.md)**

:   构建了安全策略改进（SPI）的理论框架，将世界模型和表示学习与策略更新保证统一起来：通过基于重要性比率的邻域算子约束策略更新，确保单调改进和收敛；结合局部转移/奖励损失控制世界模型质量和表示稳定性，提出 DeepSPI 算法在 ALE-57 基准上匹配或超越 PPO 和 DeepMDP。

**[DiVE-k: Differential Visual Reasoning for Fine-grained Image Recognition](dive-k_differential_visual_reasoning_for_fine-grained_image_recognition.md)**

:   提出 DiVE-k 框架，利用大视觉语言模型自身的 top-k 生成结果构造选择题，通过 GRPO 强化学习训练模型进行差异化视觉推理，在细粒度图像识别的 base-to-novel 泛化上大幅超越现有方法。

**[Divide, Harmonize, Then Conquer It: Shooting Multi-Commodity Flow Problems with Multimodal Language Models](divide_harmonize_then_conquer_it_shooting_multi-commodity_flow_problems_with_mul.md)**

:   提出 Pram 框架，首次利用多模态语言模型（MLM）求解多商品流（MCF）问题，通过分区将原问题分解为子问题，以多智能体强化学习（MARL）协调各子问题的全局一致性，理论证明收敛到最优解，实测速度比 LP 快 1-2 个数量级且性能接近最优。

**[Dual-Robust Cross-Domain Offline Reinforcement Learning Against Dynamics Shifts](dual-robust_cross-domain_offline_reinforcement_learning_against_dynamics_shifts.md)**

:   首次同时解决跨域离线 RL 的"训练时鲁棒性"（源域-目标域不匹配）和"测试时鲁棒性"（部署环境动态偏移）：提出 DROCO，通过 Robust Cross-Domain Bellman (RCB) 算子对源域数据施加鲁棒 Bellman 更新、对目标域数据施加标准更新，将动态不确定性映射为可处理的状态扰动。

**[DVLA-RL: Dual-Level Vision-Language Alignment with Reinforcement Learning Gating for Few-Shot Learning](dvla-rl_dual-level_vision-language_alignment_with_reinforcement_learning_gating_.md)**

:   提出 DVLA-RL 框架，通过双层语义构建（DSC）生成互补的低层属性和高层描述，并以 RL 门控注意力（RLA）动态平衡自注意力和交叉注意力在不同网络层的贡献，实现从低层到高层的层次化视觉-语言对齐，在 9 个少样本学习基准上达到 SOTA。

**[Echo: Towards Advanced Audio Comprehension via Audio-Interleaved Reasoning](echo_towards_advanced_audio_comprehension_via_audio-interleaved_reasoning.md)**

:   提出音频交错推理（audio-interleaved reasoning）新范式，将音频视为推理过程中的主动组件而非静态上下文，使 LALM 在推理时动态定位并重新聆听音频片段。通过 SFT+RL 两阶段训练框架和结构化数据生成流水线，构建 Echo 模型，在专家级和通用音频理解基准上超越 GPT-4o 和 Gemini-2.0-Flash。

**[Efficient Estimation of Kernel Surrogate Models for Task Attribution](efficient_estimation_of_kernel_surrogate_models_for_task_attribution.md)**

:   提出核代理模型（KernelSM）用于任务归因，通过 RBF 核岭回归捕获任务间的非线性交互效应，结合梯度投影的高效估计算法避免重复训练，在数学推理、上下文学习和多目标 RL 等场景下相比线性代理和影响函数基线提升 25% 相关性。

**[EGG-SR: Embedding Symbolic Equivalence into Symbolic Regression via Equality Graph](egg-sr_embedding_symbolic_equivalence_into_symbolic_regression_via_equality_grap.md)**

:   提出 Egg-SR 统一框架，通过等价图（e-graph）将符号等价性嵌入 MCTS、DRL 和 LLM 三类符号回归方法中，分别实现子树剪枝、梯度方差降低和反馈提示增强。理论证明 Egg-MCTS 收紧遗憾界、Egg-DRL 降低梯度估计方差，实验验证一致提升表达式发现精度。

**[Emergence of Spatial Representation in an Actor-Critic Agent with Hippocampus-Inspired Sequence Generator](emergence_of_spatial_representation_in_an_actor-critic_agent_with_hippocampus-in.md)**

:   受海马体 CA3 区内在递归回路启发，提出最小序列生成器（shift register）与 actor-critic 结合，在稀疏视觉输入下实现迷宫导航，同时涌现出位置场、DG 正交化、距离相关空间核和任务依赖重映射等神经生物学现象。

**[Empowering Small VLMs to Think with Dynamic Memorization and Exploration](empowering_small_vlms_to_think_with_dynamic_memorization_and_exploration.md)**

:   提出 DyME（Dynamic Memorize-Explore），通过逐步动态切换 SFT 记忆模式与 GRPO 探索模式，首次赋予小规模视觉语言模型（<1B 参数）在特定任务上的思维推理能力。

**[Entropy-Preserving Reinforcement Learning (REPO / ADAPO)](entropy-preserving_reinforcement_learning.md)**

:   本文揭示了策略梯度 RL 算法在 LLM 后训练中系统性导致策略熵坍缩的理论根因（优势函数与对数概率的正相关性），并提出两种互补的解法：REPO（通过修改优势函数去相关）和 ADAPO（自适应非对称裁剪），在交互式工具使用任务上实现 SOTA 性能。

**[Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward](exploration_vs_exploitation_rethinking_rlvr_through_clipping_entropy_and_spuriou.md)**

:   通过理论推导和跨模型实验，证明 RLVR 中裁剪偏差提供的学习信号可忽略不计（≤1/17），真正起作用的是裁剪对策略熵的隐式压缩效应，并提出奖励误标模型解释为何随机奖励能让强模型获益。

**[FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning](fapo_flawed-aware_policy_optimization_for_efficient_and_reliable_reasoning.md)**

:   针对 RLVR 训练中"答案正确但推理有缺陷"的 flawed-positive rollout 问题，提出 FAPO 算法：用 GenRM 检测缺陷推理，通过无参数奖励惩罚机制实现"先利用后抑制"的自然学习轨迹，同时提升结果正确性、过程可靠性和训练稳定性。

**[Flow Actor-Critic for Offline Reinforcement Learning (FAC)](flow_actor-critic_for_offline_reinforcement_learning.md)**

:   FAC 首次联合利用流模型（continuous normalizing flow）同时构建表达力强的 actor 策略和基于精确密度估计的 critic 惩罚机制，通过识别 OOD 区域对 Q 值进行选择性保守估计，在 OGBench 55 个任务上以 60.3 平均分大幅超越此前最佳的 43.6。

**[From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for RL of Open-ended Generation](from_verifiable_dot_to_reward_chain_harnessing_verifiable_reference-based_reward.md)**

:   提出 RLVRR 框架，将 RLVR（强化学习+可验证奖励）从数学/代码推理扩展到开放式文本生成：从高质量参考答案中提取关键词序列（内容奖励）和可执行 Python 检查函数（风格奖励），构成"奖励链"替代单点验证信号，在 10+ 个 benchmark 上以 10K 数据超越 100K SFT 和高级奖励模型。

**[Helix: Evolutionary Reinforcement Learning for Open-Ended Scientific Problem Solving](helix_evolutionary_reinforcement_learning_for_open-ended_scientific_problem_solv.md)**

:   提出 HELIX 框架，将强化学习（GRPO）与进化算法（NSGA-II）结合用于开放式科学问题求解：RL 迭代优化策略，进化机制平衡解的质量与多样性，in-context learning 利用历史解指导探索，仅用 14B 模型在圆填充、机器学习任务等 20 个任务中超越 GPT-4o 流水线。

**[How LLMs Learn to Reason: A Complex Network Perspective](how_llms_learn_to_reason_a_complex_network_perspective.md)**

:   从复杂网络视角统一解释RLVR训练的四大谜题（两阶段学习曲线、V型回复长度、灾难性遗忘、策略坍缩），提出稀疏概念网假说（平均度≈2），并据此设计Annealed-RLVR算法在Minerva和AIME上超越标准RLVR。

**[Is Pure Exploitation Sufficient in Exogenous MDPs with Linear Function Approximation?](is_pure_exploitation_sufficient_in_exogenous_mdps_with_linear_function_approxima.md)**

:   证明在外生MDP（Exo-MDP，不确定性仅来自独立于智能体动作的外生输入）中，纯利用（无探索）策略即可达到次线性遗憾界——表格情形下PTO算法达到 $\tilde{O}(H^2|\Xi|\sqrt{K})$，线性函数逼近下LSVI-PE算法遗憾与特征维度和外生状态空间多项式相关、与内生状态/动作空间无关。

**[LadderSym: A Multimodal Interleaved Transformer for Music Practice Error Detection](laddersym_a_multimodal_interleaved_transformer_for_music_practice_error_detectio.md)**

:   提出LadderSym架构解决音乐练习错误检测任务，通过交替式跨流对齐模块（Ladder）克服晚期融合的对齐不足，并用符号乐谱提示（Sym）减少纯音频乐谱的频率歧义，在MAESTRO-E上将漏音F1从26.8%提升到56.3%。

**[Latent Wasserstein Adversarial Imitation Learning](latent_wasserstein_adversarial_imitation_learning.md)**

:   提出LWAIL方法，用ICVF从少量随机数据学习动态感知的潜空间表示，将Wasserstein距离的"地面度量"从欧氏距离升级为潜空间距离，仅用单条状态轨迹即可达到专家级模仿性能。

**[Learning from Synthetic Data Improves Multi-hop Reasoning](learning_from_synthetic_data_improves_multi-hop_reasoning.md)**

:   发现在完全虚构的规则生成合成数据上做RLVR训练，能显著提升LLM在真实多跳推理任务上的表现（Qwen3-0.6B提升56%-131%），因为模型学到了知识组合这一通用推理技能而非记忆事实知识。

**[Learning to Generate Unit Test via Adversarial Reinforcement Learning](learning_to_generate_unit_test_via_adversarial_reinforcement_learning.md)**

:   提出UTRL框架，通过对抗RL迭代训练单元测试生成器和代码生成器——测试生成器学习生成能区分LLM代码与正确代码的判别性测试用例，代码生成器学习通过这些测试——Qwen3-4B训练后超越GPT-4.1的测试生成质量。

**[Learning to Orchestrate Agents in Natural Language with the Conductor](learning_to_orchestrate_agents_in_natural_language_with_the_conductor.md)**

:   用RL训练7B的Conductor模型，通过自然语言输出Agent工作流(子任务分配+通信拓扑)来协调GPT-5/Claude/Gemini等大模型，在LiveCodeBench和GPQA等benchmark上超越所有单模型和多Agent基线，达到SOTA(平均77.27 vs GPT-5的74.78)。

**[Learning to Play Multi-Follower Bayesian Stackelberg Games](learning_to_play_multi-follower_bayesian_stackelberg_games.md)**

:   首次研究多追随者贝叶斯Stackelberg博弈的在线学习问题，通过几何化最佳响应区域实现类型反馈下 $\tilde{O}(\sqrt{\min\{L, nK\} \cdot T})$ 的遗憾界（关于追随者数n不呈多项式增长），并提供几乎匹配的下界。

**[LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Rewards](longrlvr_long-context_reinforcement_learning_requires_verifiable_context_rewards.md)**

:   提出 LongRLVR，通过在 RLVR 训练中引入可验证的上下文奖励（context reward），解决长上下文场景下仅靠最终答案奖励导致的上下文定位（grounding）梯度消失问题，显著提升 LLM 长上下文推理能力。

**[LoongRL: Reinforcement Learning for Advanced Reasoning over Long Contexts](loongrl_rl_for_reasoning_long_contexts.md)**

:   提出 LoongRL，通过构建 KeyChain 合成数据进行强化学习训练，使 LLM 涌现出 plan–retrieve–reason–recheck 的长上下文推理模式，仅在 16K 上下文上训练即可泛化到 128K，14B 模型达到 74.2 分接近 o3-mini (74.5) 和 DeepSeek-R1 (74.9)。

**[MARS-Sep: Multimodal-Aligned Reinforced Sound Separation](mars-sep_multimodal-aligned_reinforced_sound_separation.md)**

:   将声源分离重新定义为偏好对齐问题（类似LLM的RLHF），提出MARS-Sep框架用因子化Beta掩码策略+多模态奖励模型+信任域优化，使分离结果不仅信号干净还与查询语义对齐，在文本/音频/图像引导分离中同时提升信号指标和CLAP语义分数。

**[MENLO: From Preferences to Proficiency -- Evaluating and Modeling Native-like Quality Across 47 Languages](menlo_from_preferences_to_proficiency_--_evaluating_and_modeling_native-like_qua.md)**

:   提出Menlo框架，基于受众设计理论将LLM母语级质量评估分解为4个维度（流畅度/语气/本地化语气/本地化事实），构建47种语言6423标注对的数据集(IAA=0.84)，RL微调的评审模型达到人类标注水平，并可作为生成式奖励模型改善LLM多语言能力。

**[MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding](mergemix_a_unified_augmentation_paradigm_for_visual_and_multi-modal_understandin.md)**

:   提出MergeMix统一训练范式，通过Token Merge生成注意力感知的混合图像作为偏好对中的"输者"，用混合比作为软偏好margin通过mixed SimPO损失优化，在SFT和RL之间找到效率-对齐性-稳定性的平衡点，在图像分类和MLLM基准上均达到SOTA。

**[Metis-SPECS: Decoupling Multimodal Learning via Self-distilled Preference-based Cold Start for VLMs](metis-specs_decoupling_multimodal_learning_via_self-distilled_preference-based_c.md)**

:   提出SPECS框架将VLM的冷启动从SFT替换为DPO偏好训练——通过自蒸馏生成只关注输出格式的偏好数据，DPO冷启动专注表层形式学习(格式/结构/风格)而非内容记忆，为后续GRPO的深层推理学习提供更好的起点，MEGA-Bench+4.1%、MathVista+12.2%。

**[ROMI: Model-based Offline RL via Robust Value-Aware Model Learning with Implicitly Differentiable Adaptive Weighting](model-based_offline_rl_via_robust_value-aware_model_learning_with_implicitly_dif.md)**

:   ROMI 通过 Wasserstein 对偶将动力学不确定集转化为状态不确定集来实现鲁棒的价值感知模型学习，并用隐式可微的自适应加权机制平衡动力学精度与价值感知，解决了 RAMBO 方法中的 Q 值低估和梯度爆炸问题，在 D4RL 和 NeoRL 上达到模型基离线 RL 的 SOTA。

**[Model Predictive Adversarial Imitation Learning for Planning from Observation](model_predictive_adversarial_imitation_learning_for_planning_from_observation.md)**

:   提出 MPAIL（Model Predictive Adversarial Imitation Learning），将 MPPI 规划器嵌入对抗模仿学习循环，首次实现端到端的仅观测规划框架（Planning-from-Observation），在泛化性、鲁棒性、可解释性和样本效率上全面优于基于策略的 AIL 方法，并在真实世界机器人导航中从单条观测演示成功部署。

**[MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation](momagen_generating_demonstrations_under_soft_and_hard_constraints_for_multi-step.md)**

:   MoMaGen 将双臂移动操作的演示数据生成建模为约束优化问题，通过硬约束（可达性、无碰撞、可见性）和软约束（导航中物体可见性、收回紧凑姿态）的协同，从单个人类遥操作演示自动生成大规模多样化数据集，训练出的视觉运动策略仅用 40 个真实演示微调即可部署到实体机器人。

**[MVR: Multi-view Video Reward Shaping for Reinforcement Learning](mvr_multi-view_video_reward_shaping_for_reinforcement_learning.md)**

:   提出 MVR 框架，利用多视角视频的视频-文本相似度学习状态相关性函数，结合状态依赖的奖励塑形（自动衰减 VLM 引导），在 HumanoidBench 和 MetaWorld 共 19 个任务上超越现有 VLM 奖励方法。

**[On Discovering Algorithms for Adversarial Imitation Learning](on_discovering_algorithms_for_adversarial_imitation_learning.md)**

:   用LLM引导的进化搜索自动发现对抗性模仿学习(AIL)的奖励赋值(RA)函数——将AIL分解为密度比估计(判别器)+奖励赋值(密度比→标量奖励)两阶段，发现的DAIL算法在未见环境和策略优化器上泛化且超越人工设计的GAIL/AIRL/FAIRL，分析揭示DAIL通过提供更informative的梯度信号实现更稳定训练。

**[On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification](on_the_generalization_of_sft_a_reinforcement_learning_perspective_with_reward_re.md)**

:   从RL策略梯度视角数学证明SFT梯度隐式编码了逆概率加权(1/π_θ)的病态奖励结构→低概率token梯度过大导致泛化受限，提出DFT(Dynamic Fine-Tuning)仅需一行代码修改(CE loss乘token概率：$-p\log p$)消除逆概率加权→在数学推理/代码生成/多模态任务上大幅超越SFT，离线RL设定下甚至超越GRPO/PPO。

**[On the $O(1/T)$ Convergence of Alternating Gradient Descent-Ascent in Bilinear Games](on_the_o1t_convergence_of_alternating_gradient_descent-ascent_in_bilinear_games.md)**

:   首次证明交替梯度下降上升（AltGDA）在有约束双线性零和博弈中以 $O(1/T)$ 速率收敛到Nash均衡（存在内部NE时），比同步GDA的 $O(1/\sqrt{T})$ 快，用能量函数衰减刻画轨迹碰撞边界时的"摩擦"效应，并通过性能估计编程（PEP）进一步优化步长。

**[One Model for All Tasks: Leveraging Efficient World Models in Multi-Task Planning](one_model_for_all_tasks_leveraging_efficient_world_models_in_multi-task_planning.md)**

:   提出 ScaleZero，通过在统一世界模型中引入 MoE 架构解决多任务学习中的梯度冲突和可塑性崩塌问题，结合动态参数扩展（DPS）策略自适应分配模型容量，单个多任务模型在 Atari/DMC/Jericho 三个基准上达到与单任务专家模型相当的性能，同时减少约 28.5% 的环境交互。

**[Online Minimization of Polarization and Disagreement via Low-Rank Matrix Bandits](online_minimization_of_polarization_and_disagreement_via_low-rank_matrix_bandits.md)**

:   将社交网络中极化与分歧最小化问题建模为在线低秩矩阵bandit问题，提出两阶段算法OPD-Min-ESTR（先估计子空间再低维线性bandit），将维度从 $|V|^2$ 降至 $O(|V|)$，实现 $\tilde{O}(\max\{1/\kappa, \sqrt{|V|}\}\sqrt{|V|T})$ 累积遗憾。

**[Optimistic Task Inference for Behavior Foundation Models](optimistic_task_inference_behavior_models.md)**

:   提出 OpTI-BFM——在 Behavior Foundation Model 测试时，不需要完整奖励函数或标注数据集，而是通过与环境交互仅 5 个 episode 即可推断任务并恢复 Oracle 性能，核心是利用 successor features 的线性结构将任务推断归约为线性 bandit 问题并用 UCB 策略乐观探索，提供正式的 regret bound。

**[Partially Equivariant Reinforcement Learning in Symmetry-Breaking Environments](partially_equivariant_reinforcement_learning_in_symmetry-breaking_environments.md)**

:   提出部分群不变MDP(PI-MDP)框架解决RL中的对称性破缺问题——分析证明局部对称性违反通过Bellman backup在整个状态-动作空间产生全局值估计误差，PI-MDP在对称区域使用等变更新、在破缺区域回退到标准更新→阻止误差传播，开发PE-DQN(离散)和PE-SAC(连续)算法在Grid-World/运动/操作任务上显著超越严格和近似等变基线。

**[PolicyFlow: Policy Optimization with Continuous Normalizing Flow in Reinforcement Learning](policyflow_policy_optimization_with_continuous_normalizing_flow_in_reinforcement.md)**

:   提出PolicyFlow——将连续归一化流(CNF)策略与PPO式目标结合的在线RL算法：通过沿插值路径评估速度场变化近似重要性比率(避免全流路径昂贵的反向传播)，提出受布朗运动启发的隐式熵正则器(促进单调熵增长防止模式坍缩)，在MultiGoal/PointMaze/IsaacLab/MuJoCo上超越高斯PPO和流式基线(FPO/DPPO)，特别擅长多模态动作分布。

**[Post-training Large Language Models for Diverse High-Quality Responses](post-training_large_language_models_for_diverse_high-quality_responses.md)**

:   提出 DQO（Diversity Quality Optimization），基于行列式点过程（DPP）在语义嵌入空间中定义多样性度量，将其与奖励信号联合优化，使 LLM 后训练同时提升语义多样性和响应质量，可叠加在 GRPO/PPO 之上。

**[PreferThinker: Reasoning-based Personalized Image Preference Assessment](preferthinker_reasoning-based_personalized_image_preference_assessment.md)**

:   提出PreferThinker——基于推理的个性化图像偏好评估系统：引入由15种视觉元素组成的偏好画像作为用户间桥梁，构建6万用户的CoT风格数据集(PreferImg-CoT)，采用"预测偏好画像→多维可解释评分"的predict-then-assess范式，通过冷启动SFT+GRPO强化学习+相似度感知预测奖励实现结构化推理，在个性化偏好评估上超越SOTA。

**[Principled Fast and Meta Knowledge Learners for Continual Reinforcement Learning](principled_fast_and_meta_knowledge_learners_for_continual_reinforcement_learning.md)**

:   受人脑海马体-大脑皮层交互机制启发，提出 FAME 双学习器框架，通过快速学习器进行知识迁移、元学习器进行知识整合，在原则性地最小化灾难性遗忘的前提下实现高效的持续强化学习。

**[QuRL: Efficient Reinforcement Learning with Quantized Rollout](qurl_efficient_reinforcement_learning_with_quantized_rollout.md)**

:   提出QuRL——用量化actor加速RL训练的rollout阶段：量化actor生成序列(占训练70%时间)+全精度actor做梯度更新→提出自适应裁剪范围(ACR)防止长期训练崩溃(量化/全精度策略分歧累积)+更新感知量化(UAQ用不变缩放放大权重变化超过量化粒度)→INT8/FP8量化实现20-80%rollout加速且性能不降甚至微升。

**[Reasoning Boosts Opinion Alignment in LLMs](reasoning_boosts_opinion_alignment_in_llms.md)**

:   用GRPO强化学习训练LLM从政治调查数据中学习推理式观点对齐，在美国/德国/瑞士三个数据集上证明推理能提升个体级政治观点建模的准确性。

**[RebuttalAgent: Strategic Persuasion in Academic Rebuttal via Theory of Mind](rebuttalagent_strategic_persuasion_in_academic_rebuttal_via_theory_of_mind.md)**

:   提出RebuttalAgent——首个将心智理论(ToM)融入学术rebuttal的框架：通过ToM-Strategy-Response三阶段(建模审稿人心理状态→制定说服策略→生成证据基础响应)，用RebuttalBench(7万+样本)做SFT+自奖励RL训练，开发Rebuttal-RM评估器(10万+样本,超越GPT-4.1的人类一致性)→平均超越基础模型18.3%,与SOTA闭源模型可比。

**[References Improve LLM Alignment in Non-Verifiable Domains](references_improve_llm_alignment_in_non-verifiable_domains.md)**

:   提出参考引导的LLM-as-Judge方法(RefEval)，用高质量参考输出作为"软验证器"，使LLM-judge准确率提升6.8%；进而构建两阶段自改进流程(SFT蒸馏+参考引导DPO)，在AlpacaEval/Arena-Hard上分别超过SFT蒸馏+19.2/+16.5，匹配微调奖励模型ArmoRM的性能，证明无需人类偏好标注即可实现非可验证域的高效LLM对齐。

**[Regret-Guided Search Control for Efficient Learning in AlphaZero](regret-guided_search_control_for_efficient_learning_in_alphazero.md)**

:   提出 RGSC（Regret-Guided Search Control）框架，通过训练一个 regret 网络识别高遗憾值状态并优先从这些状态重新开始自我对弈，模拟人类"反复复盘错误"的学习方式，在 9×9 围棋、10×10 黑白棋和 11×11 Hex 上平均超越 AlphaZero 77 Elo。

**[Pruning as a Cooperative Game: Surrogate-Assisted Layer Contribution Estimation for Large Language Models](remix_reinforcement_routing_for_mixtures_of_loras_in_llm_finetuning.md)**

:   将LLM层剪枝建模为合作博弈（每层=玩家，模型性能=效用）→精确Shapley值计算不可行（$2^L$种组合）→提出两阶段近似：(1)分层蒙特卡洛采样生成mask+评估PPL作为监督信号→(2)训练轻量代理网络预测任意mask的性能→高效估算每层Shapley值→捕获层间依赖→显著优于静态启发式剪枝基线。

**[Retaining Suboptimal Actions to Follow Shifting Optima in Multi-Agent RL](retaining_suboptimal_actions_to_follow_shifting_optima_in_multi-agent_reinforcem.md)**

:   提出S2Q解决合作MARL中值函数最优点在训练中漂移→次优收敛：逐步学习K个sub-value函数保留替代高价值动作+Softmax行为策略持续探索→最优变化时快速适应，SMAC Hard+和GRF上一致超越基线。

**[Robust Deep Reinforcement Learning against Adversarial Behavior Manipulation](robust_deep_reinforcement_learning_against_adversarial_behavior_manipulation.md)**

:   本文研究 RL 中一种新型威胁——行为目标攻击（adversary 通过篡改观测来引导 victim 执行特定目标策略），提出不需要白盒访问的 BIA 攻击方法和基于时间折扣的 TDRT 防御方法，TDRT 在保持对攻击鲁棒性的同时比现有防御（SA-PPO）的原始任务性能高 28.2%。

**[Routing, Cascades, and User Choice for LLMs](routing_cascades_and_user_choice_for_llms.md)**

:   将 LLM 路由建模为 provider-user Stackelberg 博弈，证明最优路由策略几乎总是静态无级联的阈值规则，并揭示当模型质量排序与成本排序不一致时产生的用户-提供商不对齐问题，以及低流失惩罚下 provider 有动机通过增加延迟来降低成本。

**[Self-Harmony: Learning to Harmonize Self-Supervision and Self-Play in Test-Time Reinforcement Learning](self-harmony_learning_to_harmonize_self-supervision_and_self-play_in_test-time_r.md)**

:   提出 Self-Harmony 框架，通过让单一模型扮演两个角色（Solver 求解原始问题 + Reframer 改述问题），将答案在原始和改述视角下的调和平均得分作为伪标签选择标准，替代传统多数投票，在 30 个实验设置中 28 个达到 SOTA，且训练零失败。

**[Self-Improving Skill Learning for Robust Skill-based Meta-Reinforcement Learning](self-improving_skill_learning_for_robust_skill-based_meta-reinforcement_learning.md)**

:   提出 SISL（Self-Improving Skill Learning），通过解耦高层策略和技能改进策略，结合最大回报重标注的技能优先级机制，在噪声离线演示数据下实现鲁棒的技能学习，显著提升基于技能的元强化学习在长时域任务中的性能。

**[Single Index Bandits: Generalized Linear Contextual Bandits with Unknown Reward Functions](single_index_bandits_generalized_linear_contextual_bandits_with_unknown_reward_f.md)**

:   提出单指标赌博机（SIB）问题——将广义线性赌博机扩展到奖励函数未知的设定，基于 Stein 方法设计了一族高效算法（STOR/ESTOR/GSTOR），在单调递增奖励函数下实现了近最优遗憾界 $\tilde{O}(\sqrt{T})$。

**[Solving Football by Exploiting Equilibrium Structure of 2p0s Differential Games with One-Sided Information](solving_football_by_exploiting_equilibrium_structure_of_2p0s_differential_games_.md)**

:   证明单边信息二人零和微分博弈中 Nash 均衡策略的原子结构——知情玩家 P1 的均衡策略集中在至多 $I$ 个动作原型上（$I$ = 博弈类型数），使博弈树复杂度从 $U^{2K}$ 降到 $I^K$，在美式足球 11v11 连续动作空间中（传统复杂度 $10^{440}$）实现 M1 MacBook 30 分钟求解。

**[Toward a Dynamic Stackelberg Game-Theoretic Framework for Agent-Based Conversational AI Defense Against LLM Jailbreaking](toward_a_dynamic_stackelberg_game-theoretic_framework_for_agent-based_conversat.md)**

:   将 LLM 越狱攻防形式化为动态 Stackelberg 扩展形式博弈，结合快速扩展随机树 (RRT) 搜索提示空间，提出 Purple Agent 防御架构实现"红队思维，蓝队行动"的预见性防御。

**[UME-R1: Exploring Reasoning-Driven Generative Multimodal Embeddings](ume-r1_exploring_reasoning-driven_generative_multimodal_embeddings.md)**

:   提出 UME-R1，首次探索推理驱动的生成式多模态嵌入范式，通过两阶段训练（冷启动SFT + 强化学习）让嵌入模型先推理再生成表示，在 MMEB-V2 基准的 78 个任务上显著超越传统判别式嵌入模型。

**[Understanding and Improving Hyperbolic Deep Reinforcement Learning](understanding_and_improving_hyperbolic_deep_reinforcement_learning.md)**

:   通过形式化梯度分析揭示双曲深度 RL 的训练不稳定根源（大范数嵌入导致信赖域违反），提出 Hyper++ 三组件方案（RMSNorm + 学习缩放 + 分类值损失）实现稳定训练并超越现有方法。

**[Value Flows](value_flows.md)**

:   Value Flows 首次将流匹配（flow matching）引入分布式 RL——学习一个向量场使生成的概率密度路径自动满足分布式 Bellman 方程，通过 flow derivative ODE 高效估计回报方差实现置信度加权优先学习，在 OGBench 62 个任务上平均 1.3× 成功率提升，回报分布估计精度比 C51/CODAC 好 3×+。

**[VerifyBench: Benchmarking Reference-based Reward Systems for Large Language Models](verifybench_benchmarking_reference-based_reward_systems_for_large_language_model.md)**

:   针对大型推理模型（LRM）训练中广泛使用的基于参考答案的奖励系统，构建了 VerifyBench 和 VerifyBench-Hard 两个评测基准，通过严格的人工标注评估各类验证系统的准确性，发现即使最强模型在困难样本上也仅达约 88% 准确率，揭示了当前验证系统的显著改进空间。

**[Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity](whatever_remains_must_be_true_filtering_drives_reasoning_in_llms_shaping_diversi.md)**

:   提出 DMVR 框架和 α-DPG 算法，通过显式定义"过滤掉错误答案"的目标分布并用 α-散度族来逼近，统一了 RLVR（Reverse KL）和拒绝采样微调（Forward KL），在 Lean 定理证明上实现了精度-覆盖率 Pareto 前沿的最优表现。
