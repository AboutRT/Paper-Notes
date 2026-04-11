<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**📹 ICCV2025** · 共 **61** 篇

**[Acknowledging Focus Ambiguity in Visual Questions](acknowledging_focus_ambiguity_in_visual_questions.md)**

:   首次定义并系统研究视觉问答中的**焦点歧义**（focus ambiguity）问题——当问题中的语言描述可能指向图像中多个合理区域时，现有 VQA 系统完全忽略了这种歧义。作者构建了 VQ-FocusAmbiguity 数据集（5,500 样本 + 12,880 实例分割），并证明现代模型在识别和定位焦点歧义方面表现很差。

**[Adaptive Prompt Learning via Gaussian Outlier Synthesis for Out-of-Distribution Detection](adaptive_prompt_learning_via_gaussian_outlier_synthesis_for_out-of-distribution_.md)**

:   提出 APLGOS 框架，利用 ChatGPT 标准化 Q&A 对来初始化可学习 ID 提示，并在类条件高斯分布的低似然区域合成虚拟 OOD 提示和图像，通过对比学习对齐文本-图像嵌入，实现更紧凑的 ID/OOD 决策边界。

**[AdvDreamer Unveils: Are Vision-Language Models Truly Ready for Real-World 3D Variations?](advdreamer_unveils_are_visionlanguage_models_truly_ready_for.md)**

:   提出AdvDreamer框架从单张图像生成物理可复现的对抗性3D变换(Adv-3DT)样本，通过零样本单目姿态操作+自然度奖励模型+逆语义概率损失，揭示当前VLM（包括GPT-4o）在3D变化下性能下降高达50-80%，并建立首个3D变化鲁棒性VQA基准MM3DTBench。

**[AIGI-Holmes: Towards Explainable and Generalizable AI-Generated Image Detection via Multimodal Large Language Models](aigi-holmes_towards_explainable_and_generalizable_ai-generated_image_detection_v.md)**

:   提出 AIGI-Holmes，通过构建包含解释性标注的 Holmes-Set 数据集和精心设计的三阶段训练流程（视觉专家预训练 → SFT → DPO），将 MLLM 改造为既能准确检测 AI 生成图像又能提供人类可验证解释的"福尔摩斯"检测器，推理阶段通过协同解码策略进一步增强泛化能力。

**[AirCache: Activating Inter-Modal Relevancy KV Cache Compression for Efficient Large Vision-Language Model Inference](aircache_activating_inter-modal_relevancy_kv_cache_compression_for_efficient_lar.md)**

:   提出 AirCache，一种面向 LVLM 的 KV Cache 压缩方法，通过精英观察窗口（Elite Observation Window）评估视觉 token 重要性，结合基于重要性分数分布强度与偏度的自适应层级预算分配，在仅保留 10% 视觉 KV Cache 时性能损失不超过 1%，解码延迟降低 29%-66%。

**[Analyzing Finetuning Representation Shift for Multimodal LLMs Steering](analyzing_finetuning_representation_shift_for_multimodal_llms_steering.md)**

:   提出一个无需训练的框架，通过概念级别分析揭示多模态大语言模型微调时的表征偏移，并利用偏移向量实现模型行为的轻量级引导（去偏、安全控制）。

**[Are They the Same? Exploring Visual Correspondence Shortcomings of Multimodal LLMs](are_they_the_same_exploring_visual_correspondence_shortcomings_of_multimodal_llm.md)**

:   本文首次系统研究了多模态大模型（MLLM）在视觉对应匹配方面的不足，构建了含1510样本的MMVM基准和220K匹配数据集，并提出CoLVA方法通过目标级对比学习和细粒度视觉专家显著提升了MLLM的跨图像实例匹配能力。

**[Attention to the Burstiness in Visual Prompt Tuning!](attention_to_the_burstiness_in_visual_prompt_tuning.md)**

:   本文揭示了视觉Prompt Tuning中自注意力模块数据的"爆发性"（burstiness）和非高斯分布问题，提出通过数据白化和双线性模型来学习"爆发性prompt"，在多个基准上大幅超越VPT及其变体，如CUB数据集上从42.15%提升至77.86%。

