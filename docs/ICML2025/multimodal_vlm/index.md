<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🧩 多模态 VLM

**🧪 ICML2025** · 共 **23** 篇

**[A Cross Modal Knowledge Distillation & Data Augmentation Recipe for Improving Transcriptomics Representations through Morphological Features](a_cross_modal_knowledge_distillation_data_augmentation_recipe_for_improving_tran.md)**

:   提出 Semi-Clipped（基于 CLIP 的跨模态蒸馏方法）和 PEA（扰动嵌入增强），在弱配对数据场景下将显微镜图像的丰富形态学特征蒸馏到转录组学表征中，在保持基因表达可解释性的同时显著提升其预测能力。

**[Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](bring_reason_to_vision_understanding_perception_and_reasoning_through_model_merg.md)**

:   通过将数学推理 LLM 的参数与 VLM 的文本部分直接加权平均（模型融合），在无需训练的情况下将推理能力迁移到 VLM，并发现感知能力集中在前层、推理能力集中在中后层的层级分布规律。

**[CoCoA-Mix: Confusion-and-Confidence-Aware Mixture Model for Context Optimization](cocoa-mix_confusion-and-confidence-aware_mixture_model_for_context_optimization.md)**

:   提出 CoCoA-Mix 框架，通过混淆感知损失 (CoA-loss) 和置信度感知权重 (CoA-weights) 构建提示混合模型，在不引入额外网络参数的情况下同时提升 VLM prompt tuning 的专精性 (specialization) 和泛化性 (generalization)。

**[Core Knowledge Deficits in Multi-Modal Language Models](core_knowledge_deficits_in_multi-modal_language_models.md)**

:   提出 CoreCognition 基准（12种核心认知能力、1503题），大规模评测230个MLLM后发现：模型在基础认知能力上系统性落后于人类，且随规模增大并未改善，而是更依赖捷径学习而非真正理解。

**[CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](corematching_a_co-adaptive_sparse_inference_framework_with_token_and_neuron_prun.md)**

:   首次揭示 VLM 中 token 稀疏与神经元稀疏之间的内在关联——核心神经元与核心 token 相互决定、相互强化，并据此提出 CoreMatching 协同稀疏推理框架，在 pre-filling 和 decoding 两阶段同时实现加速，达到 5× FLOPs 降低和 10× 整体加速。

**[DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](defame_dynamic_evidence-based_fact-checking_with_multimodal_experts.md)**

:   提出 DEFAME，一个模块化零样本多模态 LLM 流水线，通过六阶段动态流程（规划→执行→摘要→推理→判决→解释）结合外部多模态工具检索证据，实现端到端的文本-图像联合事实核查，在 AVeriTeC、MOCHEG、VERITE 三个基准上均达到新 SOTA。

**[Defending LVLMs Against Vision Attacks through Partial-Perception Supervision](defending_lvlms_against_vision_attacks_through_partial-perception_supervision.md)**

:   提出 DPS（Defense through Partial-Perception Supervision），利用裁剪图像的响应作为"弱监督"来引导全图模型在推理时自我修正，实现无需训练的黑盒 LVLM 视觉攻击防御，平均攻击成功率降低 76.3%。

**[Efficient Quantification of Multimodal Interaction at Sample Level](efficient_quantification_of_multimodal_interaction_at_sample_level.md)**

:   提出 LSMI（Lightweight Sample-wise Multimodal Interaction）估计器，首次实现了对真实世界连续分布数据的**逐样本级别**多模态交互（冗余、唯一性、协同）精确且高效的量化，并展示了其在数据分区、知识蒸馏和模型集成中的实用价值。

**[ERL-VLM: Enhancing Rating-Based RL to Leverage Feedback from Large VLMs](enhancing_rating-based_reinforcement_learning_to_effectively_leverage_feedback_f.md)**

:   提出 ERL-VLM，用大型视觉语言模型（VLM）对单条轨迹做绝对评分（rating）而非成对比较（preference），结合分层采样和 MAE 损失解决数据不平衡与噪声标签问题，显著提升 VLM 反馈驱动的奖励函数学习效果。

**[ExLM: Rethinking the Impact of [MASK] Tokens in Masked Language Models](exlm_rethinking_the_impact_of_mask_tokens_in_masked_language_models.md)**

:   本文首次系统分析了 MLM 中 [MASK] 对性能的影响，发现**语义损坏（corrupted semantics）**比**非真实token（unreal tokens）**的负面作用更大，据此提出 ExLM：通过将每个 [MASK] 扩展为多个隐状态并用转移矩阵建模依赖关系，有效缓解语义多模态性问题，在文本和分子建模任务上均取得显著提升。

**[From Black Boxes To Transparent Minds Evaluating And Enhancing The Theory Of Min](from_black_boxes_to_transparent_minds_evaluating_and_enhancing_the_theory_of_min.md)**

:   本文从可解释性角度评估多模态大模型（MLLM）的心智理论（ToM）能力，构建了基于 2D 网格世界的多模态 ToM 数据集 GridToM，并提出一种无需训练的注意力头激活干预方法来显著提升模型的 ToM 表现。

