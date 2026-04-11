<!-- 由 src/gen_blog_index.py 自动生成 -->
# 💬 LLM / NLP

**📹 ICCV2025** · 共 **10** 篇

**[A Conditional Probability Framework for Compositional Zero-shot Learning](a_conditional_probability_framework_for_compositional_zero-shot_learning.md)**

:   本文提出条件概率框架CPF，将组合零样本学习中的组合似然分解为物体似然和条件属性似然，通过文本增强的物体学习和物体引导的属性学习模块显式建模属性-物体的语义约束和上下文依赖，在UT-Zappos50K上AUC提升17.9%，在MIT-States上Unseen Accuracy提升5.5%。

**[A Conditional Probability Framework for Compositional Zero-shot Learning](a_conditional_probability_framework_for_compositional_zerosh.md)**

:   提出条件概率框架（CPF），将组合识别概率分解为对象似然 p(o|x) 和属性条件似然 p(a|o,x) 两部分，通过文本增强对象学习和对象引导属性学习两个模块显式建模属性-对象依赖关系，在三个 CZSL 基准上全面超越 SOTA。

**[Any-SSR: How Recursive Least Squares Works in Continual Learning of Large Language Models](any-ssr_how_recursive_least_squares_works_in_continual_learning_of_large_languag.md)**

:   提出Analytic Subspace Routing（Any-SSR）框架，通过为每个任务分配独立的LoRA子空间消除任务间干扰，并利用递归最小二乘（RLS）闭式解训练一个零遗忘的解析路由器，实现LLM的无回放持续学习。

**[BATCLIP: Bimodal Online Test-Time Adaptation for CLIP](batclip_bimodal_online_test-time_adaptation_for_clip.md)**

:   提出BATCLIP，一种针对CLIP的双模态在线测试时自适应（TTA）方法，通过同时适应视觉编码器和文本编码器的LayerNorm参数，引入投影匹配损失和类间可分性损失来增强图文特征对齐和类别区分度，在CIFAR-10C/100C/ImageNet-C上达到SOTA效果。

**[ChartCap: Mitigating Hallucination of Dense Chart Captioning](chartcap_mitigating_hallucination_of_dense_chart_captioning.md)**

:   构建了包含56.5万张真实图表-描述对的大规模数据集ChartCap，通过类型特定的描述模式排除无关信息、强调结构与关键洞察，并提出无参考的Visual Consistency Score评估指标，有效减少VLM在图表描述中的幻觉问题。

**[Decouple and Track: Benchmarking and Improving Video Diffusion Transformers for Motion Transfer](decouple_and_track_benchmarking_and_improving_video_diffusion_transformers_for_m.md)**

:   针对 DiT 模型中 3D 全注意力机制导致的运动-外观难以解耦问题，提出共享时序核（Shared Temporal Kernel）和稠密点跟踪损失（Dense Point Tracking Loss），同时建立了更全面的运动迁移基准 MTBench 和混合运动保真度指标。

**[ETA: Energy-based Test-time Adaptation for Depth Completion](eta_energy-based_test-time_adaptation_for_depth_completion.md)**

:   提出ETA方法，利用能量模型量化深度预测属于源域分布的可能性，并在测试时通过最小化目标域预测的能量值来引导预训练深度补全模型适配到新环境，在室外和室内场景平均比先前SOTA分别提升6.94%和10.23%。

**[Make Your Training Flexible: Towards Deployment-Efficient Video Models](make_your_training_flexible_towards_deployment-efficient_video_models.md)**

:   本文提出Flux——一种使视频模型训练灵活化的数据增强工具，通过灵活采样网格+组动态token选择，使单一模型在不同计算预算下都能高效工作；并提出Token Optimization新测试范式，在1/4 token下即可匹配前SOTA性能，节省约90%计算。

**[SVTRv2: CTC Beats Encoder-Decoder Models in Scene Text Recognition](svtrv2_ctc_beats_encoder-decoder_models_in_scene_text_recognition.md)**

:   提出 SVTRv2，通过多尺寸resize策略（MSR）、特征重排模块（FRM）和语义引导模块（SGM）三大设计，让 CTC 模型首次在多场景基准上全面超越编码器-解码器方法，同时保持推理速度优势。

**[Zeroth-Order Fine-Tuning of LLMs in Random Subspaces](zeroth-order_fine-tuning_of_llms_in_random_subspaces.md)**

:   提出 SubZero（random Subspace Zeroth-order），通过逐层低秩扰动在随机子空间中估计梯度，显著降低零阶优化的梯度方差和角度误差，以接近推理的内存开销实现 LLM 的高效微调。
