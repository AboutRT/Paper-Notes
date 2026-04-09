<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🖼️ 图像恢复

**🔬 ICLR2026** · 共 **11** 篇

**[Activation Steering for Masked Diffusion Language Models](activation_steering_for_masked_diffusion_language_models.md)**

:   首次将激活引导（activation steering）应用于 Masked Diffusion 语言模型（MDLM），发现 MDLM 的拒绝行为也受单一低维方向控制，通过在去噪过程中全局投影可完全绕过安全对齐，且与自回归模型不同，有效方向可从指令前的 token 中提取——反映了扩散模型的非因果并行处理特性。

**[Are Deep Speech Denoising Models Robust to Adversarial Noise?](are_deep_speech_denoising_models_robust_to_adversarial_noise.md)**

:   首次系统性评估 4 款 SOTA 深度语音去噪（DNS）模型在对抗噪声下的鲁棒性：通过心理声学约束的 PGD 攻击生成人耳不可感知的对抗噪声，可令 Demucs、Full-SubNet+、FRCRN 和 MP-SENet 输出完全不可理解的 gibberish，实验覆盖多种声学条件和人类评估，同时揭示了目标攻击、通用扰动和跨模型迁移的局限性。

**[Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes](beyond_scattered_acceptance_fast_and_coherent_inference_for_dlms_via_longest_sta.md)**

:   LSP 调度器通过在每个去噪步骤中原子性地提交最长连续稳定前缀（而非分散接受离散 token），将 DLM 推理加速 3.4 倍，同时保持或略微提升输出质量。

**[DiffusionBlocks: Block-wise Neural Network Training via Diffusion Interpretation](diffusionblocks_block-wise_neural_network_training_via_diffusion_interpretation.md)**

:   提出 DiffusionBlocks，将残差网络的逐层更新解释为连续时间扩散过程的离散化步骤，从而将网络切分为可完全独立训练的 block，在保持端到端训练性能的同时按 block 数 B 倍减少训练显存。

**[Generalizing Linear Autoencoder Recommenders with Decoupled Expected Quadratic Loss](generalizing_linear_autoencoder_recommenders_with_decoupled_expec.md)**

:   将 EDLAE 推荐模型的目标函数推广为解耦期望二次损失（DEQL），在超参数 $b>0$ 的更广范围内推导出闭式解，并通过 Miller 矩阵逆定理将计算复杂度从 $O(n^4)$ 降至 $O(n^3)$，在多个基准数据集上超越 EDLAE 和深度学习模型。

**[Horizon Imagination: Efficient On-Policy Rollout in Diffusion World Models](horizon_imagination_efficient_on-policy_rollout_in_diffusion_world_models.md)**

:   提出Horizon Imagination(HI)——扩散世界模型中的高效在策略想象过程：并行去噪多个未来观测(而非逐帧串行)，引入稳定化机制和新型采样调度(将去噪预算从有效horizon解耦+支持亚帧预算)，在Atari 100K和Craftium上仅用一半去噪步骤即保持控制性能，系统分析串行vs并行生成的质量trade-off。

**[InterActHuman: Multi-Concept Human Animation with Layout-Aligned Audio Conditions](interacthuman_multi-concept_human_animation_with_layout-aligned_audio_conditions.md)**

:   提出 InterActHuman，通过自动推断时空布局的掩码预测器和迭代掩码引导策略，实现多人/人物交互场景下的音频驱动视频生成，支持每个角色独立的语音驱动口型同步和身体动作。

**[ProtoTS: Learning Hierarchical Prototypes for Explainable Time Series Forecasting](protots_learning_hierarchical_prototypes_for_explainable_time_series_forecasting.md)**

:   提出 ProtoTS，通过层级原型学习实现可解释时间序列预测：少量粗粒度原型提供全局模式概览，逐级细分捕捉局部变化，结合多通道嵌入与瓶颈融合处理异质外生变量。在 LOF 数据集上 MSE 降低 48.3%，MAE 降低 20.9%，且支持专家编辑原型以进一步提升性能。

**[Skip to the Good Part: Representation Structure & Inference-Time Layer Skipping in Diffusion vs. Autoregressive LLMs](skip_to_the_good_part_representation_structure_inference-time_layer_skipping_in_.md)**

:   首次系统比较扩散语言模型（dLLM）和自回归模型（AR LLM）的层间表征结构，发现原生 dLLM 具有更强的层级抽象和早期层冗余性，据此提出静态、任务无关的推理时层跳过策略，在 LLaDA 上跳过 6 层（18.75% FLOPs 削减）仍保持 90%+ 性能。

**[Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerabilities](toward_safer_diffusion_language_models_discovery_and_mitigation_of_priming_vulne.md)**

:   揭示了掩码扩散语言模型（MDLM）中的"启动漏洞"（priming vulnerability）——在去噪中间步骤注入肯定性 token 可绕过安全防线，并提出 Recovery Alignment（RA）方法训练模型从被污染的中间状态恢复到安全响应。

**[wd1: Weighted Policy Optimization for Reasoning in Diffusion Language Models](wd1_weighted_policy_optimization_for_reasoning_in_diffusion_language_models.md)**

:   提出 wd1，一种无需策略比率（ratio-free）的加权对数似然策略优化方法用于扩散语言模型（dLLM）的 RL 微调，通过正样本加权和负样本惩罚避免了 GRPO 中策略比率估计的偏差和高方差问题，在 LLaDA-8B 上实现了 Sudoku +59%、GSM8K 84.5% 的 SOTA 性能。