**[Graph4MM: Weaving Multimodal Learning with Structural Information](graph4mm_weaving_multimodal_learning_with_structural_information.md)**

:   提出 Graph4MM 框架，通过 Hop-Diffused Attention 将多跳图结构信息注入自注意力机制，并设计 MM-QFormer 实现跨模态融合，在生成和判别任务上平均提升 6.93%。

**[Handling Imbalanced Pseudolabels for Vision-Language Models with Concept Alignment and Confusion-Aware Calibrated Margin](handling_imbalanced_pseudolabels_for_vision-language_models_with_concept_alignme.md)**

:   提出 CAP 框架，通过**概念对齐**（检测并修复 concept mismatch）和**混淆感知校准边距**（缓解 concept confusion），解决 VLM 生成伪标签时的类别不平衡问题，在六个数据集三种范式下相对 SOTA 提升 6.29%。

**[Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](kernel-based_unsupervised_embedding_alignment_for_enhanced_visual_representation.md)**

:   提出基于核函数的无监督嵌入对齐方法（KUEA），通过在核空间中对齐 CLIP 与 DINOv2 的视觉表示，仅用图像数据微调即可增强 CLIP 的细粒度感知能力，同时保持与文本编码器的兼容性，提升下游 MLLM 性能。

**[LADA: Scalable Label-Specific CLIP Adapter for Continual Learning](lada_scalable_label-specific_clip_adapter_for_continual_learning.md)**

:   提出 LADA（Label-specific ADApter），通过在冻结 CLIP 图像编码器后追加轻量级的**类别特定记忆向量**，将所有已学任务的判别信息浓缩到统一特征空间，**彻底消除推理阶段的参数选择步骤**，在 X-TAIL 持续学习设定下取得 SOTA。

**[Learning Invariant Causal Mechanism from Vision-Language Models](learning_invariant_causal_mechanism_from_vision-language_models.md)**

:   通过因果分析证明 CLIP 嵌入是真实不变/可变因子的线性变换，提出 CLIP-ICM 框架利用干预数据估计线性投影矩阵，将预测限定在不变子空间中以实现跨环境一致预测。

**[Learning Optimal Multimodal Information Bottleneck Representations](learning_optimal_multimodal_information_bottleneck_representations.md)**

:   提出 OMIB 框架，通过理论推导正则化参数 β 的上界并动态调整各模态权重 r，保证多模态信息瓶颈表示的最优性（包含全部任务相关信息、排除冗余信息）。

**[Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](look_twice_before_you_answer_memory-space_visual_retracing_for_hallucination_mit.md)**

:   提出 MemVR 解码范式，将视觉 token 作为补充证据通过 FFN 的 key-value memory 机制重新注入到中间触发层，以"再看一次"的方式缓解 MLLM 幻觉问题，不引入额外推理开销。

**[Parrot: Multilingual Visual Instruction Tuning](parrot_multilingual_visual_instruction_tuning.md)**

:   提出 Parrot，通过文本引导的跨注意力机制和 MoE 模块将英语偏置的视觉特征转换为语言特定表示，以极少量多语言数据（每种语言约 10K 样本）显著提升 MLLM 的多语言能力。

**[Reasoning Limitations of Multimodal Large Language Models. A Case Study of Bongard Problems](reasoning_limitations_of_multimodal_large_language_models_a_case_study_of_bongar.md)**

:   系统评估了 8 个 MLLM 在 Bongard Problems 上的抽象视觉推理能力，并引入 Bongard-RWR 数据集（合成概念的真实图像版本），揭示 MLLM 在合成 BP 上表现极差并非因领域差异，而是其固有的抽象推理局限。

**[Rollingq Reviving The Cooperation Dynamics In Multimodal Transformer](rollingq_reviving_the_cooperation_dynamics_in_multimodal_transformer.md)**

:   揭示多模态 Transformer 中自注意力机制因"自增强循环"导致动态适应性失效（偏向单一模态），并提出 RollingQ 算法通过旋转 query 向量打破这一循环，恢复跨模态协作动态。

**[Sk-Vqa Synthetic Knowledge Generation At Scale For Training Context-Augmented Mu](sk-vqa_synthetic_knowledge_generation_at_scale_for_training_context-augmented_mu.md)**

:   利用 GPT-4 全自动生成包含 200 万+ QA 对的大规模合成 KB-VQA 数据集 SK-VQA，训练 MLLM 适配上下文增强生成，在跨域泛化性能上显著优于已有数据集。

**[Universal Retrieval for Multimodal Trajectory Modeling](universal_retrieval_for_multimodal_trajectory_modeling.md)**

:   首次提出多模态轨迹检索（Multimodal Trajectory Retrieval）任务，构建统一代理轨迹数据集 UATD 和 GAE-Bench 基准，并提出基于 VLM 的 GAE-Retriever 框架，在轨迹级检索上显著优于基线。
