<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🎨 图像生成

**🧪 ICML2025** · 共 **57** 篇

**[Angle Domain Guidance: Latent Diffusion Requires Rotation Rather Than Extrapolation](angle_domain_guidance_latent_diffusion_requires_rotation_rather_than_extrapolati.md)**

:   发现 Classifier-Free Guidance (CFG) 导致颜色失真的根本原因是潜空间样本范数被放大，提出 Angle Domain Guidance (ADG) 算法——在角度域而非幅度域增强引导，约束范数变化的同时优化角度对齐，在高引导权重下消除颜色饱和度异常并保持甚至改善文本-图像对齐。

**[Annealing Flow Generative Models Towards Sampling High-Dimensional and Multi-Modal Distributions](annealing_flow_generative_models_towards_sampling_high-dimensional_and_multi-mod.md)**

:   提出 Annealing Flow (AF)——基于连续归一化流（CNF）的高维多模态分布采样方法，用动态最优传输（OT）目标配合 Wasserstein 正则化训练，通过退火过程引导模式探索，在高维多模态设置中大幅优于现有 NF 和 MCMC 方法。

**[Autoencoder-Based Hybrid Replay for Class-Incremental Learning](autoencoder-based_hybrid_replay_for_class-incremental_learning.md)**

:   提出基于自编码器的混合重放策略(AHR)，利用混合自编码器(HAE)将样本压缩存储在潜空间中而非原始输入空间，结合带电粒子系统能量最小化(CPSEM)和斥力算法(RFA)增量嵌入新类质心，在最坏情况下将内存复杂度从 $\mathcal{O}(t)$ 降低到 $\mathcal{O}(0.1t)$，同时保持 SOTA 性能。

**[Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment](beyond_bradley-terry_models_a_general_preference_model_for_language_model_alignm.md)**

:   提出偏好嵌入（Preference Embedding）——将响应嵌入到多维潜空间中捕捉复杂偏好结构（包括不可传递偏好），实现 $O(K)$ 的查询复杂度（与 BT 模型相同但表达力更强），配合 General Preference Optimization (GPO) 在 RewardBench 和 AlpacaEval2.0 上超越 BT 奖励模型。

**[Beyond One-Hot Labels: Semantic Mixing for Model Calibration](beyond_one-hot_labels_semantic_mixing_for_model_calibration.md)**

:   提出 CSM（Calibration-aware Semantic Mixing）——利用预训练扩散模型生成高保真的语义混合样本（如猫-狗混合体），并通过 CLIP 重标注精确的软标签置信度，用 $L_2$ 损失训练实现比现有校准方法更优的模型置信度校准。

**[BinauralFlow: A Causal and Streamable Approach for High-Quality Binaural Speech Synthesis with Flow Matching Models](binauralflow_a_causal_and_streamable_approach_for_high-quality_binaural_speech_s.md)**

:   提出 BinauralFlow，一个基于条件 Flow Matching 的流式双耳语音合成框架，通过因果 U-Net 架构和连续推理管线实现高保真、可流式生成的双耳音频，感知测试中 42% 的混淆率表明生成结果几乎无法与真实录音区分。

**[BRIDGE: Bootstrapping Text to Control Time-Series Generation via Multi-Agent Iterative Optimization and Diffusion Modeling](bridge_bootstrapping_text_to_control_time-series_generation_via_multi-agent_iter.md)**

:   提出 Bridge 框架，通过 LLM 多智能体系统生成高质量文本-时序配对数据，并利用语义原型与文本描述的混合提示驱动扩散模型，实现跨域、实例级别的文本控制时序生成（Text-Controlled TSG），在12个数据集中11个取得SOTA。

**[Broadband Ground Motion Synthesis by Diffusion Model with Minimal Condition](broadband_ground_motion_synthesis_by_diffusion_model_with_minimal_condition.md)**

:   提出 HEGGS（High-fidelity Earthquake Groundmotion Generation System），利用地震数据集中波形天然可配对的特性，结合条件隐扩散模型与 ACM 振幅校正模块，仅需最少条件信息（经纬度、震源深度、震级）即可端到端生成高保真三分量地震波形。

**[Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing](ca2-vdm_efficient_autoregressive_video_diffusion_model_with_causal_generation_an.md)**

