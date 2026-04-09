<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**🧪 ICML2025** · 共 **37** 篇

**[ADIOS: Antibody Development via Opponent Shaping](adios_antibody_development_via_opponent_shaping.md)**

:   将多智能体强化学习中的对手塑形（Opponent Shaping）引入抗体设计，提出 ADIOS 元学习框架：外层循环优化抗体，内层循环模拟病毒适应性逃逸，使设计出的"塑形抗体"（shapers）不仅能对抗当前病毒变种，还能主动引导病毒向更弱、更易被靶向的方向进化。

**[Aligning Protein Conformation Ensemble Generation with Physical Feedback](aligning_protein_conformation_ensemble_generation_with_physical_feedback.md)**

:   提出 Energy-based Alignment (EBA)，将物理力场的能量反馈融入扩散生成模型的微调过程，通过 Boltzmann 因子加权的分类目标函数对齐生成分布与物理能量景观，在 ATLAS MD 基准上实现蛋白质构象集合生成的 SOTA 性能。

**[Bayesian Inference for Correlated Human Experts and Classifiers](bayesian_inference_for_correlated_human_experts_and_classifiers.md)**

:   提出通用贝叶斯框架来建模相关人类专家和分类器之间的联合标注行为，通过潜在表示捕捉专家间相关性，用模拟推断评估额外查询的效用，在医学分类和图像标注中大幅减少专家查询次数同时保持预测准确率。

**[Boosting Masked ECG-Text Auto-Encoders as Discriminative Learners (D-BETA)](boosting_masked_ecg-text_auto-encoders_as_discriminative_learners.md)**

:   D-BETA 提出了一种融合生成式掩码自编码器与增强判别能力的对比学习框架，通过 ECG-Text Sigmoid (ETS) 损失和最近邻负采样策略 (N3S)，在 ECG-文本跨模态表征学习中显著超越现有方法，在仅用 1% 训练数据的线性探测中平均 AUC 提升 15%，零样本性能提升 2%。

**[Certification for Differentially Private Prediction in Gradient-Based Training](certification_for_differentially_private_prediction_in_gradient-based_training.md)**

:   提出 Abstract Gradient Training (AGT) 框架，通过凸松弛与界传播技术计算训练过程中模型参数的可达集上界，从而利用平滑敏感度机制大幅收紧隐私预测的隐私分析，在医学影像和 NLP 任务上实现比全局敏感度紧数个数量级的隐私界。

**[CFP-Gen: Combinatorial Functional Protein Generation via Diffusion Language Models](cfp-gen_combinatorial_functional_protein_generation_via_diffusion_language_model.md)**

:   提出 CFP-Gen——一种大规模扩散语言模型，通过注释引导特征调制（AGFM）和残基级控制编码（RCFE）实现多模态功能约束（功能注释 + 序列基序 + 3D 结构）的组合蛋白质生成，F1 分数比 ESM3 提升 30%。

**[ComRecGC: Global Graph Counterfactual Explainer through Common Recourse](comrecgc_global_graph_counterfactual_explainer_through_common_recourse.md)**

:   本文首次形式化了图神经网络的**公共补救 (Common Recourse)** 全局反事实解释问题，证明该问题是 NP-hard 的，并提出了 ComRecGC 算法——通过多头顶点增强随机游走 (Multi-head VRRW) 寻找反事实图，再用 DBScan 聚类提取公共补救，在 NCI1、Mutagenicity、AIDS、Proteins 四个真实数据集上，覆盖率全面超越现有基线 10%–30%。

**[Context Matters: Query-aware Dynamic Long Sequence Modeling of Gigapixel Images](context_matters_query-aware_dynamic_long_sequence_modeling_of_gigapixel_images.md)**

:   提出 Querent 框架——通过 query-aware 的动态区域重要性评估实现千亿像素全切片图像（WSI）中的高效长程上下文建模，在理论上有界逼近完整自注意力，在 10+ 个 WSI 数据集的生物标志物预测/基因突变预测/癌症分型/生存分析中超越 SOTA。

**[Designing Cyclic Peptides via Harmonic SDE with Atom-Bond Modeling](designing_cyclic_peptides_via_harmonic_sde_with_atom-bond_modeling.md)**

:   提出 CpSDE 框架，通过谐波 SDE 生成模型 (AtomSDE) 和残基类型预测器 (ResRouter) 的交替采样，首次实现基于 3D 受体结构的全类型环肽设计，在稳定性和亲和力上超越现有线性肽设计方法。

