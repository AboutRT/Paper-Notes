<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**🤖 AAAI2026** · 共 **72** 篇

**[A Closer Look at Knowledge Distillation in Spiking Neural Network Training](a_closer_look_at_knowledge_distillation_in_spiking_neural_ne.md)**

:   针对ANN→SNN知识蒸馏中教师ANN连续特征/logits与学生SNN离散稀疏spike特征/logits之间分布差异被忽视的问题，提出基于显著性缩放激活图蒸馏（SAMD）和噪声平滑logits蒸馏（NLD）的CKDSNN框架，在CIFAR-10/100、ImageNet-1K和CIFAR10-DVS上均取得SNN训练的新SOTA。

**[AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization](adafuse_accelerating_dynamic_adapter_inference_via_token-lev.md)**

:   针对动态MoE-LoRA适配器推理延迟暴增（250%-950%）的问题，提出了一种token级预门控架构，只在第一层做一次全局路由决策，配合自研的SGMM融合CUDA内核将所有激活的LoRA适配器一次性合并进骨干网络，在保持精度的同时将解码延迟降低2.4倍。

**[AgentODRL: A Large Language Model-based Multi-agent System for ODRL Generation](agentodrl_a_large_language_model-based_multi-agent_system_fo.md)**

:   提出AgentODRL，一个基于Orchestrator-Workers架构的LLM多智能体系统，通过任务分解、语法验证循环和LoRA驱动的语义反思机制，将自然语言数据权限规则高质量地转换为ODRL格式。

**[ALTER: Asymmetric LoRA for Token-Entropy-Guided Unlearning of LLMs](alter_asymmetric_lora_for_token-entropy-guided_unlearning_of.md)**

:   提出ALTER框架，利用非对称LoRA架构结合Token级别的Tsallis熵引导，实现LLM中目标知识的精准遗忘，同时通过参数隔离机制保留模型基础能力，在TOFU、WMDP和MUSE三个基准上达到SOTA。

**[Beyond Sharpness: A Flatness Decomposition Framework for Efficient Continual Learning](beyond_sharpness_a_flatness_decomposition_framework_for_efficient_continual_lear.md)**

:   提出 FLAD 框架，将 sharpness-aware 扰动方向分解为梯度对齐分量与随机噪声分量，仅保留噪声分量进行正则化，结合零阶与一阶 sharpness 以极低额外开销提升持续学习的泛化能力。

**[Break the Tie: Learning Cluster-Customized Category Relationships for Categorical Data Clustering](break_the_tie_learning_cluster-customized_category_relationships_for_categorical.md)**

:   提出 DISC 方法，为每个聚类簇学习定制化的属性类别关系（而非全局统一距离），通过关系树建模与聚类联合优化，在 12 个数据集上以平均排名 1.25 大幅超越现有最佳方法（5.21）。

**[Bridging the Multilingual Safety Divide: Efficient, Culturally-Aware Alignment for Global South Languages](bridging_the_multilingual_safety_divide_efficient_culturally-aware_alignment_for.md)**

:   本文综合多项实证研究，揭示LLM安全机制在低资源语言和代码混合场景下的严重失效，并提出基于参数高效安全引导、文化驱动偏好数据和社区参与式对齐的资源感知蓝图。

**[CAMERA: Multi-Matrix Joint Compression for MoE Models via Micro-Expert Redundancy Analysis](camera_multi-matrix_joint_compression_for_moe_models_via_mic.md)**

:   提出"micro-expert"概念将MoE层的输出分解为跨矩阵（up/gate/down_proj）的微专家线性组合，基于能量排序进行结构化剪枝(Camera-P)和混合精度量化(Camera-Q)，在Deepseek-MoE-16B/Qwen2-57B/Qwen3-30B上20%-60%剪枝率全面超越NAEE和D²-MoE，且分析Qwen2-57B仅需单卡A100不到5分钟。

**[Can You Tell the Difference? Contrastive Explanations for ABox Entailments](can_you_tell_the_difference_contrastive_explanations_for_abox_entailments.md)**

:   提出对比式ABox解释（Contrastive ABox Explanations）的形式化框架，用于回答"为什么a是C的实例而b不是"的问题，在描述逻辑知识库中同时考虑正向蕴涵和缺失蕴涵，并分析不同描述逻辑和优化准则下的计算复杂度。

**[Catastrophic Forgetting in Kolmogorov-Arnold Networks](catastrophic_forgetting_in_kolmogorov-arnold_networks.md)**

