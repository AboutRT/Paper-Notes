<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**📹 ICCV2025** · 共 **34** 篇

**[AdvDreamer Unveils: Are Vision-Language Models Truly Ready for Real-World 3D Variations?](advdreamer_unveils_are_visionlanguage_models_truly_ready_for.md)**

:   提出AdvDreamer框架从单张图像生成物理可复现的对抗性3D变换(Adv-3DT)样本，通过零样本单目姿态操作+自然度奖励模型+逆语义概率损失，揭示当前VLM（包括GPT-4o）在3D变化下性能下降高达50-80%，并建立首个3D变化鲁棒性VQA基准MM3DTBench。

**[CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance](coavla_improving_visionlanguageaction_models_via_visualtext.md)**

:   提出Chain-of-Affordance（CoA-VLA）框架，将四类机器人affordance（物体、抓取、空间、运动）以文本和视觉双模态形式注入VLA模型的策略网络，在真实机器人7任务多任务学习中达到85.54%成功率，比OpenVLA高30.65%，并展现出对未见物体姿态和障碍物的泛化能力。

**[Controlling Multimodal LLMs via Reward-guided Decoding](controlling_multimodal_llms_via_reward-guided_decoding.md)**

:   提出多模态奖励引导解码 (MRGD)，通过构建两个奖励模型分别控制物体精度和召回率，在推理时实现对 MLLM 输出的细粒度可控性，同时显著降低物体幻觉。

**[Controlling Multimodal LLMs via Reward-guided Decoding](controlling_multimodal_llms_via_rewardguided_decoding.md)**

:   提出MRGD（Multimodal Reward-Guided Decoding），通过训练一个基于PaliGemma的物体幻觉奖励模型和一个基于OWLv2的物体召回奖励模型，在MLLM推理时通过线性加权组合两个奖励来逐句搜索最优候选输出，在CHAIR上将LLaVA-1.5的CHAIRi从15.05降至4.53（降70%）且支持精度-召回率的动态可控权衡。

**[CVPT: Cross Visual Prompt Tuning](cvpt_cross_visual_prompt_tuning.md)**

:   针对 Visual Prompt Tuning (VPT) 中 prompt token 参与 self-attention 导致的计算冗余和注意力破坏问题，提出 CVPT，通过 cross-attention 解耦 prompt 与 image token 的交互，并利用权重共享机制初始化 cross-attention，在 25 个数据集上显著超越 VPT，性能媲美主流 adapter 方法。

**[Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](dita_scaling_diffusion_transformer_for_generalist_visionlang.md)**

:   提出Dita，用Transformer架构进行统一的多模态扩散过程直接去噪连续动作序列，通过in-context conditioning实现去噪动作与历史视觉观察的细粒度对齐，在跨embodiment数据集上scaling后实现SOTA仿真性能和10-shot真实世界长horizon任务适应。

**[DocThinker: Explainable Multimodal Large Language Models with Rule-based Reinforcement Learning for Document Understanding](docthinker_explainable_multimodal_large_language_models_with.md)**

:   提出DocThinker，首个将GRPO（Group Relative Policy Optimization）强化学习应用于文档理解的框架，通过四目标规则奖励（格式、答案准确度、RoI IoU、问题改写质量）训练MLLM自主生成可解释的推理过程，仅用4K训练数据在DocVQA上将Qwen2.5-VL-7B从0.355提升到0.579（RL vs SFT: 0.579 vs 0.355），并在视觉定位任务上达到82.4%精度。

**[Dynamic Group Detection using VLM-augmented Temporal Groupness Graph](dynamic_group_detection_using_vlm-augmented_temporal_groupness_graph.md)**

:   本文提出基于VLM增强的时序群组图（temporal groupness graph）进行视频中的动态人群群组检测，核心创新是用CLIP提取包含人对和背景的groupness-augmented特征来估计成组概率，并通过全帧时序图的Louvain聚类实现动态变化群组的检测。

**[EVEv2: Improved Baselines for Encoder-Free Vision-Language Models](evev2_improved_baselines_for_encoderfree_visionlanguage_mode.md)**

:   系统性地探索无视觉编码器VLM的最优架构和训练策略，提出Divide-and-Conquer架构将transformer完全分解为模态专用组件（attention/FFN/LayerNorm各模态独立），在仅100M公开数据下超越所有encoder-free同类并接近encoder-based VLM性能。

**[FALCON: Resolving Visual Redundancy and Fragmentation in High-resolution Multimodal Large Language Models via Visual Registers](falcon_resolving_visual_redundancy_and_fragmentation_in_high.md)**

:   针对高分辨率MLLM中裁切子图导致的视觉编码分裂和token冗余问题，提出可学习的Visual Registers在encoder内部自适应聚合关键信息（ReCompact）并跨子图交互（ReAtten），实现9倍视觉token压缩且性能更优。

