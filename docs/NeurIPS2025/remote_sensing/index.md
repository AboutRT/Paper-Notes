---
title: >-
  NeurIPS2025 遥感方向 10篇论文解读
description: >-
  10篇NeurIPS2025 遥感方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛰️ 遥感

**🧠 NeurIPS2025** · 共 **10** 篇

**[C3Po Cross-View Cross-Modality Correspondence By Pointmap Prediction](c3po_cross-view_cross-modality_correspondence_by_pointmap_prediction.md)**

:   构建了包含 90K 地面照片-平面图对（597 个场景、153M 像素级对应和 85K 相机位姿）的 C3 数据集，揭示现有对应模型在跨视角跨模态（如地面照片 vs. 平面图）场景下的局限性，通过在该数据上训练可将最佳方法的 RMSE 降低 34%。

**[Chamaevit Unifying Channelaware Masked Autoencoders And Mult](chamaevit_unifying_channelaware_masked_autoencoders_and_mult.md)**

:   提出ChA-MAEViT，通过动态通道-patch联合掩码、记忆token、混合token融合和通道感知解码器四大组件增强多通道图像（MCI）的跨通道特征学习，在卫星和显微三大数据集上平均超越SOTA 3.0-21.5%。

**[Connecting The Dots A Machine Learning Ready Dataset For Ionospheric Forecasting](connecting_the_dots_a_machine_learning_ready_dataset_for_ionospheric_forecasting.md)**

:   作为2025 NASA Heliolab的成果，本文构建了首个全面的ML-ready电离层预测数据集，将太阳动力学观测站（SDO）极紫外辐照度嵌入、太阳风参数、行星际磁场、地磁活动指数、JPL稠密TEC全球电离层图、Madrigal稀疏TEC、太阳通量指数以及轨道力学参数等7大类异构数据源统一对齐到一致的时间-空间结构中，并在此基础上训练了包括LSTM、球面神经算子（SFNO）和GraphCast在内的多种时空预测架构，实现了对全球垂直总电子含量（vTEC）在安静和地磁活跃条件下长达12小时的自回归预测，超越了持续性基线。

**[Geolink Empowering Remote Sensing Foundation Model With Openstreetmap Data](geolink_empowering_remote_sensing_foundation_model_with_openstreetmap_data.md)**

:   GeoLink将OpenStreetMap矢量数据直接融入遥感基础模型预训练，通过异构GNN编码OSM数据并设计多粒度跨模态学习目标（区域-图像级对比 + 对象-patch级融合），在127万样本对上高效预训练后，7个分类和4个分割/变化检测benchmark全面超越现有RS FM。

**[Greenhyperspectra A Multi-Source Hyperspectral Dataset For Global Vegetation Tra](greenhyperspectra_a_multi-source_hyperspectral_dataset_for_global_vegetation_tra.md)**

:   构建了包含14万+多源高光谱植被反射率光谱的GreenHyperSpectra预训练数据集，涵盖近端、机载和星载平台，通过半监督和自监督方法在标签稀缺场景下显著超越全监督基线的多性状预测精度。

**[Mass Conservation On Rails -- Rethinking Physics-Informed Learning Of Ice Flow V](mass_conservation_on_rails_--_rethinking_physics-informed_learning_of_ice_flow_v.md)**

:   提出散度无关神经网络（dfNN），通过流函数的辛梯度从架构上精确保证质量守恒（散度恒为零），结合方向引导学习策略，在南极Byrd冰川冰通量插值中显著优于软约束PINNs和无约束NN。

**[Orbitzoo Real Orbital Systems Challenges For Reinforcement Learning](orbitzoo_real_orbital_systems_challenges_for_reinforcement_learning.md)**

:   提出OrbitZoo——一个基于工业级轨道动力学库Orekit的多智能体强化学习环境，支持碰撞规避、编队飞行等场景，在Starlink真实数据验证中MAPE仅为0.16%。

**[Ortholoc Uav 6-Dof Localization And Calibration Using Orthographic Geodata](ortholoc_uav_6-dof_localization_and_calibration_using_orthographic_geodata.md)**

:   OrthoLoC构建了首个面向正射地理数据（DOP+DSM）的大规模UAV 6-DoF定位基准数据集，包含16425张真实UAV图像覆盖德国和美国47个区域，并引入AdHoP（自适应单应性预处理）匹配改进技术，在不修改特征匹配器的情况下将匹配性能提升95%、平移误差降低63%。

**[RSCC: Large-Scale Remote Sensing Change Caption Dataset for Disasters](rscc_a_large-scale_remote_sensing_change_caption_dataset_for_disaster_events.md)**

:   提出RSCC数据集——62,351对灾前/灾后遥感图像配以丰富变化描述文本，覆盖地震/洪水/野火等，填补灾害相关双时相图像-文本缺口。

**[Scaling Image Geo-Localization To Continent Level](scaling_image_geo-localization_to_continent_level.md)**

:   混合方法结合分类学习的原型和航拍图像嵌入，在覆盖西欧43.3万平方公里上实现200m内68%+、100m内59.2%的定位率，首次在大陆规模实现此精度。
