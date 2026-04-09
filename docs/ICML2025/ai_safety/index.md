<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI 安全

**🧪 ICML2025** · 共 **35** 篇

**[A Certified Unlearning Approach without Access to Source Data](a_certified_unlearning_approach_without_access_to_source_data.md)**

:   提出首个无需访问原始训练数据的认证遗忘框架，利用代理数据集（surrogate dataset）近似原始数据统计特性，通过基于源分布与代理分布之间统计距离的噪声缩放机制，实现可证明的数据删除保证。

**[Accelerating Spectral Clustering under Fairness Constraints](accelerating_spectral_clustering_under_fairness_constraints.md)**

:   将公平谱聚类（Fair SC）问题转化为凸差分（DC）优化框架，通过变量增广策略和 ADMM 类型算法，避免了昂贵的特征分解计算，在大规模问题上实现显著加速。

**[Adversarial Inception Backdoor Attacks against Reinforcement Learning](adversarial_inception_backdoor_attacks_against_reinforcement_learning.md)**

:   提出"inception"后门攻击框架——通过在 RL 智能体的训练轨迹中插入触发器并将高回报动作替换为目标对抗动作，首次在严格奖励约束下实现 100% 攻击成功率，同时保持智能体在正常任务上的表现。

**[Align-then-Unlearn: Embedding Alignment for LLM Unlearning](align-then-unlearn_embedding_alignment_for_llm_unlearning.md)**

:   提出 Align-then-Unlearn 框架，通过在语义嵌入空间（而非 token 级别）执行遗忘操作，先训练嵌入预测模块对齐未来语义表示，再微调 LLM 使预测嵌入远离目标概念嵌入，实现对 prompt 改写鲁棒的概念级知识遗忘。

**[An Efficient Private GPT Never Autoregressively Decodes](an_efficient_private_gpt_never_autoregressively_decodes.md)**

:   提出 POST（Public decOding and Secure verificaTion）方法，利用公开 GPT 模型生成草稿 token 并通过私有模型安全验证，借助安全解码对输入长度不敏感的特性，实现 2.1×~6.0× 的隐私推理加速，同时保持与标准安全解码相同的隐私和生成质量。

**[Can One Safety Loop Guard Them All? Agentic Guard Rails for Federated Computing](can_one_safety_loop_guard_them_all_agentic_guard_rails_for_federated_computing.md)**

:   提出 Guardian-FC——一个双层框架，通过 Agentic-AI 控制平面和后端无关的领域特定语言（DSL），统一管理不同隐私机制（FHE/MPC/DP）的安全护栏，实现联邦计算中的跨后端一致性安全执行和可审计性。

**[Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](cape_context-aware_prompt_perturbation_mechanism_with_differential_privacy.md)**

:   提出 Cape——一种上下文感知的 prompt 扰动机制，通过混合效用函数（结合 token 嵌入距离和上下文 logit）以及分桶指数采样机制，在 local DP 保证下实现比现有方法更优的隐私-效用权衡。

**[Cascade: Token-Sharded Private LLM Inference](cascade_token-sharded_private_llm_inference.md)**

:   提出 Cascade——一种基于 token 维度分片的多方推理协议，通过将隐藏状态按 token 维度分发给不同计算节点，避免密码学原语的高昂开销，在保持抵抗 vocab-matching 攻击能力的同时实现比 SMPC 方案快 100× 的推理速度。

**[Clients Collaborate: Flexible Differentially Private Federated Learning with Guaranteed Improvement of Utility-Privacy Trade-off](clients_collaborate_flexible_differentially_private_federated_learning_with_guar.md)**

:   提出 FedCEO 框架，通过在服务器端对堆叠的客户端模型参数进行张量低秩近端优化，利用不同客户端间的语义互补性恢复 DP 噪声破坏的语义信息，将效用-隐私权衡界改进了 $O(\sqrt{d})$ 量级。

**[Collaborative Mean Estimation Among Heterogeneous Strategic Agents Individual Ra](collaborative_mean_estimation_among_heterogeneous_strategic_agents_individual_ra.md)**

:   针对异构成本的多智能体协作均值估计问题，设计了同时满足个体理性(IR)、激励相容(IC)和公平性的无货币机制，在最坏情况下实现 $\mathcal{O}(\sqrt{m})$ 近似比，并证明了三条不可能性结果。

**[Connecting Thompson Sampling and UCB: Towards More Efficient Trade-offs Between Privacy and Regret](connecting_thompson_sampling_and_ucb_towards_more_efficient_best-fixed_action_.md)**

:   本文提出 DP-TS-UCB 算法，通过限制每轮高斯采样次数并在采样预算耗尽后切换为 UCB 式探索，实现了隐私与遗憾的参数化权衡，将 GDP 保证从 $O(\sqrt{T})$ 大幅改善至 $\tilde{O}(T^{0.25(1-\alpha)})$，同时保持近最优的遗憾界。

**[Connecting Thompson Sampling and UCB: Towards More Efficient Trade-offs Between Privacy and Regret](connecting_thompson_sampling_and_ucb_towards_more_efficient_trade-offs_between_p.md)**