:   提出 Ca2-VDM，通过因果生成（Causal Generation）和缓存共享（Cache Sharing）两大设计，消除自回归视频扩散模型中条件帧的冗余计算，将计算复杂度从二次降至线性，生成 80 帧视频速度比基线快 2.5 倍，同时保持 SOTA 级生成质量。

**[Compositional Flows for 3D Molecule and Synthesis Pathway Co-design](compositional_flows_for_3d_molecule_and_synthesis_pathway_co-design.md)**

:   提出 CGFlow（Compositional Generative Flows）——将 flow matching 扩展到组合对象的逐步生成，交织组合结构采样（合成路径）和连续状态传输（3D 构象），作为 3DSynthFlow 应用于可合成药物设计，在 LIT-PCBA 15个靶标上首次同时达到结合亲和力和可合成性的 SOTA。

**[ContinualFlow: Learning and Unlearning with Neural Flow Matching](continualflow_learning_and_unlearning_with_neural_flow_matching.md)**

:   提出 ContinualFlow，一种基于 Flow Matching 的生成模型定向遗忘框架，通过能量函数重加权软性减去数据分布中不需要的区域，无需重新训练或直接访问待遗忘样本即可实现高效遗忘。

**[Continuous Semi-Implicit Models](continuous_semi-implicit_models.md)**

:   提出 CoSIM——将层级半隐式模型扩展为连续时间框架，通过连续转移核实现无仿真高效训练，并设计保持一致性的转移核实现分布级别的多步扩散模型蒸馏，在 ImageNet 512×512 上达到或超越现有扩散加速方法。

**[Continuous Visual Autoregressive Generation via Score Maximization](continuous_visual_autoregressive_generation_via_score_maximization.md)**

:   提出连续视觉自回归（Continuous VAR）框架——基于严格适当评分规则（strictly proper scoring rules）的理论，用能量分数（energy score）作为训练目标，实现不需要向量量化的连续 token 自回归图像生成。

**[DCTdiff: Intriguing Properties of Image Generative Modeling in the DCT Space](dctdiff_intriguing_properties_of_image_generative_modeling_in_the_dct_space.md)**

:   提出 DCTdiff，首次在离散余弦变换（DCT）频域空间中进行端到端扩散图像生成，无需 VAE 即可无缝扩展至 512×512 分辨率，并在生成质量和训练效率上均优于像素空间扩散模型。

**[Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning](diffusion-vla_generalizable_and_interpretable_robot_foundation_model_via_self-ge.md)**

:   提出 DiffusionVLA (DiVLA)，将自回归 VLM 的推理能力与扩散模型的动作生成能力统一到一个端到端框架中，通过推理注入模块（Reasoning Injection Module）将自生成的语言推理直接嵌入策略学习过程，实现了对未见物体的泛化分类、可解释的动作决策以及高速推理（2B 模型 82Hz）。

**[Discriminative Policy Optimization for Token-Level Reward Models](discriminative_policy_optimization_for_token-level_reward_models.md)**

:   提出 Q-function Reward Model (Q-RM)，通过将奖励建模与语言生成解耦，定义判别式策略来学习 token 级 Q 函数，从偏好数据中无需细粒度标注即可获得精确的 token 级奖励信号，显著提升 PPO/REINFORCE 的推理性能与训练效率。

**[Distillation of Discrete Diffusion through Dimensional Correlations (Di4C)](distillation_of_discrete_diffusion_through_dimensional_correlations.md)**

:   提出Di4C方法，通过"mixture"模型捕获维度间相关性，配合一致性损失函数，将多步离散扩散模型蒸馏为少步模型，同时在图像和语言任务上展示了有效性。

**[DRAG: Data Reconstruction Attack using Guided Diffusion](drag_data_reconstruction_attack_using_guided_diffusion.md)**

:   提出 DRAG，利用预训练潜在扩散模型（LDM）的图像先验知识，通过引导扩散过程从分割推理（Split Inference）的深层中间表示中高保真地重建原始输入图像，揭示视觉基础模型（CLIP、DINOv2）在 SI 场景下的严重隐私漏洞。

