<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**🧪 ICML2025** · 共 **33** 篇

**[B-score: Detecting biases in large language models using response history](b-score_detecting_biases_in_large_language_models_using_response_history.md)**

:   提出B-score指标，通过比较LLM在单轮(single-turn)与多轮(multi-turn)对话中的回答概率差异来检测偏见，发现LLM在多轮对话中能"自我去偏"，并利用B-score提升答案验证准确率。

**[Bayesian Neural Scaling Law Extrapolation with Prior-Data Fitted Networks](bayesian_neural_scaling_law_extrapolation_with_prior-data_fitted_networks.md)**

:   首个面向神经缩放定律(Neural Scaling Law)的贝叶斯外推方法，通过设计专门的先验分布（覆盖Down/Down-Down/Down-Up-Down三种功能族），利用PFN (Prior-data Fitted Networks) meta-learn外推能力，在点估计精度和不确定性质量上均优于现有方法。

**[Binary Hypothesis Testing for Softmax Models and Leverage Score Models](binary_hypothesis_testing_for_softmax_models_and_leverage_score_models.md)**

:   从理论角度研究Softmax模型和Leverage Score模型的二元假设检验问题，建立了在能量约束下区分两个参数化模型所需的查询次数的紧界，与理解LLM不同能力域的区分性问题相关。

**[Build Agent Advocates, Not Platform Agents](build_agent_advocates_not_platform_agents.md)**

:   Position paper，指出LMA（语言模型代理）若被平台公司控制将成为加剧监控、锁定和注意力操控的"platform agents"，提出应发展用户控制的"agent advocates"来保护个人自主权，并给出三大干预措施：开放模型/算力、互操作性标准、市场监管。

**[Communicating Activations Between Language Model Agents](communicating_activations_between_language_model_agents.md)**

:   提出让 LLM 智能体通过中间层激活（而非自然语言）进行通信的方法——在模型 B 的前向传播中间层注入模型 A 的激活向量，无需额外参数和数据，在多项推理基准上比自然语言通信提升 27%，计算量仅为 1/4。

**[Correlated Errors in Large Language Models](correlated_errors_in_large_language_models.md)**

:   本文通过对超过350个LLM的大规模实证分析，发现不同LLM之间存在高度相关的错误模式——在两个模型都出错时约60%的情况下会选择同一个错误答案，且越准确的模型相关性越高；进而研究了这种相关性对LLM-as-Judge评估和招聘市场的下游影响。

**[Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](disentangling_and_integrating_relational_and_sensory_information_in_transformer_.md)**

:   本文提出了 Dual Attention Transformer（DAT），通过在标准注意力机制中引入"关系注意力"头，将感知信息和关系信息解耦后并行处理再整合，在关系推理基准、数学问题求解、图像识别和语言建模等任务上均展现出显著的数据效率和参数效率提升。

**[Does Data Scaling Lead to Visual Compositional Generalization?](does_data_scaling_lead_to_visual_compositional_generalization.md)**

:   本文通过受控实验系统研究了数据规模与数据多样性对视觉模型组合泛化能力的影响，发现组合泛化的关键驱动力是数据多样性而非数据量，并证明当表示呈线性分解结构时仅需每个概念值2个组合样本即可完美泛化。

**[Dynamical Phases of Short-Term Memory Mechanisms in RNNs](dynamical_phases_of_short-term_memory_mechanisms_in_rnns.md)**

:   本文发现了支持RNN短时记忆的两种不同潜在动力学机制——慢点流形（slow-point manifolds）和极限环（limit cycles），通过解析 toy 模型推导出各自最大可学习率的幂律缩放定律（SP: beta 约4-5 vs LC: beta 约2-3），并通过训练约80,000个RNN进行了大规模实证验证。

**[Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](emergent_symbolic_mechanisms_support_abstract_reasoning_in_large_language_models.md)**

:   本文通过因果分析、表征分析和注意力分析等方法，在13个开源LLM中识别出支持抽象推理的三阶段涌现符号架构——符号抽象头将输入token转化为抽象变量、符号归纳头在抽象变量层面进行序列归纳、检索头根据预测的抽象变量检索对应值来完成下一token预测。

**[G-Sim: Generative Simulations with Large Language Models and Gradient-Free Calibration](g-sim_generative_simulations_with_large_language_models_and_gradient-free_calibr.md)**

:   提出 G-Sim 混合框架，利用 LLM 自动设计仿真器的因果结构（子模块与连接关系），再通过无梯度优化（GFO）或仿真推断（SBI）对数值参数进行经验校准，在迭代循环中不断改进，生成可靠、可干预的通用仿真器。

**[How to Synthesize Text Data without Model Collapse?](how_to_synthesize_text_data_without_model_collapse.md)**