**[AutoComPose: Automatic Generation of Pose Transition Descriptions for Composed Pose Retrieval Using Multimodal LLMs](autocompose_automatic_generation_of_pose_transition_descriptions_for_composed_po.md)**

:   本文提出AutoComPose，首个利用多模态大语言模型（MLLM）自动生成人体姿态转换描述的框架，通过身体部位级描述生成、多样化增强和循环一致性损失，在取代昂贵的人工标注的同时实现了更优的组合姿态检索性能。

**[BabyVLM: Data-Efficient Pretraining of VLMs Inspired by Infant Learning](babyvlm_data-efficient_pretraining_of_vlms_inspired_by_infant_learning.md)**

:   受人类婴儿高效学习能力的启发，提出BabyVLM框架，包括合成训练数据集（将通用数据转化为儿童导向的格式）和多个发展对齐的评估基准，实现了紧凑VLM在有限数据下的高效预训练，性能优于仅用SAYCam或通用数据训练的模型。

**[Background Invariance Testing According to Semantic Proximity](background_invariance_testing_according_to_semantic_proximity.md)**

:   本文提出基于语义邻近度的背景不变性测试方法，通过关联分析构建关键词本体来系统采样背景场景，实现兼顾测试多样性（recall）和人类判断一致性（precision）的最优平衡，并验证可视化测试框架比全局统计指标更具信息量。

**[BASIC: Boosting Visual Alignment with Intrinsic Refined Embeddings in Multimodal Large Language Models](basic_boosting_visual_alignment_with_intrinsic_refined_embeddings_in_multimodal_.md)**

:   通过分析 LLM 浅层对视觉嵌入的语义精炼过程，提出 BASIC 方法，利用 LLM 内部精炼后的视觉嵌入作为监督信号，从方向对齐和语义分布两个维度直接指导视觉投射器生成更好的初始视觉嵌入。

**[Bidirectional Likelihood Estimation with Multi-Modal Large Language Models for Text-Video Retrieval](bidirectional_likelihood_estimation_with_multi-modal_large_language_models_for_t.md)**

:   揭示了基于MLLM的检索系统中"候选先验偏差"问题——候选似然估计倾向于选择先验概率高而非语义最相关的候选，提出BLiM（双向似然估计）和CPN（候选先验归一化）模块来解决此问题，在四个文本-视频检索基准上平均R@1提升6.4。

**[Boosting MLLM Reasoning with Text-Debiased Hint-GRPO](boosting_mllm_reasoning_with_text-debiased_hint-grpo.md)**

:   揭示GRPO在MLLM推理中的两大问题——低数据利用率（难题上所有输出均错误导致梯度无效）和文本偏差（模型忽视图像仅依赖文本推理），提出Hint-GRPO（自适应提供推理提示）和文本偏差校准（测试时增强图像条件）两套方案，在3个基座MLLM上的11个数据集上显著提升推理能力。

**[CAD-Assistant: Tool-Augmented VLLMs as Generic CAD Task Solvers](cad-assistant_tool-augmented_vllms_as_generic_cad_task_solvers.md)**

:   提出CAD-Assistant，首个面向通用CAD任务的工具增强视觉大语言模型框架，通过集成CAD专用工具集（草图参数化器、渲染模块、约束检查器等）和FreeCAD Python API，在零样本设置下超越了监督式任务特定方法。

**[CapeLLM: Support-Free Category-Agnostic Pose Estimation with Multimodal Large Language Models](capellm_support-free_category-agnostic_pose_estimation_with_multimodal_large_lan.md)**

:   首次将多模态大语言模型（MLLM）引入类别无关姿态估计（CAPE），仅需查询图像和文本描述即可预测任意类别的关键点位置，无需传统的支持图像和标注，在MP-100基准上超越5-shot SOTA。

**[CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance](coa-vla_improving_vision-language-action_models_via_visual-text_chain-of-afforda.md)**

:   提出 CoA-VLA，将四类机器人可供性（物体、抓取、空间、运动）组织为链式推理，通过视觉-文本协同注入模块融合到扩散策略网络中，显著提升 VLA 模型在多任务操作中的精度和泛化能力。

**[CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance](coavla_improving_visionlanguageaction_models_via_visualtext.md)**