:   首个系统性研究KAN（Kolmogorov-Arnold Networks）中灾难性遗忘行为的工作：建立了遗忘与激活支持重叠和数据内禀维度之间的理论框架，并提出KAN-LoRA用于语言模型的持续微调知识编辑。

**[CoEvo: Continual Evolution of Symbolic Solutions Using Large Language Models](coevo_continual_evolution_of_symbolic_solutions_using_large_language_models.md)**

:   提出CoEvo框架，结合LLM与进化搜索方法论，通过动态知识库和多表示空间（自然语言/数学公式/代码）实现符号解的持续开放式进化，在AI Feynman基准上大幅超越现有符号回归方法。

**[ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning](comorag_a_cognitive-inspired_memory-organized_rag_for_stateful_long_narrative_re.md)**

:   受人脑前额叶皮层元认知调控机制启发，提出 ComoRAG 框架，通过动态记忆工作空间和迭代探测查询实现有状态的多步推理，在长篇叙事理解（200K+ tokens）任务上显著超越现有 RAG 方法。

**[Compensating Distribution Drifts in Class-incremental Learning of Pre-trained Vision Transformers](compensating_distribution_drifts_in_class-incremental_learning_of_pre-trained_vi.md)**

:   提出 Sequential Learning with Drift Compensation (SLDC)，通过学习潜在空间转换算子（线性/弱非线性）来补偿预训练 ViT 在类增量学习中因序列微调导致的分布漂移，结合知识蒸馏后性能接近联合训练上界。

**[Condensed Data Expansion Using Model Inversion for Knowledge Distillation](condensed_data_expansion_using_model_inversion_for_knowledge_distillation.md)**

:   提出用浓缩数据集作为原型指导模型反演（MI）过程，通过特征对齐判别器使生成的合成数据与浓缩样本分布一致，从而扩展浓缩数据集用于知识蒸馏，在 CIFAR/ImageNet 上比标准 MI 蒸馏提升高达 11.4%。

**[Consensus-Aligned Neuron Efficient Fine-Tuning Large Language Models for Multi-Domain Machine Translation](consensus-aligned_neuron_efficient_fine-tuning_large_language_models_for_multi-d.md)**

:   提出 CANEFT，通过互信息（MI）识别 LLM 中跨域一致对齐的神经元（consensus-aligned neurons），仅微调这些神经元即可实现多域机器翻译的高效适应，在 3 个 LLM、10 个翻译域上超越 LoRA 等 PEFT 基线，且无需额外参数。

**[Correcting False Alarms from Unseen: Adapting Graph Anomaly Detectors at Test Time](correcting_false_alarms_from_unseen_adapting_graph_anomaly_detectors_at_test_tim.md)**

:   提出 TUNE，一个即插即用的测试时适应框架，通过图对齐器变换节点特征来解决图异常检测中因新正常类别出现导致的"正常性偏移"问题，利用聚合污染程度作为无监督适应信号，在 10 个真实数据集上显著增强多种预训练 GAD 模型的泛化能力。

**[Credal Ensemble Distillation for Uncertainty Quantification](credal_ensemble_distillation_for_uncertainty_quantification.md)**

:   提出Credal Ensemble Distillation（CED）框架，将深度集成教师蒸馏为单模型CREDIT，该模型预测类别概率区间（定义credal集）而非单一softmax分布，在OOD检测任务上实现了优于或可比的不确定性估计，同时大幅降低推理开销（推理时间从5×降为1×）。

**[Data Whitening Improves Sparse Autoencoder Learning](data_whitening_improves_sparse_autoencoder_learning.md)**

:   本文将经典稀疏编码中的 PCA 白化（whitening）引入现代稀疏自编码器（SAE）训练，通过理论分析和仿真证明白化能使优化景观更凸更各向同性，在 SAEBench 上的实验表明白化显著提升可解释性指标（Sparse Probing +7.3%、SCR +54%、TPP +372%），尽管重构质量略有下降。

**[Distilling Cross-Modal Knowledge via Feature Disentanglement](distilling_cross-modal_knowledge_via_feature_disentanglement.md)**

:   提出频域解耦跨模态知识蒸馏（FD-CMKD），通过傅里叶变换将特征分解为低频（模态共享语义）和高频（模态特有细节）分量，分别施加强一致性 MSE 和弱一致性 logMSE 损失，并引入尺度标准化与共享分类器对齐特征空间，在音频-视觉、图像-文本、语义分割等多个跨模态场景全面超越现有蒸馏方法。