:   提出 DP-TS-UCB 算法，通过限制高斯采样次数并复用最大模型值，在 Thompson Sampling 和 UCB 之间建立连接，实现 $\tilde{O}(T^{0.25(1-\alpha)})$-GDP 隐私保证和 $O(K\ln^{\alpha+1}(T)/\Delta)$ 遗憾上界的参数化权衡。

**[Convex Markov Games: A New Frontier for Multi-Agent Reinforcement Learning](convex_markov_games_a_new_frontier_for_multi-agent_reinforcement_learning.md)**

:   提出**凸 Markov 博弈 (cMG)** 框架，将单 agent 凸 MDP 推广到多 agent 设定，允许对占用度量 (occupancy measure) 施加一般凸偏好（如熵、KL 散度、公平性惩罚、安全约束），证明纯策略 Nash 均衡存在，并设计可微的投影梯度损失 (PGL) 算法逼近均衡。

**[CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](crow_eliminating_backdoors_from_large_language_models_via_internal_consistency_r.md)**

:   提出 CROW（Internal Consistency Regularization），通过对抗扰动 + 层间隐藏状态一致性正则化来消除 LLM 中的后门，仅需 100 条干净样本、单卡 4 分钟微调即可将攻击成功率降至 5% 以下，且不需要干净参考模型或触发器先验知识。

**[Disparate Conditional Prediction in Multiclass Classifiers](disparate_conditional_prediction_in_multiclass_classifiers.md)**

:   提出 Disparate Conditional Prediction (DCP) 度量从二分类到多类分类的扩展，通过局部优化和线性规划方法为多类分类器的公平性偏离程度提供上下界估计，支持在混淆矩阵已知或仅有人口级别统计信息两种场景下进行公平性审计。

**[Distributed and Decentralised Training: Technical Governance Challenges in a Shifting AI Landscape](distributed_and_decentralised_training_technical_governance_challenges_in_a_shif.md)**

:   本文系统区分了分布式训练（multi-data centre）与去中心化训练（community-driven）两种新兴范式，分析了低通信训练算法（如 DiLoCo）如何使这两种范式成为可能，并深入讨论了它们对AI技术治理（计算结构化、能力扩散、可关停性）带来的挑战与机遇。

**[Do Not Mimic My Voice: Speaker Identity Unlearning for Zero-Shot Text-to-Speech](do_not_mimic_my_voice_speaker_identity_unlearning_for_zero-shot_text-to-speech.md)**

:   首次提出零样本TTS中的说话人身份遗忘任务，设计了Teacher-Guided Unlearning (TGU) 框架，通过引入随机性使模型"忘记"目标说话人的声纹特征，同时保持对其他说话人的高质量语音合成能力，并提出 spk-ZRF 指标量化遗忘效果。

**[EgoPrivacy: What Your First-Person Camera Says About You?](egoprivacy_what_your_first-person_camera_says_about_you.md)**

:   提出 EgoPrivacy——首个大规模第一人称视频隐私基准，定义三类隐私（人口统计/个体/情境）七大任务，并设计检索增强攻击 (RAA) 将 ego-to-exo 检索与分类联合，证明基础模型零样本即可以 70–80% 准确率推断佩戴者性别、种族等敏感属性。

**[Empirical Privacy Variance](empirical_privacy_variance.md)**

:   揭示了在相同 $(ε,δ)$-DP 保证下，DP-SGD 不同超参数配置训练出的语言模型在经验隐私（记忆化程度）上存在显著差异，并提出了兼顾经验隐私的超参数选择启发式方法。

**[Faster Rates for Private Adversarial Bandits](faster_rates_for_private_adversarial_bandits.md)**

:   为差分隐私对抗性 bandits 问题提出简洁高效的非私有→私有转换框架，通过批量化损失+Laplace 噪声实现 O(√(KT/ε)) 的后悔界，首次证明中心 DP 和本地 DP 在该问题上存在分离，并给出首个私有 bandits with expert advice 算法。

**[Ferret: Federated Full-Parameter Tuning at Scale for Large Language Models](ferret_federated_full-parameter_tuning_at_scale_for_large_language_models.md)**

:   提出 Ferret，首个结合一阶优化与共享随机性的联邦全参数微调方法，通过将本地更新投影到低维空间实现 $10^6\times$ 通信压缩和 $6\times$ 计算加速，同时保持与 FedAvg 相当的模型精度。

**[Generalization in Federated Learning: A Conditional Mutual Information Framework](generalization_in_federated_learning_a_conditional_mutual_information_framework.md)**

:   首次将条件互信息（CMI）框架引入联邦学习的两层泛化分析，通过构造"超级客户端"和"超级样本"，推导出有界的 CMI 泛化界，证明隐私约束蕴含泛化保证，并给出在低经验风险区间恢复最优收敛率的快速率界。

**[ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks](iclshield_exploring_and_mitigating_in-context_learning_backdoor_attacks.md)**

