<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**🧪 ICML2025** · 共 **42** 篇

**[A Mathematical Framework for AI-Human Integration in Work](a_mathematical_framework_for_ai-human_integration_in_work.md)**

:   本文提出了一个评估 AI-人类工作集成的数学框架，将技能分解为决策层和执行层两类子技能，理论证明了工作成功概率存在相变效应、互补技能融合可带来超加性收益，并解释了 GenAI 辅助中低技能工人获益更大的"生产力压缩"现象，通过 O*NET 和 Big-bench Lite 数据验证了框架的实用性。

**[ABKD: Pursuing a Proper Allocation of the Probability Mass in Knowledge Distillation via α-β-Divergence](abkd_pursuing_a_proper_allocation_of_the_probability_mass_in_knowledge_distillat.md)**

:   本文深入分析了知识蒸馏中 FKLD 和 RKLD 的概率质量分配缺陷，发现它们在 Hardness-Concentration 和 Confidence-Concentration 两种效应上分别处于极端，提出基于 α-β-divergence 的 ABKD 框架，通过调节 α 和 β 灵活平衡两种效应，在 17 个语言/视觉数据集、12 种师生配置上取得了 SOTA 性能。

**[Agent WARPP: Workflow Adherence via Runtime Parallel Personalization](agent_warpp_workflow_adherence_via_runtime_parallel_personalization.md)**

:   提出 WARPP，一个无需训练的多智能体框架，在运行时根据用户属性动态剪枝条件分支工作流，并通过并行化的 Personalizer 智能体与模块化域特定智能体协同执行，在提升工具调用精度和参数保真度的同时减少 token 消耗。

**[An Efficient Matrix Multiplication Algorithm for Accelerating Inference in Binary and Ternary Neural Networks](an_efficient_matrix_multiplication_algorithm_for_accelerating_inference_in_binar.md)**

:   提出 RSR/RSR++ 算法——通过预处理固定的二值/三值权重矩阵构建分桶排列索引，实现 $O(n^2/\log n)$ 复杂度的向量-矩阵乘法，比标准 $O(n^2)$ 方法快最高 29× 的矩阵乘法、6× 的内存节省，并在 1.58-bit LLM 推理中实现 5.24× 加速。

**[any4: Learned 4-bit Numeric Representation for LLMs](any4_learned_4-bit_numeric_representation_for_llms.md)**

:   提出 any4——一种通过 k-means 聚类学习每行权重矩阵的最优 4-bit 非均匀量化码本的方法，无需权重/激活预处理，在 Llama 2/3、Mistral、Mixtral 上均优于 int4/fp4/nf4，且仅用单个校准样本即可。

**[Beyond Communication Overhead: A Multilevel Monte Carlo Approach for Mitigating Compression Bias in Distributed Learning](beyond_communication_overhead_a_multilevel_monte_carlo_approach_for_mitigating_c.md)**

:   本文提出了一种基于多级蒙特卡洛（MLMC）的梯度压缩方案，利用有偏压缩器构造统计无偏的梯度估计，将压缩偏差转化为可控方差，从而在保持有偏压缩器经验效率的同时享受无偏方法的理论保证，结合自适应概率优化在 BERT 微调和 CIFAR-10 上验证了优越性。

**[BlockDialect: Block-wise Fine-grained Mixed Format Quantization for Energy-Efficient LLM Inference](blockdialect_block-wise_fine-grained_mixed_format_quantization_for_energy-effici.md)**

:   提出 BlockDialect——对权重和激活进行块级细粒度混合格式量化，为每个 block 从 FP4 变体（方言）格式书中选择最优数值格式，在 LLaMA3-8B 上比 MXFP4 准确率提升 10.78%，仅比全精度低 5.45%。

**[BoA: Attention-aware Post-training Quantization without Backpropagation](boa_attention-aware_post-training_quantization_without_backpropagation.md)**