:   提出Chain-of-Affordance（CoA-VLA）框架，将四类机器人affordance（物体、抓取、空间、运动）以文本和视觉双模态形式注入VLA模型的策略网络，在真实机器人7任务多任务学习中达到85.54%成功率，比OpenVLA高30.65%，并展现出对未见物体姿态和障碍物的泛化能力。

**[Controlling Multimodal LLMs via Reward-guided Decoding](controlling_multimodal_llms_via_reward-guided_decoding.md)**

:   提出多模态奖励引导解码 (MRGD)，通过构建两个奖励模型分别控制物体精度和召回率，在推理时实现对 MLLM 输出的细粒度可控性，同时显著降低物体幻觉。

**[Controlling Multimodal LLMs via Reward-guided Decoding](controlling_multimodal_llms_via_rewardguided_decoding.md)**

:   提出MRGD（Multimodal Reward-Guided Decoding），通过训练一个基于PaliGemma的物体幻觉奖励模型和一个基于OWLv2的物体召回奖励模型，在MLLM推理时通过线性加权组合两个奖励来逐句搜索最优候选输出，在CHAIR上将LLaVA-1.5的CHAIRi从15.05降至4.53（降70%）且支持精度-召回率的动态可控权衡。

**[CVPT: Cross Visual Prompt Tuning](cvpt_cross_visual_prompt_tuning.md)**

:   针对 Visual Prompt Tuning (VPT) 中 prompt token 参与 self-attention 导致的计算冗余和注意力破坏问题，提出 CVPT，通过 cross-attention 解耦 prompt 与 image token 的交互，并利用权重共享机制初始化 cross-attention，在 25 个数据集上显著超越 VPT，性能媲美主流 adapter 方法。

**[DASH: Detection and Assessment of Systematic Hallucinations of VLMs](dash_detection_and_assessment_of_systematic_hallucinations_of_vlms.md)**

:   提出DASH自动化流水线，通过LLM生成文本查询（DASH-LLM）和扩散模型优化图像查询（DASH-OPT）两种策略，在ReLAION-5B中系统性地发现VLM的假阳性对象幻觉聚类，共发现19k+聚类和950k+图像，并构建了更具挑战性的DASH-B基准。

**[Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](dita_scaling_diffusion_transformer_for_generalist_visionlang.md)**

:   提出Dita，用Transformer架构进行统一的多模态扩散过程直接去噪连续动作序列，通过in-context conditioning实现去噪动作与历史视觉观察的细粒度对齐，在跨embodiment数据集上scaling后实现SOTA仿真性能和10-shot真实世界长horizon任务适应。

**[DocThinker: Explainable Multimodal Large Language Models with Rule-based Reinforcement Learning for Document Understanding](docthinker_explainable_multimodal_large_language_models_with.md)**

:   提出DocThinker，首个将GRPO（Group Relative Policy Optimization）强化学习应用于文档理解的框架，通过四目标规则奖励（格式、答案准确度、RoI IoU、问题改写质量）训练MLLM自主生成可解释的推理过程，仅用4K训练数据在DocVQA上将Qwen2.5-VL-7B从0.355提升到0.579（RL vs SFT: 0.579 vs 0.355），并在视觉定位任务上达到82.4%精度。

**[Dynamic Group Detection using VLM-augmented Temporal Groupness Graph](dynamic_group_detection_using_vlm-augmented_temporal_groupness_graph.md)**

:   本文提出基于VLM增强的时序群组图（temporal groupness graph）进行视频中的动态人群群组检测，核心创新是用CLIP提取包含人对和背景的groupness-augmented特征来估计成组概率，并通过全帧时序图的Louvain聚类实现动态变化群组的检测。

**[Enrich and Detect: Video Temporal Grounding with Multimodal LLMs](enrich_and_detect_video_temporal_grounding_with_multimodal_llms.md)**

:   提出 ED-VTG，将视频时序定位分为"先丰富查询、再预测时间区间"两阶段，利用多模态 LLM 的描述能力增补查询细节，配合轻量区间解码器和多实例学习框架，在多个基准上首次让 LLM 方法全面追平甚至超越专用模型。

