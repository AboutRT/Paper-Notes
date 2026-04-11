<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛰️ 遥感

**📹 ICCV2025** · 共 **8** 篇

**[AstroLoc: Robust Space to Ground Image Localizer](astroloc_robust_space_to_ground_image_localizer.md)**

:   提出AstroLoc，首个利用30万张人工标注宇航员照片进行训练的太空对地定位模型，通过查询-卫星配对损失和无监督挖掘技术学习鲁棒的地球表面特征表征，在recall@1上平均提升35%，recall@100持续超过99%，已在实际中完成50万+照片的定位。

**[CityNav: A Large-Scale Dataset for Real-World Aerial Navigation](citynav_a_large-scale_dataset_for_real-world_aerial_navigation.md)**

:   构建了首个面向真实城市环境的大规模空中视觉语言导航数据集 CityNav（32,637 条人类演示轨迹，覆盖 4.65 km²），并提出地理语义地图（GSM）辅助表示，显著提升基线模型的导航性能。

**[GeoDistill: Geometry-Guided Self-Distillation for Weakly Supervised Cross-View Localization](geodistill_geometry-guided_self-distillation_for_weakly_supervised_cross-view_lo.md)**

:   提出GeoDistill框架，通过基于视场角（FoV）遮挡的教师-学生自蒸馏范式增强局部判别性特征学习，在弱监督条件下（仅需粗略GPS标注）实现稳健的跨视角定位，性能提升超过10%且可即插即用于不同定位框架。

**[GeoExplorer: Active Geo-Localization with Curiosity-Driven Exploration](geoexplorer_active_geo-localization_with_curiosity-driven_exploration.md)**

:   提出 GeoExplorer，一个结合目标导向和好奇心驱动内在奖励的主动地理定位（AGL）智能体，通过联合动作-状态动力学建模和好奇心探索实现更鲁棒的 UAV 搜索策略，在未知目标和环境中展现出优越的泛化能力。

**[Pan-Crafter: Learning Modality-Consistent Alignment for Pan-Sharpening](pan-crafter_learning_modality-consistent_alignment_for_pan-sharpening.md)**

:   PAN-Crafter 提出模态一致性对齐框架，通过模态自适应重建（MARs）和跨模态对齐感知注意力（CM3A）显式处理 PAN 和 MS 图像的跨模态错位问题，在多个遥感基准数据集上达到 SOTA，且推理速度比扩散模型快 **1110×**。

**[RS-vHeat: Heat Conduction Guided Efficient Remote Sensing Foundation Model](rs-vheat_heat_conduction_guided_efficient_remote_sensing_foundation_model.md)**

:   首次将物理热传导过程引入遥感基础模型，提出 RS-vHeat，用热传导算子（HCO）替代注意力机制来建模遥感图像中的局部区域相关性，在 4 个任务 10 个数据集上取得优异性能的同时，相比注意力基线减少 84% 显存、24% FLOPs、提升 2.7 倍吞吐量。

**[Towards a Unified Copernicus Foundation Model for Earth Vision](towards_a_unified_copernicus_foundation_model_for_earth_visi.md)**

:   提出由Copernicus-Pretrain（1870万张覆盖全部Sentinel任务的对齐图像）、Copernicus-FM（通过扩展动态超网络和Fourier元数据编码处理任意光谱/非光谱传感器的统一基础模型）、Copernicus-Bench（15个分层下游任务基准）三位一体的完整EO基础模型体系，首次实现从地表到大气的跨模态联合预训练，在15个下游任务中11个以冻结编码器超越全参数监督训练。

**[WildSAT: Learning Satellite Image Representations from Wildlife Observations](wildsat_learning_satellite_image_representations_from_wildlife_observations.md)**

:   提出 WildSAT，利用公民科学平台上的数百万地理标记野生动物观测数据，通过对比学习将卫星图像、物种位置和文本描述对齐，显著提升遥感图像表征质量，并支持零样本文本检索。
