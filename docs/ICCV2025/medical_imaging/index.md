<!-- 由 src/gen_blog_index.py 自动生成 -->
# 🏥 医学图像

**📹 ICCV2025** · 共 **16** 篇

**[AcZeroTS: Active Learning for Zero-shot Tissue Segmentation in Pathology Images](aczerots_active_learning_for_zeroshot_tissue_segmentation_in.md)**

:   提出AcZeroTS框架，将主动学习与基于VLM的原型引导零样本分割模型ProZS结合，通过同时考虑不确定性、多样性和原型覆盖unseen类的能力来选择最有价值的标注样本，以最少标注实现seen和unseen组织类型的高质量分割。

**[Alleviating Textual Reliance in Medical Language-guided Segmentation via Prototype-driven Semantic Approximation](alleviating_textual_reliance_in_medical_language-guided_segmentation_via_prototy.md)**

:   提出ProLearn框架，首次通过原型驱动的语义近似（PSA）模块从根本上缓解医学语言引导分割对文本的依赖——仅需少量图文配对数据初始化原型空间，训练和推理均可无文本输入，在1%文本可用性下仍保持强劲性能（QaTa-COV19 Dice=0.857），且参数量比LLM方案减少1000倍，推理速度快100倍。

**[An OpenMind for 3D Medical Vision Self-Supervised Learning](an_openmind_for_3d_medical_vision_self-supervised_learning.md)**

:   发布了最大的公开 3D 医学影像预训练数据集 OpenMind（114k 脑部 MRI），并系统性地对比了多种 3D 自监督学习方法在 CNN（ResEnc-L）和 Transformer（Primus-M）上的表现，证明 MAE 预训练在分割任务上最优、对比学习在分类任务上最优，且首次展示预训练 Transformer 可在部分数据集上超越从头训练的 CNN。

**[An OpenMind for 3D Medical Vision Self-supervised Learning](an_openmind_for_3d_medical_vision_selfsupervised_learning.md)**

:   发布了最大的公开3D医学影像预训练数据集OpenMind（114k脑MRI体积），并在该数据集上系统性benchmark了现有3D SSL方法在最先进CNN（ResEnc-L）和Transformer（Primus-M）架构上的表现，明确了3D医学图像SSL的当前SOTA。

**[Beyond Brain Decoding: Visual-Semantic Reconstructions to Mental Creation Extension Based on fMRI](beyond_brain_decoding_visualsemantic_reconstructions_to_ment.md)**

:   提出NeuroCreat——一种结合LLM视觉与文本能力的脑多模态架构，将fMRI解码从单一的视觉刺激重建扩展到**图像重建 + 文本描述（captioning）+ 心理创造（creation）**三个层次，通过Prompt Variant Alignment模块有效弥合fMRI低分辨率信号与高级语义表征之间的鸿沟。

**[Boosting Vision Semantic Density with Anatomy Normality Modeling for Medical Vision-language Pre-training](boosting_vision_semantic_density_with_anatomy_normality_mode.md)**

:   提出 ViSD-Boost，通过疾病级视觉对比学习增强视觉语义 + VQ-VAE 建模解剖正常性分布来放大异常信号，解决医学 VLP 中视觉语义密度低导致的对齐偏差，在腹部 CT 54 种疾病零样本诊断达到 84.9% AUC。

**[Boosting Vision Semantic Density with Anatomy Normality Modeling for Medical Vision-language Pre-training](boosting_vision_semantic_density_with_anatomy_normality_modeling_for_medical_vis.md)**

:   提出 ViSD-Boost 方法，通过疾病级视觉对比学习增强视觉语义、以及基于 VQ-VAE 的解剖正常性建模来放大异常信号，解决医学视觉语言预训练中视觉模态语义密度低导致的对齐偏差问题，在 15 个器官 54 种疾病的零样本诊断上达到 84.9% AUC。

**[COIN: Confidence Score-Guided Distillation for Annotation-Free Cell Segmentation](coin_confidence_score-guided_distillation_for_annotation-free_cell_segmentation.md)**