**[Does Less Hallucination Mean Less Creativity? An Empirical Investigation in LLMs](does_less_hallucination_mean_less_creativity_an_empirical_investigation_in_llms.md)**

:   系统研究三种幻觉缓解方法（CoVe、DoLa、RAG）对LLM创造力的影响，发现它们对发散性创造力有截然相反的效果——CoVe增强、DoLa抑制、RAG无影响——而收敛性创造力基本不受影响，这一规律跨模型家族和参数规模一致成立。

**[Don't Start Over: A Cost-Effective Framework for Migrating Personalized Prompts Between LLMs](dont_start_over_a_cost-effective_framework_for_migrating_personalized_prompts_be.md)**

:   提出PUMA框架，通过轻量级适配器和分组用户选择策略，高效地将个性化软提示从源LLM迁移到不同架构的目标LLM，在三个大规模数据集上匹配甚至超越从头训练的性能，同时减少计算成本高达98%。

**[DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation](dos_distilling_observable_softmaps_of_zipfian_prototypes_for_self-supervised_poi.md)**

:   提出DOS框架，通过仅在可观测（未掩码）点上蒸馏语义软图（Softmap），结合Zipfian先验的Zipf-Sinkhorn正则化来处理3D语义的长尾分布，在六个3D基准上实现了自监督学习的SOTA，线性探测可达监督性能的95%。

**[DP-GenG: Differentially Private Dataset Distillation Guided by DP-Generated Data](dp-geng_differentially_private_dataset_distillation_guided_by_dp-generated_data.md)**

:   提出 DP-GenG 框架，利用差分隐私生成数据（DP-generated data）引导数据集蒸馏的初始化、特征匹配和专家校准三个阶段，在有限隐私预算下显著提升蒸馏数据集的实用性和隐私保护能力。

**[DynaQuant: Dynamic Mixed-Precision Quantization for Learned Image Compression](dynaquant_dynamic_mixed-precision_quantization_for_learned_i.md)**

:   针对学习图像压缩（LIC）模型部署效率低的痛点，提出DynaQuant框架，在参数层面通过可学习scale/zero-point + Distance-Aware Gradient Modulator实现内容自适应量化，在架构层面通过轻量Bit-Width Selector动态为每层分配最优比特宽度，在Cheng2020/ELIC/Ballé三个基线上实现接近FP32的R-D性能，同时获得最高5.17×加速和模型大小降至原来的~1/4。

**[Earth-Adapter: Bridge Geospatial Domain Gaps with Mixture of Frequency Adaptation](earth-adapter_bridge_the_geospatial_domain_gaps_with_mixture_of_frequency_adapta.md)**

:   提出 Earth-Adapter，首个针对遥感图像**伪影问题**设计的参数高效微调 (PEFT) 方法，通过频率引导的混合适配器 (MoA) 将特征分解为高低频子空间、独立优化后动态聚合，在遥感语义分割 (SS)、域自适应 (DA) 和域泛化 (DG) 三个设定中均超越基线 Rein。

**[EEG-DLite: Dataset Distillation for Efficient Large EEG Model Training](eeg-dlite_dataset_distillation_for_efficient_large_eeg_model_training.md)**

:   提出 EEG-DLite 数据蒸馏框架，通过自监督编码+异常值过滤+多样性采样，将2500小时 EEG 数据集压缩至仅5%即可达到甚至超越全数据集预训练的基础模型性能，GPU预训练时间从30小时降至2小时。

**[Efficient Reasoning for Large Reasoning Language Models via Certainty-Guided Reflection Suppression](efficient_reasoning_for_large_reasoning_language_models_via_certainty-guided_ref.md)**

:   提出 CGRS（Certainty-Guided Reflection Suppression），一种无需训练的高效推理方法，通过在模型高置信度时动态抑制反思触发词（如"Wait""But"），将大型推理语言模型的 token 消耗降低18.5%~41.9%，同时保持推理精度不变。

**[Efficient Thought Space Exploration Through Strategic Intervention](efficient_thought_space_exploration_through_strategic_intervention.md)**

:   提出 Hint-Practice Reasoning（HPR）框架，通过大模型（hinter）在稀疏关键 token 处提供短提示、小模型（practitioner）完成主要推理的协作模式，仅需1/5的 token 即可达到 self-consistency 基线的性能，同时在相同 FLOPs 下精度最高提升5.1%。

**[EfficientFSL: Enhancing Few-Shot Classification via Query-Only Tuning in Vision Transformers](efficientfsl_enhancing_few-shot_classification_via_query-only_tuning_in_vision_t.md)**

:   提出 EfficientFSL，一种针对 ViT 少样本分类的 query-only 参数高效微调框架，通过 Forward Block（解耦的主动/冻结子块）、Combine Block（自适应多层特征融合）和 SQ Attention Block（支持-查询分布对齐）三个模块，仅用1.25M~2.48M可训练参数即可在4个域内+6个跨域基准上达到 SOTA。

**[Explore and Establish Synergistic Effects between Weight Pruning and Coreset Selection](explore_and_establish_synergistic_effects_between_weight_pruning_and_coreset_sel.md)**

:   首次系统探索权重剪枝与核心集选择之间的交互关系，提出SWaST机制交替执行两者以建立协同效应，并设计状态保持机制解决"双重损失"问题，在10%–90% FLOPs削减下实现最高17.83%的精度提升。

**[FactGuard: Event-Centric and Commonsense-Guided Fake News Detection](factguard_event-centric_and_commonsense-guided_fake_news_detection.md)**

:   提出 FactGuard 框架，利用 LLM 提取事件核心内容（去风格化）并生成常识推理，通过 Rationale Usability Evaluator 动态评估 LLM 建议的可信度，并通过知识蒸馏获得无需 LLM 的轻量版 FactGuard-D，在假新闻检测中兼顾鲁棒性和效率。

**[Finding the Translation Switch: Discovering and Exploiting the Task-Initiation Features in LLMs](finding_the_translation_switch_discovering_and_exploiting_the_task-initiation_fe.md)**

:   利用稀疏自编码器（SAE）发现 LLM 中控制翻译任务启动的"翻译启动特征"，通过因果干预验证其功能（增强特征→提升翻译质量/减少幻觉，消除特征→产生幻觉），并将该机制洞察转化为实用的数据选择策略——优先在"机制困难"样本上微调，显著提升数据效率和抑制幻觉。

**[First-Order Error Matters: Accurate Compensation for Quantized Large Language Models](first-order_error_matters_accurate_compensation_for_quantized_large_language_mod.md)**

:   本文揭示了LLM后训练量化中逐列补偿过程会导致一阶梯度项不可忽略的问题，提出FOEM方法通过将一阶项纳入误差补偿公式来提升量化精度，在3-bit量化下将Llama3-8B的困惑度降低17.3%，且几乎不增加计算开销。

**[Focusing on Language: Revealing and Exploiting Language Attention Heads in Multilingual Large Language Models](focusing_on_language_revealing_and_exploiting_language_attention_heads_in_multil.md)**

:   本文提出LAHIS方法，仅需一次前向-后向传播即可高效识别多语言LLM中的语言特异性和语言通用性注意力头，并展示了通过调控这些头来实现跨语言注意力转移、缓解非目标语言生成问题，以及仅用14-20个可训练参数就能提升多语言QA性能的能力。

**[HCF: Hierarchical Cascade Framework for Distributed Multi-Stage Image Compression](hcf_hierarchical_cascade_framework_for_distributed_multi-stage_image_compression.md)**

:   本文提出HCF框架，通过直接在潜在空间进行跨节点变换（避免像素域重压缩）并引入策略驱动的量化控制，在分布式多级图像压缩中实现了最高12.64% BD-Rate的PSNR提升，同时节省高达97.8%的FLOPs和96.5%的GPU内存。

**[Hierarchical Pedagogical Oversight: A Multi-Agent Adversarial Framework for Reliable AI Tutoring](hierarchical_pedagogical_oversight_a_multi-agent_adversarial_framework_for_relia.md)**

:   本文提出HPO框架，通过三阶段流水线（情报蒸馏→对抗辩论→综合判定）实现可靠的AI辅导评估，仅用8B参数的模型在MRBench中学数学对话数据集上以Macro F1 0.845超越GPT-4o（0.812）3.3%，证明了交互结构而非模型规模是可靠AI辅导的关键。

**[Is the Information Bottleneck Robust Enough? Towards Label-Noise Resistant Information Bottleneck Learning](is_the_information_bottleneck_robust_enough_towards_label-noise_resistant_inform.md)**

:   本文揭示了信息瓶颈（IB）原理在标签噪声下的固有脆弱性，提出 LaT-IB 方法，通过将表征解耦为干净标签空间和噪声标签空间两部分，结合"最小-充分-干净"（MSC）准则和三阶段训练框架，在多种噪声条件下实现了对现有 IB 方法的显著超越。

**[KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache](kvmix_gradient-based_layer_importance-aware_mixed-precision_.md)**

:   提出 KVmix，通过计算 Key/Value 投影权重梯度的 $L_2$ 范数来评估各层 KV Cache 的重要性，实现层级混合精度量化（Key 平均 2.19bit、Value 平均 2.38bit），并结合动态关键上下文选择（RPC）策略，在 Llama/Mistral 等模型上实现近无损推理、4.9× 内存压缩和 5.3× 吞吐加速。

**[LexChronos: An Agentic Framework for Structured Event Timeline Extraction in Indian Jurisprudence](lexchronos_an_agentic_framework_for_structured_event_timeline_extraction_in_indi.md)**

:   本文提出LexChronos，一个双智能体迭代框架，用于从印度最高法院判决书中提取结构化事件时间线：通过LoRA微调的抽取智能体识别候选事件，预训练的反馈智能体通过置信度驱动的循环进行评分和精炼，在合成数据集上取得BERT F1 0.8751，且结构化时间线在下游的法律文本摘要中被GPT-4在75%的案例中评为优于非结构化基线。

**[Lightweight Optimal-Transport Harmonization on Edge Devices](lightweight_optimal-transport_harmonization_on_edge_devices.md)**

:   提出 MKL-Harmonizer，利用经典最优传输理论中的 Monge-Kantorovich 线性映射（MKL），训练一个轻量级编码器预测 12 维颜色变换参数，实现边缘设备上的实时图像颜色协调，在 AR 场景的感知质量-速度综合指标上达到最优。

**[LLMs for Game Theory: Entropy-Guided In-Context Learning and Adaptive CoT Reasoning](llms_for_game_theory_entropy-guided_in-context_learning_and_adaptive_cot_reasoni.md)**

:   提出一种基于熵引导的自适应 LLM 推理框架，结合动态上下文检索和自适应链式思维（CoT）推理，在井字棋博弈任务中将 LLM 的平均对局结果从 -11.6% 提升至 +9.5%，同时保持较低的 LLM 查询次数。

**[MCTSr-Zero: Self-Reflective Psychological Counseling Dialogues Generation via Principles and Adaptive Exploration](mctsr-zero_self-reflective_psychological_counseling_dialogues_generation_via_pri.md)**

:   提出 MCTSr-Zero 框架，将 MCTS 与领域原则自评估、元提示自适应探索机制结合，用于生成高质量心理咨询多轮对话数据，微调得到的 PsyLLM 在自建的 PsyEval 基准上达到 SOTA。

**[MoSE: Hierarchical Self-Distillation Enhances Early Layer Embeddings](mose_hierarchical_self-distillation_enhances_early_layer_embeddings.md)**

:   提出 ModularStarEncoder（MoSE），一个 10 亿参数的多出口编码器，通过新颖的自蒸馏机制（高层引导低层训练）显著增强早期层表示，在 CodeSearchNet 等代码理解任务上超越所有开源模型，同时支持灵活的计算-精度权衡部署。

**[Parametric Pareto Set Learning for Expensive Multi-Objective Optimization](parametric_pareto_set_learning_for_expensive_multi-objective_optimization.md)**

:   本文提出 PPSL-MOBO 框架，通过超网络 + LoRA 架构学习从偏好和外在参数到 Pareto 最优解的统一映射，结合高斯过程代理模型和超体积改进采集策略，高效解决昂贵的参数化多目标优化问题。

**[Pocketllm Ultimate Compression Of Large Language Models Via Meta Networks](pocketllm_ultimate_compression_of_large_language_models_via_meta_networks.md)**

:   PocketLLM提出通过元网络（编码器-码本-解码器）在潜空间中压缩LLM权重向量，用小型解码器+紧凑码本+索引替代原始权重矩阵，在Llama 2-7B上实现10×压缩且精度损失可忽略，突破了传统量化/剪枝在极端压缩比下的精度瓶颈。

**[Post Training Quantization for Efficient Dataset Condensation](post_training_quantization_for_efficient_dataset_condensation.md)**

:   首次将训练后量化（PTQ）应用于数据集蒸馏，提出基于补丁的量化框架（PAQ+分组+精炼），在 2-bit 极低比特下将蒸馏数据集的测试精度几乎翻倍（如 DM IPC=1 从 26.0% 提升至 54.1%），作为即插即用框架可应用于各种蒸馏方法。

**[PrefixGPT: Prefix Adder Optimization by a Generative Pre-trained Transformer](prefixgpt_prefix_adder_optimization_by_a_generative_pre-trained_transformer.md)**

:   提出PrefixGPT，将前缀加法器优化建模为序列生成问题，通过定制的GPT模型预训练学习设计规则后用RL微调生成优化设计，在面积-延迟乘积(ADP)上取得SOTA且对初始化不敏感。

**[Prototype-Based Semantic Consistency Alignment for Domain Adaptive Retrieval](prototype-based_semantic_consistency_alignment_for_domain_adaptive_retrieval.md)**

:   提出 PSCA 两阶段框架，通过正交 prototype 建立类级语义连接，结合几何-语义一致性对齐动态修正伪标签可靠性，并在重建特征上进行 hash 编码，显著提升跨域检索性能。

**[Put the Space of LoRA Initialization to the Extreme to Preserve Pre-trained Knowledge](put_the_space_of_lora_initialization_to_the_extreme_to_preserve_pre-trained_know.md)**

:   提出 LoRA-Null，将 LoRA 初始化在预训练知识 input activation 的 null space 中（而非权重的 null space），从信息论角度论证 activation 的 effective rank 远小于权重，因此其 null space 包含更少预训练知识信息，显著减轻微调时的灾难性遗忘。

**[QuEPT: Quantized Elastic Precision Transformers with One-Shot Calibration for Multi-Bit Switching](quept_quantized_elastic_precision_transformers_with_one-shot_calibration_for_mul.md)**

:   提出QuEPT弹性精度量化框架，通过Multi-Bit Token Merging和Multi-Bit Cascaded LoRA两大核心模块，实现一次校准即可在ViT/LLM/MLLM上实时切换任意预定义位宽，性能媲美甚至超越单位宽SOTA PTQ方法。

**[Reinforced Rate Control for Neural Video Compression via Inter-Frame Rate-Distortion Awareness](reinforced_rate_control_for_neural_video_compression_via_inter-frame_rate-distor.md)**

:   提出首个基于约束马尔可夫决策过程（CMDP）的强化学习速率控制框架，通过时空状态建模联合捕获帧内容特征与帧间率-失真耦合依赖，直接映射到逐帧编码参数，在多种神经视频编解码器上将平均比特率误差降至1.20%，BD-Rate节省最高达13.98%。

**[Rethinking Long-tailed Dataset Distillation: A Uni-Level Framework with Unbiased Recovery and Relabeling](rethinking_long-tailed_dataset_distillation_a_uni-level_framework_with_unbiased_.md)**

:   提出首个面向长尾分布的单层(uni-level)数据集蒸馏框架，通过专家模型去偏、BN统计量公平校准和置信度引导初始化三大策略，在CIFAR-100-LT上提升15.6%、Tiny-ImageNet-LT上提升11.8%，全面超越DAMED。

**[RRRA: Resampling and Reranking through a Retriever Adapter](rrra_resampling_and_reranking_through_a_retriever_adapter.md)**

:   提出RRRA框架，通过在Bi-Encoder上添加轻量级可学习适配器来建模每个候选文档的假阴性概率，并将其同时用于训练时的负样本重采样和推理时的重排序，在NQ/TQ/MS MARCO上持续超越SimANS/TriSampler等强基线。

**[SafeSieve: From Heuristics to Experience in Progressive Pruning for LLM-based Multi-Agent Communication](safesieve_from_heuristics_to_experience_in_progressive_pruning_for_llm-based_mul.md)**

:   提出SafeSieve，一种渐进式自适应多智能体通信剪枝框架，通过语义启发初始化→历史反馈驱动的双阶段边评分和0-extension聚类机制，在6个基准上实现94.01%平均准确率同时减少12.4%-27.8% token消耗，并展现出对prompt注入攻击的天然鲁棒性。

**[Satisficing and Optimal Generalised Planning via Goal Regression (Extended Version)](satisficing_and_optimal_generalised_planning_via_goal_regression_extended_versio.md)**

:   提出 Moose 规划器，利用目标回归（goal regression）从训练问题中合成泛化规划程序：将训练问题的目标拆解为单目标子问题逐个最优求解，通过回归和提升（lifting）得到一阶条件-动作规则集，用于满足性规划（直接执行规则）或最优规划（编码为公理剪枝搜索空间）。

**[SCoPe: Intrinsic Semantic Space Control for Mitigating Copyright Infringement in LLMs](scope_intrinsic_semantic_space_control_for_mitigating_copyright_infringement_in_.md)**

:   将LLM版权侵权缓解问题重新定义为内在语义空间控制，利用稀疏自编码器(SAE)将隐状态映射到高维稀疏空间，识别版权敏感子空间并在解码时钳制其激活，无需外部过滤器或参数更新即可有效减少版权内容复制，同时保持模型通用能力。

**[Share Your Attention: Transformer Weight Sharing via Matrix-Based Dictionary Learning](share_your_attention_transformer_weight_sharing_via_matrix-based_dictionary_lear.md)**

:   受字典学习启发，提出 MASA 框架，将 Transformer 各层注意力投影矩阵（Q/K/V/O）分解为共享矩阵原子的线性组合，以 66.7% 的注意力参数压缩率实现与原始 Transformer 持平甚至更优的性能。

**[Sharp Eyes and Memory for VideoLLMs: Information-Aware Visual Token Pruning for Efficient and Reliable VideoLLM Reasoning](sharp_eyes_and_memory_for_videollms_information-aware_visual_token_pruning_for_e.md)**

:   SharpV 提出一个两阶段无训练视觉Token剪枝框架，在Pre-LLM阶段基于时空信息自适应调整每帧剪枝比例，在Intra-LLM阶段基于视觉信息退化假说进行KV Cache剪枝，首次实现与Flash Attention完全兼容，在多个视频理解基准上以约12%的Token保留率达到与稠密模型相当甚至更优的性能。

**[Shrinking the Teacher: An Adaptive Teaching Paradigm for Asymmetric EEG-Vision Alignment](shrinking_the_teacher_an_adaptive_teaching_paradigm_for_asymmetric_eeg-vision_al.md)**

:   提出自适应教学范式（Adaptive Teaching Paradigm），通过无残差连接的瓶颈结构 ShrinkAdapter 让视觉"教师"主动收缩和调整其知识结构以适配 EEG"学生"的学习能力，在零样本脑-图像检索任务上 Top-1 准确率达到 60.2%，超越前 SOTA 9.8 个百分点。

**[SIGN: Schema-Induced Games for Naming](sign_schema-induced_games_for_naming.md)**

:   SIGN 提出在LLM多智能体命名博弈中引入轻量级消息Schema（如 `@say {name: Ck}`），发现结构化先验可将群体约定一致性提升5.8×，收敛所需Token减少一个数量级，为高效多智能体协调提供了简单可控的"调节旋钮"。

**[SkipCat: Rank-Maximized Low-Rank Compression of Large Language Models via Shared Projection and Block Skipping](skipcat_rank-maximized_low-rank_compression_of_large_language_models_via_shared_.md)**

:   SkipCat 提出了一种秩最大化的低秩压缩框架，通过层内共享投影（Cat）和块跳跃（Skip）两项技术，在相同压缩率下保留更多有效秩，无需微调即可在零样本任务上比现有低秩方法提升7%准确率。

**[SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning](spark_query-aware_unstructured_sparsity_with_recoverable_kv_cache_channel_prunin.md)**

:   提出SparK——一种training-free的KV cache通道级非结构化剪枝方法，通过query-aware的saliency评估选择关键通道+recovery机制恢复被剪枝通道的贡献，在80%剪枝率下性能损失<5%，与token eviction方法正交互补，可额外减少30%+ KV cache存储。

**[SparseRM: A Lightweight Preference Modeling with Sparse Autoencoder](sparserm_a_lightweight_preference_modeling_with_sparse_autoencoder.md)**

:   SparseRM 利用稀疏自编码器（SAE）从LLM中间表示中提取偏好相关方向，通过投影向量构建轻量级奖励模型，仅需不到1%的可训练参数即可超越大多数主流奖励模型，并在在线迭代对齐框架中表现出更强的泛化能力。

**[SpecQuant: Spectral Decomposition and Adaptive Truncation for Ultra-Low-Bit LLMs Quantization](specquant_spectral_decomposition_and_adaptive_truncation_for_ultra-low-bit_llms_.md)**

:   SpecQuant 提出一种基于自适应傅里叶域分解的两阶段量化框架：先将激活离群值平滑迁移到权重，再通过通道级低频傅里叶截断吸收权重中的高频噪声，在LLaMA-3 8B上实现W4A4量化仅1.5%精度损失，同时获得2×加速和3×内存节省。

**[SR-KI: Scalable and Real-Time Knowledge Integration into LLMs via Supervised Attention](sr-ki_scalable_and_real-time_knowledge_integration_into_llms_via_supervised_atte.md)**

:   提出SR-KI框架，通过两阶段训练（检索层定位 + 注意力监督损失）实现结构化知识库向LLM KV缓存的高效注入，在单块A100 40GB GPU上支持最多40K知识库条目的注入，且通过top-100压缩实现高达99.75%的压缩率，同时保持88%以上的平均Recall@10检索性能。

**[Steering Pretrained Drafters during Speculative Decoding](steering_pretrained_drafters_during_speculative_decoding.md)**

:   提出 SD²，通过从验证器隐藏状态中提取转向向量（steering vector）并注入预训练 drafter 的 MLP 层，实现推测解码中 drafter-verifier 的动态对齐，在标准采样下将被接受 token 数提升高达 35%，同时计算开销可忽略不计。

**[StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion](stepfun-formalizer_unlocking_the_autoformalization_potential_of_llms_through_kno.md)**

:   提出 ThinkingF 流水线，通过大规模知识蒸馏与模板引导的推理轨迹合成分别增强 LLM 的形式语言领域知识和非形式到形式的推理能力，再经两阶段 SFT + RLVR 融合两种能力，7B/32B 模型在 FormalMATH-Lite 和 ProverBench 上达到 SOTA。

**[Stratified Knowledge-Density Super-Network for Scalable Vision Transformers](stratified_knowledge-density_super-network_for_scalable_vision_transformers.md)**

:   提出将预训练 ViT 转化为"分层知识密度超网络"（SKD Super-Network），通过 WPAC（加权 PCA 注意力收缩）和 PIAD（渐进式重要性感知 Dropout）两步实现知识的分层组织，使得任意大小的子网络均可以 O(1) 代价提取，且无需额外微调即可达到或超越 SOTA 压缩方法的性能。

**[Structured Language Generation Model: Loss Calibration and Formatted Decoding for Efficient Text](structured_language_generation_model_loss_calibration_and_formatted_decoding_for.md)**

:   提出 SLGM 框架，通过**结构化输入格式**、**格式损失**和**格式感知解码**三大组件，将生成式语言模型的结构化预测任务重构为分类问题，在不增加模型参数的前提下显著提升 <1B 模型在 NER、RE、SRL 等 5 类 13 个数据集上的结构预测性能。

**[TGDD: Trajectory Guided Dataset Distillation with Balanced Distribution](tgdd_trajectory_guided_dataset_distillation_with_balanced_distribution.md)**

:   提出 TGDD，将静态分布匹配重新定义为沿训练轨迹的动态对齐过程，通过阶段式分布匹配（Stage-wise Distribution Matching）捕获演化语义 + 分布约束正则化（Stage-wise Distribution Constraint）减少类间重叠，在 10 个数据集上达到 SOTA，高分辨率基准上准确率提升 5.0%。

**[Towards Test-time Efficient Visual Place Recognition via Asymmetric Query Processing](towards_test-time_efficient_visual_place_recognition_via_asymmetric_query_proces.md)**

:   提出面向视觉位置识别（VPR）的高效非对称框架 AsymVPR，通过**地理记忆库**替代昂贵的 k-NN 预计算，以及**隐式嵌入增强**弥合轻量查询网络与高容量图库网络的能力差距，实现仅用 ~8% FLOPs 的轻量网络达到接近全尺寸模型的检索性能。

**[When Small Models Are Right for Wrong Reasons: Process Verification for Trustworthy Agents](when_small_models_are_right_for_wrong_reasons_process_verification_for_trustwort.md)**

:   通过分析 10,734 条推理轨迹揭示小型语言模型（7-9B）存在严重的"答对但理由错"（RWR）现象——50-69% 的正确答案包含根本性推理缺陷；提出推理完整性评分（RIS）作为过程级指标，发现 RAG 能有效改善推理质量而元认知干预反而有害，并蒸馏出快速分类器（0.86 F1, 100× 加速）用于实时部署。
