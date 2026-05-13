# 内审补充文献清单

内审意见要求补充 2025、2026 年近两年文献。建议按第一章三个综述部分分散加入，每部分 3--4 篇，不集中堆在一个段落。

## 一、计及不确定性的健康状态估计

建议优先补充以下 4 篇。它们可支撑真实车辆工况、多模态 SOH 估计、车载健康评估、早期退化预测和部分充电数据下的可靠估计。

1. `liu2025multimodal_soh`
   - Nature Communications, 2025
   - 适合位置：数据驱动 SOH 估计模型小节，强调真实车辆开放数据、多模态健康指标和复杂工况 SOH 估计。

2. `che2025diagnostic_free`
   - Joule, 2025
   - 适合位置：物理约束/车载健康评估相关段落，强调无需专门诊断工况的 onboard battery health assessment。

3. `hu2026batterygpt`
   - Nature Communications, 2026
   - 适合位置：数据驱动估计模型或小节末尾趋势段，强调 GPT/Transformer 用于早期 SOH、膝点和 EOL 预测。

4. `li2026fourier_lstm`
   - Journal of Energy Storage, 2026
   - 适合位置：数据驱动 SOH 估计模型小节，强调部分充电数据、频域先验和可解释性。

```bibtex
@article{liu2025multimodal_soh,
  author  = {Liu, Hongao and Li, Chang and Hu, Xiaosong and Li, Jinwen and Zhang, Kai and Xie, Yang and Wu, Ranglei and Song, Ziyou},
  title   = {Multi-modal framework for battery state of health evaluation using open-source electric vehicle data},
  journal = {Nature Communications},
  year    = {2025},
  volume  = {16},
  pages   = {1137},
  doi     = {10.1038/s41467-025-56485-7},
}

@article{che2025diagnostic_free,
  author  = {Che, Yunhong and Lam, Vivek N. and Rhyu, Jinwook and Schaeffer, Joachim and Kim, Minsu and Bazant, Martin Z. and Chueh, William C. and Braatz, Richard D.},
  title   = {Diagnostic-free onboard battery health assessment},
  journal = {Joule},
  year    = {2025},
  volume  = {9},
  number  = {8},
  pages   = {102010},
  doi     = {10.1016/j.joule.2025.102010},
}

@article{hu2026batterygpt,
  author  = {Hu, Jincheng and Fu, Pengyu and Wei, Zhongbao and Huang, Yanjun and Early, Juliana and Fly, Ashley and Zhang, Yuanjian},
  title   = {Early prediction of lithium-ion battery degradation with a generative pre-trained transformer},
  journal = {Nature Communications},
  year    = {2026},
  volume  = {17},
  pages   = {126},
  doi     = {10.1038/s41467-025-66819-0},
}

@article{li2026fourier_lstm,
  author  = {Li, Tianfu and He, Jiang and Liu, Tao and Wang, Fujin and Zhao, Zhibin and Che, Yunhong},
  title   = {A novel Fourier-informed long short-term memory network for reliable state of health estimation of lithium-ion batteries with partial charging data},
  journal = {Journal of Energy Storage},
  year    = {2026},
  volume  = {154},
  pages   = {121177},
  doi     = {10.1016/j.est.2026.121177},
}
```

## 二、面向分布漂移的退化建模

建议优先补充以下 4 篇。它们覆盖跨老化条件寿命预测、少实验/零样本寿命预测、跨材料 EIS 迁移估计和物理-神经网络融合 PHM。

1. `zhang2025batlinet`
   - Nature Machine Intelligence, 2025
   - 适合位置：面向分布漂移的退化建模小节，强调跨循环协议、温度、材料体系的寿命泛化预测。

2. `zhang2026discovery_learning`
   - Nature, 2026
   - 适合位置：退化建模小节末尾趋势段，强调 Discovery Learning、主动学习、物理引导和 zero-shot 预测。

3. `zhou2026eis_dada`
   - Journal of Energy Storage, 2026
   - 适合位置：域适应/迁移学习段落，强调跨材料、跨 SOH 的 EIS 物理特征和双重分布对齐。

4. `wang2026phynet_review`
   - Engineering Applications of Artificial Intelligence, 2026
   - 适合位置：物理知识和神经网络融合的综述性过渡段，支撑物理先验与数据驱动退化建模融合趋势。

