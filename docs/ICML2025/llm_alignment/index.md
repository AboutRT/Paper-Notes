<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚖️ 对齐 / RLHF

**🧪 ICML2025** · 共 **23** 篇

**[AssistanceZero: Scalably Solving Assistance Games](assistancezero_scalably_solving_assistance_games.md)**

:   提出 AssistanceZero，首次将 assistance game 扩展到复杂环境（Minecraft 建筑辅助，$10^{400}$ 种可能目标），通过扩展 AlphaZero 增加 reward 预测头和人类行为预测头，在 MCTS 下进行不确定性规划，显著优于 PPO 和模仿学习基线，人类实验证明能有效减少用户操作并展现挖地基、推断屋顶、从纠正中学习等涌现行为。

**[BOPO: Neural Combinatorial Optimization via Best-anchored and Objective-guided Preference Optimization](bopo_neural_combinatorial_optimization_via_best-anchored_and_objective-guided_pr.md)**

:   将 preference optimization（偏好优化）引入神经组合优化（NCO），提出 BOPO：通过 (1) best-anchored 偏好对构建（hybrid rollout + uniform filtering + best-anchored pairing）和 (2) objective-guided 自适应缩放损失函数（$\beta = g(y_l)/g(y_w)$），在 JSP/TSP/FJSP 三类经典组合优化问题上全面超越 SOTA，无需 reward model 或参考策略。

**[Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](bounded_rationality_for_llms_satisficing_alignment_at_inference-time.md)**

:   提出 SITAlign——基于有界理性的满意决策框架，在推理时最大化主要目标（如有用性）同时确保次要目标（如无害性）满足阈值约束，通过对偶理论求解，在 GPT-4 评估上相比多目标解码 SOTA 提升 22.3% 胜率。

**[Can RLHF be More Efficient with Imperfect Reward Models? A Policy Coverage Perspective](can_rlhf_be_more_efficient_with_imperfect_reward_models_a_policy_coverage_perspe.md)**

:   发现 RLHF 中 KL 正则化带来的结构性质——策略对最优策略的 coverage 被其次优性控制（$\text{Cov}^{\pi^*|\pi} \leq 1 + \kappa \cdot (J(\pi^*) - J(\pi))/\beta$），据此提出两条迁移学习原则：(1) 选高 policy value 的 transfer policy，(2) self-transfer 从在线数据蒸馏策略。设计 TPO 算法实现早期 $O(W\sqrt{T})$、后期 $O(\sqrt{T})$ 的 regret，可模块化集成 DPO/IPO/XPO，在 T5 summarization 实验上验证有效。

**[Challenges and Future Directions of Data-Centric AI Alignment](challenges_and_future_directions_of_data-centric_ai_alignment.md)**

:   Position paper，主张从算法中心转向数据中心的 AI 对齐视角，系统分析了人类反馈和 AI 反馈在数据层面的可靠性挑战（标注者不一致、时间漂移、上下文依赖、AI 反馈偏差等），并提出改进反馈收集/清洗/验证的未来研究方向。

**[ConfPO: Exploiting Policy Model Confidence for Critical Token Selection in Preference Optimization](confpo_exploiting_policy_model_confidence_for_critical_token_selection_in_prefer.md)**

:   提出 ConfPO，通过策略模型自身的置信度分数识别偏好关键 token 并仅对其优化，无需额外模型或计算开销，在 AlpacaEval 2 和 Arena-Hard 上一致优于均匀优化的 DAA 方法，同时缓解奖励黑客问题。

**[D-Fusion: Direct Preference Optimization for Aligning Diffusion Models with Visually Consistent Samples](d-fusion_direct_preference_optimization_for_aligning_diffusion_models_with_visua.md)**

:   本文提出 D-Fusion 方法，通过 mask 引导的自注意力融合（Self-Attention Fusion）构建视觉一致的偏好数据对并保留去噪轨迹，解决了 DPO 训练扩散模型时因视觉不一致导致效果受限的问题，在多种 RL 算法和 prompt 类型上显著提升了 prompt-image 对齐质量。

**[Diverging Preferences: When do Annotators Disagree and do Models Know?](diverging_preferences_when_do_annotators_disagree_and_do_models_know.md)**

:   本文系统分析了 RLHF 偏好数据集中标注者分歧的原因（建立了包含 10 个类别的分类法），发现超过 75% 的分歧源于个人偏好而非标注噪声，提出了分布式奖励模型（Mean-Var Reward Model）来有效区分分歧偏好与高一致偏好，并揭示了 LLM-as-Judge 评估方法在分歧情况下的系统性偏见。

**[DPO Meets PPO: Reinforced Token Optimization for RLHF](dpo_meets_ppo_reinforced_token_optimization_for_rlhf.md)**

:   本文提出 Reinforced Token Optimization (RTO)，将 RLHF 建模为 token 级别的 MDP（而非句子级 bandit），利用 DPO 隐式地提取 token-wise 奖励信号后用 PPO 进行策略优化，在 AlpacaEval 2 上比 PPO 高 7.5 分、在 Arena-Hard 上高 4.1 分，且仅需 1/8 数据量即可达到 PPO 级别性能。

**[Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](layer-wise_alignment_examining_safety_alignment_across_image_encoder_layers_in_v.md)**

:   本文发现了 VLM 中图像编码器的"早退出"漏洞（ICET）——跳过图像编码器的部分层会大幅增加有害输出概率，提出 Layer-wise PPO (L-PPO) 修改 Clipped-PPO 算法在不同层级做多模态 RLHF，在 ASR 上降低高达 48%、毒性分数降低 33.64%。

**[MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](mmedpo_aligning_medical_vision-language_models_with_clinical-aware_multimodal_pr.md)**