**[Do Multiple Instance Learning Models Transfer?](do_multiple_instance_learning_models_transfer.md)**

:   首次系统评估计算病理学中 MIL 模型的迁移学习能力，发现在 pancancer 数据集上预训练的 MIL 模型能够跨器官、跨任务泛化，以不到 10% 的预训练数据超越自监督 slide foundation model（CHIEF、GigaPath）。

**[Doubly Protected Estimation for Survival Outcomes Utilizing External Controls for Randomized Clinical Trials](doubly_protected_estimation_for_survival_outcomes_utilizing_external_controls_fo.md)**

:   提出一种双重保护（doubly protected）的生存结局估计框架，通过密度比加权校正协变量偏移、DR-Learner检测结局漂移并选择性借用可比外部对照，在保证一致性和效率提升的同时对外部数据异质性具有鲁棒性。

**[Efficient Molecular Conformer Generation with SO(3)-Averaged Flow Matching and Reflow](efficient_molecular_conformer_generation_with_so3-averaged_flow_matching_and_ref.md)**

:   提出 SO(3)-Averaged Flow 训练目标，通过解析地对旋转群 SO(3) 上所有旋转取平均来消除先验-数据分布间的旋转对齐需求，结合 Reflow+蒸馏实现高质量的少步乃至单步分子构象生成。

**[Efficient Noise Calculation in Deep Learning-based MRI Reconstructions](efficient_noise_calculation_in_deep_learning-based_mri_reconstructions.md)**

:   提出基于 Jacobian Sketching 的高效方法，通过随机相向量探测 DL 重建网络的 Jacobian 对角元，以无偏估计加速 MRI 重建中的体素级噪声方差，计算和内存需求降低一个数量级以上，与 Monte Carlo 参考相关系数达 99.8%。

**[Empower Structure-Based Molecule Optimization with Gradient Guided Bayesian Flow Networks](empower_structure-based_molecule_optimization_with_gradient_guided_bayesian_flow.md)**

:   提出 MolJO 框架，利用贝叶斯流网络（BFN）的连续可微参数空间 $\boldsymbol{\theta}$，实现对分子坐标（连续）和原子类型（离散）的联合梯度引导优化，并设计滑动窗口后向校正策略平衡探索与利用，在 CrossDocked2020 上以 51.3% Success Rate 大幅领先现有方法。

**[Enhancing Statistical Validity and Power in Hybrid Controlled Trials: A Randomization Inference Approach with Conformal Selective Borrowing](enhancing_statistical_validity_and_power_in_hybrid_controlled_trials_a_randomiza.md)**

:   提出基于 Fisher 随机化检验（FRT）+ 保形选择性借用（CSB）的混合对照试验推断框架，实现有限样本精确的 I 类错误率控制和模型无关的统计推断，通过自适应阈值最小化 MSE，在保持严格 I 类错误控制的同时提升检验功效。

**[Flexibility-conditioned Protein Structure Design with Flow Matching](flexibility-conditioned_protein_structure_design_with_flow_matching.md)**

:   提出 BackFlip（从骨架预测残基级柔性）和 FliPS（以柔性 profile 为条件的 SE(3)-等变 flow matching 模型），首次实现根据目标柔性分布生成具有期望动态特性的蛋白质骨架结构，并通过 300 ns 分子动力学模拟验证。

**[GenMol: A Drug Discovery Generalist with Discrete Diffusion](genmol_a_drug_discovery_generalist_with_discrete_diffusion.md)**

:   提出 GenMol，一个基于掩码离散扩散（Masked Discrete Diffusion）的通用分子生成框架，通过非自回归双向并行解码生成 SAFE 序列，并引入片段重掩码（fragment remasking）和分子上下文引导（MCG），用**单一模型**覆盖从头生成、片段约束生成、目标导向 hit 生成和先导化合物优化四大药物发现场景，全面超越此前最优方法。

**[Geometric Generative Modeling with Noise-Conditioned Graph Networks](geometric_generative_modeling_with_noise-conditioned_graph_networks.md)**

:   提出 Noise-Conditioned Graph Networks (NCGNs)，使 GNN 架构根据噪声级别动态调整消息传递的范围和图分辨率：高噪声时用远程连接+低分辨率，低噪声时用局部连接+高分辨率，在 3D 点云、空间转录组和图像生成中均超越固定架构基线。

