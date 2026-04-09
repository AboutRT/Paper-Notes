<!-- 由 src/gen_blog_index.py 自动生成 -->
# ⚡ LLM 效率

**📹 ICCV2025** · 共 **3** 篇

**[ArgoTweak: Towards Self-Updating HD Maps through Structured Priors](argotweak_towards_self-updating_hd_maps_through_structured_priors.md)**

:   提出 ArgoTweak，首个提供"旧地图先验 + 当前传感器数据 + 最新真值地图"完整三元组的 HD 地图数据集，通过双射映射框架将大规模地图修改分解为元素级原子变化，并引入可解释的评测指标（mAPC/mACC），将模型在 ArgoTweak 上训练后的 sim2real 差距降低 10 倍以上。

**[LayerTracer: Cognitive-Aligned Layered SVG Synthesis via Diffusion Transformer](layertracer_cognitive-aligned_layered_svg_synthesis_via_diffusion_transformer.md)**

:   LayerTracer 提出首个基于 Diffusion Transformer（DiT）的认知对齐分层 SVG 生成框架：通过构建 2 万+ 设计师操作序列数据集，训练 DiT 生成模拟设计师工作流程的多阶段光栅化蓝图，再通过逐层矢量化和路径去重转换为干净可编辑的分层 SVG；同时支持文本驱动生成和图像到分层 SVG 的转换。

**[StreamMind: Unlocking Full Frame Rate Streaming Video Dialogue through Event-Gated Cognition](streammind_unlocking_full_frame_rate_streaming_video_dialogue_through_event-gate.md)**

:   StreamMind 提出"事件门控 LLM 调用"范式替代现有的"逐帧 LLM 调用"，通过在视频编码器和 LLM 之间插入认知门控网络（Cognition Gate），仅在查询相关事件发生时才调用 LLM，配合基于状态空间方法的事件保持特征提取器（EPFE）实现常量感知成本，在单张 A100 上达到 **100 fps** 的流式视频处理速度。
