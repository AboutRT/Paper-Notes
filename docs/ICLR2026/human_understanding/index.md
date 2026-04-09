<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧑 人体理解

**🔬 ICLR2026** · 共 **40** 篇

**[AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations](amemgym_interactive_memory_benchmarking_for_assistants_in_long-horizon_conversat.md)**

:   提出AMemGym——首个支持on-policy交互式评估的长程对话记忆基准环境，通过结构化数据采样（用户画像→状态演化→个性化问答）驱动LLM模拟用户进行角色扮演，揭示了off-policy评估的排名偏差问题，并系统诊断了RAG/长上下文/Agent记忆系统的write/read/utilization三阶段失败模式。

**[AMPED: Adaptive Multi-objective Projection for balancing Exploration and skill Diversification](amped_adaptive_multi-objective_projection_for_balancing_exploration_and_skill_di.md)**

:   提出AMPED框架，在技能预训练阶段用梯度手术（PCGrad）平衡探索（熵+RND）和技能多样性（AnInfoNCE）之间的梯度冲突，在微调阶段用SAC-based技能选择器自适应选择最优技能，在Maze和URLB基准上超越DIAYN/CeSD/CIC等SBRL基线。

**[An Efficient, Provably Optimal Algorithm for the 0-1 Loss Linear Classification Problem](an_efficient_provably_optimal_algorithm_for_the_0-1_loss_linear_classification_p.md)**

:   提出增量单元枚举算法（ICE），首个具有严格证明的独立算法，可以在 $O(N^{D+1})$ 时间内精确求解0-1损失线性分类问题的全局最优解，并扩展到多项式超曲面分类。

**[Antibody: Strengthening Defense Against Harmful Fine-Tuning for Large Language Models via Attenuating Harmful Gradient Influence](antibody_strengthening_defense_against_harmful_fine-tuning_for_large_language_mo.md)**

:   提出Antibody防御框架：在对齐阶段通过平坦度正则化使模型处于有害损失的平坦区域（梯度小→难被攻击），在微调阶段用基于模型安全知识的样本加权方案（对比目标完成 vs 拒绝的似然比）抑制有害样本的学习，平均Harmful Score从15.29%降至7.04%。

**[Bayesian Influence Functions for Hessian-Free Data Attribution](bayesian_influence_functions_for_hessian-free_data_attribution.md)**

:   提出 Local Bayesian Influence Function (BIF)，用 SGLD 采样估计的协方差替代经典影响函数中不可行的 Hessian 逆运算，实现了对数十亿参数模型的无架构限制数据归因，在重训练实验中达到 SOTA。

**[Biologically Plausible Online Hebbian Meta-Learning: Two-Timescale Local Rules for Spiking Neural Brain Interfaces](biologically_plausible_online_hebbian_meta-learning_two-timescale_local_rules_fo.md)**

:   提出一种无需BPTT的在线SNN解码器，通过三因子Hebbian局部学习规则结合双时间尺度eligibility trace和自适应学习率控制，在O(1)内存下实现可比离线训练方法的BCI神经解码精度（Pearson R≥0.63/0.81），并在闭环仿真中展现了对神经信号非平稳性的持续适应能力。

**[COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics](cold-steer_steering_large_language_models_via_in-context_one-step_learning_dynam.md)**

:   提出 COLD-Steer，通过近似梯度下降在上下文示例上产生的表征变化来实现无训练的 LLM 激活转向，在仅用 50 分之一样本量的情况下达到 95% 的转向效果。

**[CollectiveKV: Decoupling and Sharing Collaborative Information in Sequential Recommendation](collectivekv_decoupling_and_sharing_collaborative_information_in_sequential_reco.md)**

:   观察到序列推荐中不同用户的 KV cache 具有显著跨用户相似性（协同信号），提出 CollectiveKV 将 KV 分解为低维用户特有部分和从全局 KV 池检索的高维共享部分，实现 0.8% 的压缩率且性能不降。

**[Condition Matters in Full-head 3D GANs](condition_matters_in_full-head_3d_gans.md)**

