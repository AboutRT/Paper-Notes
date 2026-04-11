<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📚 预训练/数据

**🤖 AAAI2026** · 共 **4** 篇

**[ELSPR: Evaluator LLM Training Data Self-Purification on Non-Transitive Preferences](elspr_evaluator_llm_training_data_self-purification_on_non-transitive_preference.md)**

:   ELSPR 将 LLM 评估器的成对偏好建模为锦标赛图，通过强连通分量 (SCC) 识别非传递偏好，提出归一化有向图结构熵指标，并基于图重构过滤有问题的训练数据——过滤后的评估器非传递性降低 13.8%、结构熵降低 0.088，且丢弃数据的人类一致性仅 34.4%（vs 保留数据 52.6%）。

**[No-Regret Strategy Solving in Imperfect-Information Games via Pre-Trained Embedding](no-regret_strategy_solving_in_imperfect-information_games_via_pre-trained_embedd.md)**

:   提出 Embedding CFR 算法，将不完美信息博弈中的信息集映射到连续低维嵌入空间（而非离散聚类），在相同空间开销下实现更快的可利用性收敛和更高质量的策略求解。

**[Scaling and Transferability of Annealing Strategies in Large Language Model Training](scaling_and_transferability_of_annealing_strategies_in_large_language_model_trai.md)**

:   提出模型无关的预测框架，分解训练损失为前向效应项（学习率积分S）、退火动量项（Adam-style动量积分M）和模型尺寸项N，证明退火策略可从小模型/小batch迁移到大模型/大batch，预测误差MAPE<2%。

**[Uncovering Pretraining Code in LLMs: A Syntax-Aware Attribution Approach](uncovering_pretraining_code_in_llms_a_syntax-aware_attribution_approach.md)**

:   提出SynPrune——首个语法感知的代码成员推断攻击方法，通过识别47种Python语法约定并在计算成员推断分数时剪除语法决定的token（仅保留反映作者特征的token），平均AUROC提升15.4%，可有效检测代码LLM的预训练数据归属。