**[iDPA: Instance Decoupled Prompt Attention for Incremental Medical Object Detection](idpa_instance_decoupled_prompt_attention_for_incremental_medical_object_detectio.md)**

:   提出 iDPA 框架，通过实例级 Prompt 生成（IPG）和解耦 Prompt 注意力（DPA）两大模块，在冻结的视觉-语言目标检测模型上实现增量医学目标检测（IMOD），仅训练 1.4% 的参数即在 13 个跨模态医学数据集上全面超越 SOTA。

**[LDMol: A Text-to-Molecule Diffusion Model with Structurally Informative Latent Space Surpasses AR Models](ldmol_a_text-to-molecule_diffusion_model_with_structurally_informative_latent_sp.md)**

:   提出 LDMol，通过 SMILES 枚举对比学习构建结构感知的潜在空间，在该空间上训练条件扩散模型实现文本到分子生成，首次让扩散模型在文本数据生成任务上超越自回归模型。

**[Leveraging Partial SMILES Validation Scheme for Enhanced Drug Design in Reinforcement Learning Frameworks](leveraging_partial_smiles_validation_scheme_for_enhanced_drug_design_in_reinforc.md)**

:   提出 PSV-PPO 算法，在自回归 SMILES 分子生成的每一步引入部分 SMILES 验证（PSV）真值表，实时惩罚无效 token，在保持分子有效性的同时增强化学空间探索能力。

**[MF-LAL: Drug Compound Generation Using Multi-Fidelity Latent Space Active Learning](mf-lal_drug_compound_generation_using_multi-fidelity_latent_space_active_learnin.md)**

:   提出 MF-LAL 框架，将多保真度代理模型与分子生成模型统一到层次化潜空间中，通过主动学习高效整合分子对接（低保真）和结合自由能计算（高保真）两类预言机，生成具有显著更优结合自由能的候选药物分子（平均 ABFE 得分提升约 50%）。

**[Multivariate Conformal Selection](multivariate_conformal_selection.md)**

:   将 Conformal Selection 从单变量响应推广到多变量设定，提出区域单调性 (Regional Monotonicity) 概念，设计距离型 (mCS-dist) 和学习型 (mCS-learn) 两种非一致性分数，在有限样本下保证 FDR 控制并提升选择功效。

**[On the Vulnerability of Applying Retrieval-Augmented Generation within Knowledge-Intensive Application Domains](on_the_vulnerability_of_applying_retrieval-augmented_generation_within_knowledge.md)**

:   本文系统揭示了 RAG 检索系统在知识密集型领域（医疗、法律）中面临的**通用投毒攻击**漏洞，提出"正交增强"性质解释攻击成因，并设计基于分布感知距离的检测防御方法，在几乎所有场景中达到近乎完美的检测率。

**[Out-of-Distribution Detection Methods Answer the Wrong Questions](out-of-distribution_detection_methods_answer_the_wrong_questions.md)**

:   本文系统论证了当前主流OOD检测方法（基于特征和基于logit）在根本上回答了错误的问题——它们检测的是"特征是否异常"或"模型是否不确定"，而非"输入是否来自不同分布"，并证明了各种常见改进策略也无法解决这一根本性错位。

**[PolyConf: Unlocking Polymer Conformation Generation through Hierarchical Generative Models](polyconf_unlocking_polymer_conformation_generation_through_hierarchical_generati.md)**

:   提出 PolyConf——首个专为聚合物构象生成设计的层次化生成框架：Phase 1 用掩码自回归模型（MAR）+ 扩散过程在随机顺序下生成各重复单元的局部构象，Phase 2 用 SO(3) 扩散模型生成朝向变换以将局部构象组装为完整聚合物构象；同时构建了首个聚合物构象基准 PolyBench（5万+聚合物，~2000原子/构象），在所有结构和能量指标上均大幅超越现有方法 25%+。

**[Raptor: Scalable Train-Free Embeddings for 3D Medical Volumes Leveraging Pretrained 2D Foundation Models](raptor_scalable_train-free_embeddings_for_3d_medical_volumes_leveraging_pretrain.md)**

:   提出 Raptor（Random Planar Tensor Reduction），一种完全免训练的方法，利用冻结的 2D 基础模型（DINOv2-L）对 3D 医学体积沿三轴提取视觉 token，再通过随机投影大幅压缩维度，在 10 个医学任务上超越所有需要大规模预训练的 SOTA 方法。

