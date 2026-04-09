<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🛡️ AI 安全

**📹 ICCV2025** · 共 **4** 篇

**[A Framework for Double-Blind Federated Adaptation of Foundation Models](a_framework_for_doubleblind_federated_adaptation_of_foundati.md)**

:   BlindFed提出了双盲联邦基础模型适配框架：通过FHE友好的架构重设计（多项式近似非线性操作）+ 两阶段分割学习（离线知识蒸馏 + 在线加密推理）+ 隐私增强（样本置换 + 随机块采样），在数据方看不到模型、模型方看不到数据的约束下实现了接近LoRA的适配精度。

**[Active Membership Inference Test (aMINT): Enhancing Model Auditability with Multi-Task Learning](active_membership_inference_test_amint_enhancing_model_audit.md)**

:   提出Active MINT（aMINT），将成员推断检测作为训练时的优化目标，通过多任务学习让被审计模型与MINT模型联合训练、共享早期特征层，在不显著损失主任务性能的前提下，将训练数据的识别准确率从被动MINT的~60%大幅提升至80%以上。

**[SpecGuard: Spectral Projection-based Advanced Invisible Watermarking](specguard_spectral_projection-based_advanced_invisible_watermarking.md)**

:   SpecGuard 提出将水印信息嵌入到小波分解后的高频子带的频谱域中（通过 FFT 近似的频谱投影），编码端用强度因子增强鲁棒性，解码端利用 Parseval 定理设计可学习阈值进行比特恢复，在保持高图像质量（PSNR>42dB）的同时实现了对畸变、再生成和对抗攻击的全面鲁棒性，超越了现有 SOTA 方法。

**[Towards Adversarial Robustness via Debiased High-Confidence Logit Alignment](towards_adversarial_robustness_via_debiased_high-confidence_logit_alignment.md)**

:   揭示了逆向对抗攻击（inverse adversarial attack）在对抗训练中导致模型注意力偏移至背景特征的虚假相关性问题，提出 DHAT 方法通过去偏高置信度 logit 正则化（DHLR）和前景 logit 正交增强（FLOE）两个组件来消除这种偏差，在 CIFAR-10/100 和 ImageNet-1K 上取得了 SOTA 的对抗鲁棒性。