:   发现全头 3D GAN 中视角条件导致严重方向偏差（条件视角生成质量远优于其他视角），提出用视角不变的语义特征（正脸 CLIP 特征）替代视角作为条件，配合 Flux.1 Kontext 合成的 1120 万张 360° 平衡数据集，首次实现全视角一致的高保真多样全头生成。

**[DGNet: Discrete Green Networks for Data-Efficient Learning of Spatiotemporal PDEs](dgnet_discrete_green_networks_for_data-efficient_learning_of_spatiotemporal_pdes.md)**

:   基于Green函数理论，将叠加原理嵌入物理-神经混合架构，构建离散Green网络DGNet，在仅用数十条训练轨迹的条件下实现SOTA精度，并展现对未见源项的鲁棒零样本泛化。

**[DiffVax: Optimization-Free Image Immunization Against Diffusion-Based Editing](diffvax_optimization-free_image_immunization_against_diffusion-based_editing.md)**

:   DiffVax 训练一个前馈免疫器（UNet++），对任意图像仅需一次前向传播（~70ms）即可生成不可感知的对抗扰动，使基于扩散模型的恶意编辑失败，相比先前逐图优化方法实现 250,000× 加速，并首次将免疫扩展到视频内容。

**[Distilling and Adapting: A Topology-Aware Framework for Zero-Shot Interaction Prediction in Multiplex Biological Networks](distilling_and_adapting_a_topology-aware_framework_for_zero-shot_interaction_pre.md)**

:   提出CAZI-MBN框架，通过融合领域特定LLM序列嵌入、拓扑感知图分词器、上下文感知跨层注意力和教师-学生蒸馏，实现多重生物网络中未见实体的零样本交互预测，在5个基准数据集上AUROC较最优baseline提升3.1-20.4%。

**[EgoHandICL: Egocentric 3D Hand Reconstruction with In-Context Learning](egohandicl_egocentric_3d_hand_reconstruction_with_in-context_learning.md)**

:   首次将上下文学习（ICL）范式引入3D手部重建，通过VLM引导的模板检索、多模态ICL分词器和MAE驱动的重建流程，在ARCTIC和EgoExo4D基准上显著超越SOTA方法。

**[Function Spaces Without Kernels: Learning Compact Hilbert Space Representations](function_spaces_without_kernels_learning_compact_hilbert_space_representations.md)**

:   证明函数编码器（Function Encoders）通过学习神经网络基函数定义了一个有效的核，建立了神经特征学习与RKHS理论的桥梁，并提出PCA引导的紧凑基选择算法和有限样本泛化界。

**[GaitSnippet: Gait Recognition Beyond Unordered Sets and Ordered Sequences](gaitsnippet_gait_recognition_beyond_unordered_sets_and_ordered_sequences.md)**

:   提出 Snippet 范式：将步态轮廓序列组织为若干"片段"（snippet），每个 snippet 由一个连续区间内随机抽取的帧构成，兼顾短程时序上下文与长程时序依赖，在 Gait3D 上以 2D 卷积骨干达到 77.5% Rank-1，超越所有 3D 卷积方法。

**[Generalizable End-to-End Tool-Use RL with Synthetic CodeGym](generalizable_end-to-end_tool-use_rl_with_synthetic_codegym.md)**

:   提出 CodeGym 框架，将编程题自动转化为多轮工具调用的交互式环境，用于 LLM agent 的强化学习训练，在分布外基准上取得显著泛化提升（如 Qwen2.5-32B 在 τ-Bench 上 +8.7 点）。

**[Heterogeneous Federated Fine-Tuning with Parallel One-Rank Adaptation](heterogeneous_federated_fine-tuning_with_parallel_one-rank_adaptation.md)**

:   提出Fed-PLoRA框架，用多个并行一秩模块(PLoRA)替代多秩LoRA，通过Select-N-Fold策略（选N个训练+折叠其余到冻结权重）实现异构联邦微调的零初始化噪声和最小聚合噪声，在6个LLM/多任务上全面超越现有方法。