:   提出 BoA——首个在训练后量化中考虑跨层依赖性的无反向传播算法，通过构建注意力感知 Hessian 矩阵捕捉注意力模块内的层间交互，在低位宽（INT2）下显著超越现有 PTQ 方法。

**[Context Tuning for In-Context Optimization](context_tuning_for_in-context_optimization.md)**

:   提出 Context Tuning，用少样本示例初始化可训练的 prompt/KV 前缀，通过梯度优化上下文表示（而非模型参数）来增强 LLM 的 few-shot 适应能力，CT-KV 变体在线性时间复杂度下达到与 TTT 竞争的精度。

**[Core Context Aware Transformers for Long Context Language Modeling](core_context_aware_transformers_for_long_context_language_modeling.md)**

:   提出 Core Context Aware (CCA) Attention，通过全局感知池化将输入 token 动态压缩为少量核心 token，结合局部保持模块捕获邻近细粒度信息，实现即插即用地替换标准自注意力，在 128K 上下文下获得 7.9× 加速和 46% 显存节省，同时保持建模性能。

**[DLP: Dynamic Layerwise Pruning in Large Language Models](dlp_dynamic_layerwise_pruning_in_large_language_models.md)**

:   提出动态层级剪枝方法 DLP，利用权重与激活值的中位数自适应计算每层的相对重要性，按"越重要稀疏率越低"的原则进行非均匀剪枝，在 70% 高稀疏率下将 LLaMA2-7B 的困惑度降低 7.79、平均零样本准确率提升 2.7%。

**[Do Sparse Autoencoders Generalize? A Case Study of Answerability](do_sparse_autoencoders_generalize_a_case_study_of_answerability.md)**

:   本文系统评估了稀疏自编码器（SAE）提取的特征在"可回答性"（answerability）任务上的跨域泛化能力，发现 SAE 特征的域外迁移表现极不一致——在某些数据集上优于残差流线性探针，但在另一些上接近随机，揭示了当前 SAE 可解释性方法在捕获抽象概念方面的根本局限。

**[DRAGON: Guard LLM Unlearning in Context via Negative Detection and Reasoning](dragon_guard_llm_unlearning_in_context_via_negative_detection_and_reasoning.md)**

:   提出 DRAGON，一种无需微调的 LLM 遗忘框架，通过双层检测模块识别需遗忘的 prompt，再由 CoT guard 模型生成推理指令做上下文干预，在不修改模型参数的前提下实现高效遗忘。

**[Expert Evaluation of LLM World Models: A High-Tc Superconductivity Case Study](expert_evaluation_of_llm_world_models_a_high-t_c_superconductivity_case_study.md)**

:   以高温超导（HTS）领域为案例，构建了专家级数据集（1,726篇论文 + 67道专家问题），系统评估6种LLM系统的科学文献理解能力，发现基于精选文献的RAG系统在事实完整性和证据支持方面显著优于通用闭源模型。

**[FlatQuant: Flatness Matters for LLM Quantization](flatquant_flatness_matters_for_llm_quantization.md)**

:   提出 FlatQuant，通过可学习仿射变换（Kronecker 分解）使权重和激活分布更平坦，在 W4A4 量化下首次在 LLaMA-3-70B 上实现 ≤1% 精度损失，同时 prefill 加速 2.3×、decoding 加速 1.7×。

**[FloE: On-the-Fly MoE Inference on Memory-constrained GPU](floe_on-the-fly_moe_inference_on_memory-constrained_gpu.md)**

:   提出 FloE，一个面向消费级 GPU 的 MoE 即时推理系统，通过专家内部混合压缩（上下文稀疏化 + 超低比特量化）和双预测器实现计算-传输流水线化，在 RTX 3090 上仅 11GB 显存即可部署 Mixtral-8×7B，相比 DeepSpeed-MII 加速 48.7 倍，性能仅下降 4.4%~7.6%。

**[From Language Models over Tokens to Language Models over Characters](from_language_models_over_tokens_to_language_models_over_characters.md)**