:   提出 Token-level Editing (ToEdit)，通过对人类数据进行 token 级别的局部重采样（而非完全生成合成数据），在理论上证明测试误差存在有限上界，从而避免 model collapse，并在预训练、持续预训练和微调三个阶段验证了有效性。

**[Interchangeable Token Embeddings for Extendable Vocabulary and Alpha-Equivalence](interchangeable_token_embeddings_for_extendable_vocabulary_and_alpha-equivalence.md)**

:   提出双部分 token 嵌入策略（共享可学习部分 + 随机区分部分），使语言模型能在训练后泛化到更大词表，并对 alpha-等价变换具有天然鲁棒性。

**[Investigating Non-Transitivity in LLM-as-a-Judge](investigating_non-transitivity_in_llm-as-a-judge.md)**

:   揭示了 LLM-as-a-Judge 框架中评判偏好的**非传递性**问题（A>B, B>C 不能推出 A>C），证明固定基线模型的排名方式不可靠，提出基于循环赛 + Bradley-Terry 模型的排名方法及高效的 Swim 锦标赛策略。

**[Language Model Developers Should Report Train-Test Overlap](language_model_developers_should_report_train-test_overlap.md)**

:   本文系统性地调研了30个语言模型开发者在训练-测试重叠（train-test overlap）方面的报告实践，发现仅9个模型提供了足够的重叠信息，并呼吁所有开发者在发布评估结果时必须同时报告训练-测试重叠统计数据或公开训练数据。

**[Large Language Models are Demonstration Pre-Selectors for Themselves](large_language_models_are_demonstration_pre-selectors_for_themselves.md)**

:   提出 FEEDER（FEw yet Essential Demonstration prE-selectoR），一个基于"充分性"和"必要性"度量的示例预选框架，利用 LLM 自身能力从训练数据中识别代表性子集，在 ICL 和微调两个场景下均可减少 20%+ 数据量同时保持甚至提升性能。

**[LASER: Attention with Exponential Transformation](laser_attention_with_exponential_transformation.md)**

:   通过分析注意力机制中 softmax 的梯度反向传播瓶颈，提出 LASER 注意力——在指数变换的 Value 空间中做注意力计算（即对 exp(V) 做 attention 再取 log），从而获得更大的 Jacobian 信号，改善参数学习效率。

**[Learning Distribution-Wise Control in Representation Space for Language Models](learning_distribution-wise_control_in_representation_space_for_language_models.md)**

:   将表示微调（Representation Fine-tuning）中的确定性节点替换为随机节点，通过重参数化技巧学习潜在分布而非单点变换，在常识推理和数学推理任务上取得了一致性能提升，尤其在早期层的干预效果最为显著。

**[Leveraging Online Olympiad-Level Math Problems for LLMs Training and Contamination-Resistant Evaluation](leveraging_online_olympiad-level_math_problems_for_llms_training_and_contaminati.md)**

:   利用 Art of Problem Solving (AoPS) 论坛的社区内容，构建了 652K 奥赛级数学 QA 对的训练集 AoPS-Instruct 和带时间戳的抗污染评估集 LiveAoPSBench，揭示了 LLM 在旧数据上的高表现可能源于预训练数据泄露而非真正推理能力。

**[Metadata Conditioning Accelerates Language Model Pre-training](metadata_conditioning_accelerates_language_model_pre-training.md)**

:   提出 MeCo（Metadata Conditioning then Cooldown），在预训练时将文档的 URL 等元数据前置拼接到文本中，帮助模型区分异质数据源，最后 10% 训练用标准数据做 cooldown，使 1.6B 模型用 **33% 更少的数据**即可达到同等下游性能，同时解锁了通过条件推理引导生成的能力。

**[On Expressive Power of Looped Transformers: Theoretical Analysis and Enhancement via Timestep Encoding](on_expressive_power_of_looped_transformers_theoretical_analysis_and_enhancement_.md)**

:   本文首次建立了 Looped Transformer 关于循环次数和目标函数连续性模的逼近速率理论，揭示了循环架构特有的逼近误差来源（上下文连续性与 token 连续性），并提出 Timestep-Modulated Looped Transformer (TMLT) 通过时间步编码消除该限制，在推理、上下文学习和语言建模任务上取得一致提升。

**[PhantomWiki: On-Demand Datasets for Reasoning and Retrieval Evaluation](phantomwiki_on-demand_datasets_for_reasoning_and_retrieval_evaluation.md)**

:   提出 PhantomWiki——一个按需生成虚构世界语料库和 QA 对的评测框架，通过上下文无关文法（CFG）控制推理难度、调节宇宙规模控制检索难度，实现对 LLM 推理与检索能力的解耦评估，同时天然抵抗数据泄漏。

**[POQD: Performance-Oriented Query Decomposer for Multi-Vector Retrieval](poqd_performance-oriented_query_decomposer_for_multi-vector_retrieval.md)**