**[Editable Noise Map Inversion: Encoding Target-image into Noise For High-Fidelity Image Manipulation](editable_noise_map_inversion_encoding_target-image_into_noise_for_high-fidelity_.md)**

:   提出 Editable Noise Map Inversion (ENM Inversion)，通过在反演过程中同时优化重建误差和编辑对齐误差，使 noise map 同时"铭刻"源图像与目标图像信息，在内容保持和编辑忠实度之间取得最优平衡。

**[Efficient Diffusion Models for Symmetric Manifolds](efficient_diffusion_models_for_symmetric_manifolds.md)**

:   提出一种高效的对称流形（环面、球面、SO(n)、U(n)）扩散模型框架，通过欧几里得布朗运动的投影和Itô引理绕过热核计算，将训练复杂度从指数级降至近线性，并提供多项式级采样精度保证。

**[Elucidating Flow Matching ODE Dynamics via Data Geometry and Denoisers](elucidating_flow_matching_ode_dynamics_with_respect_to_data_geometries_and_denoi.md)**

:   本文从denoiser的角度深入分析了Flow Matching (FM) ODE的采样轨迹动力学，揭示了轨迹演化的三个阶段（初始→中间→终端），建立了FM ODE在数据支撑在低维子流形上时的收敛性理论。

**[Expressive Score-Based Priors for Distribution Matching with Geometry-Preserving Regularization](expressive_score-based_priors_for_distribution_matching_with_geometry-preserving.md)**

:   提出基于 score function 的表达性先验分布（SAUB），通过 Score Function Substitution (SFS) 技巧绕过先验密度估计，结合 Gromov-Wasserstein 几何保持约束实现稳定高效的分布匹配，在公平分类、域适应和域翻译任务上取得优越表现。

**[Flat-Lora Low-Rank Adaptation Over A Flat Loss Landscape](flat-lora_low-rank_adaptation_over_a_flat_loss_landscape.md)**

:   提出 Flat-LoRA，通过在**全参数空间**中引入基于贝叶斯期望损失的随机权重扰动，使 LoRA 收敛到全参数空间中更平坦的极小值区域，提升域内和域外泛化性能，且几乎不增加训练时间和显存开销。

**[Graph Generative Pre-trained Transformer (G2PT)](graph_generative_pre-trained_transformer.md)**

:   提出 G2PT——将图编码为节点+边的 token 序列，用 GPT 风格的自回归 Transformer 做 next-token prediction 来生成图，并通过拒绝采样微调(RFT)和 PPO 强化学习实现目标导向分子生成，在通用图和分子数据集上均达到 SOTA。

**[Hessian Geometry of Latent Space in Generative Models](hessian_geometry_of_latent_space_in_generative_models.md)**

:   提出通过重建 Fisher 信息度量来分析生成模型潜空间几何的方法，发现扩散模型潜空间中存在分形结构的相变边界，在相边界处 Lipschitz 常数发散。

**[Hierarchical Reinforcement Learning with Uncertainty-Guided Diffusional Subgoals](hierarchical_reinforcement_learning_with_uncertainty-guided_diffusional_subgoals.md)**

:   提出 HIDI 框架，以条件扩散模型建模子目标分布，并引入高斯过程 (GP) 先验进行不确定性正则化与子目标选择，在长时域连续控制任务上显著超越现有层次强化学习方法。

**[Importance Sampling for Nonlinear Models](importance_sampling_for_nonlinear_models.md)**

:   通过引入非线性映射的伴随算子（adjoint operator），将线性模型中经典的范数采样和杠杆分数采样系统性地推广到非线性模型，首次为神经网络等非线性模型的重要性采样提供了理论近似保证。

**[Integrating Intermediate Layer Optimization and Projected Gradient Descent for Solving Inverse Problems with Diffusion Models](integrating_intermediate_layer_optimization_and_projected_gradient_descent_for_s.md)**

:   提出 DMILO 和 DMILO-PGD 两种方法，通过中间层优化（ILO）分解扩散模型采样过程以大幅降低显存，并结合投影梯度下降（PGD）避免次优收敛，在线性和非线性逆问题上全面超越 DMPlug 等 SOTA 方法。

**[IntLoRA: Integral Low-rank Adaptation of Quantized Diffusion Models](intlora_integral_low-rank_adaptation_of_quantized_diffusion_models.md)**