**[Inference-Time Backdoors via Hidden Instructions in LLM Chat Templates](inference-time_backdoors_via_hidden_instructions_in_llm_chat_templates.md)**

:   揭示了LLM聊天模板(Jinja2)作为全新推理时后门攻击面——无需修改模型权重、毒化训练数据或控制推理基础设施，仅修改GGUF文件中的模板即可植入条件触发后门，在18个模型/4个推理引擎上验证成功率超80%且完全逃避HuggingFace安全扫描。

**[Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision](inference-time_safety_for_code_llms_via_retrieval-augmented_revision.md)**

:   提出SOSecure方法，在LLM生成代码后通过检索Stack Overflow安全讨论作为上下文引导模型推理时修正潜在漏洞，无需重训练即可适应新的安全实践，在多个数据集上减少漏洞且不引入新的安全问题。

**[Inverse Virtual Try-On: Generating Multi-Category Product-Style Images from Clothed Individuals](inverse_virtual_try-on_generating_multi-category_product-style_images_from_cloth.md)**

:   提出TEMU-VTOFF——面向虚拟脱衣(VTOFF)任务的Dual-DiT架构，通过特征提取器+服装生成器分工协作，结合多模态混合注意力(MHA)融合图像/文本/掩码信息消解视觉歧义，并设计DINOv2驱动的服装对齐器保留高频细节，在VITON-HD和Dress Code多品类场景均达到SOTA。

**[LLM Unlearning with LLM Beliefs](llm_unlearning_with_llm_beliefs.md)**

:   揭示GA/NPO等LLM遗忘方法存在"挤压效应"(squeezing effect)——降低目标响应概率后概率质量转移到语义相关的高似然区域导致虚假遗忘，提出基于Bootstrapping的框架，利用模型自身高置信度预测(model beliefs)作为额外遗忘目标，BS-T(token级)和BS-S(序列级)两种实现在TOFU/MUSE/WMDP多个基准上实现更彻底的遗忘且保持模型效用。

**[LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations](llms_encode_their_failures_predicting_success_from_pre-generation_activations.md)**

:   发现LLM在生成答案前的激活中已编码了成功概率信息，线性探针可高效提取→该信号代表的是模型特异难度(≠人类难度)，且随扩展推理加深两者差异增大。探针引导的模型路由以70%成本降低匹配最强模型性能。

**[Maximizing Asynchronicity in Event-based Neural Networks](maximizing_asynchronicity_in_event-based_neural_networks.md)**

:   提出EVA框架，将事件类比为语言token，用基于RWKV-6的线性注意力异步编码器实现逐事件特征更新，结合多表示预测(MRP)+下一表示预测(NRP)的自监督学习获得可泛化特征，首次在异步-同步(A2S)范式中成功完成高难度目标检测任务(Gen1数据集0.477 mAP)。

**[NeuroGaze-Distill: Brain-informed Distillation and Depression-Inspired Geometric Priors for Robust Facial Emotion Recognition](neurogaze-distill_brain-informed_distillation_and_depression-inspired_geometric_.md)**

:   提出 NeuroGaze-Distill 跨模态蒸馏框架：从 EEG 脑电训练的教师模型中提取静态 Valence-Arousal 原型，通过 Proto-KD 和抑郁症启发的几何先验（D-Geo）注入纯视觉学生模型，无需 EEG-人脸配对数据，提升表情识别的跨数据集鲁棒性。

**[OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning](omnieva_embodied_versatile_planner_via_task-adaptive_3d-grounded_and_embodiment-.md)**

:   提出OmniEVA——通过任务自适应门控路由器动态注入3D位置编码(仅在需要时启用几何推理)和具身感知推理框架(将物理约束融入规划循环),解决了空间MLLM的两大gap：几何适应性差(2D-only或硬编码3D)和具身约束缺失(理论可行但实际不可执行的计划),在8个基准中7个达到SOTA。