:   提出 POQD，一个面向性能的查询分解框架，利用 LLM-based Prompt Optimizer 迭代优化查询分解 prompt，并通过交替训练算法联合优化 prompt 和下游 RAG 模型参数，在检索和端到端 QA 任务上大幅超越现有方法。

**[Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](product_of_experts_with_llms_boosting_performance_on_arc_is_a_matter_of_perspect.md)**

:   将 LLM 同时用作候选解生成器和评分器，通过基于 DFS 的搜索算法生成高概率候选解，再利用多视角增强下的 Product of Experts (PoE) 打分选出最优答案，在 ARC-AGI 公开评估集上以 71.6% 的准确率达到开源 SOTA，超越人类平均水平（60.2%），且单任务推理成本仅约 $0.02。

**[QuEst: Enhancing Estimates of Quantile-Based Distributional Measures Using Model Predictions](quest_enhancing_estimates_of_quantile-based_distributional_measures_using_model_.md)**

:   提出 QuEst 框架，将少量高质量观测数据与大量模型预测（imputed）数据相结合，对分位数相关的分布度量（QBDM）给出更精确的点估计和严格的置信区间，覆盖 CVaR、Interval-VaR 等经典指标。

**[Random Registers for Cross-Domain Few-Shot Learning](random_registers_for_cross-domain_few-shot_learning.md)**

:   在跨域小样本学习（CDFSL）中发现可学习 prompt 会损害目标域泛化性能，而用随机噪声替代（即随机寄存器）反而能持续提升性能，并基于此提出 REAP 方法，通过在图像语义区域添加随机寄存器来增强注意力扰动，实现高效的域无关特征学习。

**[ResearchTown: Simulator of Human Research Community](researchtown_simulator_of_human_research_community.md)**

:   提出 ResearchTown，一个基于 agent-data 图和 TextGNN（文本空间消息传递）的多智能体框架，将人类科研社区建模为异构图，统一模拟论文阅读、论文写作和审稿三大核心研究活动，并通过节点掩码预测任务 (ResearchBench) 进行可扩展、客观的仿真质量评估。

**[Supernova Event Dataset: Interpreting Large Language Models' Personality through Critical Event Analysis](supernova_event_dataset_interpreting_large_language_models_personality_through_c.md)**

:   提出 Supernova Event Dataset（包含传记、历史事件、新闻、科学发现的 Wikipedia 文章），通过让 LLM 从长文本中抽取并排序关键事件，再由另一个 LLM 作为评判者推断目标模型的"人格特质"，揭示不同 LLM 在主观决策中的一致性行为模式差异。

**[Taming Knowledge Conflicts in Language Models](taming_knowledge_conflicts_in_language_models.md)**

:   揭示了语言模型注意力头中"上下文信息与参数记忆的叠加"（CP Superposition）现象，提出 JuICE（Just Run Twice）方法，通过双次推理的注意力干预策略，在不微调的前提下灵活引导模型偏向参数知识或上下文知识，在 11 个数据集 × 6 种模型架构上达到 SOTA。

**[The Lock-in Hypothesis: Stagnation by Algorithm](the_lock-in_hypothesis_stagnation_by_algorithm.md)**

:   本文提出并形式化了"锁定假说"（Lock-in Hypothesis）：LLM 训练与部署过程中形成的人类-AI 反馈循环会固化用户的现有信念，导致群体观点多样性不可逆地丧失，甚至锁定在错误信念上。

**[The Sharpness Disparity Principle in Transformers for Accelerating Language Model Pre-Training](the_sharpness_disparity_principle_in_transformers_for_accelerating_language_mode.md)**

:   揭示了 Transformer 中不同类型模块（Emb、QK、FFN、VO、Norm）存在显著且持久的**锐度差异**（sharpness disparity），并据此提出 Blockwise LR 策略，为低锐度模块分配更大学习率，在不损失稳定性的前提下实现 LLM 预训练近 **2× 加速**。

**[Theoretical Limitations of Ensembles in the Age of Overparameterization](theoretical_limitations_of_ensembles_in_the_age_of_overparameterization.md)**

:   在过参数化条件下，无限集成模型与单个无穷宽模型逐点等价，集成方差不再反映传统贝叶斯不确定性而是衡量增加模型容量的预期效果，从理论上解释了深度集成相比大模型无本质泛化优势的经验观察。

**[Tokenized Bandit for LLM Decoding and Alignment](tokenized_bandit_for_llm_decoding_and_alignment.md)**

:   将 LLM 解码与对齐问题形式化为 **tokenized bandit**（token化老虎机）问题，提出 DDMC（Diminishing Distance with More Commons）假设，证明在该假设下贪心解码近似最优，并设计了具有次线性遗憾的在线学习算法 EOFUL 和 GreedyETC。