**[Evading Data Provenance in Deep Neural Networks](evading_data_provenance_in_deep_neural_networks.md)**

:   揭示了当前数据集所有权验证（DOV）方法的安全假象——通过一个统一的规避框架 Escaping DOV，利用教师模型在 OOD 数据集上向代理学生传输任务相关但标识无关的知识，成功同时绕过所有 11 种 DOV 方法。

**[EVEv2: Improved Baselines for Encoder-Free Vision-Language Models](evev2_improved_baselines_for_encoderfree_visionlanguage_mode.md)**

:   系统性地探索无视觉编码器VLM的最优架构和训练策略，提出Divide-and-Conquer架构将transformer完全分解为模态专用组件（attention/FFN/LayerNorm各模态独立），在仅100M公开数据下超越所有encoder-free同类并接近encoder-based VLM性能。

**[FA: Forced Prompt Learning of Vision-Language Models for Out-of-Distribution Detection](fa_forced_prompt_learning_of_vision-language_models_for_out-of-distribution_dete.md)**

:   提出FA（Forced prompt leArning），通过引入一个可学习的"强制提示"并迫使其产生比冻结原始提示更高的ID类别匹配度，使提示学到超越标签文本语义的丰富ID类别描述，在无需外部辅助数据和额外参数的条件下显著提升基于CLIP的少样本OOD检测性能。

**[FALCON: Resolving Visual Redundancy and Fragmentation in High-resolution Multimodal Large Language Models via Visual Registers](falcon_resolving_visual_redundancy_and_fragmentation_in_high.md)**

:   针对高分辨率MLLM中裁切子图导致的视觉编码分裂和token冗余问题，提出可学习的Visual Registers在encoder内部自适应聚合关键信息（ReCompact）并跨子图交互（ReAtten），实现9倍视觉token压缩且性能更优。

**[Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration](feather_the_throttle_revisiting_visual_token_pruning_for_vis.md)**

:   揭示了VLM中视觉token剪枝方法（如FastV）因RoPE的长程衰减特性导致系统性地保留图像底部token的严重缺陷，并提出FEATHER方法通过去除RoPE+均匀采样+两阶段剪枝修复该问题，在定位任务上实现5倍以上的性能提升。

**[FedMVP: Federated Multimodal Visual Prompt Tuning for Vision-Language Models](fedmvp_federated_multimodal_visual_prompt_tuning_for_vision-language_models.md)**

:   提出FedMVP，在联邦学习场景下通过PromptFormer网络融合图像视觉特征和LLM生成的类别属性文本特征，生成动态多模态视觉提示注入CLIP的视觉编码器，在20个数据集、三种泛化设置下显著超越现有联邦提示学习方法1.57%-2.26%。

**[GRAB: A Challenging GRaph Analysis Benchmark for Large Multimodal Models](grab_a_challenging_graph_analysis_benchmark_for_large_multimodal_models.md)**

:   GRAB 是一个面向大型多模态模型（LMM）的图表分析基准测试，包含 3284 道合成题目覆盖 5 个任务和 23 个图形属性，当前最强模型 Claude 3.5 Sonnet 仅达到 21.0% 的准确率，揭示了 LMM 在视觉分析推理方面的严重不足。

**[GTR: Guided Thought Reinforcement Prevents Thought Collapse in RL-Based VLM Agent](gtr_guided_thought_reinforcement_prevents_thought_collapse_in_rl-based_vlm_agent.md)**

:   发现 VLM 智能体在 RL 训练中仅依赖结果奖励会导致"思维崩塌"（thought collapse），提出 GTR 框架通过外部 VLM 纠正器自动纠正推理过程并结合 PPO + SFT 联合训练思维和行动，在 24 点游戏和 ALFWorld 环境中实现 3-5 倍的任务成功率提升。

**[Harmonizing Visual Representations for Unified Multimodal Understanding and Generation](harmonizing_visual_representations_for_unified_multimodal_un.md)**

:   发现Masked Autoregressive (MAR)模型的编码器同时具备优秀的语义理解能力和生成能力，基于此提出Harmon框架——用共享的MAR编码器统一视觉理解和生成任务，通过三阶段渐进训练在生成benchmark上达SOTA同时在理解benchmark上匹配专用语义编码器方法。