:   首次提出"双重学习假说"揭示 ICL 后门攻击的理论机制，并设计 ICLShield 防御方法，通过动态添加高置信度和高相似度的干净示例来调节概念偏好比，平均降低攻击成功率 26.02%。

**[Identifying and Understanding Cross-Class Features in Adversarial Training](identifying_and_understanding_cross-class_features_in_adversarial_training.md)**

:   从类别级特征归因的角度揭示对抗训练(AT)中的"跨类特征"如何先被学习后被遗忘，统一解释了鲁棒过拟合和软标签训练优势两大现象。

**[Improving the Variance of Differentially Private Randomized Experiments through Clustering](improving_the_variance_of_differentially_private_randomized_experiments_through_.md)**

:   提出 Cluster-DP 机制，利用非敏感的聚类结构信息改善差分隐私随机实验中因果效应估计的隐私-方差权衡，在不牺牲隐私保证的前提下，通过更同质的聚类结构显著降低 ATE 估计的方差损失。

**[Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](invariance_makes_llm_unlearning_resilient_even_to_unanticipated_downstream_fine-.md)**

:   将不变风险最小化（IRM）引入 LLM 遗忘框架，提出 ILU 正则化方法，使被遗忘的知识在后续下游微调中不会被恢复，仅用单个无关微调数据集即可泛化到多个未知下游任务。

**[On Differential Privacy for Adaptively Solving Search Problems via Sketching](on_differential_privacy_for_adaptively_solving_search_problems.md)**

:   本文首次将差分隐私技术扩展到搜索问题（返回解向量而非数值），提出用于自适应近似近邻搜索和回归问题的高效数据结构，在温和假设下实现 $O(\sqrt{T})$ 份数据结构副本即可正确回答 $T$ 个自适应查询。

**[On Differential Privacy for Adaptively Solving Search Problems via Sketching](on_differential_privacy_for_adaptively_solving_search_problems_via_sketching.md)**

:   首次将差分隐私技术拓展到**搜索问题**（近似最近邻查询和回归解向量输出），在稀疏邻域假设和良好条件数假设下，实现仅需 $\widetilde{O}(\sqrt{T})$ 份数据结构副本即可应对 $T$ 次自适应查询的搜索型数据结构。

**[Private Model Personalization Revisited](private_model_personalization_revisited.md)**

:   在用户级差分隐私约束下，提出高效联邦模型个性化算法 Private FedRep，通过共享低维嵌入学习实现个性化，在自然参数区间下将隐私误差相比先前工作降低 O(dk) 倍，并给出维度无关的分类风险界。

**[Quadratic Upper Bound for Boosting Robustness](quadratic_upper_bound_for_boosting_robustness.md)**

:   利用交叉熵损失关于 logit 的凸性，推导出对抗训练损失的二次上界 (QUB)，作为即插即用的损失函数替换应用于现有快速对抗训练方法，显著提升鲁棒性。

**[SecEmb: Sparsity-Aware Secure Federated Learning of On-Device Recommender System with Large Embedding](secemb_sparsity-aware_secure_federated_learning_of_on-device_recommender_system_.md)**

:   提出 SecEmb，一种利用嵌入更新稀疏性的无损安全联邦推荐协议，通过函数秘密共享（FSS）在保护用户评分物品索引和梯度隐私的同时，将上传/下载通信开销降低最高 90 倍、用户端计算时间降低最高 70 倍。

**[Theoretically Unmasking Inference Attacks Against LDP-Protected Client Data in Federated Vision Models](theoretically_unmasking_inference_attacks_against_ldp-protected_client_data_in_.md)**

:   本文为联邦学习中恶意服务器的主动成员推断攻击（AMI）提供了首个理论分析框架，推导出即使在 LDP 保护下攻击成功率的下界和上界，揭示 LDP 保护强度与模型效用之间的根本矛盾。

**[Theoretically Unmasking Inference Attacks Against LDP-Protected Clients in Federated Vision Models](theoretically_unmasking_inference_attacks_against_ldp-protected_clients_in_feder.md)**

:   首次为联邦学习中基于全连接层和自注意力层的**主动成员推断攻击（AMI）**在**LDP保护下**推导出理论成功率的上下界，揭示即使在LDP保护下，隐恓风险仍依赖于隐私预算 $\varepsilon$，且要有效缓解攻击所需的噪声会严重损害模型效用。

**[Towards Trustworthy Federated Learning with Untrusted Participants](towards_trustworthy_federated_learning_with_untrusted_participants.md)**

:   提出 CafCor 算法，通过参与者间的共享随机性实现关联噪声注入，结合新型鲁棒聚合方法 CAF，在不信任服务器、存在恶意参与者的联邦学习场景下，实现接近中心化 DP 的隐私-效用权衡。

**[TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](tuco_measuring_the_contribution_of_fine-tuning_to_individual_responses_of_llms.md)**

:   提出 Tuning Contribution (TuCo) 指标，通过将微调后 LLM 的前向传播精确分解为预训练分量 (PTC) 和微调分量 (FTC)，首次实现在推理时逐 prompt 量化微调对模型输出的贡献，并揭示越狱攻击通过削弱 FTC 幅度来绕过安全防护。
