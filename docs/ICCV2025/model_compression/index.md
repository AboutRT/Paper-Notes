<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📦 模型压缩

**📹 ICCV2025** · 共 **25** 篇

**[A Good Teacher Adapts Their Knowledge for Distillation](a_good_teacher_adapts_their_knowledge_for_distillation.md)**

:   本文揭示了知识蒸馏中教师-学生容量差距问题的本质原因在于**输出分布的类内分布不匹配**，并提出 AID（Adapted Intra-class Distribution）方法，在蒸馏前对教师模型进行微调以优化其类内分布使之更符合学生的学习能力，在多种架构组合上取得了SOTA性能。

**[Achieving More with Less: Additive Prompt Tuning for Rehearsal-Free Class-Incremental Learning](achieving_more_with_less_additive_prompt_tuning_for_rehearsal-free_class-increme.md)**

:   提出 APT（Additive Prompt Tuning），用加法操作替代传统的提示拼接范式，仅在 CLS token 的 key/value 上添加两个可学习向量，在大幅降低计算开销（GFLOPs 减少 41.5%）和可训练参数（减少 78.2%）的同时实现 SOTA 的类增量学习性能。

**[Aligning Information Capacity Between Vision and Language via Dense-to-Sparse Feature Distillation](aligning_information_capacity_between_vision_and_language_via_dense-to-sparse_fe.md)**

:   提出D2S-VSE框架，通过两阶段训练（稠密文本预训练+稠密到稀疏特征蒸馏微调）增强视觉语义嵌入的信息容量，解决图文匹配中图像与文本信息密度不对称的核心问题。

**[ARGMatch: Adaptive Refinement Gathering for Efficient Dense Matching](argmatch_adaptive_refinement_gathering_for_efficient_dense_matching.md)**

:   提出自适应精炼聚合（Adaptive Refinement Gathering）管线，包含内容感知偏移估计器、局部一致匹配校正器和局部一致上采样器三个模块，配合自适应门控机制，大幅减少了稠密匹配对重量级特征提取器和全局匹配器的依赖，以轻量级模型实现与SOTA可比的性能。

**[B-VLLM: A Vision Large Language Model with Balanced Spatio-Temporal Tokens](b-vllm_a_vision_large_language_model_with_balanced_spatio-temporal_tokens.md)**

:   本文提出B-VLLM框架，通过文本条件自适应帧选择、时序帧Token合并和空间Token采样三个模块，在VLLM的上下文窗口限制内动态平衡视频的时空线索，在MVBench上带来10%的性能提升。

**[Beyond Low-Rank Tuning: Model Prior-Guided Rank Allocation for Effective Transfer in Low-Data and Large-Gap Regimes](beyond_low-rank_tuning_model_prior-guided_rank_allocation_for_effective_transfer.md)**

:   提出SR-LoRA（Stable Rank-Guided LoRA），利用预训练权重矩阵的稳定秩（Stable Rank）作为自然先验为每层LoRA模块分配最优秩，无需搜索即可实现灵活的逐层秩分配，在大域差距+少样本迁移场景（如医学影像）中显著优于固定低秩LoRA和其他自适应秩方法。

**[TokenBridge: Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation](bridging_continuous_and_discrete_tokens_for_autoregressive_v.md)**

:   TokenBridge提出对预训练VAE连续特征进行后训练维度级量化，将连续token无损转化为离散token，再通过轻量级维度级自回归头高效建模指数级大词表空间，在ImageNet 256×256上用标准交叉熵损失达到了与连续token方法（如MAR）相当的生成质量（FID=1.55），且推理快5.94倍。

**[Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation](bridging_continuous_and_discrete_tokens_for_autoregressive_visual_generation.md)**

:   提出TokenBridge，通过对预训练连续VAE特征进行后训练维度级量化，将连续token转化为离散token，在保持连续token高保真表示能力的同时，使用标准交叉熵损失进行简洁的自回归建模，在ImageNet 256×256上达到与连续方法可比的生成质量。

**[CIARD: Cyclic Iterative Adversarial Robustness Distillation](ciard_cyclic_iterative_adversarial_robustness_distillation.md)**

