<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🖼️ 图像恢复

**📹 ICCV2025** · 共 **7** 篇

**[ALOcc: Adaptive Lifting-Based 3D Semantic Occupancy and Cost Volume-Based Flow Predictions](alocc_adaptive_liftingbased_3d_semantic_occupancy_and_cost_v.md)**

:   提出ALOcc框架，通过遮挡感知的自适应提升机制、语义原型对齐和BEV代价体flow预测三个改进，在多个占据预测基准上取得SOTA，同时保持较高推理速度。

**[Benchmarking Burst Super-Resolution for Polarization Images: Noise Dataset and Analysis](benchmarking_burst_superresolution_for_polarization_images_n.md)**

:   针对偏振相机"光效低、分辨率低、噪声大"的硬件瓶颈，构建了两个专用数据集（PolarNS用于噪声统计分析，PolarBurstSR用于burst超分的训练/评测），提出偏振噪声传播分析模型，并将5种SOTA burst超分方法适配到偏振域，证明偏振专用训练在强度图(s0)和偏振角(AoLP)重建上显著优于RGB通用训练。

**[Blind2Sound: Self-Supervised Image Denoising without Residual Noise](blind2sound_self-supervised_image_denoising_without_residual_noise.md)**

:   提出 Blind2Sound 框架，通过自适应重可见损失（adaptive re-visible loss）感知噪声水平并实现个性化去噪，配合 Cramer Gaussian 损失提升噪声参数估计精度，在自监督盲去噪中消除残余噪声，性能超越同期所有自监督方法甚至部分有监督基线。

**[Blind Noisy Image Deblurring Using Residual Guidance Strategy](blind_noisy_image_deblurring_using_residual_guidance_strateg.md)**

:   提出残差引导策略（RGS），在图像金字塔的粗到细估计过程中，利用相邻粗尺度的卷积残差经 guided filter 去噪后校正当前尺度的模糊图像，从而在高噪声（σ=0.1）下显著提升盲去模糊的核估计精度和恢复质量，无需训练即超越多种深度学习方法。

**[Generic Event Boundary Detection via Denoising Diffusion (DiffGEBD)](generic_event_boundary_detection_via_denoising_diffusion.md)**

:   DiffGEBD 首次将扩散模型引入通用事件边界检测（GEBD），通过将边界预测建模为从随机噪声到合理边界分布的去噪过程，利用 Classifier-Free Guidance 控制预测多样性，并提出了对称 F1 和 Diversity Score 两项新评估指标来衡量多预测场景下的质量与多样性。

**[Low-Light Image Enhancement using Event-Based Illumination Estimation (RetinEV)](low-light_image_enhancement_using_event-based_illumination_estimation.md)**

:   RetinEV 提出利用事件相机的"时间映射事件"（temporal-mapping events，由透射率调制触发）而非传统"运动事件"进行光照估计，结合 Retinex 理论将低光照图像分解为光照和反射率分量，通过光照辅助反射率增强（IRE）模块实现高质量低光照图像增强，在 640×480 分辨率下达到 35.6 FPS 实时速度。

**[Robust Adverse Weather Removal via Spectral-based Spatial Grouping (SSGformer)](robust_adverse_weather_removal_via_spectral-based_spatial_grouping.md)**

:   SSGformer 提出一种基于光谱分解和分组注意力的 All-in-One 恶劣天气图像复原方法：利用 Sobel 算子提取高频边缘信息和 SVD 分析低频退化纹理，将二者融合后生成空间分组掩码（grouping-mask），在组内执行通道和空间注意力以实现对多种天气退化（雨、雪、雾、雨滴）的鲁棒去除。
