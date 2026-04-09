<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💡 LLM 推理

**🧪 ICML2025** · 共 **7** 篇

**[A Reasoning-Based Approach to Cryptic Crossword Clue Solving](a_reasoning-based_approach_to_cryptic_crossword_clue_solving.md)**

:   提出三阶段LLM推理pipeline（答案候选生成→wordplay解释→Python形式化验证），使用开源9B模型在Cryptonite密码填字谜数据集上实现新SOTA，关键创新在于将wordplay推理形式化为可执行Python代码并通过带hints的verifier迭代修正。

**[Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](improving_rationality_in_the_reasoning_process_of_language_models_through_self-p.md)**

:   本文提出 Critic-Discernment Game（CDG），通过自博弈语言游戏让 LLM 与"有帮助的批评者"和"误导性批评者"互动，用 ReST 强化学习联合优化三个角色，无需人类或更强模型的监督即可显著提升 LLM 对自身推理过程的理性理解，在数学推理、逐步错误检测、自我纠错和长链推理四个任务上均取得一致提升。

**[One Missing Piece for Open-Source Reasoning Models: A Dataset to Mitigate Cold-Starting Short CoT LLMs in RL](one_missing_piece_for_open-source_reasoning_models_a_dataset_to_mitigate_cold-st.md)**

:   提出 Long CoT Collection——一个由短CoT LLM（如GPT-4o）标注的100K长链推理数据集，通过从o1提取推理流程（reasoning flow）作为间接引导，使短CoT模型也能生成高质量长推理链，从而有效缓解开源推理模型在强化学习阶段的冷启动问题，初始化后的模型在RLVR中获得2-3倍的性能提升。

**[PCoT: Persuasion-Augmented Chain of Thought for Detecting Fake News and Social Media Disinformation](pcot_persuasion-augmented_chain_of_thought_for_detecting_fake_news_and_social_me.md)**

:   提出 PCoT（Persuasion-Augmented Chain of Thought），通过两阶段推理——先让 LLM 识别文本中的说服策略，再将说服分析结果注入虚假信息检测推理——在零样本设置下，跨 5 个 LLM 和 5 个数据集平均提升 F1 约 15%。

**[Rethinking External Slow-Thinking: From Snowball Errors to Probability of Correct Reasoning](rethinking_external_slow-thinking_from_snowball_errors_to_probability_of_correct.md)**

:   本文从信息论视角系统分析了 LLM 推理中的"雪球误差"现象，建立了雪球误差与推理正确概率之间的理论联系，证明了外部慢思考方法（如 BoN、MCTS）本质上是通过扩展搜索宽度来缓解误差累积，并在理论和实验上证明了方法效果主要取决于总推理代价和奖励函数可靠性，而非搜索框架本身。

**[Towards Better Chain-of-Thought: A Reflection on Effectiveness and Faithfulness](towards_better_chain-of-thought_a_reflection_on_effectiveness_and_faithfulness.md)**

:   本文从有效性（effectiveness）和忠实性（faithfulness）两个维度系统分析了 CoT 的性能影响因素，发现问题难度、信息增益和信息流是影响 CoT 有效性的关键因子，而不忠实 CoT 的根因在于模型在预测答案时绕过 CoT 直接从问题中召回了正确信息，并据此提出 QUIRE 方法同时提升 CoT 的有效性和忠实性。

**[Training Software Engineering Agents and Verifiers with SWE-Gym](training_software_engineering_agents_and_verifiers_with_swe-gym.md)**

:   本文提出 SWE-Gym——首个用于训练软件工程 Agent 的环境，包含来自 11 个开源 Python 仓库的 2438 个真实任务实例，通过在 SWE-Gym 上进行拒绝采样微调训练 SWE Agent 和 Verifier，在 SWE-Bench Verified/Lite 上最终达到 32.0%/26.0% 的解决率，创造了开源权重 SWE Agent 的新 SOTA。