:   本文提出 MMedPO，一种临床感知的多模态医学偏好优化方法，通过注入可信幻觉和局部病灶加噪构建多模态偏好数据，利用多个医学 LLM 协作评估临床相关性作为加权信号融入 DPO 训练，在 Med-VQA 和报告生成任务上分别平均提升 14.2% 和 51.7%。

**[Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](model_swarms_collaborative_search_to_adapt_llm_experts_via_swarm_intelligence.md)**

:   借鉴粒子群优化（PSO）算法，将多个 LLM 专家视为"粒子"，在权重空间中协作搜索，通过个体最优/全局最优/全局最差三个信号引导专家迭代移动，仅需 200 个样本即可实现无需微调的模型适配，在 9 个任务上平均超越 12 个基线 13.3%。

**[MPO: An Efficient Post-Processing Framework for Mixing Diverse Preference Alignment](mpo_an_efficient_post-processing_framework_for_mixing_diverse_preference_alignme.md)**

:   提出 MPO（Mixing Preference Optimization），一个轻量级后处理框架，通过对数线性组合已有单目标策略来实现多偏好对齐，避免了多目标 RLHF 中昂贵的强化学习过程。

**[On the Robustness of Reward Models for Language Model Alignment](on_the_robustness_of_reward_models_for_language_model_alignment.md)**

:   提出 Batch-wise Sum-to-Zero Regularization (BSR)，通过约束每个 batch 内奖励分数之和为零来抑制隐状态范数的过度弥散，从根源上解决奖励模型的过优化问题，使 8B 规模 RM 在复杂偏好预测任务上超越 SOTA 5%+，并在 RLHF 下游训练中将生成长度降低 40% 同时提升 7% 胜率。

**[OR-Bench: An Over-Refusal Benchmark for Large Language Models](or-bench_an_over-refusal_benchmark_for_large_language_models.md)**

:   提出首个大规模 LLM 过度拒绝（over-refusal）基准 OR-Bench，包含 80K 安全但易被拒绝的 prompt，揭示安全性与过度拒绝之间存在 Spearman 相关系数高达 0.89 的强权衡关系。

**[Preference Optimization for Combinatorial Optimization Problems](preference_optimization_for_combinatorial_optimization_problems.md)**

:   将RLHF中的偏好优化思想引入组合优化（COP），把定量奖励信号转化为定性偏好信号，结合熵正则化目标和局部搜索微调，在TSP/CVRP/FFSP等标准基准上实现了1.5x-2.5x的收敛加速和更优解质量。

**[Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](raising_the_bar_investigating_the_values_of_large_language_models_via_generative.md)**

:   提出 GETA 框架，将心理测量学中的计算机自适应测试（CAT）与自动出题（AIG）结合，通过变分 IRT 和 LLM 驱动的题目生成器动态探测 LLM 的价值边界，解决静态基准因数据泄漏和难度饱和导致的"评估时效性效应"（evaluation chronoeffect）问题。

**[Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](reasoning_through_execution_unifying_process_and_outcome_rewards_for_code_genera.md)**

:   提出 ORPS（Outcome-Refining Process Supervision），通过将代码执行反馈与 LLM 自我批评结合，在树状搜索框架中统一过程奖励与结果奖励，无需训练 PRM 即可在代码生成中实现 26.9% 的正确率提升和 42.2% 的效率提升。

**[Right Now, Wrong Then: Non-Stationary Direct Preference Optimization under Preference Drift](right_now_wrong_then_non-stationary_direct_preference_optimization_under_prefere.md)**

:   提出 NS-DPO，通过 Dynamic Bradley-Terry 模型引入单一指数衰减参数 γ 对训练数据进行时序加权，使 DPO 在偏好随时间漂移的场景下仍能鲁棒对齐，同时在平稳场景下不损失性能。

**[Safety Alignment Can Be Not Superficial With Explicit Safety Signals](safety_alignment_can_be_not_superficial_with_explicit_safety_signals.md)**

:   通过在LLM中引入显式的安全二分类任务（[CLS] token），并设计策略性注意力机制和解码策略，在推理过程中动态评估安全性，以不到0.2x的额外开销将对抗攻击成功率从90%+降至接近0%。

**[Self-Consistency Preference Optimization](self-consistency_preference_optimization.md)**

:   将推理时的自一致性(self-consistency)概念引入训练阶段，通过投票机制构建偏好对并使用加权DPO损失进行迭代训练，在无需金标签的情况下大幅提升LLM的数学和逻辑推理能力。

**[Smoothed Preference Optimization via ReNoise Inversion for Aligning Diffusion Models with Varied Human Preferences](smoothed_preference_optimization_via_renoise_inversion_for_aligning_diffusion_mo.md)**

:   提出 SmPO-Diffusion，通过平滑偏好建模替代二元偏好标签 + ReNoise Inversion 替代前向加噪估计，在大幅降低训练成本（比 DPO 快 6.5 倍，比 KTO 快 26 倍）的同时实现了 T2I 扩散模型偏好对齐的 SOTA 性能。

**[TGDPO: Harnessing Token-Level Reward Guidance for Enhancing Direct Preference Optimization](tgdpo_harnessing_token-level_reward_guidance_for_enhancing_direct_preference_opt.md)**

:   将序列级PPO分解为一系列token级近端策略优化问题，并引入token级奖励引导函数 $f(\hat{r}(s_t, a_t))$ 来替代DPO中的固定常数 $\beta$，使不同token根据各自奖励值呈现不同程度的偏离参考策略，在MT-Bench/AlpacaEval 2/Arena-Hard上分别提升最多7.5/6.2/4.3个胜率点。