**[One Language, Two Scripts: Probing Script-Invariance in LLM Concept Representations](one_language_two_scripts_probing_script-invariance_in_llm_concept_representation.md)**

:   利用塞尔维亚语双文字系统(拉丁/西里尔文)作为天然控制实验，探究Sparse Autoencoders(SAE)学到的特征是否捕获了超越表面token化的抽象语义：发现跨文字的相同句子激活高度重叠的SAE特征(Jaccard~0.58)，且切换文字造成的表征差异小于同文字内的改写差异，且此不变性随模型规模增强，表明SAE特征确实捕获了超越正字法的语义结构。

**[P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling](p-genrm_personalized_generative_reward_model_with_test-time_user-based_scaling.md)**

:   提出P-GenRM——首个个性化生成式奖励模型：将混合偏好信号(显式准则+隐式历史)转化为结构化评价链(用户画像+评分标准)，通过三阶段训练(PSI监督微调→CRE强化学习→课程学习)学习自适应评估，再用双粒度测试时scaling(个体级多次评分聚合+原型级相似用户协同)减少噪声并增强新用户泛化，在个性化奖励基准上SOTA+3%测试时scaling增益。

**[ConflictScope: Generative Value Conflicts Reveal LLM Priorities](quamo_quaternion_motions_for_vision-based_3d_human_kinematics_capture.md)**

:   提出ConflictScope——自动化价值冲突场景生成与评估流水线：给定任意价值集合，自动生成价值对之间的冲突场景，通过模拟用户的开放式交互（而非选择题）评估LLM的价值优先级排序；发现模型在开放式评估中从"保护性价值"（如无害性）显著转向"个人价值"（如用户自主性），系统提示可使对齐目标排序提升14%。

**[Rapid Training of Hamiltonian Graph Networks using Random Features](rapid_training_of_hamiltonian_graph_networks_using_random_features.md)**

:   提出RF-HGN——用随机特征替代迭代梯度优化训练哈密顿图网络：随机采样隐藏层参数+用线性求解器确定输出层→训练速度比15种优化器快150-600倍且精度相当，保持置换/旋转/平移不变性，在8节点上训练可零样本泛化到4096节点系统，挑战了物理系统NN训练必须用梯度下降的主导范式。

**[REA-RL: Reflection-Aware Online Reinforcement Learning for Efficient Reasoning](rea-rl_reflection-aware_online_reinforcement_learning_for_efficient_reasoning.md)**

:   提出REA-RL——反思感知的在线RL框架解决LRM过度思考问题：(1)训练小型反思模型在线生成截断修订(首次正确答案后截断→同时支持并行采样和顺序修订)，(2)设计反思奖励防止RL训练中的非反思退化(模型完全丧失反思能力→退回朴素CoT)，两者结合实现推理成本降低36%而不损失性能。

**[Refine Now, Query Fast: A Decoupled Refinement Paradigm for Implicit Neural Fields](refine_now_query_fast_a_decoupled_refinement_paradigm_for_implicit_neural_fields.md)**

:   提出DRR(Decoupled Representation Refinement)范式解决隐式神经场的保真度-速度困境：用深层精化器网络离线增强嵌入结构的表达能力→精化结果缓存→推理时仅需快速嵌入插值+轻量解码→实现27x推理加速同时达到SOTA保真度，另提出Variational Pairs数据增强策略改善稀疏集成数据下的训练。

**[RuleReasoner: Reinforced Rule-based Reasoning via Domain-aware Dynamic Sampling](rulereasoner_reinforced_rule-based_reasoning_via_domain-aware_dynamic_sampling.md)**

:   提出RuleReasoner——通过大规模规则推理数据集(RuleCollection-32K, 8类任务)+域感知动态采样(Dads, 基于历史奖励动态调整域采样权重)的RLVR方法增强LLM规则推理→8B模型在OOD任务上超越OpenAI-o1(Δ10.4%)和DeepSeek-R1(Δ14%),且训练步数更少(更高效)。

**[Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study](safety_subspaces_are_not_linearly_distinct_a_fine-tuning_case_study.md)**