**[IDEATOR: Jailbreaking and Benchmarking Large Vision-Language Models Using Themselves](ideator_jailbreaking_and_benchmarking_large_visionlanguage_m.md)**

:   提出IDEATOR，首个用VLM自身做红队攻击VLM的黑盒越狱框架——利用一个弱安全对齐的VLM（MiniGPT-4）作为攻击者，结合Stable Diffusion生成语义丰富的图文越狱对，通过breadth-depth探索策略迭代优化，在MiniGPT-4上达94%攻击成功率（平均5.34次查询），迁移到LLaVA/InstructBLIP/Chameleon达75-88%，并构建VLJailbreakBench（3654样本）揭示11个VLM的安全漏洞。

**[Jailbreaking Multimodal Large Language Models via Shuffle Inconsistency](jailbreaking_multimodal_large_language_models_via_shuffle_inconsistency.md)**

:   发现多模态大语言模型(MLLMs)在理解能力和安全能力之间存在**打乱不一致性(Shuffle Inconsistency)**——模型能理解打乱后的有害指令，但安全机制却无法防御；据此提出基于查询的黑盒越狱攻击方法 SI-Attack，在开源和闭源商用模型上均显著提升攻击成功率。

**[LATTE: Collaborative Test-Time Adaptation of Vision-Language Models in Federated Learning](latte_collaborative_test-time_adaptation_of_vision-language_models_in_federated_.md)**

:   提出 Latte 框架，在联邦学习的去中心化场景下，通过本地记忆与外部记忆的协同机制，实现视觉语言模型（如 CLIP）的协作式测试时自适应，兼顾跨客户端知识共享与个性化。

**[LLaVA-CoT: Let Vision Language Models Reason Step-by-Step](llavacot_let_vision_language_models_reason_stepbystep.md)**

:   通过构建包含结构化推理标注的LLaVA-CoT-100k数据集，训练VLM自主执行"总结→视觉解读→逻辑推理→结论"四阶段推理，配合测试时SWIRES搜索策略，11B模型超越GPT-4o-mini和Gemini-1.5-pro等大模型。

**[LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models](llavaprumerge_adaptive_token_reduction_for_efficient_large_m.md)**

:   利用CLIP-ViT中[CLS] token与视觉token之间注意力分数的稀疏特性，通过IQR异常值检测自适应选择重要视觉token，再用k-近邻聚类将被剪除token的信息合并回保留token，实现视觉token 14倍压缩且性能几乎不降。

**[MAVias: Mitigate Any Visual Bias](mavias_mitigate_any_visual_bias.md)**

:   提出 MAVias，一个开放集视觉偏差缓解框架：利用图像标注基础模型提取视觉属性标签，用 LLM 筛选与目标类别无关的标签作为潜在偏差，再通过 vision-language embedding 编码偏差并融入训练过程以学习偏差不变表示，在 CelebA、Waterbirds、UrbanCars 和 ImageNet9 上大幅超越现有方法。

**[MetaMorph: Multimodal Understanding and Generation via Instruction Tuning](metamorph_multimodal_understanding_and_generation_via_instru.md)**

:   提出Visual-Predictive Instruction Tuning (VPiT)——一种简单有效的视觉指令微调扩展，让预训练LLM同时预测离散文本token和连续视觉token，发现视觉生成能力是视觉理解能力提升的自然副产物，少量生成数据即可解锁，LLM的预训练知识可以迁移到视觉生成中克服常见失败模式。

**[Mitigating Object Hallucinations via Sentence-Level Early Intervention](mitigating_object_hallucinations_via_sentence-level_early_intervention.md)**

:   提出 SENTINEL 框架，通过句子级早期干预和域内偏好学习有效缓解 MLLM 的物体幻觉，在 Object HalBench 上将幻觉率降低超过 90%，同时保持甚至提升通用能力。

**[MM-IFEngine: Towards Multimodal Instruction Following](mm-ifengine_towards_multimodal_instruction_following.md)**

:   提出 MM-IFEngine 管线，系统性地生成高质量的图像-指令对数据（含 SFT 和 DPO 版本），并构建 MM-IFEval 基准，显著提升 MLLM 在多模态指令遵循任务上的表现。

