<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🕸️ 图学习

**🧪 ICML2025** · 共 **22** 篇

**[A Cognac Shot To Forget Bad Memories: Corrective Unlearning for Graph Neural Networks](a_cognac_shot_to_forget_bad_memories_corrective_unlearning_for_graph_neural_netw.md)**

:   提出 Cognac——首个有效的 GNN 纠正性遗忘方法，通过交替执行图邻域对比遗忘（CoGN）和解耦梯度上升/下降（AC⚡DC），在仅识别 5% 被操纵实体时即可恢复接近 oracle（完全干净数据训练）的性能，比从头重训高效 8×。

**[A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition](a_general_graph_spectral_wavelet_convolution_via_chebyshev_order_decomposition.md)**

:   提出 WaveGC——通过分离 Chebyshev 多项式的奇偶项构建严格满足可容许性条件的可学习图小波，结合矩阵值滤波核的多分辨率图谱卷积网络，在短程和长程图任务上均实现一致改进（VOC 上提升 15.7%）。

**[A Recipe for Causal Graph Regression: Confounding Effects Revisited](a_recipe_for_causal_graph_regression_confounding_effects_revisited.md)**

:   首次系统性地将因果图学习从分类扩展到回归任务，通过增强型图信息瓶颈（Enhanced GIB）承认混淆子图的预测能力，并用对比学习替代依赖离散标签的因果干预方法，在图级 OOD 回归基准上显著超越现有方法。

**[Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based Centrality](balancing_efficiency_and_expressiveness_subgraph_gnns_with_walk-based_centrality.md)**

:   提出 HyMN——通过游走中心性（Subgraph Centrality）对子图 GNN 的子图包进行高效采样，仅需 1-2 个子图即可媲美全包 Subgraph GNN 的性能，同时将中心性作为结构编码进一步增强判别能力，使子图方法首次可扩展到数百倍更大的图。

**[Banyan: Improved Representation Learning with Explicit Structure](banyan_improved_representation_learning_with_explicit_structure.md)**

:   Banyan 通过**纠缠层次树结构**和**对角化消息传递**两大创新，仅用 14 个非嵌入参数就在语义文本相似度任务上超越了大规模 Transformer 模型，为低资源语言的语义表示学习提供了高效可行的替代方案。

**[CoDy: Counterfactual Explainers for Dynamic Graphs](cody_counterfactual_explainers_for_dynamic_graphs.md)**

:   提出 CoDy——首个用于时序图神经网络（TGNN）的反事实解释方法，通过蒙特卡洛树搜索（MCTS）结合时空启发式策略高效探索可能的解释子图空间，在多个数据集上 AUFSC+ 提升 16%。

**[Diss-l-ECT: Dissecting Graph Data with Local Euler Characteristic Transforms](diss-l-ect_dissecting_graph_data_with_local_euler_characteristic_transforms.md)**

:   提出 Local Euler Characteristic Transform (ℓ-ECT)，将经典 ECT 拓扑不变量扩展到图的局部邻域，为每个节点生成无损的拓扑-几何指纹，在节点分类任务（尤其是高异质性图）上超越标准 GNN，同时提供理论可逆性保证与可解释性。

**[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](from_rag_to_memory_non-parametric_continual_learning_for_large_language_models.md)**

:   提出 HippoRAG 2，通过将段落节点融入知识图谱、用 query-to-triple 深度上下文化链接、以及 LLM 驱动的识别记忆过滤，全面超越标准 RAG 在事实记忆、语义理解和关联推理三大维度的表现，向 LLM 的非参数化持续学习迈进一步。

**[Graph-Constrained Reasoning Faithful Reasoning On Knowledge Graphs With Large La](graph-constrained_reasoning_faithful_reasoning_on_knowledge_graphs_with_large_la.md)**

:   提出 Graph-constrained Reasoning (GCR)，通过将知识图谱编码为 KG-Trie 并嵌入 LLM 解码过程，实现零幻觉的忠实推理，在 KGQA 基准上达到 SOTA 且具备零样本跨图谱迁移能力。

**[Graph Attention is Not Always Beneficial: A Theoretical Analysis of Graph Attention Mechanisms via Contextual Stochastic Block Models](graph_attention_is_not_always_beneficial_a_theoretical_analysis_of_graph_attenti.md)**

:   通过 CSBM 理论分析揭示图注意力并非总有益：结构噪声>特征噪声时有效，反之简单卷积更优；多层 GAT 的完美分类 SNR 要求从 $\omega(\sqrt{\log n})$ 放松到 $\omega(\sqrt{\log n}/\sqrt[3]{n})$。

**[GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers](grokformer_graph_fourier_kolmogorov-arnold_transformers.md)**

:   提出 GrokFormer，通过傅里叶级数参数化的 Kolmogorov-Arnold 可学习激活函数，在图 Laplacian 的多阶谱上自适应学习滤波器基，同时具备 **谱阶自适应** 和 **谱自适应** 能力，是目前唯一在两个维度上都可学习的图 Transformer 滤波器。