**[Reliable Algorithm Selection for Machine Learning-Guided Design](reliable_algorithm_selection_for_machine_learning-guided_design.md)**

:   提出一种设计算法选择方法，通过将候选设计算法配置的成功判定形式化为多重假设检验问题，结合预测驱动推断（Prediction-Powered Inference）技术校正预测误差，以高概率保证选出在未标注设计分布上满足用户定义成功准则的算法配置。

**[Roll the Dice & Look Before You Leap: Going Beyond the Creative Limits of Next-Token Prediction](roll_the_dice_look_before_you_leap_going_beyond_the_creative_limits_of_next-toke.md)**

:   本文设计了一套最小化算法任务来量化语言模型的"创造力极限"，证明 next-token 学习在需要"思维跳跃"的开放式任务中是近视的，而多 token 方法（teacherless 训练、离散扩散模型）以及输入层噪声注入（seed-conditioning）能显著提升生成的多样性与原创性。

**[SAFER: A Calibrated Risk-Aware Multimodal Recommendation Model for Dynamic Treatment Regimes](safer_a_calibrated_risk-aware_multimodal_recommendation_model_for_dynamic_treatm.md)**

:   提出 SAFER 框架，融合结构化 EHR 与临床笔记的多模态信息，通过 KL 散度度量标签不确定性并结合保形推断控制 FDR，为高风险动态治疗推荐提供统计安全保障。

**[Scalable Generation of Spatial Transcriptomics from Histology Images via Whole-Slide Flow Matching](scalable_generation_of_spatial_transcriptomics_from_histology_images_via_whole-s.md)**

:   提出 STFlow，一种基于 flow matching 的生成模型，通过建模整张切片的基因表达联合分布来显式捕获细胞间交互，并采用局部空间注意力实现高效全切片编码，在 HEST-1k 和 STImage-1K4M 上相对最优基线提升 18%。

**[Scssl-Bench Benchmarking Self-Supervised Learning For Single-Cell Data](scssl-bench_benchmarking_self-supervised_learning_for_single-cell_data.md)**

:   提出 scSSL-Bench，一个系统性 benchmark，在 9 个单细胞数据集上评估 19 种自监督学习方法在批次校正、细胞类型注释和缺失模态预测三个下游任务上的表现，揭示了通用 SSL 方法与领域专用方法之间的任务特异性权衡。

**[SGD Jittering: A Training Strategy for Robust and Accurate Model-Based Architectures](sgd_jittering_a_training_strategy_for_robust_and_accurate_model-based_architectu.md)**

:   提出 SGD jittering 训练策略，在模型迭代重建过程中逐步注入零均值高斯噪声，理论证明其同时提升模型鲁棒性和泛化精度，且无需对抗训练的高计算开销。

**[SPACE: Your Genomic Profile Predictor is a Powerful DNA Foundation Model](space_your_genomic_profile_predictor_is_a_powerful_dna_foundation_model.md)**

:   提出 SPACE（Species-Profile Adaptive Collaborative Experts），论证**监督式基因组图谱预测**比无监督序列预训练能学到更有效的 DNA 表征，并通过物种感知 MoE 编码器和双门控解码器在 18 项 NT 下游任务中 11 项 SOTA。

**[Supercharging Graph Transformers with Advective Diffusion](supercharging_graph_transformers_with_advective_diffusion.md)**

:   提出 Advective Diffusion Transformer（AdvDIFFormer），一种物理启发的图Transformer模型，通过结合非局部扩散（全局注意力）和对流（局部消息传递）两种机制，在拓扑分布偏移下具有可证明的泛化误差控制能力，优于仅依赖局部扩散的GNN。

**[The Disparate Benefits of Deep Ensembles](the_disparate_benefits_of_deep_ensembles.md)**

:   系统揭示 Deep Ensembles 的"差异化收益效应"：集成带来的性能提升在不同受保护群体间分配不均，往往有利于已优势群体，导致公平性指标恶化；并发现集成成员间的 per-group 预测多样性差异是根本原因，Hardt 后处理可有效缓解。

**[UniMoMo: Unified Generative Modeling of 3D Molecules for De Novo Binder Design](unimomo_unified_generative_modeling_of_3d_molecules_for_de_novo_binder_design.md)**

:   提出 UniMoMo，首个统一小分子、肽和抗体三类分子的 3D binder 设计框架，使用“块图”作为统一表示、迭代全原子自编码器压缩潜空间、E(3)-等变扩散模型生成，在三个基准上超越领域特定模型。