**[MMAT-1M: A Large Reasoning Dataset for Multimodal Agent Tuning](mmat1m_a_large_reasoning_dataset_for_multimodal_agent_tuning.md)**

:   提出首个百万规模的多模态agent调优数据集MMAT-1M，通过四阶段数据引擎（基础数据→推理轨迹生成→反思纠错→格式整合）为MLLM注入CoT推理、工具调用和反思能力，在InternVL2.5-8B上平均提升2.7%，RAG任务上提升8.8%。

**[MUSE-VL: Modeling Unified VLM through Semantic Discrete Encoding](muse-vl_modeling_unified_vlm_through_semantic_discrete_encoding.md)**

:   提出语义离散编码 (SDE)，通过在视觉 tokenizer 的量化过程中融入预训练 CLIP 语义特征，使离散视觉 token 与语言 token 天然对齐，在仅用 24M 图文对的情况下实现了统一理解与生成的 SOTA 性能。

**[MUSE-VL: Modeling Unified VLM through Semantic Discrete Encoding](musevl_modeling_unified_vlm_through_semantic_discrete_encodi.md)**

:   提出语义离散编码（SDE）视觉tokenizer，在VQGAN基础上加入SigLIP语义特征约束，使离散视觉token与语言token语义对齐，构建统一的自回归VLM（MUSE-VL），在仅用24M数据的条件下理解性能比Emu3提升4.8%，超过LLaVA-NeXT 34B专用理解模型3.7%，同时支持图像生成。

**[ONLY: One-Layer Intervention Sufficiently Mitigates Hallucinations in Large Vision-Language Models](only_onelayer_intervention_sufficiently_mitigates_hallucinat.md)**

:   提出ONLY，一种training-free的单层干预解码方法——通过Text-to-Visual Entropy Ratio（TVER）选择偏向文本的attention head生成textually-enhanced logits，然后与原始logits做自适应对比/协作解码，仅增加1.07×推理时间就在POPE上比VCD/M3ID高3.14%，在CHAIR上降低CHAIR_S 6.2个点。

**[Pi-GPS: Enhancing Geometry Problem Solving by Unleashing the Power of Diagrammatic Information](pi-gps_enhancing_geometry_problem_solving_by_unleashing_the_power_of_diagrammati.md)**

:   Pi-GPS 提出利用几何图形信息消解文本描述中的歧义，通过"纠正器+验证器"微模块解决了先前被忽视的文本模糊性问题，在 Geometry3K 上比此前最优神经符号方法提升近 10%。

**[PRO-VPT: Distribution-Adaptive Visual Prompt Tuning via Prompt Relocation](pro-vpt_distribution-adaptive_visual_prompt_tuning_via_prompt_relocation.md)**

:   提出 PRO-VPT 框架，通过嵌套优化将提示分布优化 (ADO) 与视觉提示调优 (VPT) 协同设计，利用闲置分数剪枝和强化学习分配策略迭代重定位提示，在 VTAB-1k 和 FGVC 上较 VPT 分别提升 1.6pp 和 2.0pp。

**[Safeguarding Vision-Language Models: Mitigating Vulnerabilities to Gaussian Noise in Perturbation-based Attacks](safeguarding_vision-language_models_mitigating_vulnerabilities_to_gaussian_noise.md)**

:   发现主流VLM普遍缺乏高斯噪声鲁棒性，提出Robust-VLGuard安全数据集（含图文对齐/不对齐场景）配合噪声增强微调提升高斯噪声鲁棒性，再结合DiffPure将对抗噪声转化为高斯噪声，构建DiffPure-VLM通用防御框架，有效抵御多种强度的对抗攻击。

**[Scaling Inference-Time Search with Vision Value Model for Improved Visual Comprehension](scaling_inferencetime_search_with_vision_value_model_for_imp.md)**

:   提出Vision Value Model（VisVM），用TD learning训练一个能预测VLM生成句子长期价值的价值网络，指导推理时逐句搜索生成更少幻觉、更丰富细节的图像描述，并进一步将VisVM生成的高质量caption用于自训练，在9个benchmark上平均提升LLaVA-Next 10.8%。

**[Scaling Laws for Native Multimodal Models](scaling_laws_for_native_multimodal_models.md)**