:   提出将 token 级语言模型精确转换为字符级语言模型的算法框架，通过定义 covering（最小前缀编码集合）并基于 beam search 近似求解，解决了 prompt boundary 等 token 化导致的用户端问题，同时改善了压缩率（bits/byte）。

**[From Low Rank Gradient Subspace Stabilization To Low-Rank Weights Observations T](from_low_rank_gradient_subspace_stabilization_to_low-rank_weights_observations_t.md)**

:   通过 Hessian 谱分析揭示 LLM 不同权重矩阵的低秩收敛差异，据此提出 WeLore——同时统一模型压缩与参数高效微调的非均匀低秩分解方法。

**[Function-Space Learning Rates](function-space_learning_rates.md)**

:   提出**逐层函数空间学习率**的高效蒙特卡洛估计方法，并基于此设计 **FLeRM**（Function-space Learning Rate Matching），在小模型上记录函数空间学习率，自动调整大模型的参数空间学习率，实现跨宽度、深度、初始化尺度和 LoRA rank 的超参数迁移。

**[Generalization Bounds via Meta-Learned Model Representations: PAC-Bayes and Sample Compression Hypernetworks](generalization_bounds_via_meta-learned_model_representations_pac-bayes_and_sampl.md)**

:   本文提出了一种基于 hypernetwork 的 meta-learning 框架来获取神经网络的紧泛化界，设计了三种 encoder-decoder 架构（PAC-Bayes 编码器、样本压缩编码器、混合编码器），其中混合方法基于一个新的 PAC-Bayes 样本压缩定理支持连续消息，通过信息瓶颈显式度量模型复杂度，在合成和真实数据集上获得了非空洞的泛化保证。

**[Generalized Interpolating Discrete Diffusion](generalized_interpolating_discrete_diffusion.md)**

:   提出广义插值离散扩散框架 GIDD，将掩码扩散 (MDM) 推广为支持任意时变混合分布的扩散族，通过结合掩码与均匀噪声赋予模型自纠错能力，在扩散语言建模中取得 compute-matched SOTA。

**[GuidedQuant: Large Language Model Quantization via Exploiting End Loss Guidance](guidedquant_large_language_model_quantization_via_exploiting_end_loss_guidance.md)**

:   提出 GuidedQuant，通过将端到端损失的梯度信息融入逐层量化目标（保留输出通道内的权重交互），作为即插即用模块显著提升现有 SOTA PTQ 方法在标量/向量/权重-激活量化上的性能；同时提出 LNQ 算法用于非均匀标量量化，实现 2-bit 下 Llama-2-7B perplexity 从 39.58 降至 8.83。

**[Gumiho: A Hybrid Architecture to Prioritize Early Tokens in Speculative Decoding](gumiho_a_hybrid_architecture_to_prioritize_early_tokens_in_speculative_decoding.md)**

:   提出 Gumiho，一种用于推测解码的混合 draft 模型架构：前两个 token 使用串行 Transformer 以确保精度，后续 token 使用并行 MLP heads 以提升效率，并通过 Full Tree Attention 机制进一步增加接受长度，在 Vicuna/LLaMA 上实现了最高 3.65x 加速。

**[Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](inference-time_decomposition_of_activations_itda_a_scalable_approach_to_interpre.md)**

:   提出 ITDA，一种基于匹配追踪（Matching Pursuit）的推理时激活分解方法，以仅 1% 的 SAE 训练成本实现可比的重构性能，可扩展到 405B 参数模型，并天然支持跨模型表示比较。

**[Instruction-Following Pruning for Large Language Models](instruction-following_pruning_for_large_language_models.md)**

:   提出 IFPruning：用一个小型稀疏预测器根据用户指令动态生成剪枝掩码，将 FFN 中间维度按需裁减，使 9B 模型仅激活 3B 参数即可在编程/数学上超越同规模 dense 模型 5-8 个百分点，且推理延迟与 3B dense 模型持平。