:   提出 IntLoRA，通过整数型低秩参数实现量化扩散模型的微调，合并权重后无需额外 PTQ 即可直接获得量化推理权重，兼顾训练与推理效率。

**[Learning Single Index Models with Diffusion Priors](learning_single_index_models_with_diffusion_priors.md)**

:   提出利用扩散模型先验从半参数单指标模型（SIM）的非线性观测中恢复信号的高效方法，只需一轮无条件采样和部分反演，无需已知链接函数，在1-bit和三次测量上以极少的NFE显著优于现有方法。

**[LIVS: A Pluralistic Alignment Dataset for Inclusive Public Spaces](livs_a_pluralistic_alignment_dataset_for_inclusive_public_spaces.md)**

:   通过两年社区参与式研究，构建了包含 37,710 对多标准偏好标注的 LIVS 数据集，用于文本到图像模型在包容性城市公共空间设计中的多元对齐，并用 DPO 微调 SDXL 验证其有效性。

**[LlavaGuard: An Open VLM-based Framework for Safeguarding Vision Datasets and Models](llavaguard_an_open_vlm-based_framework_for_safeguarding_vision_datasets_and_mode.md)**

:   提出 LlavaGuard——基于开源 VLM 的视觉内容安全审核框架，通过可定制安全分类体系、高质量人工标注数据集与策略增强训练，实现对图像内容的灵活、精准安全评估，在准确率和策略适应性上大幅超越现有开源与闭源审核工具。

**[Model Immunization from a Condition Number Perspective](model_immunization_from_a_condition_number_perspective.md)**

:   从Hessian矩阵条件数的角度定义和分析模型免疫问题，提出最大化/最小化条件数的正则化器，使预训练模型难以被微调用于有害任务而不影响正常任务性能。

**[Morse: Dual-Sampling for Lossless Acceleration of Diffusion Models](morse_dual-sampling_for_lossless_acceleration_of_diffusion_models.md)**

:   提出 Morse 双采样框架，通过快速 Dot 模型学习残差反馈来补偿 Dash（原扩散模型）跳步采样的信息损失，实现 1.78×–3.31× 的无损加速。

**[Multidimensional Adaptive Coefficient for Inference Trajectory Optimization in Flow and Diffusion](multidimensional_adaptive_coefficient_for_inference_trajectory_optimization_in_f.md)**

:   提出多维自适应系数 MAC（Multidimensional Adaptive Coefficient），作为 flow/diffusion 模型的即插即用模块，将传统的一维时间调度系数扩展为多维、样本自适应的系数，通过对抗训练优化推理轨迹，在 CIFAR-10 条件生成上以 5 NFE 取得 FID 1.37 的 SOTA 结果。

**[Nonparametric Identification of Latent Concepts](nonparametric_identification_of_latent_concepts.md)**

:   提出首个非参数概念可识别性理论框架，证明在不假设概念类型、函数关系或参数生成模型的情况下，仅通过多类别观测的多样性即可识别隐藏概念（至逐元素变换+置换不确定性）。

**[Normalizing Flows are Capable Generative Models](normalizing_flows_are_capable_generative_models.md)**

:   提出 TarFlow（Transformer AutoRegressive Flow），用堆叠因果 ViT 实现分块自回归 Normalizing Flow，首次在 ImageNet 64×64 上突破 3 BPD，并通过高斯噪声增强、score-based 去噪和 guidance 三项技术使 NF 模型的生成质量首次媲美扩散模型。

**[Ntpp Generative Speech Language Modeling For Dual-Channel Spoken Dialogue Via Ne](ntpp_generative_speech_language_modeling_for_dual-channel_spoken_dialogue_via_ne.md)**

:   提出 Next-Token-Pair Prediction (NTPP) 范式，首次用 decoder-only 架构对双通道语音对话进行 speaker-independent 联合分布建模，实现更自然的轮次转换、更低的推理延迟和更强的说话人无关性。

**[One Image is Worth a Thousand Words: A Usability Preservable Text-Image Collaborative Erasing Framework](one_image_is_worth_a_thousand_words_a_usability_preservable_text-image_collabora.md)**

