<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📈 时间序列

**🧪 ICML2025** · 共 **13** 篇

**[Are LLMs Prescient? A Continuous Evaluation using Daily News as the Oracle](are_llms_prescient_a_continuous_evaluation_using_daily_news_as_the_oracle.md)**

:   提出 Daily Oracle 基准——从每日新闻自动生成 QA 对来持续评估 LLM 的时间泛化和预测能力，揭示 LLM 性能随预训练数据过时而持续退化（True/False 题平均下降 21.55%），且 RAG 也无法完全挽救。

**[Breaking Silos: Adaptive Model Fusion Unlocks Better Time Series Forecasting](breaking_silos_adaptive_model_fusion_unlocks_better_time_series_forecasting.md)**

:   提出 TimeFuse——一个样本级自适应模型融合框架，通过元特征描述输入时间序列特征并训练可学习融合器预测最优模型组合权重，在多个预测基准上对 SOTA 模型实现近乎普遍的改进（95.1% 样本优于最佳单模型）。

**[Causal Discovery from Conditionally Stationary Time Series](causal_discovery_from_conditionally_stationary_time_series.md)**

:   提出 SDCI（State-Dependent Causal Inference）——处理条件平稳时间序列的因果发现方法，通过离散潜状态变量建模非平稳行为，实现状态依赖的因果结构恢复，在粒子交互、基因调控网络和 NBA 球员运动预测中验证有效性。

**[Causality-Aware Contrastive Learning for Robust Multivariate Time-Series Anomaly Detection](causality-aware_contrastive_learning_for_robust_multivariate_time-series_anomaly.md)**

:   提出 CAROTS——将因果关系融入对比学习的多变量时间序列异常检测框架，用因果保持增强作为正样本（正常变化），因果破坏增强作为负样本（模拟异常），训练编码器基于因果结构区分正常与异常。

**[Context is Key: A Benchmark for Forecasting with Essential Textual Information](context_is_key_a_benchmark_for_forecasting_with_essential_textual_information.md)**

:   提出 CiK 基准——将数值时间序列与精心设计的文本上下文配对，要求模型必须理解文本才能成功预测，评估统计模型、时序基础模型和 LLM 预测器，发现简单的 LLM 提示方法在需要上下文信息的任务上表现最优。

**[Customizing the Inductive Biases of Softmax Attention using Structured Matrices](customizing_the_inductive_biases_of_softmax_attention_using_structured_matrices.md)**

:   提出用高效结构化矩阵（BTT 和 MLR）替换 softmax attention 中的低秩打分函数，既解决了标准 attention 的低秩瓶颈问题，又通过 MLR 引入了距离依赖的计算偏置，在上下文回归、语言建模和长程时间序列预测上均取得改进。

**[Event-Aware Sentiment Factors from LLM-Augmented Financial Tweets: A Transparent Framework for Interpretable Quant Trading](event-aware_sentiment_factors_from_llm-augmented_financial_tweets_a_transparent_.md)**

:   利用大语言模型对金融推文进行多标签事件分类标注，将非结构化社交媒体文本转化为结构化、可解释的事件驱动量化因子，发现特定事件类别（如谣言/投机）具有显著的负Alpha信号（Sharpe ratio低至-0.38）。

**[IMTS is Worth Time × Channel Patches: Visual Masked Autoencoders for Irregular Multivariate Time Series Prediction](imts_is_worth_time_times_channel_patches_visual_masked_autoencoders_for_irregula.md)**

:   提出 VIMTS 框架，将不规则多变量时间序列（IMTS）转化为 time × channel 的类图像 patch 结构，借助在大规模 RGB 图像上预训练的视觉 MAE 的稀疏多通道建模能力，结合 GCN 跨通道补全与粗到细预测策略，在 IMTS 预测任务上实现 SOTA 性能和强 few-shot 能力。

**[Learning Soft Sparse Shapes for Efficient Time-Series Classification](learning_soft_sparse_shapes_for_efficient_time-series_classification.md)**

:   提出 SoftShape 模型，用基于贡献分数的软稀疏化替代传统硬筛选 shapelet 的方式，结合 MoE 驱动的 intra-shape 和 shared expert 的 inter-shape 双模式时序模式学习，在 128 个 UCR 数据集上取得 SOTA 分类精度。

**[Lightgts A Lightweight General Time Series Forecasting Model](lightgts_a_lightweight_general_time_series_forecasting_model.md)**

:   提出 LightGTS，利用时间序列固有的尺度不变周期性归纳偏置，通过 Periodical Tokenization 和 Periodical Parallel Decoding 两个核心技术，仅用不到 500 万参数就在 9 个基准数据集上的 zero-shot 和 full-shot 设定中取得了 SOTA 性能，比现有时序基础模型小 10-100 倍。

**[Risk and Cross Validation in Ridge Regression with Correlated Samples](risk_and_cross_validation_in_ridge_regression_with_correlated_samples.md)**

:   利用随机矩阵理论和自由概率技术，为训练样本具有任意相关性的高维岭回归推导了精确的风险渐近公式，提出了修正的广义交叉验证估计器 CorrGCV，在样本相关条件下准确预测样本外风险。

**[TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation](timing_temporality-aware_integrated_gradients_for_time_series_explanation.md)**

:   提出 TIMING 方法，通过引入时序感知的分段随机掩码基线改进 Integrated Gradients，同时设计新评估指标 CPD/CPP 解决现有时序 XAI 评估中正负归因相互抵消的问题，在多个真实数据集上全面超越现有基线。

**[Winner-takes-all for Multivariate Probabilistic Time Series Forecasting](winner-takes-all_for_multivariate_probabilistic_time_series_forecasting.md)**

:   提出 TimeMCL，将 Multiple Choice Learning 的 Winner-Takes-All (WTA) 损失引入多变量概率时序预测，通过多头网络单次前向传播即可生成多样且具代表性的未来轨迹，兼顾预测质量与计算效率。