**[Feather the Throttle: Revisiting Visual Token Pruning for Vision-Language Model Acceleration](feather_the_throttle_revisiting_visual_token_pruning_for_vis.md)**

:   揭示了VLM中视觉token剪枝方法（如FastV）因RoPE的长程衰减特性导致系统性地保留图像底部token的严重缺陷，并提出FEATHER方法通过去除RoPE+均匀采样+两阶段剪枝修复该问题，在定位任务上实现5倍以上的性能提升。

**[Harmonizing Visual Representations for Unified Multimodal Understanding and Generation](harmonizing_visual_representations_for_unified_multimodal_un.md)**

:   发现Masked Autoregressive (MAR)模型的编码器同时具备优秀的语义理解能力和生成能力，基于此提出Harmon框架——用共享的MAR编码器统一视觉理解和生成任务，通过三阶段渐进训练在生成benchmark上达SOTA同时在理解benchmark上匹配专用语义编码器方法。

**[IDEATOR: Jailbreaking and Benchmarking Large Vision-Language Models Using Themselves](ideator_jailbreaking_and_benchmarking_large_visionlanguage_m.md)**

:   提出IDEATOR，首个用VLM自身做红队攻击VLM的黑盒越狱框架——利用一个弱安全对齐的VLM（MiniGPT-4）作为攻击者，结合Stable Diffusion生成语义丰富的图文越狱对，通过breadth-depth探索策略迭代优化，在MiniGPT-4上达94%攻击成功率（平均5.34次查询），迁移到LLaVA/InstructBLIP/Chameleon达75-88%，并构建VLJailbreakBench（3654样本）揭示11个VLM的安全漏洞。

**[Jailbreaking Multimodal Large Language Models via Shuffle Inconsistency](jailbreaking_multimodal_large_language_models_via_shuffle_inconsistency.md)**

:   发现多模态大语言模型(MLLMs)在理解能力和安全能力之间存在**打乱不一致性(Shuffle Inconsistency)**——模型能理解打乱后的有害指令，但安全机制却无法防御；据此提出基于查询的黑盒越狱攻击方法 SI-Attack，在开源和闭源商用模型上均显著提升攻击成功率。

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

**[PRO-VPT: Distribution-Adaptive Visual Prompt Tuning via Prompt Relocation](pro-vpt_distribution-adaptive_visual_prompt_tuning_via_prompt_relocation.md)**

:   提出 PRO-VPT 框架，通过嵌套优化将提示分布优化 (ADO) 与视觉提示调优 (VPT) 协同设计，利用闲置分数剪枝和强化学习分配策略迭代重定位提示，在 VTAB-1k 和 FGVC 上较 VPT 分别提升 1.6pp 和 2.0pp。

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

**[ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools](toolvqa_a_dataset_for_multistep_reasoning_vqa_with_external.md)**

:   提出ToolVQA，一个23K样本的多模态工具使用VQA数据集，通过ToolEngine数据生成pipeline（图像引导DFS + LCS示例匹配）从真实图像中构造隐式多步推理问题（平均2.78步），在该数据上微调LLaVA-7B后在5个OOD benchmark上超过GPT-3.5-Turbo，并揭示了当前LFM在参数预测和答案总结方面的瓶颈。

**[Unified Multimodal Understanding via Byte-Pair Visual Encoding](unified_multimodal_understanding_via_byte-pair_visual_encoding.md)**

:   将 NLP 中的 Byte-Pair Encoding (BPE) 策略应用于视觉 token 化，提出优先级引导的编码方案（融合频率和空间一致性）、课程式数据混合和渐进式参数解冻三阶段训练策略，构建的 Being-VL-0.5（8B）在离散 token 路线上接近连续 embedding 方法的主流水平。

**[Visual Interestingness Decoded: How GPT-4o Mirrors Human Interests](visual_interestingness_decoded_how_gpt-4o_mirrors_human_interests.md)**

:   系统性研究了 GPT-4o 等大型多模态模型对"图像有趣性"这一主观视觉概念的理解程度，发现 GPT-4o 与人类评判有中等正相关（配对图像一致率 73.8%），并提出利用 GPT-4o 自动标注图像对训练 learning-to-rank 模型来预测图像有趣性，超越了所有现有方法。

**[WikiAutoGen: Towards Multi-Modal Wikipedia-Style Article Generation](wikiautogen_towards_multi-modal_wikipedia-style_article_generation.md)**

:   提出 WikiAutoGen 多智能体框架，通过整合文本和图像的多模态检索与多视角自反思机制，自动生成高质量的多模态 Wikipedia 风格文章，在自建基准 WikiSeek 上相比已有方法提升 8%–29%。