:   通过4个系统实验(权重投影/正交补/更新相似度/激活空间)在5个LLM上证明安全对齐信息与通用学习在线性空间中不可分离——放大安全行为的子空间同时放大有用行为,有害更新与安全更新的相似性并非最高→基于线性子空间的安全防御策略面临根本性限制。

**[Scalable Exploration for High-Dimensional Continuous Control via Value-Guided Flow](scalable_exploration_for_high-dimensional_continuous_control_via_value-guided_fl.md)**

:   提出Qflex(Q-guided Flow Exploration)——在高维连续动作空间中实现可扩展探索的RL方法：从可学习源分布沿Q函数诱导的概率流传输动作→探索与任务相关梯度对齐(而非各向同性噪声)→在多种高维基准上超越高斯/扩散RL基线,成功控制700执行器的全身人体肌骨模型执行敏捷复杂动作。

**[Scalable In-Context Q-Learning](scalable_in-context_q-learning.md)**

:   提出S-ICQL——将动态规划和世界模型引入监督式ICRL框架：(1)多头Transformer同时预测最优策略和情境值函数，(2)预训练通用世界模型→将原始轨迹转化为轻量级提示(精确编码任务信息),(3)迭代策略改进(Q函数上尾期望拟合+优势加权回归)→从次优数据学习时相比AD/DPT等基线大幅提升,在离散和连续环境中一致优越。

**[Scaling Generalist Data-Analytic Agents](scaling_generalist_data-analytic_agents.md)**

:   提出DataMind——可扩展的数据分析Agent训练pipeline：(1)细粒度18类任务分类法+递归由简到难任务组合→多样高质量合成query,(2)知识增强轨迹采样+自一致性过滤,(3)SFT+RL动态混合训练目标,(4)内存友好的稳定多轮代码rollout框架→DataMind-14B在多个基准上SOTA(71.16%,超越DeepSeek-V3.1和GPT-5)。

**[Scaling Speech Tokenizers with Diffusion Autoencoders](scaling_speech_tokenizers_with_diffusion_autoencoders.md)**

:   提出SiTok(Speech Diffusion Tokenizer)——将扩散自编码器扩展到1.6B参数+2200万小时语音训练的语音tokenizer：联合优化量化和重建(不分两阶段)+CTC语义正则化确保token编码语义信息→在12.5Hz/200bps极低token率下→理解(ASR/情感/说话人)和重建/生成任务都超越强基线→shortcut微调实现2-4步高质量解码。

**[SemHiTok: A Unified Image Tokenizer via Semantic-Guided Hierarchical Codebook](semhitok_a_unified_image_tokenizer_via_semantic-guided_hierarchical_codebook_for.md)**

:   提出SemHiTok——通过语义引导层次codebook(SGHC)统一理解和生成的tokenizer：预训练语义codebook上建像素子codebook，结构和训练解耦(分阶段优化)避免联合训练的语义-像素冲突，LLaVA设定下离散tokenizer中理解和重建都SOTA。

**[Soft Equivariance Regularization for Invariant Self-Supervised Learning](soft_equivariance_regularization_for_invariant_self-supervised_learning.md)**

:   提出 SER（Soft Equivariance Regularization），通过在 ViT 中间层施加软等变正则化、在最终层保持不变性目标的层解耦设计，在不引入额外模块的情况下，为不变性 SSL 方法（MoCo-v3, DINO, Barlow Twins）带来一致的分类精度和鲁棒性提升。

**[STRIDE: Subset-Free Functional Decomposition for XAI in Tabular Settings](stride_subset-free_functional_decomposition_for_xai_in_tabular_settings.md)**

:   提出STRIDE——在RKHS中通过递归核中心化实现无需子集枚举的正交功能分解，从标量归因升级到完整功能成分f_S(x_S)，揭示特征如何交互而非仅什么重要，10个表格数据集中位加速3.0x(vs TreeSHAP)、均值R2=0.93，首创成分手术隔离量化单一交互的性能影响。
