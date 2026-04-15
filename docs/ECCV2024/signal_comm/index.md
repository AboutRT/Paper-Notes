---
title: >-
  ECCV2024 信号/通信方向 3篇论文解读
description: >-
  3篇ECCV2024 信号/通信方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# 📡 信号/通信

**🎞️ ECCV2024** · **3** 篇论文解读

**[Querycdr Query-Based Controllable Distortion Rectification Network For Fisheye I](querycdr_query-based_controllable_distortion_rectification_network_for_fisheye_i.md)**

:   提出QueryCDR网络，通过可学习查询机制（DLQM）和两种可控调制模块（CCMB/CAMB），首次实现不同畸变程度的鱼眼图像在**不重训**的情况下进行高质量可控矫正。

**[Raw-Adapter Adapting Pre-Trained Visual Model To Camera Raw Images](raw-adapter_adapting_pre-trained_visual_model_to_camera_raw_images.md)**

:   提出 RAW-Adapter，通过输入级适配器（可学习 ISP 阶段）和模型级适配器（ISP 中间特征注入骨干网络），以极小参数量（0.2-0.8M）将 sRGB 预训练模型高效适配到 Camera RAW 图像，在正常光/暗光/过曝等多种光照条件下的检测和分割任务上达到 SOTA。

**[Unsupervised Exposure Correction](unsupervised_exposure_correction.md)**

:   提出首个无监督曝光校正（UEC）方法，利用ISP管线自由生成的多曝光序列让图像互为ground truth进行训练，设计仅含19K参数的像素级变换函数保留图像细节，在曝光校正和下游边缘检测上超越有监督SOTA。