:   通过训练457个不同架构和训练配比的模型进行系统性scaling law研究，发现Native Multimodal Models（NMM）的early-fusion架构（不依赖视觉编码器/tokenizer）在小参数量时优于late-fusion，训练更高效且部署更简单，结合MoE可进一步显著提升性能。

**[ShortV: Efficient Multimodal Large Language Models by Freezing Visual Tokens in Ineffective Layers](shortv_efficient_multimodal_large_language_models_by_freezin.md)**

:   发现MLLM中约60%的层对视觉token的变换几乎不影响模型输出（Layer Contribution极低），提出ShortV方法在这些"ineffective layers"中冻结视觉token（不参与attention query和FFN），在LLaVA-NeXT-13B上实现50% FLOPs降低且性能几乎不变，且与token剪枝方法（如FastV）正交可叠加。

**[SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs](sparsemm_head_sparsity_emerges_from_visual_concept_responses.md)**

:   发现MLLM中仅约5%的attention head主动参与视觉理解（称为"visual heads"），提出基于OCR任务的training-free识别方法量化每个head的视觉相关性，并设计SparseMM——按visual score非对称分配KV-Cache预算的策略，在DocVQA上仅用5.3%的cache（256/4830）即可维持Qwen2-VL的性能，实现1.87×加速和50%内存减少。

**[SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference](sparsevila_decoupling_visual_sparsity_for_efficient_vlm_infe.md)**

:   提出SparseVILA，将VLM推理时的视觉token稀疏化解耦为两个阶段——prefill阶段做query-agnostic剪枝（去冗余）、decode阶段做query-aware检索（精选相关token），在长视频任务上实现4.0×prefill加速、2.5×decode加速、2.6×端到端加速，同时在视频理解benchmark上精度不降反升。

**[Sparsity Outperforms Low-Rank Projections in Few-Shot Adaptation](sparsity_outperforms_low-rank_projections_in_few-shot_adaptation.md)**

:   提出稀疏优化（SO）框架，通过动态稀疏梯度选择和基于重要性的动量剪枝来替代低秩适配方法（如LoRA），在11个数据集上的少样本VLM适配任务中实现了SOTA，同时降低了内存开销。

**[ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools](toolvqa_a_dataset_for_multistep_reasoning_vqa_with_external.md)**

:   提出ToolVQA，一个23K样本的多模态工具使用VQA数据集，通过ToolEngine数据生成pipeline（图像引导DFS + LCS示例匹配）从真实图像中构造隐式多步推理问题（平均2.78步），在该数据上微调LLaVA-7B后在5个OOD benchmark上超过GPT-3.5-Turbo，并揭示了当前LFM在参数预测和答案总结方面的瓶颈。

**[Unified Multimodal Understanding via Byte-Pair Visual Encoding](unified_multimodal_understanding_via_byte-pair_visual_encoding.md)**

:   将 NLP 中的 Byte-Pair Encoding (BPE) 策略应用于视觉 token 化，提出优先级引导的编码方案（融合频率和空间一致性）、课程式数据混合和渐进式参数解冻三阶段训练策略，构建的 Being-VL-0.5（8B）在离散 token 路线上接近连续 embedding 方法的主流水平。

**[Visual Interestingness Decoded: How GPT-4o Mirrors Human Interests](visual_interestingness_decoded_how_gpt-4o_mirrors_human_interests.md)**

:   系统性研究了 GPT-4o 等大型多模态模型对"图像有趣性"这一主观视觉概念的理解程度，发现 GPT-4o 与人类评判有中等正相关（配对图像一致率 73.8%），并提出利用 GPT-4o 自动标注图像对训练 learning-to-rank 模型来预测图像有趣性，超越了所有现有方法。

**[WikiAutoGen: Towards Multi-Modal Wikipedia-Style Article Generation](wikiautogen_towards_multi-modal_wikipedia-style_article_generation.md)**

:   提出 WikiAutoGen 多智能体框架，通过整合文本和图像的多模态检索与多视角自反思机制，自动生成高质量的多模态 Wikipedia 风格文章，在自建基准 WikiSeek 上相比已有方法提升 8%–29%。