:   提出CIARD，通过对比推离损失（Contrastive Push Loss）解决双教师ARD框架中clean teacher和robust teacher的优化目标冲突，并设计迭代教师训练（ITT）策略持续更新robust teacher以防止性能退化，在CIFAR-10/100和Tiny-ImageNet上同时提升对抗鲁棒性+3.53%和干净准确率+5.87%。

**[Color Matching Using Hypernetwork-Based Kolmogorov-Arnold Networks (cmKAN)](color_matching_using_hypernetwork-based_kolmogorov-arnold_networks.md)**

:   提出cmKAN，利用超网络驱动的Kolmogorov-Arnold Network进行颜色匹配，通过生成器预测空间变化的KAN样条参数，支持有监督/无监督/配对优化三种场景和raw-to-raw/raw-to-sRGB/sRGB-to-sRGB三种任务，在所有任务上平均超越现有方法37.3%且极轻量（76.4K参数）。

**[Colors See Colors Ignore: Clothes Changing ReID with Color Disentanglement](colors_see_colors_ignore_clothes_changing_reid_with_color_disentanglement.md)**

:   提出CSCI方法，通过引入Color token学习颜色表示（Color See），并利用新颖的S2A自注意力机制将颜色信息与ReID特征解耦（Color Ignore），在无需外部标注的情况下有效消除换衣行人重识别中的外观偏差。

**[Competitive Distillation: A Simple Learning Strategy for Improving Visual Classification](competitive_distillation_a_simple_learning_strategy_for_improving_visual_classif.md)**

:   提出竞争蒸馏策略，在多网络联合训练中，每个迭代动态选择表现最好的网络作为教师，配合随机扰动机制引入类似遗传算法的变异操作，显著提升视觉分类性能。

**[Dataset Distillation via the Wasserstein Metric](dataset_distillation_via_the_wasserstein_metric.md)**

:   提出 WMDD（Wasserstein Metric-based Dataset Distillation），使用 Wasserstein 重心替代 MMD 进行分布匹配，结合逐类 BatchNorm 正则化，在 ImageNet-1K 等大规模数据集上达到 SOTA 数据集蒸馏性能。

**[DuoLoRA: Cycle-Consistent and Rank-Disentangled Content-Style Personalization](duolora_cycle-consistent_and_rank-disentangled_content-style_personalization.md)**

:   DuoLoRA 提出在 LoRA 的秩维度上学习掩码（ZipRank），结合 SDXL 层先验信息和循环一致性损失（Constyle loss），实现了高效的内容-风格 LoRA 合并，在多个基准上超过 ZipLoRA 等 SOTA 方法，且可训练参数减少 19 倍。

**[Efficient Adaptation of Pre-Trained Vision Transformer Underpinned by Approximation Theory](efficient_adaptation_of_pre-trained_vision_transformer_underpinned_by_approximat.md)**

:   本文发现预训练 ViT 权重矩阵的行/列向量具有近似正交性，而 LoRA/Adapter 的投影矩阵不具备此性质；提出 AOFT 策略，用单个可学习向量生成近似正交的下/上投影矩阵，使其与骨干网络性质对齐，从而降低泛化误差上界，在 FGVC 和 VTAB-1k 上用更少参数达到竞争性能。

**[FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning](fastvar_linear_visual_autoregressive_modeling_via_cached_token_pruning.md)**

:   FastVAR 提出一种无需训练的后处理加速方法，通过观察 VAR 模型中大尺度步骤主要建模高频纹理且对剪枝鲁棒的特性，利用频域引导的关键 token 选择（PTS）仅保留高频 token 参与前向，并用缓存的早期尺度 token 恢复被剪枝的位置（CTR），在 FlashAttention 基础上实现额外 2.7× 加速且性能损失 <1%，并首次实现单张 3090 GPU 上 1.5 秒生成 2K 图像。

**[Gain-MLP: Improving HDR Gain Map Encoding via a Lightweight MLP](gain-mlp_improving_hdr_gain_map_encoding_via_a_lightweight_mlp.md)**