:   提出COIN框架，通过无监督语义分割+最优传输的像素级细胞传播、基于模型-SAM一致性的实例级置信度评分、以及置信度引导的递归自蒸馏三步策略，解决了无标注细胞实例分割中"无错误实例缺失"的关键问题，在MoNuSeg和TNBC上超越半监督/弱监督方法。

**[Controllable Latent Space Augmentation for Digital Pathology](controllable_latent_space_augmentation_for_digital_pathology.md)**

:   提出HistAug——一种基于Transformer的轻量级潜在空间增强模型，通过条件式跨注意力机制在特征空间中模拟真实图像变换（色相、腐蚀等），以极低计算开销为病理MIL训练提供可控且高效的数据增强。

**[CryoFastAR: Fast Cryo-EM Ab initio Reconstruction Made Easy](cryofastar_fast_cryoem_ab_initio_reconstruction_made_easy.md)**

:   首个将DUSt3R式的几何基础模型范式引入冷冻电镜(cryo-EM)领域的工作，通过ViT编码器+跨视图注意力解码器直接从大量含噪粒子图像前馈预测姿态（无需迭代优化），实现了比传统方法快10-33倍的ab initio蛋白质三维重建。

**[CuMPerLay: Learning Cubical Multiparameter Persistence Vectorizations](cumperlay_learning_cubical_multiparameter_persistence_vectorizations.md)**

:   提出 CuMPerLay，一个可微的立方多参数持久同调 (Cubical Multiparameter Persistence, CMP) 向量化层，将 CMP 分解为多条可学习的单参数持久同调线，通过联合学习双滤过 (bifiltration) 函数实现端到端训练，嵌入 Swin Transformer 后在医学图像分类和语义分割任务上（尤其小数据场景）取得显著提升。

**[RadGPT: Constructing 3D Image-Text Tumor Datasets](radgpt_constructing_3d_image-text_tumor_datasets.md)**

:   本文提出 RadGPT——一个解剖感知的 VL AI 管线，通过将放射科医师修订的肿瘤分割 mask 经由确定性算法转化为结构化报告、再由 LLM 适配为叙述性报告，构建了首个大规模公开腹部 CT 图文肿瘤数据集 AbdomenAtlas 3.0（9,262 例 CT、每体素标注 + 报告），并证明分割辅助可显著提升 AI 报告中的肿瘤检测率。

**[SegAnyPET: Universal Promptable Segmentation from Positron Emission Tomography Images](seganypet_universal_promptable_segmentation_from_positron_emission_tomography_im.md)**

:   本文构建了迄今最大的PET分割数据集PETS-5k（5731例3D全身PET图像，超130万张2D切片），并提出SegAnyPET——首个针对PET影像的3D可提示分割基础模型，通过跨提示置信学习（CPCL）策略处理标注质量不一致问题，在已见和未见目标上均大幅超越现有基础模型和任务专用模型。

**[Toward Long-Tailed Online Anomaly Detection through Class-Agnostic Concepts](toward_long-tailed_online_anomaly_detection_through_class-agnostic_concepts.md)**

:   本文提出长尾在线异常检测（LTOAD）新任务和benchmark，核心创新是用可学习的"类无关概念集"替代传统的类标签依赖，结合Concept VQ-VAE和综合prompt学习框架，在不需要类标签的情况下于offline和online场景下均达到SOTA。

**[Vector Contrastive Learning for Pixel-wise Pretraining in Medical Vision](vector_contrastive_learning_for_pixel-wise_pretraining_in_medical_vision.md)**

:   提出向量对比学习（Vector CL），将标准对比学习从二值优化问题重新表述为向量回归问题，通过建模特征距离来量化分散程度，解决像素级医学视觉预训练中的"过度分散"问题，在 8 个下游任务上显著优于 17 种方法。

**[Visual Surface Wave Elastography: Revealing Subsurface Physical Properties via Visible Surface Waves](visual_surface_wave_elastography_revealing_subsurface_physical_properties_via_vi.md)**

:   本文提出 VSWE（Visual Surface Wave Elastography），仅通过一段表面波传播的视频，提取色散关系并结合基于物理的有限元优化，推断介质的亚表面厚度和刚度参数，在模拟和真实明胶实验中均实现了高精度的参数恢复，为居家健康监测提供了概念验证。
