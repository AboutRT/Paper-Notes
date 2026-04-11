<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**📷 CVPR2026** · 共 **7** 篇

**[Composing Concepts from Images and Videos via Concept-prompt Binding](composing_concepts_from_images_and_videos_via_concept-prompt_binding.md)**

:   提出 Bind & Compose (BiCo)，一种one-shot方法，通过层次化binder结构将视觉概念绑定到prompt token，并通过token组合实现图像-视频概念的灵活组合，在概念一致性、prompt保真度和运动质量上全面超越前作。

**[GUIDE: Guided Updates for In-context Decision Evolution in LLM-Driven Spacecraft Operations](guide_guided_updates_for_in-context_decision_evolution_in_llm-driven_spacecraft_.md)**

:   提出GUIDE框架，利用LLM的in-context学习能力为航天器自主操作提供引导式决策进化，通过结构化的上下文信息和反馈机制让LLM在无需微调的情况下逐步改善航天任务规划和故障诊断决策的质量。

**[IAPL: Generalizable AI-Generated Image Detection via Image-Adaptive Prompt Learning](iapl_aigenerated_image_detection_adaptive_prompt.md)**

:   针对 AI 生成图像检测中现有方法难以泛化到未见生成器的问题，提出图像自适应提示学习（IAPL），在推理时根据每张测试图像动态调整输入到视觉编码器的 prompt——通过条件信息学习器提取伪造特征条件和测试时自适应 token 优化，在 UniversalFakeDetect 和 GenImage 数据集上分别达到 95.61% 和 96.7% 的 SOTA 平均准确率。

**[PhysVid: Physics Aware Local Conditioning for Generative Video](physvid_physics_aware_local_conditioning_for_generative_video_models.md)**

:   提出 PhysVid，一种物理感知的局部条件化方案——将视频分为时间片段（chunk），由 VLM 为每个 chunk 标注物理现象描述，通过 chunk 级交叉注意力注入生成模型；推理时引入"负物理提示"（反事实引导）引导生成远离物理违规，在 VideoPhy 上将物理常识分数提升约 33%。

**[SketchDeco: Training-Free Latent Composition for Precise Sketch Colourisation](sketchdeco_training-free_latent_composition_for_precise_sketch_colourisation.md)**

:   提出SketchDeco，一种无需训练的线稿上色方法，通过全局-局部两阶段策略将区域蒙版和调色板作为精确控制信号，利用扩散模型反演和自注意力注入在隐空间中实现区域精准着色与全局和谐过渡，在消费级GPU上15-20步即可完成。

**[WeaveTime: 流式视频LLM的帧级逐步记忆](weavetime_stream_from_earlier_frames_into_emergent_memory_in_videollms.md)**

:   诊断出Video-LLM的核心缺陷"时间无感"——把视频当无序图像集处理，产生时序模糊和历史/当前混淆两类失效，提出WeaveTime通过轻量时序重建目标获得顺序感知能力+Past-Current动态焦点缓存实现高效流式推理，在流式基准上一致提升。

**[WeaveTime: 流式视频LLM的帧级逐步记忆](weavetime_streaming_video_llm_memory.md)**

:   诊断出Video-LLM的核心缺陷"时间无感"——把视频当无序图像集处理，产生时序模糊和历史/当前混淆两类失效，提出WeaveTime通过轻量时序重建目标获得顺序感知能力+Past-Current动态焦点缓存实现高效流式推理，在流式基准上一致提升。