:   提出使用 10KB 轻量级 MLP 网络替代传统 JPEG/HEIC 压缩来编码 HDR gain map，以 SDR 图像的颜色和位置坐标 (r,g,b,x,y) 作为输入，结合指数残差编码（gamma map），在多个 HDR 重建指标上超越现有方法和传统压缩技术。

**[Local Dense Logit Relations for Enhanced Knowledge Distillation](local_dense_logit_relations_for_enhanced_knowledge_distillation.md)**

:   本文提出局部稠密关系 logit 蒸馏（LDRLD），通过递归解耦和重组 logit 知识来捕获细粒度的类间关系，结合自适应衰减权重（ADW）策略对关键类别对赋予更高权重，在 CIFAR-100、ImageNet-1K 和 Tiny-ImageNet 上持续优于现有 logit 蒸馏 SOTA。

**[MixA-Q: Revisiting Activation Sparsity for Vision Transformers from a Mixed-Precision Quantization Perspective](mixa-q_revisiting_activation_sparsity_for_vision_transformers_from_a_mixed-preci.md)**

:   提出 MixA-Q，一种混合精度激活量化框架，将窗口级激活稀疏性（原本用于剪枝）转化为量化维度的利用——对不重要的窗口分配更低比特宽度而非完全跳过计算，在 COCO 目标检测上实现 PTQ 无损 1.35× 加速和 QAT 无损 1.25× 加速，同时具有更好的 OOD 鲁棒性。

**[MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion](motionfollower_editing_video_motion_via_score-guided_diffusion.md)**

:   提出 MotionFollower，通过两个轻量卷积控制器（姿态+外观）和基于分数函数正则化的一致性引导机制，实现视频运动编辑，在 GPU 显存消耗减少约 80% 的同时超越 MotionEditor 等强基线。

**[MSQ: Memory-Efficient Bit Sparsification Quantization](msq_memory-efficient_bit_sparsification_quantization.md)**

:   提出MSQ，通过RoundClamp量化器从权重直接计算最低有效位(LSB)并施加L1正则化诱导稀疏性，无需显式创建bit-level可训练参数即可实现混合精度量化发现，训练参数减少8倍、训练时间减少86%，同时保持竞争性的精度-压缩权衡。

**[Scheduling Weight Transitions for Quantization-Aware Training](scheduling_weight_transitions_for_quantization-aware_training.md)**

:   指出传统学习率调度对量化感知训练（QAT）中量化权重的有效步长控制失效，提出转换率（Transition Rate）调度技术，通过自适应学习率（TALR）显式控制量化权重的离散跳变次数，显著提升低比特量化模型性能。

**[StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic Data](stolenlora_exploring_lora_extraction_attacks_via_synthetic_data.md)**

:   StolenLoRA 首次提出针对 LoRA 自适应模型的模型提取攻击方向，利用 LLM 驱动的 Stable Diffusion 生成高质量合成数据替代真实数据集搜索，并设计基于分歧的半监督学习（DSL）策略通过选择性查询最大化信息增益，仅需 10k 次查询即可达到高达 96.60% 的攻击成功率，揭示了 LoRA 适配模型的严重安全漏洞。

**[Task Vector Quantization for Memory-Efficient Model Merging](task_vector_quantization_for_memory-efficient_model_merging.md)**

:   本文提出对任务向量（fine-tuned 与 pre-trained 权重之差）而非 fine-tuned 权重本身进行量化，利用任务向量更窄的数值范围实现低至 3-bit 的量化而不损失精度；进一步提出残差任务向量量化（RTVQ），将任务向量分解为共享高精度基向量和低精度偏移量，在仅用 8% 原始存储的情况下维持甚至提升模型合并性能。

**[Time-Aware Auto White Balance in Mobile Photography](time-aware_auto_white_balance_in_mobile_photography.md)**

:   本文提出一种利用手机上下文元数据（时间戳和地理位置）辅助图像颜色信息的轻量化光照估计方法（约 5K 参数），在自建 3224 张智能手机数据集上达到或超过大模型性能，且可在旗舰手机 DSP 上 0.25ms 内完成推理。