**[Joker: Joint Optimization Framework for Lightweight Kernel Machines](joker_joint_optimization_framework_for_lightweight_kernel_machines.md)**

:   提出 Joker 框架，通过对偶块坐标下降 + 信赖域 (DBCD-TR) 和随机傅里叶特征近似，以 ~2GB 内存实现多种大规模核模型（KRR / KLR / SVM 等）的统一高效训练，内存节省高达 90% 且性能不降。

**[KBQA-o1: Agentic Knowledge Base Question Answering with Monte Carlo Tree Search](kbqa-o1_agentic_knowledge_base_question_answering_with_monte_carlo_tree_search.md)**

:   提出 KBQA-o1，将 ReAct Agent 与蒙特卡洛树搜索（MCTS）结合，通过策略模型和奖励模型驱动的启发式搜索实现知识库问答，在低资源设置下以 Llama-3.1-8B 将 GrailQA F1 从 48.5%（GPT-3.5-turbo SOTA）提升至 78.5%。

**[Lacache Ladder-Shaped Kv Caching For Efficient Long-Context Modeling Of Large La](lacache_ladder-shaped_kv_caching_for_efficient_long-context_modeling_of_large_la.md)**

:   提出梯形（ladder-shaped）KV 缓存模式，在不同层保留不同 token 范围的 KV 状态，从而在固定缓存预算下扩展可捕获的上下文跨度，并通过迭代压缩机制支持无限长度的连续生成。

**[Lego Sketch A Scalable Memory-Augmented Neural Network For Sketching Data Stream](lego_sketch_a_scalable_memory-augmented_neural_network_for_sketching_data_stream.md)**

:   提出 Lego Sketch，一种基于模块化"记忆积木"的可扩展记忆增强神经网络（MANN），通过 normalized multi-hash embedding、可扩展内存和自引导加权损失，解决了现有 neural sketch 在跨数据域和不同空间预算下需要重新训练的可扩展性难题，并首次给出了 neural sketch 的误差上界。

**[Liger: Linearizing Large Language Models to Gated Recurrent Structures](liger_linearizing_large_language_models_to_gated_recurrent_structures.md)**

:   Liger 将预训练 Transformer LLM 无额外参数地转换为门控线性循环结构，利用 Key 投影矩阵复用构建门控机制，仅需 0.02% 预训练 token 即可恢复原模型 93% 的性能，同时获得线性时间推理和恒定显存开销。

**[MIB: A Mechanistic Interpretability Benchmark](mib_a_mechanistic_interpretability_benchmark.md)**

:   提出 MIB（Mechanistic Interpretability Benchmark），包含电路定位和因果变量定位两个赛道、四个任务、五个模型，通过标准化的反事实干预评估和新指标（CPR/CMD）系统比较 MI 方法，发现 attribution + mask optimization 方法在电路定位中最优，而 SAE 特征在因果变量定位中并不优于原始神经元。

**[MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning](mka_memory-keyed_attention_for_efficient_long-context_reasoning.md)**

:   提出 Memory-Keyed Attention (MKA)，将 KV 缓存组织为三级分层记忆（局部/会话/长期），通过可学习路由门动态分配注意力；加速版 FastMKA 在注意力计算前融合记忆源，实现训练吞吐量达 MLA 的 5 倍、解码延迟降至 MLA 的 54%，perplexity 仅损失约 1%。

**[Moragent Parameter Efficient Agent Tuning With Mixture-Of-Roles](moragent_parameter_efficient_agent_tuning_with_mixture-of-roles.md)**

:   提出 Mixture-of-Roles (MoR) 框架，将 Agent 能力分解为推理者、执行者、总结者三个角色，每个角色分配专门的 LoRA 组，以极少额外参数（0.16B–0.36B）实现接近甚至超越全参数微调的 Agent 性能。

**[Neutral Residues: Revisiting Adapters for Model Extension](neutral_residues_revisiting_adapters_for_model_extension.md)**

