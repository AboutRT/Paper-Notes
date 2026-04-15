---
title: >-
  CVPR2025 文本生成方向 2篇论文解读
description: >-
  2篇CVPR2025 文本生成方向论文深度解读，每篇5分钟读懂核心思想。每篇笔记含一句话总结、背景动机、方法详解、实验数据、亮点洞察与局限性分析。
---

<!-- 由 src/gen_blog_index.py 自动生成 -->
# ✍️ 文本生成

**📷 CVPR2025** · **2** 篇论文解读

**[Artformer Controllable Generation Of Diverse 3D Articulated Objects](artformer_controllable_generation_of_diverse_3d_articulated_objects.md)**

:   提出ArtFormer框架，通过树结构参数化和条件扩散Shape Prior，从文本/图像描述生成高质量、多样化且运动学关系准确的3D关节物体，在生成质量和多样性上显著超越现有方法。

**[Lotusfilter Fast Diverse Nearest Neighbor Search Via A Learned Cutoff Table](lotusfilter_fast_diverse_nearest_neighbor_search_via_a_learned_cutoff_table.md)**

:   提出LotusFilter，通过离线预计算每个向量的邻近关系构建截断表(cutoff table)，在线阶段用贪心集合删除实现多样化过滤，将传统 $O(DS^2)$ 的多样化搜索降至 $O(T+S+KL)$，过滤仅需0.02ms/query，内存仅为传统方法的1/40。