**[Hgot Self-Supervised Heterogeneous Graph Neural Network With Optimal Transport](hgot_self-supervised_heterogeneous_graph_neural_network_with_optimal_transport.md)**

:   提出 HGOT，首次将最优传输理论引入异质图自监督学习，用 branch view（元路径视图）与 central view（聚合视图）之间的 Fused Gromov-Wasserstein 传输计划替代传统对比学习中的数据增强与正负样本选取，在节点分类上平均提升超过 6%。

**[Hyperbolic-PDE GNN: Spectral Graph Neural Networks in the Perspective of A System of Hyperbolic Partial Differential Equations](hyperbolic-pde_gnn_spectral_graph_neural_networks_in_the_perspective_of_a_system.md)**

:   将消息传递建模为双曲偏微分方程组，证明节点特征的解空间由拉普拉斯矩阵的特征向量张成，从而将拓扑结构信息内嵌到节点表示中，并通过多项式近似建立与谱 GNN 的桥梁以增强其性能。

**[Learnable Spatial-Temporal Positional Encoding for Link Prediction](learnable_spatial-temporal_positional_encoding_for_link_prediction.md)**

:   提出 L-STEP，一种可学习的时空位置编码方法，从时空谱角度证明可保持图属性，仅用 MLP 即可达到 Transformer 性能，在 13 个数据集和 TGB 基准上取得领先表现，且计算复杂度更优。

**[LLM Enhancers for GNNs: An Analysis from the Perspective of Causal Mechanism Identification](llm_enhancers_for_gnns_an_analysis_from_the_perspective_of_causal_mechanism_iden.md)**

:   从因果机制识别的角度分析"LLM增强器+GNN"范式的内部机制，发现LLM增强器主要提供节点级/原始数据级信息，并据此提出注意力传输（AT）模块优化两者间的信息传递。

**[Machines and Mathematical Mutations: Using GNNs to Characterize Quiver Mutation Classes](machines_and_mathematical_mutations_using_gnns_to_characterize_quiver_mutation_c.md)**

:   利用图神经网络 (GNN) 和可解释性技术研究箭图变异等价类问题，**独立重新发现**了 $\tilde{D}$ 型箭图变异类的组合刻画定理，展示了 ML 作为数学研究工具的价值。

**[Mitigating Over-Squashing in Graph Neural Networks by Spectrum-Preserving Sparsification](mitigating_over-squashing_in_graph_neural_networks_by_spectrum-preserving_sparsi.md)**

:   提出 GOKU（稠密化-稀疏化重连范式），通过将输入图视为未知稠密潜在图的谱稀疏器并求解逆稀疏化问题，在增强图连通性的同时显式保留拉普拉斯谱，有效缓解 GNN 的 over-squashing 问题。

**[Neural Graph Matching Improves Retrieval Augmented Generation in Molecular Machine Learning](neural_graph_matching_improves_retrieval_augmented_generation_in_molecular_machi.md)**

:   提出 MARASON，将**神经图匹配（Neural Graph Matching）**引入分子机器学习的检索增强生成（RAG）框架，通过可微分的碎片级对齐机制，把检索到的参考分子谱图信息有效融入目标分子的质谱预测中，在 NIST 数据集上将 top-1 检索准确率从 19% 提升到 28%。

**[Open Your Eyes: Vision Enhances Message Passing Neural Networks in Link Prediction](open_your_eyes_vision_enhances_message_passing_neural_networks_in_link_predictio.md)**

:   首次将视觉感知引入消息传递图神经网络(MPNN)，通过将子图可视化为图像并用视觉编码器提取视觉结构特征(VSF)，提出 GVN/E-GVN 框架，在 7 个链接预测基准上均达到 SOTA。

**[Positional Encoding meets Persistent Homology on Graphs](positional_encoding_meets_persistent_homology_on_graphs.md)**

:   理论证明位置编码（PE）和持续同调（PH）互不可比——各存在对方失败但自身成功的图构造，提出 PiPE 方法统一两者，可证明比单独使用更具表达力，在分子/分类/OOD任务上表现优异。

**[Toward Data-centric Directed Graph Learning: An Entropy-driven Approach](toward_data-centric_directed_graph_learning_an_entropy-driven_approach.md)**

:   提出 EDEN（熵驱动有向图知识蒸馏），从数据中心视角利用层级知识树和互信息量化揭示有向图中拓扑与节点属性的潜在关联，作为即插即用模块增强任意 DiGNN 性能。

**[Towards Graph Foundation Models: Learning Generalities Across Graphs via Task-Trees](towards_graph_foundation_models_learning_generalities_across_graphs_via_task-tre.md)**

:   提出 Task-Tree 作为统一学习实例对齐节点/边/图级任务，理论分析其稳定性/可迁移性/泛化性，构建图基础模型 GIT 在 32 个图上通过微调/上下文学习/零样本展现跨域跨任务泛化能力。