:   提出 Co-Erasing，首次将图像监督引入概念擦除流程，通过文本-图像协同的负引导和文本引导的图像概念精炼模块，在保持良性生成质量（usability）的同时显著提升不良概念的擦除效果（efficacy）。

**[PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](pak-ucb_contextual_bandit_an_online_learning_approach_to_prompt-aware_selection_.md)**

:   提出 PAK-UCB 上下文老虎机算法，通过为每个生成模型学习独立的核函数，在线预测给定 prompt 下的最优模型，实现 prompt 级别的生成模型/LLM 选择，并用随机傅里叶特征（RFF）降低计算开销。

**[Position All Current Generative Fidelity And Diversity Metrics Are Flawed](position_all_current_generative_fidelity_and_diversity_metrics_are_flawed.md)**

:   Position paper：系统性地证明了所有现有生成模型 fidelity 和 diversity 指标（包括 Improved Precision/Recall、Density/Coverage、α-precision/β-recall 等六对指标）在精心设计的 sanity check 中均存在大量失败，呼吁社区投入更多精力研发更可靠的评估指标。

**[Privacy Amplification Through Synthetic Data: Insights from Linear Regression](privacy_amplification_through_synthetic_data_insights_from_linear_regression.md)**

:   在线性回归框架下，证明了合成数据在对抗者控制种子时无法提供隐私放大，但在随机输入下释放有限数量的合成数据可以获得超越模型本身DP保证的隐私放大效果，放大程度为 $O(1/d)$。

**[Provable Maximum Entropy Manifold Exploration via Diffusion Models](provable_maximum_entropy_manifold_exploration_via_diffusion_models.md)**

:   提出 S-MEME 算法，将扩散模型的探索问题形式化为近似数据流形上的熵最大化，通过利用 score 函数与熵一阶变分的内在联系绕开密度估计，以镜像下降方式迭代微调预训练扩散模型，并证明收敛到最优探索策略。

**[Quantum Algorithms for Finite-horizon Markov Decision Processes](quantum_algorithms_for_finite-horizon_markov_decision_processes.md)**

:   提出四种量子值迭代算法（QVI-1/2/3/4），在精确动力学和生成模型两种设定下，对有限时域时变MDP实现了状态空间 $S$、动作空间 $A$、误差 $\epsilon$ 和时域 $H$ 多维度的量子加速，并证明了渐近最优的量子下界。

**[Representative Language Generation](representative_language_generation.md)**

:   提出"代表性生成"（representative generation）理论框架，要求生成模型的输出按比例代表训练数据中的各兴趣群组，并引入"群组闭包维度"（group closure dimension）作为刻画可生成性的关键组合量。

**[RestoreGrad: Signal Restoration Using Conditional Denoising Diffusion Models with Jointly Learned Prior](restoregrad_signal_restoration_using_conditional_denoising_diffusion_models_with.md)**

:   提出 RestoreGrad 框架，通过 Prior Net 和 Posterior Net 联合学习条件 DDPM 的先验分布（而非固定标准高斯），利用退化信号与干净信号之间的相关性构建更具信息量的先验，在语音增强和图像修复任务上实现 5-10× 更快收敛和 2-2.5× 更少推理步数。

**[SADA: Stability-guided Adaptive Diffusion Acceleration](sada_stability-guided_adaptive_diffusion_acceleration.md)**

:   提出基于ODE轨迹二阶差分的稳定性准则（Stability Criterion），统一调控步级（step-wise）和token级（token-wise）稀疏决策，在SD-2/SDXL/Flux上实现≥1.8×加速且LPIPS≤0.10、FID≤4.5，显著优于DeepCache和AdaptiveDiffusion。

**[Sample Complexity of Distributionally Robust Off-Dynamics Reinforcement Learning with Online Interaction](sample_complexity_of_distributionally_robust_off-dynamics_reinforcement_learning.md)**

:   提出 supremal visitation ratio $C_{vr}$ 度量在线鲁棒 MDP 的探索难度，设计首个支持一般 $f$-散度（TV/KL/$\chi^2$）的高效在线算法 ORBIT，并给出匹配的上下界，证明 $C_{vr}$ 是刻画 off-dynamics RL 在线可学习性的紧致度量。

