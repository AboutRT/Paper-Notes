<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📐 优化/理论

**📹 ICCV2025** · 共 **6** 篇

**[Addressing Representation Collapse in Vector Quantized Models with One Linear Layer](addressing_representation_collapse_in_vector_quantized_models_with_one_linear_la.md)**

:   提出SimVQ方法，通过一个可学习的线性变换层对码本向量进行重参数化（$\bm{C}\bm{W}$），将码本的不相交优化转化为联合空间优化，从根本上解决VQ模型中的表示崩塌问题，实现接近100%的码本利用率。

**[Adversarial Data Augmentation for Single Domain Generalization via Lyapunov Exponents](adversarial_data_augmentation_for_single_domain_generalization_via_lyapunov_expo.md)**

:   提出 LEAwareSGD 优化器，利用 Lyapunov 指数（LE）动态调节学习率，引导模型训练在混沌边缘附近，在对抗数据增强框架下实现更广泛的参数空间探索，显著提升单域泛化（SDG）性能。

**[Class-Wise Federated Averaging for Efficient Personalization](class-wise_federated_averaging_for_efficient_personalization.md)**

:   cwFedAvg 将 FedAvg 从"按客户端聚合"扩展为"按类别聚合"，为每个类别创建专属全局模型，再根据各客户端的类别分布加权组合成个性化模型，配合权重分布正则化（WDR）增强类别分布与权重范数的关联，在保持 FedAvg 通信开销的同时显著提升非 IID 场景下的个性化性能。

**[Cooperative Pseudo Labeling for Unsupervised Federated Classification](cooperative_pseudo_labeling_for_unsupervised_federated_classification.md)**

:   FedCoPL 首次将无监督联邦学习扩展到分类任务，通过协作伪标签策略（全局分配伪标签确保类别平衡）和部分 prompt 聚合协议（仅聚合视觉 prompt、保留文本 prompt 本地化）有效应对 CLIP 固有偏差和标签偏移挑战。

**[Federated Continual Instruction Tuning](federated_continual_instruction_tuning.md)**

:   首次提出联邦持续指令微调（FCIT）基准，涵盖 2 种场景、4 种设置和 12 个数据集，并设计 DISCO 框架通过动态知识组织（DKO）和子空间选择性激活（SSA）有效解决数据异构性和灾难性遗忘。

**[Memory-Efficient 4-bit Preconditioned Stochastic Optimization](memory-efficient_4-bit_preconditioned_stochastic_optimization.md)**

:   提出基于 Cholesky 分解 + 误差反馈的 4-bit 量化方案，将 Shampoo 优化器的预条件矩阵压缩至 4-bit 精度，在大幅降低 GPU 显存的同时保持与 32-bit Shampoo 接近的训练性能，并给出了光滑与非光滑两种场景下的收敛性证明。