:   提出 **Neutral Residues**，通过在 adapter 中引入 ReLU 门控 + $\ell_1$ 稀疏局部损失 + 低方差初始化，使新增残差块在原始分布上输出近零值，在 Gemma-2B 上实现新语言学习与英语保持的最佳权衡。

**[Olica Efficient Structured Pruning Of Large Language Models Without Retraining](olica_efficient_structured_pruning_of_large_language_models_without_retraining.md)**

:   提出 Olica 框架，通过对 MHA 层矩阵乘积做正交分解（PCA/SVD）并对 FFN 层做线性校准（岭回归闭式解 + 低秩近似），实现 LLM 结构化剪枝无需重训练，仅需 256 样本、3GB 显存、7 分钟即可完成 LLaMA-7B 剪枝且性能优于需要重训练的方法。

**[Parameter-Efficient Fine-Tuning of State Space Models](parameter-efficient_fine-tuning_of_state_space_models.md)**

:   本文系统性地评估了现有 PEFT 方法在 SSM（如 Mamba）模型上的效果，发现 LoRA 虽在线性投影层表现最优但无法有效调优 SSM 模块，进而提出 Sparse Dimension Tuning（SDT）——一种专为 SSM 模块设计的 PEFT 方法，结合 LoRA 用于线性层，在多个基准上达到 SOTA 性能。

**[Predictive Data Selection: The Data That Predicts Is the Data That Teaches](predictive_data_selection_the_data_that_predicts_is_the_data_that_teaches.md)**

:   提出 PreSelect 方法，基于"能预测模型能力的数据就是能教会模型的数据"这一假设，利用多模型损失排名相关性量化文档预测强度，训练 fastText 分类器实现高效数据选择，在 1B 模型上用 30B tokens 超越随机选取 300B tokens 的性能，实现 10 倍计算节省。

**[Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs](putnam-axiom_a_functional_and_static_benchmark_for_measuring_higher_level_mathem.md)**

:   提出 Putnam-AXIOM —— 522 道大学级 Putnam 竞赛数学题 + 100 道程序化功能变体，揭示 LLM 数学推理中的记忆依赖，并引入 Teacher-Forced Accuracy (TFA) 作为超越最终答案的推理质量评估指标。

**[Rethinking the Stability-Plasticity Trade-off in Continual Learning from an Architectural Perspective](rethinking_the_stability-plasticity_trade-off_in_continual_learning_from_an_arch.md)**

:   揭示了持续学习中稳定性与可塑性之间在**架构层面**的固有冲突——宽浅网络稳定性好、深窄网络可塑性强——并提出 Dual-Arch 框架，用两个专用轻量架构分别负责稳定性和可塑性，通过知识蒸馏协同，实现参数量减少最高 87% 的同时提升 CL 性能。

**[SAFE: Finding Sparse and Flat Minima to Improve Pruning](safe_finding_sparse_and_flat_minima_to_improve_pruning.md)**

:   将剪枝问题建模为稀疏约束下的锐度感知优化问题，通过增广拉格朗日对偶法（ADMM）求解，同时实现稀疏性和平坦极小值，提升剪枝后网络的泛化性能和鲁棒性。

**[SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](sparselora_accelerating_llm_fine-tuning_with_contextual_sparsity.md)**

:   提出 SparseLoRA，通过**上下文稀疏性 (contextual sparsity)** 动态选择权重子集进行前向/梯度计算，首次将推理时的稀疏加速思路迁移到 LLM 微调阶段，实现最高 2.2× FLOPs 降低和 1.6× 实测加速，同时保持精度。

**[Towards Flexible Perception With Visual Memory](towards_flexible_perception_with_visual_memory.md)**

:   将深度视觉模型的知识表示从"刻在权重里"转变为"存在外部数据库里"，用预训练编码器 + kNN 检索构建灵活的 Visual Memory，实现数据的即插即拔（添加/删除/扩展）和可解释分类，ImageNet 上达到 88.5% top-1 准确率。
