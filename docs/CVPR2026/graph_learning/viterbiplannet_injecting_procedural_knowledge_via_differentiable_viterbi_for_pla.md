# ViterbiPlanNet: Injecting Procedural Knowledge via Differentiable Viterbi for Planning in Instructional Videos

**会议**: CVPR 2026  
**arXiv**: [2603.04265](https://arxiv.org/abs/2603.04265)  
**代码**: [Project](https://gigi-g.github.io/ViterbiPlanNet/)  
**领域**: 图学习  
**关键词**: 过程规划, 可微Viterbi, 过程知识图, 教学视频, 动态规划

## 一句话总结

通过可微 Viterbi 层将过程知识图端到端集成到视频过程规划中，神经网络只学发射概率，参数量比扩散/LLM规划器少一个数量级

## 研究背景与动机

过程规划：给定初始和目标视觉状态预测动作序列。现有方法隐式学习过程结构计算昂贵。关键思想：Viterbi中max/argmax→平滑松弛使其可微，PKG嵌入训练过程

## 方法详解

### 整体框架

视觉编码→发射概率计算→可微Viterbi层(PKG参数化)→软计划输出

### 关键设计

1. PKG构建：有向图节点=动作边=转移，权重=共现统计
2. 可微Viterbi层(DVL)：softmax近似max，soft argmax近似argmax，无额外参数
3. 梯度从计划损失流回视觉编码器

### 损失函数 / 训练策略

多目标联合优化，平衡各组件贡献。详见各模块描述。

## 实验关键数据

### 主实验与关键发现

CrossTask/COIN/NIV全部SOTA，参数量减少一个数量级。端到端训练>>后处理Viterbi

## 亮点与洞察

简洁深刻：让网络只学发射概率结构由图保证；参数极少；统一评估基准开源

## 局限性 / 可改进方向

PKG质量受数据限制；仅离散动作；软近似长序列精度可能下降

## 相关工作与启发

在现有方法基础上的重要改进，所提技术路线可推广到相关任务。

## 评分

- 新颖性: ⭐⭐⭐⭐⭐
- 实验充分度: ⭐⭐⭐⭐⭐
- 写作质量: ⭐⭐⭐⭐⭐
- 价值: ⭐⭐⭐⭐⭐