**[Shielded Diffusion: Generating Novel and Diverse Images using Sparse Repellency](shielded_diffusion_generating_novel_and_diverse_images_using_sparse_repellency.md)**

:   提出 SPELL（Sparse Repellency）方法，在扩散模型生成过程中添加**稀疏排斥项**，将采样轨迹推离参考图像集合（受保护图像或已生成图像），以**免训练**方式提升输出多样性并防止复制训练集。

**[Simple and Critical Iterative Denoising: A Recasting of Discrete Diffusion in Graph Generation](simple_and_critical_iterative_denoising_a_recasting_of_discrete_diffusion_in_gra.md)**

:   提出 Simple Iterative Denoising (SID) 与 Critical Iterative Denoising (CID) 框架，通过假设中间噪声状态的条件独立性来消除离散扩散的复合去噪误差，并引入 Critic 网络自适应调节元素级重加噪概率，在图/分子生成任务上大幅超越标准离散扩散基线。

**[Task-Agnostic Pre-training and Task-Guided Fine-tuning for Versatile Diffusion Planner](task-agnostic_pre-training_and_task-guided_fine-tuning_for_versatile_diffusion_p.md)**

:   提出 SODP 框架：先用大量无奖励标签的次优多任务轨迹预训练扩散规划器，再用基于策略梯度的 RL 微调快速适配下游任务，并引入 BC 正则化防止性能崩溃，在 Meta-World 50 任务上达到 60.56% 成功率（SOTA）。

**[Theoretical Guarantees on the Best-of-n Alignment Policy](theoretical_guarantees_on_the_best-of-n_alignment_policy.md)**

:   本文推翻了文献中广泛使用的 best-of-n 策略 KL 散度公式 $\log(n) - (n-1)/n$ 的精确性声明，证明它只是一个上界，并提出了更紧的 KL 散度估计器和 win rate 理论界。

**[Tree-Sliced Wasserstein Distance: A Geometric Perspective](tree-sliced_wasserstein_distance_a_geometric_perspective.md)**

:   提出 Tree-Sliced Wasserstein distance on Systems of Lines (TSW-SL)，用树状线系统替代 SW 中的一维直线作为投影域，保留拓扑结构的同时保持闭合解的高效计算，在梯度流、风格迁移和生成模型上超越 SW 及其变体。

**[Tree-Sliced Wasserstein Distance with Nonlinear Projection](tree-sliced_wasserstein_distance_with_nonlinear_projection.md)**

:   提出非线性投影框架下的 Tree-Sliced Wasserstein（TSW）距离，通过 Circular/Spatial 两种非线性 Radon 变换替代原有线性投影，在保持度量良定义和单射性的同时，在梯度流、自监督学习和生成模型等任务上显著优于已有 SW 和 TSW 变体。

**[Understanding And Mitigating Memorization In Generative Models Via Sharpness Of ](understanding_and_mitigating_memorization_in_generative_models_via_sharpness_of_.md)**

:   通过对数概率密度的 Hessian 曲率（sharpness）建立扩散模型记忆化的几何分析框架，提出可在生成初始阶段检测记忆化的新指标，并设计无需重训练的 SAIL 初始噪声优化策略来缓解记忆化。

**[Unsupervised Learning for Class Distribution Mismatch (UCDM)](unsupervised_learning_for_class_distribution_mismatch.md)**

:   提出 UCDM，利用扩散模型从无标注数据中合成正负样本对来训练分类器，在不依赖标注数据的情况下解决训练集与目标任务之间的类别分布不匹配（CDM）问题，在 closed-set 和 open-set 任务上均大幅超越现有半监督方法。

**[When Diffusion Models Memorize: Inductive Biases in Probability Flow of Minimum-Norm Shallow Neural Nets](when_diffusion_models_memorize_inductive_biases_in_probability_flow_of_minimum-n.md)**

:   从理论上分析了最小 $\ell^2$ 范数浅层 ReLU 去噪器驱动的扩散模型概率流的收敛行为，证明概率流可以收敛到训练样本（记忆化）、训练样本之和（"虚拟点"）或超盒边界上的流形点（泛化），且扩散时间调度器的"早停"效应决定了收敛目标。
