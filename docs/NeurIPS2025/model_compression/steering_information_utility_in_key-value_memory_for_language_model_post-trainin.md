# Steering Information Utility in Key-Value Memory for Language Model Post-Training

**会议**: NeurIPS 2025  
**arXiv**: [2507.05158](https://arxiv.org/abs/2507.05158)  
**代码**: https://github.com/chili-lab/InfoSteer  
**领域**: 模型压缩  
**关键词**: 后训练优化, FFN记忆向量, 信息利用, 键分布, 知识蒸馏

## 一句话总结
提出 InfoSteer，通过前向传播干预和反向传播正则化来促进 FFN 键值记忆中低活跃记忆向量的利用，使预训练知识在后训练阶段被更充分使用，在 Qwen/LLaMA/Gemma 上 15 个任务一致提升。

## 研究背景与动机
1. **领域现状**：LLM 训练流程标准化为预训练+后训练两阶段，预训练阶段注入知识，后训练（SFT）对齐和精化
2. **现有痛点**：标准 SFT 没有显式机制鼓励模型利用预训练中学到的参数化知识。例如 Gemma-2-9B 基础模型 HellaSwag 90.1%，InfoSteer 后达 95.7%，说明大量知识被"浪费"了
3. **核心 idea**：将 FFN 视为键值记忆——key coefficient 控制哪些 value（记忆向量）被激活。通过提高 key 分布的熵来激活更多记忆向量

## 方法详解

### 关键设计
1. **干预方法（Forward）**：找到每层 key coefficient 最小的 p%（默认 0.01%），将其提升至层均值的 α 倍：$k_s^{(l)} \leftarrow \alpha \cdot \frac{1}{d_m}\sum_i k_i^{(l)}$
2. **正则化方法（Backward）**：在损失中加入 key 分布的熵正则：$\mathcal{L} = \mathcal{L}_{LM} - \lambda \sum_{l=1}^L H(\hat{\mathbf{k}}^{(l)})$，$\lambda=0.01$
3. **信息代理（Fine-grained）**：将记忆向量 $v_i$ 通过解码头映射为 logits $\phi_i = v_i \cdot W_{decode}$，分析其语义特异性（低熵=高特异性知识）
4. **SwiGLU 适配**：对 SwiGLU 型 MLP，key coefficient 为 $\sigma(hW_{gate}) \odot (hW_{up})$

## 实验关键数据

### 主实验 — ID 评估

| 模型 | 方法 | HellaSwag | ARC-c | 平均9任务 |
|------|------|-----------|-------|----------|
| Gemma-2-9B | base | 90.1 | 69.2 | - |
| | vanilla SFT | 93.8 | 72.5 | - |
| | +InfoSteer | **95.7 (+5.6)** | **74.8 (+5.6)** | 显著提升 |
| LLaMA-3-8B | base | 79.3 | 55.0 | - |
| | +InfoSteer | **84.8 (+5.5)** | **58.7** | 全面提升 |

### OOD 评估 — 仅在 GSM8K 训练，测试其他算术数据集
- InfoSteer 在 6 个 OOD 数据集上一致优于 vanilla SFT，泛化能力更强

### 关键发现
- 被引导的 LM 自适应地分配信息：对语义丰富 Token 投入更多资源，对简单过渡词（逗号、and）投入更少
- 干预和正则化方法效果相当，可根据场景选择

## 亮点与洞察
- **"预训练知识未被充分利用"**这个发现本身就有重大启示——SFT 不等于知识利用
- 将 FFN 作为键值记忆来操控是一种优雅的可解释干预方式
- 方法极轻量，不增加模型参数，不改变架构

## 局限性
- 细粒度引导（基于语义特异性分析）仅带来边际改进，未充分发挥潜力
- 理论上 key 分布高熵不一定总是好的——某些任务可能需要稀疏激活

## 评分
- 新颖性: ⭐⭐⭐⭐ FFN 键值记忆引导是新视角
- 实验充分度: ⭐⭐⭐⭐⭐ 6个模型/15个任务/ID+OOD
- 写作质量: ⭐⭐⭐⭐ 方法直觉清晰
- 价值: ⭐⭐⭐⭐ 立即可用的 SFT 改进方案