```bibtex
@article{zhang2025batlinet,
  author  = {Zhang, Han and Li, Yuqi and Zheng, Shun and Lu, Ziheng and Gui, Xiaofan and Xu, Wei and Bian, Jiang},
  title   = {Battery lifetime prediction across diverse ageing conditions with inter-cell deep learning},
  journal = {Nature Machine Intelligence},
  year    = {2025},
  volume  = {7},
  pages   = {270--277},
  doi     = {10.1038/s42256-024-00972-x},
}

@article{zhang2026discovery_learning,
  author  = {Zhang, Jiawei and Zhang, Yifei and Yi, Baozhao and Ren, Yao and Jiao, Qi and Bai, Hanyu and Jiang, Weiran and Song, Ziyou},
  title   = {Discovery Learning predicts battery cycle life from minimal experiments},
  journal = {Nature},
  year    = {2026},
  volume  = {650},
  pages   = {110--115},
  doi     = {10.1038/s41586-025-09951-7},
}

@article{zhou2026eis_dada,
  author  = {Zhou, Xinye and Xu, Jiaxiu and Sun, Yiguo and Yuan, Hongming and Feng, Mingqi and Wang, Fujin and Zhao, Zhibin},
  title   = {{EIS-DADA}: A transferable approach for state of charge estimation in lithium-ion batteries based on impedance spectroscopy},
  journal = {Journal of Energy Storage},
  year    = {2026},
  volume  = {154},
  pages   = {121188},
  doi     = {10.1016/j.est.2026.121188},
}

@article{wang2026phynet_review,
  author  = {Wang, Fujin and Liu, Weiyuan and Sun, Meng and Zhai, Zhi and Zhao, Zhibin and Chen, Xuefeng},
  title   = {Merging physics and neural network: A promising tool for prognostics and health management},
  journal = {Engineering Applications of Artificial Intelligence},
  year    = {2026},
  volume  = {165},
  pages   = {113385},
  doi     = {10.1016/j.engappai.2025.113385},
}
```

## 三、幻觉鲁棒的旋转机械故障诊断

第三部分建议改为以下候选。相比普通 Transformer/多模态诊断论文，这些文献更贴近“大模型、LLM、多模态大模型、信号到文本、知识图谱推理、诊断报告生成”等主题。

1. `bi2025drsc`
   - IEEE Internet of Things Journal, 2025
   - 已在 `Biblio/ref.bib` 中，对应 key 为 `10944708`。适合保留，用于支撑跨域和类别不平衡旋转机械诊断。

2. `yu2026lmm_fd`
   - Journal of Industrial Information Integration, 2026
   - 更推荐。大模型 + 多模态机械故障诊断，包含知识图谱、跨模态对齐、文本诊断报告和零样本泛化。

3. `lai2026fr_llm`
   - Reliability Engineering & System Safety, 2026
   - 更推荐。LLM 同时处理故障诊断和 RUL 预测，信号到文本编码，和你的诊断/PHM 叙事贴合。

4. `lin2026moe_llm`
   - Advanced Engineering Informatics, 2026
   - 可选。MoE-LLM 多传感器柔性融合，直接面向旋转机械故障诊断。

5. `di2026spacehmchat`
   - arXiv, 2026
   - 你已确认质量较好。它不是期刊论文，但适合在第三部分作为“人机协同闭环健康管理大模型”的补充引用，建议不要替代期刊论文，而是作为趋势性引用。

```bibtex
@article{bi2025drsc,
  author  = {Bi, Yuanguo and Fu, Rao and Jiang, Cunyu and Zhang, Xiaoling and Li, Fengyun and Zhao, Liang and Han, Guangjie},
  title   = {{DRSC}: Dual-Reweighted Siamese Contrastive Learning Network for Cross-Domain Rotating Machinery Fault Diagnosis With Multisource Domain Imbalanced Data},
  journal = {IEEE Internet of Things Journal},
  year    = {2025},
  volume  = {12},
  number  = {13},
  pages   = {23678--23693},
  doi     = {10.1109/JIOT.2025.3555688},
}

@article{yu2026lmm_fd,
  author  = {Yu, Shupeng and Li, Xiang and Lei, Yaguo and Yang, Bin and Li, Naipeng and Feng, Ke},
  title   = {Multimodal data-enabled large model for machine fault diagnosis towards intelligent operation and maintenance},
  journal = {Journal of Industrial Information Integration},
  year    = {2026},
  volume  = {50},
  pages   = {101061},
  doi     = {10.1016/j.jii.2026.101061},
}

@article{lai2026fr_llm,
  author  = {Lai, Yuming and Wu, Zhangjun and Chen, Mengyao and Liu, Chao and Shao, Haidong},
  title   = {{FR-LLM}: Multi-task large language model with signal-to-text encoding and adaptive optimization for joint fault diagnosis and {RUL} prediction},
  journal = {Reliability Engineering \& System Safety},
  year    = {2026},
  volume  = {269},
  pages   = {112091},
  doi     = {10.1016/j.ress.2025.112091},
}

@article{lin2026moe_llm,
  author  = {Lin, Tantao and Ren, Zhijun and Huang, Kai and Karimi, Hamid Reza and Zhu, Yongsheng and Feng, Ke and Hong, Jun},
  title   = {A {MoE-LLM}-based multisensor flexible fusion fault diagnosis method for rotating machinery},
  journal = {Advanced Engineering Informatics},
  year    = {2026},
  volume  = {69},
  pages   = {104009},
  doi     = {10.1016/j.aei.2025.104009},
}

@misc{di2026spacehmchat,
  author       = {Di, Yi and Zhao, Zhibin and Wang, Fujin and Liu, Xue and Tang, Jiafeng and Ren, Jiaxin and Zhai, Zhi and Chen, Xuefeng},
  title        = {Empowering All-in-Loop Health Management of Spacecraft Power System in the Mega-Constellation Era via Human-AI Collaboration},
  year         = {2026},
  eprint       = {2601.12667},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi          = {10.48550/arXiv.2601.12667},
}
```
