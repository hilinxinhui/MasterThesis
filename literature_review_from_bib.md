# 文献综述汇总（来自 .bib 文件）

> **说明**：本文档从三篇论文的 .bib 文件中提取文献信息，包含准确的元信息（标题、作者、期刊、年份等）。
> **摘要字段留空**，供您后续自行添加。

---

## 统计信息

| 论文 | 引用数量 |
|------|----------|
| HSSTT | 19 |
| RODTNet | 19 |
| DA-TMLLM | 20 |
| **总计** | **58** |

---

## 第一部分：HSSTT 论文引用文献

基于物理模型和数据驱动的不确定性量化方法。

### [1] 7386653
- **标题**: Remaining Useful Life Prediction and Uncertainty Quantification of Proton Exchange Membrane Fuel Cell Under Variable Load
- **作者**: Bressel, Mathieu and Hilairet, Mickaël and Hissel, Daniel and Ould Bouamama, Belkacem
- **期刊**: IEEE Trans. Ind. Electron.
- **年份**: 2016
- **卷期**: 63 (4)
- **页码**: 2569-2577
- **DOI**: 10.1109/TIE.2016.2519328
- **摘要**: Although, the proton exchange membrane fuel cell is a promising clean and efficient energy converter that can be used to power an entire building in electricity and heat in a combined manner, it suffers from a limited lifespan due to degradation mechanisms. As a consequence, in the past years, researches have been conducted to estimate the state of health and now the remaining useful life (RUL) in order to extend the life of such devices. However, the developed methods are unable to perform prognostics with an online uncertainty quantification due to the computational cost. This paper aims at tackling this issue by proposing an observer-based prognostic algorithm. An extended Kalman filter estimates the actual state of health and the dynamic of the degradation with the associated uncertainty. An inverse first-order reliability method is used to extrapolate the state of health until a threshold is reached, for which the RUL is given with a 90% confidence interval. The global method is validated using a simulation model built from degradation data. Finally, the algorithm is tested on a dataset coming from a long-term experimental test on an eight-cell fuel cell stack subjected to a variable power profile.
- **论文中的描述**: Bressel et al. propose an extended Kalman filter-based algorithm integrated with the inverse first-order reliability method for SOH and RUL prediction, along with the corresponding confidence intervals.
<!-- 文献\cite{7386653}中，Bressel等人提出了一种基于观测器的预测方法，所提出的方法通过扩展卡尔曼滤波器（Extended Kalman Filter, EKF）建模设备的健康状态和退化动态，基于逆一阶可靠度方法（Inverse First-Order Reliability Method, IFORM）外推健康状态轨迹直至触发预设的失效阈值，从而实现对变功率负载工况下的质子交换膜燃料电池的剩余使用寿命预测，并给出90\%置信区间作为对预测结果的不确定性的量化。 -->

### [2] 9032349
- **标题**: A Novel Prognostics Approach Using Shifting Kernel Particle Filter of Li-Ion Batteries Under State Changes
- **作者**: Kim, Seokgoo and Park, Hyung Jun and Choi, Joo-Ho and Kwon, Daeil
- **期刊**: IEEE Trans. Ind. Electron.
- **年份**: 2021
- **卷期**: 68 (4)
- **页码**: 3485-3493
- **DOI**: 10.1109/TIE.2020.2978688
- **摘要**: Lithium-ion (Li-ion) batteries are used in various applications as the rechargeable power sources. The batteries undergo capacity fade during the repeated charge-discharge cycles, which eventually leads to the end of life (EOL). For the purpose of timely replacement before reaching the EOL, reliable prediction of the remaining useful life (RUL) during the cycles is of great importance. However, there may exist unhealthy batteries exhibiting the change of state at some cycles from those of normal degradation, which leads to their EOL sooner than expected. In this article, we propose a novel prognostic method using the particle filter (PF) that is capable of detecting the point of state change and adapting its algorithm to the new battery degradation pattern. The performance of the proposed method is demonstrated by the case study of Li-ion battery degradation data, comparing with the original PF algorithm. As a result, the proposed method shows better performance in terms of anomaly detection of degradation and adaptability to the new degradation process, which leads to more accurate and reliable RUL prediction.
- **论文中的描述**: Kim et al. propose a prognostic model utilizing a dynamic particle filter which quantifies the uncertainty associated with the battery's end-of-life and adaptively adjusts the parameters of the degradation model.
<!-- 文献\cite{9032349}中，Kim等人结合异常检测技术和基于粒子滤波（Particle Filter, PF）的预测方法提出了一种平移核粒子滤波（Shifting Kernel Particle Filter, SKPF）算法，解决了特定循环阶段带有异常退化轨迹的电池的突变特征辨识问题，实现了兼具精度和稳健性的剩余使用寿命预测，所提出方法同样给出预测结果的置信区间。 -->

### [3] 9113648
- **标题**: Sparse Kernel Ridge Regression Assisted Particle Filter Based Remaining Useful Life Estimation of Cascode GaN FET
- **作者**: Haque, Moinul Shahidul and Choi, Seungdeog
- **期刊**: IEEE Trans. Ind. Electron.
- **年份**: 2021
- **卷期**: 68 (8)
- **页码**: 7516-7525
- **DOI**: 10.1109/TIE.2020.3000126
- **摘要**: This article proposes a novel sparse kernel ridge regression assisted particle filter (SKRR-PF) based remaining useful life (RUL) estimation method to address the reliability of the cascode gallium nitride field-effect transistors in emerging power electronics systems. The proposed method will overcome three main challenges in this area: first, a large variation in the RUL estimation under the severe noise uncertainty; second, sample degeneracy and sample impoverishment; and third, the low capability of tracing the dynamic and abrupt change in the fault precursor trajectory. The state-of-the-art RUL estimation methods require a significant number of samples to address such issues, including particle degeneracy and sample impoverishment. Also, the state-of-the-art methods mostly fail to apply under a system's dynamic condition changes over a switch's lifetime. The proposed method will significantly enhance the estimation accuracy by introducing SKRR in resampling the posterior probability density function estimation, especially under the dynamically varying system's health condition due to the harsh industrial operation. Thus, the proposed method will offer fast tracing the sudden change in the RDS,ON trajectory, leading to a significant accurate RUL estimation. The performance of the proposed method has been rigorously validated through the purposely designed power cycling testbed.
- **论文中的描述**: Haque and Choi propose a prognostic model utilizing a sparse kernel ridge regression-assisted particle filter and quantifie abrupt changes in degradation trajectories by accounting for noise uncertainty.
<!-- 晶体管的可靠应用依赖剩余使用寿命预测，晶体管性能退化具有不确定性、突变性和样本贫化性，这与电池性能退化在数据表现上一致，文献\cite{9113648}中，Haque和Choi提出了一种稀疏核岭回归辅助的粒子滤波（Sparse Kernel Ridge Regression Assisted Particle Filter, SKRR-PF）算法，通过在后验概率密度函数估计的重采样环节引入稀疏核岭回归机制，实现了对晶体管器件导通电阻轨迹突变的识别和剩余使用寿命的预测。 -->

### [4] AHWIADI2022110817
- **标题**: An enhanced particle filter technology for battery system state estimation and RUL prediction
- **作者**: Mohamed Ahwiadi and Wilson Wang
- **期刊**: Measurement
- **年份**: 2022
- **卷期**: 191 ()
- **页码**: 
- **DOI**: https://doi.org/10.1016/j.measurement.2022.110817
- **摘要**: *(待添加)*
- **论文中的描述**: Ahwiadi and Wang propose an enhanced particle filter model based on evolutionary fuzzy predictors to mitigate sample degeneracy and impoverishment issues while achieving high-precision remaining useful life interval estimation.
<!-- 文献\cite{AHWIADI2022110817}中，Ahwiadi和Wang提出了一种增强型粒子滤波（Enhanced Particle Filter, EPF）框架，通过融合增强型粒子机制和演化模糊预测器（Evolving Fuzzy Predictor, EFP），克服基于传统PF方法进行电池系统状态估计和寿命预测时由权值退化和粒子多样性丧失导致的建模不确定性，从而实现准确且鲁棒的电池系统健康状态估计和剩余寿命预测。 -->

### [5] REZAEI2023107883
- **标题**: A fuzzy robust two-stage unscented Kalman filter method for uncertainty and state of charge estimation of lithium-ion batteries
- **作者**: Omid Rezaei and Ali Rahdan and Sohrab Sardari and Masoud Dahmardeh and Zhanle Wang
- **期刊**: J. Energy Storage
- **年份**: 2023
- **卷期**: 68 ()
- **页码**: 
- **DOI**: https://doi.org/10.1016/j.est.2023.107883
- **摘要**: *(待添加)*
- **论文中的描述**: Rezaei et al. develope a fuzzy robust two-stage unscented Kalman filter to estimate cycle capacity and quantify uncertainty in a phased manner using the noise covariance matrix.
<!-- 文献\cite{REZAEI2023107883}中，Rezaei~等人提出了一种模糊鲁棒两阶段无迹卡尔曼滤波器（Fuzzy Robust Two-Stage Unscented Kalman Filter, FRTSUKF），实现对缺乏先验统计特性的电池模型进行不确定性建模，其在第一阶段基于模糊推理系统剔除测量噪声，初步估计电池模型状态变量，在第二阶段进行不确定性量化，并基于量化结果补偿电池性能退化向状态变量引入的不确定性。 -->

### [6] 10385053
- **标题**: A Novel Robust Dual Unscented Particle Filter Method for Remaining Useful Life Prediction of Rolling Bearings
- **作者**: Cui, Lingli and Li, Wenjie and Liu, Dongdong and Wang, Huaqing
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2024
- **卷期**: 73 ()
- **页码**: 1-9
- **DOI**: 10.1109/TIM.2024.3351254
- **摘要**: It is still challenging to accurately predict the remaining useful life (RUL) of bearings with fluctuating degradation processes. To address this issue, this article proposes a novel robust dual unscented particle filter (DUPF) method for RUL prediction. First, a dual-stream unscented particle filter model is constructed to leverage the hidden degradation information at different time scales with different prediction models, which enhances model’s capability to track various fluctuating degradation trends. Second, a comprehensive fusion strategy is designed to adaptively optimize the weights of double streams, in which the maximum failure probability of dynamic Bayesian (DB) is quantitatively evaluated to improve the reliability of the prediction results. The proposed method is tested using two datasets and compared with several state-of-the-art methods. The results show that the proposed method can improve prediction accuracy and is robust to fluctuations in degradation processes.
- **论文中的描述**: Cui et al. design a prognostic model based on dual unscented particle filters to address uncertainties in dynamic degradation trajectories and achieve robust prediction.
<!-- 旋转机械设备维护过程同样存在状态估计和寿命预测需求，且设备性能退化行为与电池系统一致。文献\cite{10385053}中，Cui~等人提出了一种双无迹粒子滤波器（Dual Unscented Particle Filter, DUPF），通过集成双流异构模型并设计全局融合策略，实现跨时间尺度轴承退化特征，并通过显式量化动态贝叶斯最大失效概率提升了预测分布的统计可靠性。 -->

### [7] 10672556
- **标题**: Online Capacity Prediction of Lithium-Ion Batteries Based on Physics-Constrained Zonotopic Kalman Filter
- **作者**: Wang, Zhenhua and Zhao, Zhenwen and Zhou, Meng and Wang, Jing and Shen, Yi
- **期刊**: IEEE Trans. Reliab.
- **年份**: 2024
- **卷期**:  ()
- **页码**: 1-14
- **DOI**: 
- **摘要**: This article presents a novel physics-constrained zonotopic Kalman filter method for online capacity prediction of lithium-ion batteries. To describe capacity degradation, a state-space formulation is devised using the autoregressive model and an indirect representation of capacity. The approach consists of three steps: First, a zonotopic Kalman filter is proposed to estimate model parameters and parameter intervals. Subsequently, considering the capacity regeneration phenomenon, a physics-based constraint term is presented to optimize parameters, which updates the estimated model parameters obtained by the zonotopic Kalman filter. Finally, parameters and interval estimation are utilized to predict the future short-term capacity. The case study demonstrates the validity of our approach. Moreover, comparisons with the ellipsoid-based extended Kalman filter and predictive maintenance toolbox suggest that our approach can obtain more precise capacity prediction and tighter capacity interval results.
- **论文中的描述**: Wang et al. propose a zonotopic Kalman filter-based method with physics constraints to achieve online capacity interval estimation.
<!-- 文献\cite{10672556}中，为了实现电池在线容量估计，Wang~等人提出了一种物理约束中心对称多胞形卡尔曼滤波器（Physics-Constrained Zonotopic Kalman Filter, PCZKF），其中所提出的滤波器实现电池模型的参数及其区间估计的联合更新，所提出的物理约束则用于应对电池容量再生挑战，所提出的方法相比传统基于~KF~的方法能够输出更加精确容量预测轨迹和更加收敛的容量置信区间。 -->

### [8] rvr_rul_9552552
- **标题**: Multivariate relevance vector regression based degradation modeling and remaining useful life prediction
- **作者**: Wang, Xiuli and Jiang, Bin and Wu, Shaomin and Lu, Ningyun and Ding, Steven X.
- **期刊**: IEEE Trans. Ind. Electron.
- **年份**: 2022
- **卷期**: 69 (9)
- **页码**: 9514-9523
- **DOI**: 10.1109/TIE.2021.3114724
- **摘要**: *(待添加)*
- **论文中的描述**: Wang et al. introduce a prognostic method based on relevance vector regression (RVR).
<!-- 文献{rvr_rul_9552552}中，Wang~等人针对传统~RVR~方法局限于一维退化过程和单变量观测数据的问题，提出了一种基于动态多元相关向量回归（Dynamic Multivariate Relevance Vector Regression, DMRVR）的退化轨迹跟踪和剩余寿命预测框架，所提出方法考虑多元物理环境因素，构建多步回归架构以表征退化动力学，并依据RVR中间结果的矩阵分布基于加速梯度算法优化求解过程。 -->

### [9] gpr_soh_8263147
- **标题**: Gaussian process regression for in situ capacity estimation of lithium-ion batteries
- **作者**: Richardson, Robert R. and Birkl, Christoph R. and Osborne, Michael A. and Howey, David A.
- **期刊**: IEEE Trans. Ind. Inform.
- **年份**: 2019
- **卷期**: 15 (1)
- **页码**: 127-138
- **DOI**: 10.1109/TII.2018.2794997
- **摘要**: *(待添加)*
- **论文中的描述**: Richardson et al. employ Gaussian process regression (GPR) for SOH estimation.
<!-- 文献\cite{gpr_soh_8263147}中，Richardson~等人面向恒流充放电工况提出了一种基于高斯过程回归的原位容量数据驱动诊断方法（Gaussian Process Regression for \textit{In Situ} Capacity Estimation, GP-ICE），其在特定的电压窗口内，仅需提取短至十秒的连续恒流工况片段即可实现高精度电池健康状态估计。所提方法是一种贝叶斯非参数化回归方法，能够输出预测结果的不确定性作为对数据复杂性的表征。 -->

### [10] bbb_rul_9738999
- **标题**: A Bayesian mixture neural network for remaining useful life prediction of lithium-ion batteries
- **作者**: Zhang, Shuxin and Liu, Zhitao and Su, Hongye
- **期刊**: IEEE Trans. Transp. Electrif.
- **年份**: 2022
- **卷期**: 8 (4)
- **页码**: 4708-4721
- **DOI**: 10.1109/TTE.2022.3161140
- **摘要**: Remaining useful life (RUL) is one of the essential ingredients in the battery management system. However, due to the characteristic of the dynamic and time-varying electrochemical system with nonlinear and complicated internal mechanisms, the uncertainty of RUL estimation has been expanded, and it is difficult to give an accurate time to reach the end of life. This article proposes the Bayesian mixture neural network (BMNN), a probabilistic deep learning method, to obtain more accurate RUL prediction and provide uncertainty estimation, while the quasi-Gramian angular field (Q-GAF) beneficial to identify prior distribution is utilized to transform time-series sequence into temporal images. BMNN consists of the Bayesian convolutional neural network (BCNN) extracting features in temporal images and Bayesian long short-term memory (B-LSTM) learning correlation between retention capacity and other degradation inducements. After concatenating two terms, the variational Bayesian neural network outputs the distribution of prediction results. In the experimental stage, the performance of the proposed method is validated on four different lithium-ion battery datasets and demonstrates higher stability, lower uncertainty, and more accuracy than other methods.
- **论文中的描述**: Zhang et al. develop a Bayesian mixture neural network (BMNN) to capture the distribution of prediction results.
<!-- 文献\cite{bbb_rul_9738999}中，Zhang~等人提出了一种贝叶斯混合神经网络（Bayesian Mixture Neural Network, BMNN）以应对因内部反应非线性和高混杂性导致的剩余寿命预测不确定性大的问题。所提出网络引入准格雷姆角场（Quasi-Gramian Angular Field, Q-GAF）进行信号预处理以增强先验分布辨识能力，并融合贝叶斯卷积神经网络（Bayesian Convolutional Neural Network, BCNN）和贝叶斯长短期记忆网络（Bayesian Long Short-Term Memory Network, B-LSTM），由变分贝叶斯推断层输出预测结果的后验概率分布。 -->

### [11] capsnet_rul_li2024sensor
- **标题**: Sensor-aware CapsNet: Towards trustworthy multisensory fusion for remaining useful life prediction
- **作者**: Li, Dongpeng and Chen, Jiaxian and Huang, Ruyi and Chen, Zhuyun and Li, Weihua
- **期刊**: J. Manuf. Syst.
- **年份**: 2024
- **卷期**: 72 ()
- **页码**: 26-37
- **DOI**: 10.1016/j.jmsy.2023.11.009
- **摘要**: Multisensory data-driven remaining useful life (RUL) prediction based on deep learning techniques is gaining increasing popularity as it captures the degradation process of mechanical equipment more comprehensively, the prediction performance of which is generally higher. However, less emphasis has been placed on enhancing the trustworthiness of the model, especially in terms of reasonability and interpretability in uncertainty-aware prediction. Aiming to solve such a problem, a novel framework called a sensor-aware capsule neural network (SACN) is proposed for multisensory fusion in RUL prediction. Then a novel Monte Carlo-based dropout method based on the activation level of capsules was developed for uncertainty quantification. Furthermore, the proposed method allows for multisensory fusion interpretation to attribute prediction results and uncertainties to the relevant features across sensors. A case study on C-MAPSS dataset shows that the proposed method outperforms the popular deep learning-based methods. In particular, the SACN based on capsule dropout achieves both greater accuracy and better reasonability than Gaussian dropout, as evaluated by conventional accuracy metrics and the proposed uncertainty coverage score, and the relationship between input features and final results can be revealed through multisensory fusion interpretation, which evaluates the contributions of each sensor for the given input.
- **论文中的描述**: Li et al. propose a dropout-based remaining useful life (RUL) prediction framework named SACN.
<!-- 为了解决考虑不确定性的预测方法存在的模型合理性和可解释性欠缺的问题，文献\cite{capsnet_rul_li2024sensor}中，Li~等人提出了一种考虑传感器的胶囊神经网络（Sensor-Aware Capsule Neural Network, SACN），这一工作提出了基于胶囊神经元激活水平的蒙特卡洛随机失活机制（Capsule-Activation-Based Monte-Carlo Dropout, CA-MCD），并开展了考虑跨传感器相关特征分布的不确定性归因研究。 -->

### [12] ensemble2_soh_10102497
- **标题**: State of health estimation for lithium-ion batteries under arbitrary usage using data-driven multimodel fusion
- **作者**: Zhang, Yizhou and Wik, Torsten and Bergström, John and Zou, Changfu
- **期刊**: IEEE Trans. Transp. Electrif.
- **年份**: 2024
- **卷期**: 10 (1)
- **页码**: 1494-1507
- **DOI**: 10.1109/TTE.2023.3267124
- **摘要**: Accurately estimating the state of health (SoH) of batteries is indispensable for the safety, reliability, and optimal energy and power management of electric vehicles. However, from a data-driven perspective, complications, such as dynamic vehicle operating conditions, stochastic user behaviors, and cell-to-cell variations, make the estimation task challenging. This work develops a data-driven multimodel fusion method for SoH estimation under arbitrary usage profiles. All possible operating conditions are categorized into six scenarios. For each scenario, an appropriate feature set is extracted to indicate the SoH. Based on the obtained features, four machine learning algorithms are applied individually to train SoH estimation models using time-series data. In addition to the estimates at the current time step, a histogram data-based and online adaptive model is taken from previous work for predicting the next-step SoH. Then, a Kalman filter is applied to systematically fuse the results of all the estimation and prediction models. Experimental data collected from different types of batteries operated under diverse profiles verify the effectiveness and practicability of the developed method, as well as its superiority over individual models.
- **论文中的描述**: Zhang et al. combine a multi-model fusion method and a deep ensemble neural network to quantify SOH estimation uncertainty, known as DeNN.
<!-- 文献\cite{ensemble2_soh_10102497}中，Zhang~等人针对包含复杂环境噪声的动力电池循环信号，提出一种面向任意使用工况的数据驱动多模型融合健康状态评估方法，命名为DeNN。该方法利用模型集成（Model Ensemble, ME）技术并利用~KF~实现多个模型的输出的融合，既实现了多样负载工况下准确的健康状态估计，又实现了不确定性量化。 -->

### [13] mcdropout_autoencoder_10412192
- **标题**: Automatic Feature Extraction-Enabled Lithium-Ion Battery Capacity Estimation Using Random Fragmented Charging Data
- **作者**: Zhou, Ziyou and Liu, Yonggang and Zhao, Zhigang and Xia, Huan and Chen, Zheng and Zhang, Yuanjian
- **期刊**: IEEE Trans. Transp. Electrif.
- **年份**: 2024
- **卷期**: 10 (4)
- **页码**: 8845-8856
- **DOI**: 10.1109/TTE.2024.3357728
- **摘要**: Nowadays, health diagnosis for lithium-ion batteries is critical to ensure their normal and safe operations. However, precise estimation of battery capacity is a challenging task, especially under complex and varying operation conditions. To tackle this problem, we propose an automatic feature extraction technique that utilizes random fragmented charging data to achieve precise capacity estimation across diverse operational scenarios. The automatic feature extraction is achieved by a deep autoencoder (DAE) model and can be applied to other conditions without additional training, justifying its generalization performance. Through a comprehensive exploration of the capacity estimation performance across various input data segments, we introduce a novel approach to select preferable input data and develop a universal estimation model for achieving accurate capacity estimation. Additionally, the Bayesian neural network (NN) is exploited in the universal estimation model to quantify the uncertainty of the estimated results. Experimental datasets from three distinct types of batteries operating under diverse conditions are applied to examine the performance of the proposed method. The results manifest that our method yields robust and precise capacity estimation under various charging conditions.
- **论文中的描述**: Zhou et al. design a Bayesian deep autoencoder (BDAE) with Monte Carlo dropout (MCD) and variational inference to measure the uncertainty in SOH estimates.
<!-- 文献\cite{mcdropout_autoencoder_10412192}中，Zhou~等人提出了一种基于MCD的贝叶斯深度自编码器（Bayesian Deep Autoencoder, BDAE）以克服锂离子电池复杂且高度时变的实际运行工况带来的健康诊断挑战。该编码器首先进行自动化退化特征提取，继而开展优选输入数据筛选并构建回归模型，最后对预测结果关联的不确定性实施定量表征。 -->

### [14] nemani2023uncertainty
- **标题**: Uncertainty quantification in machine learning for engineering design and health prognostics: A tutorial
- **作者**: Nemani, Venkat and Biggio, Luca and Huan, Xun and Hu, Zhen and Fink, Olga and Tran, Anh and Wang, Yan and Zhang, Xiaoge and Hu, Chao
- **期刊**: Mech. Syst. Signal Proc.
- **年份**: 2023
- **卷期**: 205 ()
- **页码**: 1-69
- **DOI**: 10.1016/j.ymssp.2023.110796
- **摘要**: On top of machine learning (ML) models, uncertainty quantification (UQ) functions as an essential layer of safety assurance that could lead to more principled decision making by enabling sound risk assessment and management. The safety and reliability improvement of ML models empowered by UQ has the potential to significantly facilitate the broad adoption of ML solutions in high-stakes decision settings, such as healthcare, manufacturing, and aviation, to name a few. In this tutorial, we aim to provide a holistic lens on emerging UQ methods for ML models with a particular focus on neural networks and the applications of these UQ methods in tackling engineering design as well as prognostics and health management problems. Towards this goal, we start with a comprehensive classification of uncertainty types, sources, and causes pertaining to UQ of ML models. Next, we provide a tutorial-style description of several state-of-the-art UQ methods: Gaussian process regression, Bayesian neural network, neural network ensemble, and deterministic UQ methods focusing on spectral-normalized neural Gaussian process. Established upon the mathematical formulations, we subsequently examine the soundness of these UQ methods quantitatively and qualitatively (by a toy regression example) to examine their strengths and shortcomings from different dimensions. Then, we review quantitative metrics commonly used to assess the quality of predictive uncertainty in classification and regression problems. Afterward, we discuss the increasingly important role of UQ of ML models in solving challenging problems in engineering design and health prognostics. Two case studies with source codes available on GitHub are used to demonstrate these UQ methods and compare their performance in the life prediction of lithium-ion batteries at the early stage (case study 1) and the remaining useful life prediction of turbofan engines (case study 2).
- **论文中的描述**: Nemani et al. propose a strategy focusing on the spectral-normalized neural Gaussian process (SNGP) for deterministic uncertainty quantification.
<!-- 基于蒙特卡洛随机失活机制（Monte-Carlo Dropout, MCD）的确定性-随机模型变换方法需要多次后采样，不利于深度学习模型的实时应用。文献\cite{nemani2023uncertainty}中，Nemani~综述了BDL的主要分支，并提出了一种基于谱归一化神经高斯过程（Spectral-Normalized Neural Gaussian Process, SNGP）的考虑不确定性的寿命预测框架。该框架将铺归一化应用于模型隐藏的残差层并使用高斯过程层替换全连接层，从而实现不确定性量化，并具有与单一确定性网络相当的推理延迟水平。 -->

### [15] 9729404
- **标题**: A Bayesian deep learning framework for RUL prediction incorporating uncertainty quantification and calibration
- **作者**: Lin, Yanhui and Li, Ganghui
- **期刊**: IEEE Trans. Ind. Inform.
- **年份**: 2022
- **卷期**: 18 (10)
- **页码**: 7274-7284
- **DOI**: 10.1109/TII.2022.3156965
- **摘要**: In this article, deep learning (DL) has attracted increasing attention for remaining useful life (RUL) prediction. However, most DL-based prognostics methods only provide deterministic RUL values while ignoring the associated epistemic and aleatoric uncertainties. In practice, it is important to know the exact confidence in model predictions for decision making. In this article, a Bayesian deep learning (BDL) framework for RUL prediction incorporating uncertainty quantification and calibration is proposed. First, the epistemic and aleatoric uncertainties, which account for the ignorance about the model and the noise inherent in the observations, respectively, are characterized by integrating both types of uncertainties into a BDL framework. Second, to avoid under- and over-confident predictions, a novel iterative calibration method is proposed to jointly calibrate epistemic, aleatoric, and predictive uncertainties by combining isotonic regression with standard deviation scaling. The effectiveness of the proposed method is demonstrated by the case study of turbofan engines and lithium-ion batteries datasets.
- **论文中的描述**: Lin and Li introduce a Bayesian neural networks (BNN) framework utilizing Concrete Dropout for RUL prediction, in which an iterative calibration is integrated by combining isotonic regression with standard deviation (STD) scaling.
<!-- 文献\cite{9729404}中，Lin~和~Li~面向可靠性决策对模型预测结果全局置信水平准确量化的需求，提出了一种基于贝叶斯深度学习（Bayesian Deep Learning, BDL）的剩余使用寿命预测框架。所提出的框架首先给出认知不确定性和偶然不确定性的数学表征和解耦方法，继而建立基于长短期记忆神经网络（Long-Short Term Memory Network, LSTM）的贝叶斯模型，该框架最后提出了一种迭代式校准策略，基于保序回归和标准差缩放（Standard Deviation Scaling, SDS）技术实现对认知不确定性、偶尔不确定性和全局预测不确定性的联合校准。 -->

### [16] 10217044
- **标题**: Early prediction of knee point and knee capacity for fast-charging lithium-ion battery with uncertainty quantification and calibration
- **作者**: Ke, Yuqi and Jiang, Yiyue and Zhu, Rong and Peng, Weiwen and Tan, Xiaojun
- **期刊**: IEEE Trans. Transp. Electrif.
- **年份**: 2024
- **卷期**: 10 (2)
- **页码**: 2873-2885
- **DOI**: 10.1109/TTE.2023.3304670
- **摘要**: *(待添加)*
- **论文中的描述**: Ke et al. develop a MCD-based BNN model for LIBs' knee capacity prediction and also used the STD scaling method for uncertainty calibration.
<!-- 文献\cite{10217044}中，Ke等人提出了一种基于贝叶斯神经网络（Bayesian Neural Network, BNN）的拐点-拐点容量早期预测框架。该框架引入一种基于容量矩阵滑动窗口的退化特征提取机制，继而基于BNN和MCD实现锂离子电池缓慢老化-加速老化拐点的容量预测及对应的不确定性量化，最后基于SDS技术标定所量化的不确定性。 -->

### [17] 10391265
- **标题**: State of health estimation for second-life lithium-ion batteries in energy storage system with partial charging-discharging workloads
- **作者**: Yiyue Jiang and Yuqi Ke and Fangfang Yang and Jinchen Ji and Weiwen Peng
- **期刊**: IEEE Trans. Ind. Electron.
- **年份**: 2024
- **卷期**: 71 (10)
- **页码**: 13178-13188
- **DOI**: 10.1109/TIE.2023.3344825
- **摘要**: *(待添加)*
- **论文中的描述**: Jiang et al. present a neural network based on Bayes-by-Backprop strategy with uncertainty calibration to estimate SOH of second-life batteries.
<!-- 储能系统是锂离子电池的一个重要应用领域，其使用电动汽车退役锂电池，也即梯次利用锂电池。在这个应用场景中，大规模处于不同生命周期的锂电池通过串联或并联在一起提供均衡稳定电能。储能系统中电池初始健康状态不尽相同，且不同局部的锂电池经历不同的充放电工况，导致了数据驱动的健康状态估计模型的评估不确定性。
针对此，文献\cite{10391265}中，Jiang~等人提出了一种梯次利用锂离子电池健康状态评估方法，该方法设计了一种联合特征提取策略以从电池循环序列中结构包含工况无关退化机理的健康状态表征信息，随后，基于具备不确定性校准能力的BNN生成全局健康状态估计结果，并定量表征模型评估过程的不确定性。 -->

### [18] chen2003bayesian
- **标题**: Bayesian filtering: From Kalman filters to particle filters, and beyond
- **作者**: Chen, Zhe
- **期刊**: Statistics
- **年份**: 2003
- **卷期**: 182 (1)
- **页码**: 1-69
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: The employed filters—predominantly Kalman filters and particle filters—leverage inherent Bayesian frameworks to quantify uncertainty through probabilistic inference over system states and noise distributions, enabling dynamic confidence bounds on predictive results.

\cite{chen2003bayesian}

### [19] ABDAR2021243
- **标题**: A review of uncertainty quantification in deep learning: Techniques, applications and challenges
- **作者**: Moloud Abdar and Farhad Pourpanah and Sadiq Hussain and Dana Rezazadegan and Li Liu and Mohammad Ghavamzadeh and Paul Fieguth and Xiaochun Cao and Abbas Khosravi and U. Rajendra Acharya and Vladimir Makarenkov and Saeid Nahavandi
- **期刊**: Inf. Fusion
- **年份**: 2021
- **卷期**: 76 ()
- **页码**: 243-297
- **DOI**: https://doi.org/10.1016/j.inffus.2021.05.008
- **摘要**: *(待添加)*
- **论文中的描述**: Uncertainty-aware data-driven prognostic models can be classified into statistical learning-based methods and deep learning-based methods. Deep learning methods address uncertainty by leveraging the statistical properties of randomized parameter spaces or output distributions.

\cite{ABDAR2021243}

---

## 第二部分：RODTNet 论文引用文献

域适应与域泛化方法。

### [1] LI2021116410
- **标题**: Lithium-ion battery capacity estimation — A pruned convolutional neural network approach assisted with transfer learning
- **作者**: Yihuan Li and Kang Li and Xuan Liu and Yanxia Wang and Li Zhang
- **期刊**: Appl. Energy
- **年份**: 2021
- **卷期**: 285 ()
- **页码**: 
- **DOI**: 
- **摘要**: Online battery capacity estimation is a critical task for battery management system to maintain the battery performance and cycling life in electric vehicles and grid energy storage applications. Convolutional Neural Networks, which have shown great potentials in battery capacity estimation, have thousands of parameters to be optimized and demand a substantial number of battery aging data for training. However, these parameters require massive memory storage while collecting a large volume of aging data is time-consuming and costly in real-world applications. To tackle these challenges, this paper proposes a novel framework incorporating the concepts of transfer learning and network pruning to build compact Convolutional Neural Network models on a relatively small dataset with improved estimation performance. First, through the transfer learning technique, the Convolutional Neural Network model pre-trained on a large battery dataset is transferred to a small dataset of the targeted battery to improve the estimation accuracy. Then a contribution-based neuron selection method is proposed to prune the transferred model using a fast recursive algorithm, which reduces the size and computational complexity of the model while maintaining its performance. The proposed model is capable of achieving fast online capacity estimation at any time, and its effectiveness is verified on a target dataset collected from four Lithium iron phosphate battery cells, and the performance is compared with other Convolutional Neural Network models. The test results confirm that the proposed model outperforms other models in terms of accuracy and computational efficiency, achieving up to 68.34% model size reduction and 80.97% computation savings.
- **论文中的描述**: Li et al. propose a lightweight and generalizable model for battery SOH estimation that integrates the pretraining-finetuning paradigm with pruned convolutional neural network.
<!-- 针对在线电池容量估计对轻量化模型的需求，文献\cite{LI2021116410}中，Li~等人提出了一种轻量化且可泛化的卷积神经网络（Convolutional Neural Networks, CNN），该方法基于快速递归算法对目标电池上的CNN模型执行后剪枝，通过基于预训练-微调的策略实现从大规模电池数据集训练所得CNN模型参数到目标电池稀缺数据集的定向迁移，加强模型部署时轻量化。 -->

### [2] 9372902
- **标题**: Estimating State of Charge for xEV Batteries Using 1D Convolutional Neural Networks and Transfer Learning
- **作者**: Bhattacharjee, Arnab and Verma, Ashu and Mishra, Sukumar and Saha, Tapan K.
- **期刊**: IEEE Trans. Veh. Technol.
- **年份**: 2021
- **卷期**: 70 (4)
- **页码**: 3123-3135
- **DOI**: 
- **摘要**: In this paper we propose a one-dimensional convolutional neural network (CNN)-based state of charge estimation algorithm for electric vehicles. The CNN is trained using two publicly available battery datasets. The influence of different types of noises on the estimation capabilities of the CNN model has been studied. Moreover, a transfer learning mechanism is proposed in order to make the developed algorithm generalize better and estimate with an acceptable accuracy when a battery with different chemical characteristics than the one used for training the model, is used. It has been observed that using transfer learning, the model can learn sufficiently well with significantly less amount of battery data. The proposed method fares well in terms of estimation accuracy, learning speed and generalization capability.
- **论文中的描述**: Bhattacharjee et al. utilize finetune 1D CNN to facilitate state estimation for varying battery chemistries.
<!-- 电动汽车运行过程中存在的多种噪声扰动影响数据驱动模型状态估计的鲁棒性，文献\cite{9372902}中，Bhattacharjee~等人讨论了这种潜在的影响并提出了一种基于一维~CNN和预训练-微调策略的迁移学习框架，仅利用少量目标域的观测数据即完成充分的特征空间映射，实现了跨数据集的电池荷电状态估计。 -->

### [3] 9343713
- **标题**: Predictive Battery Health Management With Transfer Learning and Online Model Correction
- **作者**: Che, Yunhong and Deng, Zhongwei and Lin, Xianke and Hu, Lin and Hu, Xiaosong
- **期刊**: IEEE Trans. Veh. Technol.
- **年份**: 2021
- **卷期**: 70 (2)
- **页码**: 1269-1277
- **DOI**: 
- **摘要**: Significant progress has been made in transportation electrification in recent years. As the main energy storage device, lithium-ion batteries are one of the key components that need to be properly managed. The remaining useful life, which represents battery health, has attracted increasing attention. Because accurate and robust predictions provide important information for predictive maintenance and cascade utilization. This paper proposes a novel method to predict remaining useful life based on the optimized health indicators and online model correction with transfer learning. Gaussian process regression is used to optimize the threshold for health indicators to determine the end of life, and a usefulness evaluation strategy is proposed to assess the health indicators. Then, a combination of transfer learning and gated recurrent neural network is designed to predict the remaining useful life based on the optimized health indicators directly, which can promote online applications. The prediction model initially trained based on a relevant battery is further fine-tuned according to the early degradation cycling data of the test battery to provide accurate predictions. Moreover, a self-correction strategy is proposed to retrain the regression models so that the models can gradually reach the optimal prediction performance during the operating cycles, which could not be achieved by traditional methods. The recommended input sequence lengths for potential applications are discussed. The method is verified by experiments of a batch of batteries under fast charging conditions, and the results show that, after fine-tuning, the proposed method predicts remaining useful life with an error of fewer than 5 cycles.
- **论文中的描述**: Che et al. introduce an online self-calibrating model for RUL prediction based on Gaussian process regression, long short-term memory neural network, and a pretraining-finetuning strategy.

文献\cite{9343713}中，Che~等人面向设备前瞻性维护和电池梯次利用提出一种基于优化健康因子与融合迁移学习的在线模型校正剩余寿命预测方法，该方法基于GPR自动搜索电池服役寿命终点（End of Life, EOL），通过微调门控循环神经网络（Gated Recurrent Neural Network, GRNN）实现高精度剩余寿命预测，并提出一种自校正策略迭代式提高模型在系统运行周期内预测能力。

### [4] LIU2025115347
- **标题**: Battery state of health estimation using a novel BiLSTM-Mamba2 network with differential voltage features and transfer learning
- **作者**: Yunong Liu and Yuefeng Liu and Hongyu Shen and Liuxu Ding
- **期刊**: J. Energy Storage
- **年份**: 2025
- **卷期**: 110 ()
- **页码**: 
- **DOI**: 
- **摘要**: Currently, most data-driven methods for estimating the state of health (SOH) of lithium-ion batteries extract features directly from charge-discharge cycles. However, these features often fail to accurately reflect the battery's internal aging mechanisms. Furthermore, significant differences in feature distributions across various battery datasets, along with the challenge of obtaining sufficient cycle data from practical applications, limit the generalization ability of conventional models. To address these challenges, we first introduce a novel differential voltage feature, extracted from partial charging data. Additionally, considering the coupling between the state of charge (SOC) and SOH, we employ the new Mamba2 model to thoroughly explore both local and global features of SOH, achieving efficient SOH estimation. Finally, using a fine-tuning strategy, we effectively eliminate differences in sample distributions across datasets, enabling successful transfer learning from the source domain to the target domain. Experimental results show that our model achieved MAE and RMSE of 1.31 % and 1.71 %, respectively, for SOH estimation in the source domain, demonstrating higher accuracy compared to other methods. In the target domain, the model generated 1,226,900 sets of prediction samples, with 78.5 % of the samples having an absolute error within 3 %, indicating the model's strong generalization capability.
- **论文中的描述**: Liu et al. fine-tune a bidirectional long short-term memory (BiLSTM)-Mamba2 model based on differential voltage features to achieve SOH estimation across batteries with different operating conditions and electrode materials.
<!-- 为了应对多源电池数据特征分布异质性和实验室工况和实际运行工况之间存在显著差异的现状，文献\cite{LIU2025115347}中，Liu~等人融合双向长短期记忆神经网络（bidirectional long short-term memory, Bi-LSTM）和~Mamba2~架构以同时捕捉长期和短期退化特征，同时通过在目标域上的精细微调，实现了有效退化知识迁移。 -->

### [5] D2EE01676A
- **标题**: Real-time personalized health status prediction of lithium-ion batteries using deep transfer learning
- **作者**: Ma, Guijun and Xu, Songpei and Jiang, Benben and Cheng, Cheng and Yang, Xin and Shen, Yue and Yang, Tao and Huang, Yunhui and Ding, Han and Yuan, Ye
- **期刊**: Energy Environ. Sci.
- **年份**: 2022
- **卷期**: 15 ()
- **页码**: 4083-4094
- **DOI**: 
- **摘要**: Real-time and personalized lithium-ion battery health management is conducive to safety improvement for end-users. However, personalized prognostic of the battery health status is still challenging due to diverse usage interests, dynamic operational patterns and limited historical data. We generate a comprehensive dataset consisting of 77 commercial cells (77 discharge protocols) with over 140 000 charge–discharge cycles—the largest dataset to our knowledge of its kind, and develop a transfer learning framework to realize real-time personalized health status prediction for unseen battery discharge protocols, at any charge–discharge cycle. Our method can achieve mean testing errors of 0.176% and 8.72% for capacity estimation and remaining useful life (RUL) prediction, respectively. Additionally, the proposed framework can leverage the knowledge from two other well-known battery datasets, with a variety of charge configurations and a different battery chemistry respectively, to reliably estimate the capacity (0.328%/0.193%) and predict the RUL (9.80%/9.90%) of our cells. This study allows end users to tailor battery consumption plans and motivates manufacturers to improve battery designs.
- **论文中的描述**: Ma et al. propose a real-time personalized battery degradation modeling framework named CRNN, based on convolutional-recurrent neural network, achieving joint prediction of SOH and RUL across operating conditions.
<!-- 文献\cite{D2EE01676A}中，Ma~等人提出面向健康状态和剩余寿命联合预测的电芯个性化估计框架，命名为~CRNN。该方法针对实际应用中用例偏好差异、运行模式多样以及历史观测有限等问题，引入基于预训练-微调范式的深度迁移结构，从多电池充放电轨迹中抽取时序退化特征，并在有限循环数据条件下对新放电策略下的健康状态与剩余可用寿命进行在线推断，从而实现对个体电芯的实时健康管理。 -->

### [6] wang2024physics
- **标题**: Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis
- **作者**: Wang, Fujin and Zhai, Zhi and Zhao, Zhibin and Di, Yi and Chen, Xuefeng
- **期刊**: Nat. Commun.
- **年份**: 2024
- **卷期**: 15 ()
- **页码**: 
- **DOI**: 
- **摘要**: Accurate state-of-health (SOH) estimation is critical for reliable and safe operation of lithium-ion batteries. However, reliable and stable battery SOH estimation remains challenging due to diverse battery types and operating conditions. In this paper, we propose a physics-informed neural network (PINN) for accurate and stable estimation of battery SOH. Specifically, we model the attributes that affect the battery degradation from the perspective of empirical degradation and state space equations, and utilize neural networks to capture battery degradation dynamics. A general feature extraction method is designed to extract statistical features from a short period of data before the battery is fully charged, enabling our method applicable to different battery types and charge/discharge protocols. Additionally, we generate a comprehensive dataset consisting of 55 lithium-nickel-cobalt-manganese-oxide (NCM) batteries. Combined with three other datasets from different manufacturers, we use a total of 387 batteries with 310,705 samples to validate our method. The mean absolute percentage error (MAPE) is 0.87%. Our proposed PINN has demonstrated remarkable performance in regular experiments, small sample experiments, and transfer experiments when compared to alternative neural networks. This study highlights the promise of physics-informed machine learning for battery degradation modeling and SOH estimation.
- **论文中的描述**: Wang et al. propose a physics-informed neural network (PINN) for battery degradation modeling and achieve cross-dataset battery health state prediction using the pretraining-finetuning paradigm.

<!-- 文献\cite{wang2024physics}中，Wang~等人提出基于物理信息神经网络（Physics-Informed Neural Network, PINN）的可学习动力学模块。该方法从经验退化机理和状态方程描述电池老化，并由神经网络学习退化动力学，使模型在不同电池类型及充放电条件下保持高精度与稳定性，同时，将这种方法应用在退化模式迁移问题中，基于预训练-微调范式实现跨数据集健康状态迁移估计。 -->

### [7] 10886998
- **标题**: Robust State of Health Estimation for Heterogeneous Batteries With Privacy Preserving
- **作者**: Wang, Tianjing and Zhang, Zhijun and Tao, Yuechuan and Dong, Zhao Yang
- **期刊**: IEEE Trans. Veh. Technol.
- **年份**: 2025
- **卷期**: 74 (6)
- **页码**: 8921-8937
- **DOI**: 
- **摘要**: The state-of-the-art approaches to state of health (SOH) estimation typically generate models tailored to specific battery datasets, requiring retraining for other battery types and failing to construct a universally robust model across diverse battery data. Challenges in achieving a robust model span statistical heterogeneity, adaptability, and resilience to noise and cyber-attacks. This study introduces a novel, privacy-preserving robust SOH estimation for heterogeneous batteries using customized federated learning (FL). The approach aggregates local SOH models into a global model while preserving data privacy at the source. It leverages statistical and system utility indicators for battery management system client selection, incorporating the Epsilon-Greedy method to dynamically include new clients and adjust the participant count based on global model efficacy. Additionally, a performance-discrepancy weighted aggregation mechanism is designed by using the L2 distance and loss indices as weights for local models. A discrepancy-based personalization method further refines the number of personalization layers, enhancing local model performance. Through detailed case analysis, the proposed algorithm is shown to surpass conventional FL, centralized, and local training methods across scenarios of varied battery types, data inaccuracies, communication errors, and operational risks, demonstrating superior adaptability and robustness.
- **论文中的描述**: Wang et al. propose a decentralized framework to achieve robust SOH estimation across heterogeneous battery datasets.
出于隐私保护的需求，来自不同设备或系统的电池的异构循环数据不可直接共享，通常通过联邦学习（Federated Learning, FL）策略训练具有全局泛化能力的模型。为了解决异构电池系统聚合过程中存在的数据统计异构性、模型动态适应性、复杂噪声扰动和网络安全工具防御韧性等挑战，文献\cite{10886998}中，Wang~等人提出了一种异构电池集群的隐私保护鲁棒健康状态估计方法。首先，该方法提出了一种融合统计特征和系统效用的客户端选择机制，基于~Epsilon~贪心策略吸纳异构节点，其次，提出了一种基于基于性能差异的加权聚合机制，最后，引入基于差异分布的个性化机制增强本地模型的性能。

### [8] 9788003
- **标题**: A Transfer Learning-Based Method for Personalized State of Health Estimation of Lithium-Ion Batteries
- **作者**: Ma, Guijun and Xu, Songpei and Yang, Tao and Du, Zhenbang and Zhu, Limin and Ding, Han and Yuan, Ye
- **期刊**: IEEE Trans. Neural Netw. Learn. Syst.
- **年份**: 2024
- **卷期**: 35 (1)
- **页码**: 759-769
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Ma et al. propose a method named ConvMMD that aligns source and target domains by minimizing the maximum mean discrepancy of lower-order moments between them, facilitating a condition-robust estimation of SOH of batteries.
<!-- 文献\cite{9788003}中，Ma~等人提出跨工况的电池个性化退化预测模型，命名为~ConvMMD。该方法基于知识迁移思想，利用卷积式深度网络从原始充电电压轨迹中自动提取特征，并通过最大均值差异（Maximum Mean Discrepancy, MMD）度量构造域间对齐的连续量预测形式，以缩减源电池与目标电池数据分布差异。 -->

### [9] HAN2022230823
- **标题**: End-to-end capacity estimation of Lithium-ion batteries with an enhanced long short-term memory network considering domain adaptation
- **作者**: Te Han and Zhe Wang and Huixing Meng
- **期刊**: J. Power Sources
- **年份**: 2022
- **卷期**: 520 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Han et al. present a high-precision degradation model requiring only a few target domain samples, achieved by incorporating a domain adaptation layer into long short-term memory neural networks, known as LSTM-DA.

<!-- 文献\cite{HAN2022230823}中，Han~等人构建电池跨域容量预测方法，命名为~LSTM-DA。该方法针对训练与测试电池退化轨迹分布不一致的问题，引入深层长短记忆结构从端电压与工作电流序列中学习容量演化特征，并在高层特征空间叠加基于均值匹配的~MMD~对齐模块，以缓解源域与目标域退化表征之间的偏移，从而实现对不同电池个体的跨域在线容量评估。 -->

### [10] 9560040
- **标题**: State-of-Health Estimation for Lithium-Ion Batteries Using Domain Adversarial Transfer Learning
- **作者**: Ye, Zhuang and Yu, Jianbo
- **期刊**: IEEE Trans. Power Electron.
- **年份**: 2022
- **卷期**: 37 (3)
- **页码**: 3528-3543
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Ye et al. design a method named DDAN that realizes unsupervised degradation feature alignment via adversarial training across source and target domains, enabling a transferable prognostic model.
<!-- 文献\cite{9560040}中，Ye~和Yu~针对锂离子电池退化预测中的跨工况分布偏移问题，提出基于深层跨域对抗结构的预测模型，命名为~DDAN。该模型通过构建无标注特征对齐指标将 MMD 与相关结构对齐机制联合，并辅以生成式对抗训练策略，引导特征编码器学习跨域稳定表征，同时采用稠密双向门控循环单元（Dense Bidirectional Gated Recurrent Unit, D-BiGRU）从传感信号中抽取时序退化特征，从而提升在多工况场景下的电池退化预测能力。 -->

### [11] 10029904
- **标题**: State of Health Estimation of Lithium Iron Phosphate Batteries Based on Degradation Knowledge Transfer Learning
- **作者**: Lu, Xin and Qiu, Jing and Lei, Gang and Zhu, Jianguo
- **期刊**: IEEE Trans. Transp. Electrif.
- **年份**: 2023
- **卷期**: 9 (3)
- **页码**: 4692-4703
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Lu et al. develop a two-stage prognostic framework named DKTL, which combines degradation mechanisms and achieves knowledge transfer of degradation patterns from synthetic data to real data.
<!-- 文献\cite{10029904}中，Lu~等人提出结合退化知识迁移的预测方法，命名为~DKTL。该方法利用退化机理与工况条件构建面向性能完好度估计的条件时序对抗生成网络，并针对合成与真实锂离子电池循环数据分布不匹配的问题，构建退化机理回归模型，通过基于二阶统计矩对齐的跨域策略实现源域与目标域退化表征的一致化。 -->

### [12] WANG2023108897
- **标题**: Feature disentanglement and tendency retainment with domain adaptation for Lithium-ion battery capacity estimation
- **作者**: Fujin Wang and Zhibin Zhao and Zhi Zhai and Yanjie Guo and Huan Xi and Shibin Wang and Xuefeng Chen
- **期刊**: Reliab. Eng. Syst. Saf.
- **年份**: 2023
- **卷期**: 230 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Wang et al. develop a dual-branch model with a domain invariant-specific feature decoupling strategy and a degradation trend preservation strategy to align degradation patterns across domains, known as DR-Net.
<!-- 针对锂离子电池在多种化学体系及工况下容量评估的跨域偏移问题，文献\cite{WANG2023108897}，Wang~等人提出特征解缠与趋势保持网络，命名为~DR-Net。该网络从监测电压电流序列中抽取特征，在表征空间中区分域无关共享表征与域特异私有表征，并保留容量退化趋势信息，从而在训练域与应用域分布不一致时仍能实现稳健容量预测。 -->

### [13] 9782500
- **标题**: Generalizing to Unseen Domains: A Survey on Domain Generalization
- **作者**: Wang, Jindong and Lan, Cuiling and Liu, Chang and Ouyang, Yidong and Qin, Tao and Lu, Wang and Chen, Yiqiang and Zeng, Wenjun and Yu, Philip S.
- **期刊**: IEEE Trans. Knowl. Data Eng.
- **年份**: 2023
- **卷期**: 35 (8)
- **页码**: 8052-8072
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Domain generalization paradigm involves three main categories, namely data manipulation, representation learning, and specific learning strategy.

### [14] CHEN2024234696
- **标题**: Domain generalization-based state-of-health estimation of lithium-ion batteries
- **作者**: Liping Chen and Xinyuan Bao and António M. Lopes and Xin Li and Huifang Kong and Yi Chai and Penghua Li
- **期刊**: J. Power Sources
- **年份**: 2024
- **卷期**: 610 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Chen et al. develop a dual-branch feature extractor to process domain samples with mixed and separated sources. By leveraging a domain discriminator and a health state estimator, their approach enables domain-invariant degradation feature extraction, culminating in a representation learning-based degradation pattern generalization method termed DGSOH.
文献\cite{CHEN2024234696}中，Chen~等人提出了一种名为~DGSOH~的可泛化健康状态估计器，该方法融和CNN和GRNN作为多源异构退化特征提取器，同时创建了一个预判别器对成对的数据进行所属域分类。该方法具有一种两支的结构，第一个独立分支保留输入样本的域信息，第二个混杂分支则将所有输入数据混杂在一起，通过最小化两个分支的估计损失和独立分支的判别损失构成的总损失，该方法实现了退化模式泛化。

### [15] TAN2024103725
- **标题**: Forecasting battery degradation trajectory under domain shift with domain generalization
- **作者**: Ruifeng Tan and Xibin Lu and Minhao Cheng and Jia Li and Jiaqiang Huang and Tongyi Zhang
- **期刊**: Energy Storage Mater.
- **年份**: 2024
- **卷期**: 72 ()
- **页码**: 
- **DOI**: 
- **摘要**: Rechargeable batteries play a pivotal role in the carbon-neutral green environment by electrifying transportation and mitigating the intermittency of renewable energies. Forecasting the degradation of batteries is crucial for the optimal usage of batteries, while predicting battery degradation is not trivial due to diverse working conditions and complex failure mechanisms. To address this challenge, we develop a deep learning model that treats differences in operating conditions as domain shifts and utilizes meta-learning-based and task-driven domain generalization techniques to attack the domain shifts. The model effectiveness is demonstrated on three datasets comprising 203 cells of various operating conditions and chemistries, with improvements in prediction accuracy ranging from 18.1% to 30.0% (23.8% on average). Moreover, the model has gained some generalization capability via learning the correlation between domain gaps in the model and the degradation modes behind various operating conditions. Collectively, our work not only showcases the promise of the high-reliability data-driven model for diverse conditions and chemistries by exploiting domain generalization, but also spotlights the potential interplay between artificial intelligence and domain knowledge.
- **论文中的描述**: Tan et al. design a meta learning-based domain generalization method named MAGNet. It couples a two-phase meta-optimization strategy (training/testing cycles) with RUL-driven health prediction, enforcing domain-invariant representation learning through task-aligned gradient synchronization.

文献\cite{TAN2024103725}中，Tan~等人针对电池退化轨迹的可靠预测面临的挑战，构建了一种基于元学习的退化泛化方法，命名为MAGNet。该方法以基于~Transformer~的网络作为骨干网络以高效提取退化特征。该方法通过元划分模拟跨工况分布差异，通过多阶段交叉训练和误差联合最小化策略驱动骨干网络学习全局鲁棒退化表征。该方法设计并嵌入了任务驱动的域泛化模块，基于多任务联合学习，将退化先验注入骨干网络，从而增强模型分布外泛化能力。

### [16] liu2024itransformer
- **标题**: iTransformer: Inverted Transformers Are Effective for Time Series Forecasting
- **作者**: Yong Liu and Tengge Hu and Haoran Zhang and Haixu Wu and Shiyu Wang and Lintao Ma and Mingsheng Long
- **期刊**: Proc. Int. Conf. Learn. Represent.
- **年份**: 2024
- **卷期**:  ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Liu et al. propose a method designed to obtain robust sequence representations against OOD temporal patterns through the inclusion of a transposed attention module and a feed-forward network module, known as iTransformer.
<!-- 文献\cite{liu2024itransformer}中，Liu~等人提出倒置结构的~Transformer~预测框架。该方法通过重排时间维和变量维，将时间点嵌入为变量片段，在片段上施加自注意以刻画多元相关性，并在片段中配置前馈子网络提取非线性表征，从而缓解传统基于时间片表示的~Transformer~在长观测窗口下的混叠与算力开销。 -->

### [17] nie2023a
- **标题**: A Time Series is Worth 64 Words: Long-term Forecasting with Transformers
- **作者**: Yuqi Nie and Nam H Nguyen and Phanwadee Sinthong and Jayant Kalagnanam
- **期刊**: Proc. Int. Conf. Learn. Represent.
- **年份**: 2023
- **卷期**:  ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Nie et al. present a time-series modeling framework resistant to pattern drift known as PatchTST. The model employs subsequence segmentation and channel-independent modeling to enhance its adaptability to dynamic temporal patterns.
<!-- 文献\cite{nie2023a}中，Nie~等人构建序列依赖的片段化时序~Transformer~框架，命名为~PatchTST。该方法通过将原始时间序列划分为若干子序列片段单元作为注意编码网络的输入，并采用通道独立建模策略在各变量间共享嵌入映射与注意权重，从而在保留局部语义结构的同时显著降低注意映射的计算与存储开销并扩展可感知的历史数据范围。 -->

### [18] chen2023tsmixer
- **标题**: TSMixer: An All-MLP Architecture for Time Series Forecasting
- **作者**: Sian Chen and Chunliang Li and Sercan O Arik and Nathanael Christian Yoder and Tomas Pfister
- **期刊**: Trans. Mach. Learn. Res.
- **年份**: 2023
- **卷期**:  ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Chen et al. develop a purely linear model capable of efficiently extracting spatio-temporal dependencies without relying on task-specific prior knowledge, known as TSMixer.
文献\cite{chen2023tsmixer}中，Chen~等人提出多序列混合器，命名为~TSMixer，通过堆叠多层前馈网络并在时间轴与特征维度上执行混合变换，分别进行时间混合和特征混合，有效挖掘跨序列信息。该方法结构上完全基于前馈网络，在迁移效率上具有显著优势。

### [19] 10980357
- **标题**: Advancing Electric Vehicle Battery Management: A Data-Driven Digital Twin Approach for Real-Time Monitoring and Performance Enhancement
- **作者**: Alamin, Khaled Sidahmed Sidahmed and Chen, Yukai and Macii, Enrico and Poncino, Massimo and Vinco, Sara
- **期刊**: IEEE Trans. Veh. Technol.
- **年份**: 2025
- **卷期**: 74 (9)
- **页码**: 13850-13864
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Alamin et al. propose a digital twin framework to realize effective cloud-vehicle generalization for BMS.

---

## 第三部分：DA-TMLLM 论文引用文献

机械故障诊断与大语言模型幻觉检测方法。

### [1] Peng_Liu_Du_Gao_Wang_2025
- **标题**: BearLLM: A Prior Knowledge-Enhanced Bearing Health Management Framework with Unified Vibration Signal Representation
- **作者**: Peng, Haotian and Liu, Jiawei and Du, Jinsong and Gao, Jie and Wang, Wei
- **期刊**: Proc. AAAI Conf. Artif. Intell.
- **年份**: 2025
- **卷期**: 39 ()
- **页码**: 19866-19874
- **DOI**: 
- **摘要**: We propose a bearing health management framework leveraging large language models (BearLLM), a novel multimodal model that unifies multiple bearing-related tasks by processing user prompts and vibration signals. Specifically, we introduce a prior knowledge-enhanced unified vibration signal representation to handle various working conditions across multiple datasets. This involves adaptively sampling the vibration signals based on the sampling rate of the sensor, incorporating the frequency domain to unify input dimensions, and using a fault-free reference signal as an auxiliary input. To extract features from vibration signals, we first train a fault classification network, then convert and align the extracted features into word embedding, and finally concatenate these with text embedding as input to an LLM. To evaluate the performance of the proposed method, we constructed the first large-scale multimodal bearing health management (MBHM) dataset, including paired vibration signals and textual descriptions. With our unified vibration signal representation, BearLLM using one set of pre-trained weights achieves state-of-the-art performance on nine publicly available fault diagnosis benchmarks, outperforming specific methods designed for individual datasets. We provide a dataset, our model, and code to inspire future research on building more capable industrial multimodal models.
- **论文中的描述**: H. Peng et al. design a cross-dataset diagnostic LLM, termed BearLLM.
文献\cite{Peng_Liu_Du_Gao_Wang_2025}中，Peng~等人提出了一种融合多模态大语言模型的轴承健康管理框架，命名为~BearLLM，仅需加载一套预训练权重即可实现跨数据集高精度故障诊断。该框架首先提出了一种先验知识增强的统一振动信号表征机制；进一步地，预训练一个故障分类网络捕获信号深度表征；最后，基于所标注的大规模振动信号-文本描述对，将所提取的时序特征映射对齐到词嵌入空间，通过大语言模型联合推理。

### [2] VGCDM
- **标题**: Generating HSR Bogie Vibration Signals via Pulse Voltage-Guided Conditional Diffusion Model
- **作者**: Liu, Xuan and Chen, Jinglong and Xie, Jingsong and Chang, Yuanhong
- **期刊**: IEEE Trans. Intell. Transp. Syst.
- **年份**: 2025
- **卷期**: 26 (1)
- **页码**: 116-127
- **DOI**: 
- **摘要**: Generative Adversarial Networks (GANs) for generating realistic data, have substantially improved fault diagnosis algorithms in various Internet of Things (IoT) systems. However, challenges such as training instability and dynamical inaccuracy limit their utility in high-speed rail (HSR) bogie fault diagnosis. To address these challenges, we introduce the Pulse Voltage-Guided Conditional Diffusion Model (VGCDM). Unlike traditional implicit GANs, VGCDM adopts a sequential U-Net architecture, facilitating multi-steps denoising diffusion for generation, which bolsters training stability and mitigate convergence issues. VGCDM also incorporates control pulse voltage by cross-attention mechanism to ensure the alignment of vibration with voltage signals, enhancing the Conditional Diffusion Model’s progressive controlablity. Consequently, solely straightforward sampling of control voltages, ensuring the efficient transformation from Gaussian Noise to vibration signals. This adaptability remains robust even in scenarios with time-varying speeds. To validate the effectiveness, we conducted two case studies using SQ dataset and high-simulation HSR bogie dataset. The results of our experiments unequivocally confirm that VGCDM outperforms other generative models, achieving the best RSME, PSNR, and FSCS, showing its superiority in conditional HSR bogie vibration signal generation. For access, our code is available at https://github.com/xuanliu2000/VGCDM.
- **论文中的描述**: X. Liu et al. introduce pulse-voltage embeddings into the diffusion process for controllable vibration synthesis.
文献\cite{VGCDM}中，Liu~等人针对基于对抗生成网络（Generative Adversarial Networks, GANs）生成仿真数据过程中存在训练过程不稳定和动力学特征刻画不精准的问题，提出了一种电压信号引导的条件扩散模型（Voltage-Guided Conditional Diffusion Model, VGCDM），该模型基于序列化~U-Net~架构和渐进式多步去噪扩散机制合成铁路转向架故障信号，并基于交叉注意力机制引入控制脉冲电压，实现面向变速度事变复杂工况的鲁棒故障诊断。

### [3] DCGAN
- **标题**: Deep convolutional generative adversarial network with semi-supervised learning enabled physics elucidation for extended gear fault diagnosis under data limitations
- **作者**: Kai Zhou and Edward Diehl and Jiong Tang
- **期刊**: Mech. Syst. Signal Proc.
- **年份**: 2023
- **卷期**: 185 ()
- **页码**: 
- **DOI**: 
- **摘要**: Fault detection and diagnosis of gear systems using vibration measurements play an important role in ensuring their functional reliability and safety. Computational intelligence, leveraging upon classification through various surrogate models, has recently demonstrated certain level of success. Major challenge however remains. The establishment of surrogate models generally requires large size of training data with specific labels corresponding to explicitly known gear fault conditions, which may not be available in practical applications. Both the size of available data and the respective labels may be quite limited due to the high cost, which hinders the diagnosis of unseen/unexpected faults with desired reliability. In this research we synthesize a deep convolutional generative adversarial network (DCGAN) to tackle this challenge. This new approach follows the semi-supervised learning concept, the performance of which is significantly enhanced by introducing additionally the inexpensive unlabeled data. The balanced adversarial effect between the discriminator and generator in DCGAN is realized by appropriately designing their architectures, which as a result can enable the high accuracy of diagnosis with scarce labeled data. More importantly, by taking full advantage of the rich fault signatures in the unlabeled data that point to the diverse unseen faults, the intrinsic correlation of underlying physics between the unseen and known faults can be implicitly elucidated via unique semi-supervised learning strategy featured in DCGAN. Therefore, the extended capability in diagnosing the unseen faults that are beyond the known faults in training dataset can be realized, which bears practical significance. Systematic case studies using experimental data acquired from a lab-scale gear system are carried out to validate the new diagnosis framework.
- **论文中的描述**: K. Zhou et al. develop a balanced generator-discriminator architecture to diagnose gear defects, termed DCGAN.
为了提升基于代理模型的故障诊断方法对未见故障模式的鲁棒性和可靠性，文献\cite{DCGAN}中，Zhou~等人提出了一种基于深度卷积对抗网络（Deep Convolutional Generative Adversarial Network, DCGAN）的故障诊断框架，该框架基于半监督学习范式，从无标签数据中提取指向多源未见故障的特征指纹，并挖掘未见故障模式与已知故障模式在底层物理机制上的映射关联，提升了数据驱动故障诊断模型的泛化能力。

### [4] WOS:000688310200005
- **标题**: A Hybrid Generalization Network for Intelligent Fault Diagnosis of Rotating Machinery under Unseen Working Conditions
- **作者**: Han, Te and Li, Yan-Fu and Qian, Min
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2021
- **卷期**: 70 ()
- **页码**: 
- **DOI**: 
- **摘要**: The data-driven methods in machinery fault diagnosis have become increasingly popular in the past two decades. However, the wide applications of this scheme are generally compromised in real-world conditions because of the discrepancy between the training data and testing data. Although the recently emerging transfer fault diagnosis can learn transferable features from relevant source data and adapt the diagnostic model to the target data, these methods still only work on the target domain with a priori data distribution. The generalization capability of the transferred model cannot be guaranteed for unseen domains. Since the working conditions of machinery are varying during operation, the generalization capability of the diagnosis methods is crucial in this case. To tackle this challenge, this article proposes a domain generalization-based hybrid diagnosis network for deploying to unseen working conditions. The main idea is to regularize the discriminant structure of the deep network with both intrinsic and extrinsic generalization objectives such that the diagnostic model can learn robust features and generalize to unseen domains. The triplet loss minimization of intrinsic multisource data is implemented to facilitate the intraclass compactness and the interclass separability at the class level, leading to a more generalized decision boundary. The extrinsic domain-level regularization is achieved by using adversarial training to further reduce the risk of overfitting. Extensive cross-domain diagnostic experiments on planetary gearbox demonstrate the effectiveness of the proposed method.
- **论文中的描述**: T. Han et al. propose a hybrid network that combines class constraints with adversarial domain regularization to capture transferable features.
文献\cite{WOS:000688310200005}中，Han~等人面向源域和目标域存在显著分布差异，目标域先验完全缺失的故障诊断问题，提出了一种基于~DG~的混合诊断架构，旨在实现模型向未知服役工况的高效部署。该架构通过最小化三元组损失，刻画具备强泛化能力的类别决策边界；通过实施对抗训练实现域级政策化，避免模型对特定源域的过拟合风险。

### [5] 10478558
- **标题**: Few-Shot Bearing Fault Diagnosis Via Ensembling Transformer-Based Model With Mahalanobis Distance Metric Learning From Multiscale Features
- **作者**: Vu, Manh-Hung and Nguyen, Van-Quang and Tran, Thi-Thao and Pham, Van-Truong and Lo, Men-Tzung
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2024
- **卷期**: 73 ()
- **页码**: 
- **DOI**: 
- **摘要**: Advanced deep-learning models have shown excellent performance in the task of fault-bearing diagnosis over traditional machine learning and signal-processing techniques. Few-shot learning approach has also been attracting a lot of attention in this task to address the problem of limited training data. Nevertheless, cutting-edge models for fault-bearing diagnosis are often based on convolutional neural networks (CNNs) that emphasize local features of input data. Besides, accurate classification of fault-bearing signals is still nontrivial due to the variations of data, fault types, acquisition conditions, and extremely limited data, leaving space for research on this topic. In this study, we propose a novel end-to-end approach for fault-bearing diagnosis even in the case of limited data with artificial and real faults. In particular, we propose a module for automatic feature extraction from input data namely multiscale large kernel feature extraction. The extracted features are then fed into a two-branch model including a global and a local branch. The global one includes a transformer architecture with cross-attention to handle global context and obtain the correlation between the query and support sets. The local branch is a metric-based model consisting of Mahalanobis distance for separating local features from the support set. The outputs from the two branches are then ensembled for classification purposes. Intensive experiments and ablation studies have been made on the two public datasets including CWRU and PU. Qualitative and quantitative results with different degrees of training samples by the proposed model in comparison with other state-of-the-arts have shown the superior performance of the proposed approach. Our code will be published at https://github.com/HungVu307/Few-shot-via-ensembling-Transformer-with-Mahalanobis-distance
- **论文中的描述**: M. Vu et al. propose a dual-branch diagnostic framework that enhances fault classification accuracy in sparse-label scenarios.
小样本场景下数据分布差异显著、故障类别繁杂且采集工况多变，为此，文献\cite{10478558}中，Vu~等人提出了一种端到端轴承故障诊断框架。该框架首先通过多尺度大卷积核模块提取故障特征，继而建立了一个包含两支结构的联合建模网络，分别基于交叉注意力和基于~Mahalanobis~距离的度量学习技术强化特征空间泛化能力。最后，全局-局部信息经过集成融入，实现高精度诊断决策。

### [6] QSCGAN
- **标题**: QSCGAN: An Un-Supervised Quick Self-Attention Convolutional GAN for LRE Bearing Fault Diagnosis Under Limited Label-Lacked Data
- **作者**: Wan, Wenqing and He, Shuilong and Chen, Jinglong and Li, Aimin and Feng, Yong
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2021
- **卷期**: 70 ()
- **页码**: 
- **DOI**: 
- **摘要**: For the fault diagnosis of rolling bearings in the liquid rocket engine (LRE), the fault data is scarce due to the high cost of doing experiments and lacks labels due to the unsure occurrence time of faults. Aiming at the above problem, in this article, an unsupervised fault diagnosis method based on quick self-attention convolutional generative adversarial network (QSCGAN) is proposed. QSCGAN consists of three convolutional sub-networks: a generator (G), a discriminator (D), and a classifier (C). G–D pair can map the noise distribution to the actual data distribution and then generate raw mechanical signals to enhance the training dataset of C. Finally, well-trained C finishes the task of fault diagnosis. By adding a self-attention (SA) layer to D and G, the network acquires a solid ability to mine features of the sample deeply. The spectral normalization (SN) to each layer parameter of G and D improves the stability and the convergence rate of the model. The experimental results on three cases of bearing fault diagnosis (CWRU, SQ, and the data of bearings in LREs) evaluate the effectiveness of the proposed method for fault diagnosis under small samples: get average accuracy of 99.73%, 98.74%, and 95.47%, respectively. The superiority of the proposed method is showed and discussed via comparing with related researches.
- **论文中的描述**: W. Wan et al. embed self-attention and spectral normalization within generator-discriminator architectures to augment rocket bearing data, termed QSCGAN.
文献\cite{QSCGAN}中，Wan~等人针对数据驱动轴承故障诊断问题中数据匮乏和标签缺失的双重挑战，提出了一种基于快速自注意力卷积对抗生成网络（Quick Self-Attention Convolutional Generative Adversarial Network, QSCGAN）的无监督诊断方法。该方法由生成器、判别器和分类器协同，其中生成器和判别器构成对抗博弈对，将隐空间噪声分布映射为真实数据分布，合成逼真的原始机械振动信号，以此对分类器的训练集进行数据增强。

### [7] VQVAE
- **标题**: A generalized network with domain invariance and specificity representation for bearing remaining useful life prediction under unknown conditions
- **作者**: Qing Zheng and Pengtao Teng and Kai Zhang and Guofu Ding and Xuwei Lai and Zhixuan Li and Zhaocheng Yuan
- **期刊**: Knowl.-Based Syst.
- **年份**: 2025
- **卷期**: 310 ()
- **页码**: 
- **DOI**: 
- **摘要**: The requirement to satisfy the assumption of identically and independently distributed data limits the practical application of traditional remaining useful life (RUL) prediction methods. In domain generalization methods, data augmentation and domain-invariant representations face the challenges of maintaining sequence consistency for long time-series data and prognosticating RUL under unknown operating conditions. A novel generalized network with invariance and specificity representation is proposed to address these issues. First, the run-to-failure bearing data were divided into healthy and degraded stages. Next, the time-vector quantized variational autoencoder network generates diverse data from the degradation stage. Subsequently, the domain invariant and domain-specific feature representation network (DIDSR) is proposed for cross-condition prediction of rolling bearing RUL. The DIDSR network is divided into two parts: the domain-invariant component and the domain-specific component. The former extracts shared features from multiple source domains, while the latter learns the characteristics of each source domain through a domain classifier and weights them to obtain the final prediction. Ultimately, the proposed method is extensively evaluated on two bearing run-to-failure datasets. Comparative and ablation experiments validate the effectiveness and superiority of the approach.
- **论文中的描述**: Q. Zheng et al. combine degradation stage partitioning and vector quantized augmentation to enrich degradation features, termed VQVAE.
为了解决将数据增强和域不变特征表示技术应用在未知工况健康管理时面临的长时序列内在时序一致性不足的问题，文献\cite{VQVAE}中，Zhang~等人提出了一种融合不变性和特异性特征表示的泛化网络框架，命名为VQVAE。具体地，通过引入时间序列向量量化变分自编码网络针对设备退化阶段生成多样化样本，继而分别提取源域间共享共性特征和各源域专属特征，最后加权融合所提取的两种特征，实现高精度跨域寿命预测结果。

### [8] ZHAO2022108672
- **标题**: Adaptive open set domain generalization network: Learning to diagnose unknown faults under unknown working conditions
- **作者**: Chao Zhao and Weiming Shen
- **期刊**: Reliab. Eng. Syst. Saf.
- **年份**: 2022
- **卷期**: 226 ()
- **页码**: 
- **DOI**: 
- **摘要**: Recently, domain generalization techniques have been introduced to enhance the generalization capacity of fault diagnostic models under unknown working conditions. Most existing studies assume consistent machine health states between the training and testing data. However, fault modes in the testing phase are unpredictable, and unknown fault modes usually occur, hindering the wide applications of domain generalization-based fault diagnosis methods in industries. To address such problems, this paper proposes an adaptive open set domain generalization network to diagnose unknown faults under unknown working conditions. A local class cluster module is implemented to explore domain-invariant representation space and obtain discriminative representation structures by minimizing triplet loss. An outlier detection module learns optimal decision boundaries for individual class representation spaces to classify known fault modes and recognize unknown fault modes. Extensive experimental results on two test rigs demonstrated the effectiveness and superiority of the proposed method.
- **论文中的描述**: C. Zhao et al. employ a triplet loss and a boundary adaptation method to learn compact features and optimal class boundaries.
开放集故障诊断（Open-set Fault Diagnosis, OSFD）是一类典型的涉及拒绝非期望输入的问题。文献\cite{ZHAO2022108672}中，Zhao~和Shen~提出了一种自适应开放集领域泛化网络（Adaptive Open Set Domain Generalization Network, AOSDGN），以解决实际应用场景中未知故障频发的问题。该方法设计了一种局部类聚类策略，通过最小化三元组损失挖掘领域不变的特征表征空间；并引入异常值检测模块，学习类别独立的特征空间决策边界，从而实现划分已知类别和识别未知故障。

### [9] 10262196
- **标题**: Domain Adaptation With Multi-Adversarial Learning for Open-Set Cross-Domain Intelligent Bearing Fault Diagnosis
- **作者**: Zhu, Zhixiao and Chen, Guangyi and Tang, Gang
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2023
- **卷期**: 72 ()
- **页码**: 
- **DOI**: 
- **摘要**: Adversarial domain adaptation and transfer learning have been widely applied in the field of cross-domain fault diagnosis. However, the effectiveness of existing domain adaptation-based diagnostic methods relies on the assumption that both the source and the target domain data share the same label space. In practice, it is impossible to predict the failure mode during testing, and new failure types may appear in the target domain samples. This is an open-set fault diagnosis issue. To address this problem, we propose a multi-adversarial learning domain adaption (MALDA) model for open-set cross-domain intelligent bearing fault diagnosis. The transferable features and target sample weights are obtained in adversarial learning. By introducing a transfer weight conditional adversarial network to align the joint feature-category distributions and obtain a transferable index, the identifiable predictive information from the classifier output to further adjust and optimize the model. Selective interterritory distribution alignment is achieved by weighted adversarial learning networks, and domain partition adversarial learning can accurately identify shared health states and unknown failure modes. The validity and practicality of the proposed MALDA model are validated by three experimental cases.
- **论文中的描述**: Z. Zhu et al. develop an adversarially trained open-set classifier to identify unknown classes and out-of-domain samples.
文献\cite{10262196}中，Zhu~等人面向开放集故障诊断问题，提出了一种多对抗学习域适应（Multi-Adversarial Learning Domain Adaption, MALDA）方法，该方法通过引入可迁移权重条件对抗网络，实现特征与类别的联合分布对齐，实现源域-目标域共享健康状态辨识和潜在的位置故障模式识别。

### [10] 10214410
- **标题**: A Customized Meta-Learning Framework for Diagnosing New Faults From Unseen Working Conditions With Few Labeled Data
- **作者**: Long, Jianyu and Zhang, Rongxin and Chen, Yibin and Zhao, Rong and Yang, Zhe and Huang, Yunwei and Li, Chuan
- **期刊**: IEEE/ASME Trans. Mechatron.
- **年份**: 2024
- **卷期**: 29 (2)
- **页码**: 1363-1373
- **DOI**: 
- **摘要**: Few-shot fault diagnosis aims to detect novel faults with only a few labeled samples in each category. Most of the few-shot learning (FSL)–based fault diagnosis models use meta-learning frameworks because of their effectiveness and simplicity. However, these models often fail to be generalized in unseen working conditions that exhibit domain shifts. This study focuses on the few-shot fault diagnosis while addressing the challenges in domain-shift scenarios by developing a customized meta-learning framework, which consists of three key contributions: 1) a fused deep feature learning strategy is designed using multidomain signals in time, frequency, and time–frequency to extract more discriminative features from a few labeled samples; 2) a domain shift–learned feature transformation layer is introduced by modulating the feature activations with affine transformations into the meta-learner to tackle challenges due to domain shifts under unseen working conditions; and 3) a Mahalanobis distance–based metric function is constructed leveraging an additional neural network to learn the spread variance of each fault pattern to ensure an accurate and robust label prediction. The proposed framework is tested using real-world datasets and the ablation study demonstrates the effectiveness of its key components. The results also show that the proposed framework outperforms the state-of-the-art FSL algorithms that fail to consider the domain-shift scenarios.
- **论文中的描述**: J. Long et al. develop a domain-generalized unseen fault diagnosis method by fusing a meta-learning block with the Mahalanobis metric, termed MLMM.
文献\cite{10214410}中，Long~等人针对基于小样本学习的迁移模型面对伴随域漂移现象的位置复杂工况时存在的泛化能力不足的问题，提出了一种定制化元学习框架，命名为MLMM。该方法首先设计一种融合深度特征的学习策略，整合时间、频率和时频信号以提高故障特征的判别性；继而，融合元学习策略和基于域漂移学习的特征变换层，通过特征调制实现特征迁移；最后构建基于~Mahalanobis~距离的度量函数并学习各类故障模式的分布方法，提供预测过程的准确性和鲁棒性。

### [11] ZHANG2023109518
- **标题**: Weighted domain separation based open set fault diagnosis
- **作者**: Xingwu Zhang and Yu Zhao and Xiaolei Yu and Rui Ma and Chenxi Wang and Xuefeng Chen
- **期刊**: Reliab. Eng. Syst. Saf.
- **年份**: 2023
- **卷期**: 239 ()
- **页码**: 
- **DOI**: 
- **摘要**: Cross domain fault diagnosis based on deep learning is of great significance for improving the reliability and safety of mechanical equipment. Generally, it assumes that the label sets of training data (source domain) and test data (target domain) are consistent. However, the test data usually contain unknown classes that are unseen in the training data due to unpredictable fault modes in real industrial scenarios. Therefore, the open set fault diagnosis (OSFD) where the training label set is a part of the test label set appeared. However, most previous studies directly aligned the source domain and target domain without considering the private features of each domain and required prior knowledge to set the threshold for unknown class detection. Thus, a weighted domain separation network (WDSN) is proposed. First, the unknown samples are detected by establishing the boundary between known class and unknown class by a binary classifier without setting a threshold. Then, the private features of each domain are separated to obtain the shared domain, thereby avoiding interference of unknown classes and noise during feature alignment. Results on two datasets demonstrate that the proposed method outperforms state-of-the-art methods and has more prospects for ensuring the reliability of mechanical equipment.
- **论文中的描述**: X. Zhang et al. introduce a domain-adaptive approach that disentangles private and shared features to diagnose unseen faults, termed WDSN.
开放集故障诊断方法往往倾向于开展全局的特征对齐而忽略了各个数据域的私有特征表达，且检测未知类别是依赖基于先验知识的判定阈值。针对此，文献\cite{ZHANG2023109518}中，Zhang~等人提出了一种加权域分离网络（Weighted Domain Separation Network, WDSN），引入二元分类器自适应构建已知故障类别和未知故障类别的划分边界以规避人工预设阈值，同时剥离多个源域的私有特征空间，并基于此提取跨域共享的纯净特征表示。

### [12] 10382502
- **标题**: A Novel Multidomain Contrastive-Coding-Based Open-Set Domain Generalization Framework for Machinery Fault Diagnosis
- **作者**: Lu, Biliang and Zhang, Yingjie and Sun, Qingshuai and Li, Ming and Li, Pude
- **期刊**: IEEE Trans. Ind. Inform.
- **年份**: 2024
- **卷期**: 20 (4)
- **页码**: 6369-6381
- **DOI**: 
- **摘要**: Domain generalization detection of fault categories in industrial equipment diagnosis is a challenging problem, as it demands a model with high generalization performance. Previous methods have primarily focused on a closed set, implying that the label spaces of the training and testing sets are identical. However, this approach is insufficient to reason about the intricate industrial dynamics. In this article, we fuse domain generalization and open-set recognition to introduce a new domain generalization fault diagnosis scenario, called open-set domain generalization. It learns from different source domains to achieve high performance on unknown target domains, where the distribution and label set can be different for each source and target domain. The problem can be more applicable to real-world industrial applications. In addition, we propose a multidomain contrastive coding (MDCC) framework to learn open-set domain generalizable representations. We conduct multidomain contrastive coding by designing a new contrastive coding task and loss to preserve domain-unique knowledge and generalize knowledge across domains simultaneously. Experimental results on two multidomain datasets demonstrate that the proposed MDCC framework outperforms prior methods in open-set domain generalization.
- **论文中的描述**: B. Lu et al. design a contrastive embedding-based diagnostic strategy that jointly preserves domain-specific and domain-invariant features, termed MDCC.
文献\cite{10382502}中，Lu~等人面向开放集域泛化问题，提出了一种多域对比编码（Multidomain Contrastive Coding, MDCC）框架。该框架通过设计对比编码任务和对应的损失函数驱动模型学习故障信息，实现在有效保留各数据域专属特异性知识的同时同步实现全局跨域知识的高效泛化。

### [13] 20242516270368
- **标题**: How Good Are LLMs at Out-of-Distribution Detection?
- **作者**: Liu, Bo and Zhan, Li-Ming and Lu, Zexin and Feng, Yujie and Xue, Lei and Wu, Xiao-Ming
- **期刊**: Proc. LREC-COLING
- **年份**: 2024
- **卷期**:  ()
- **页码**: 8211-8222
- **DOI**: 
- **摘要**: Out-of-distribution (OOD) detection plays a vital role in enhancing the reliability of machine learning models. As large language models (LLMs) become more prevalent, the applicability of prior research on OOD detection that utilized smaller-scale Transformers such as BERT, RoBERTa, and GPT-2 may be challenged, due to the significant differences in the scale of these models, their pre-training objectives, and the paradigms used for inference. This paper initiates a pioneering empirical investigation into the OOD detection capabilities of LLMs, focusing on the LLaMA series ranging from 7B to 65B in size. We thoroughly evaluate commonly used OOD detectors, examining their performance in both zero-grad and fine-tuning scenarios. Notably, we alter previous discriminative in-distribution fine-tuning into generative fine-tuning, aligning the pre-training objective of LLMs with downstream tasks. Our findings unveil that a simple cosine distance OOD detector demonstrates superior efficacy, outperforming other OOD detectors. We provide an intriguing explanation for this phenomenon by highlighting the isotropic nature of the embedding spaces of LLMs, which distinctly contrasts with the anisotropic property observed in smaller BERT family models. The new insight enhances our understanding of how LLMs detect OOD data, thereby enhancing their adaptability and reliability in dynamic environments. We have released the source code at https://github.com/Awenbocc/LLM-OOD for other researchers to reproduce our results.
- **论文中的描述**: B. Liu et al. benchmark LLaMA-series LLMs for undesired input detection and design a cosine distance-based detector using isotropic embeddings, termed LLM-OOD.
LLMs~在模型参数规模、预训练目标和推理范式上与传统模型存在显著差异，基于后者开展的~OOD~检测研究的结论适用性有限。文献\cite{20242516270368}中，Liu~等人针对~LLMs~的~OOD~检测能力开展了实证研究，评估了各类主流~OOD~检测器在零梯度和微调场景下的性能表现，并基于~LLMs~嵌入空间的各向同性特质，提出了一种基于余弦距离的~OOD~检测器，命名为~LLM-OOD。

### [14] 20251218102787
- **标题**: LLM-Check: Investigating Detection of Hallucinations in Large Language Models
- **作者**: Sriramanan, Gaurang and Bharti, Siddhant and Sadasivan, Vinu Sankar and Saha, Shoumik and Kattakinda, Priyatham and Feizi, Soheil
- **期刊**: Proc. Adv. Neural Inf. Process. Syst.
- **年份**: 2024
- **卷期**: 37 ()
- **页码**: 
- **DOI**: 
- **摘要**: While Large Language Models (LLMs) have become immensely popular due to their outstanding performance on a broad range of tasks, these models are prone to producing hallucinations— outputs that are fallacious or fabricated yet often appear plausible or tenable at a glance. In this paper, we conduct a comprehensive investigation into the nature of hallucinations within LLMs and furthermore explore effective techniques for detecting such inaccuracies in various real-world settings. Prior approaches to detect hallucinations in LLM outputs, such as consistency checks or retrieval-based methods, typically assume access to multiple model responses or large databases. These techniques, however, tend to be computationally expensive in practice, thereby limiting their applicability to real-time analysis. In contrast, in this work, we seek to identify hallucinations within a single response in both white-box and black-box settings by analyzing the internal hidden states, attention maps, and output prediction probabilities of an auxiliary LLM. In addition, we also study hallucination detection in scenarios where ground-truth references are also available, such as in the setting of Retrieval-Augmented Generation (RAG). We demonstrate that the proposed detection methods are extremely compute-efficient, with speedups of up to 45x and 450x over other baselines, while achieving significant improvements in detection performance over diverse datasets.
- **论文中的描述**: G. Sriramanan et al. design a compute-efficient detector that leverages the model's internal attention maps, termed LLM-Check.
传统~LLMs~幻觉检测需要获取多轮模型响应或依赖庞大外部数据库而难以部署在实际环境中的问题，文献\cite{20251218102787}中，Sriramanan~等人提出了一种利用~LLMs~隐状态、注意力映射图集输出预测概率分布实现在黑盒和白盒的双重设定下，仅使用单次模型响应即可实现幻觉识别的方法，命名为~LLM-Check。所提出方法可以拓展至具备真实参考文本的特定应用场景，如检索增强生成范式下的幻觉检测问题。

### [15] 20243917091282
- **标题**: Shifting Attention to Relevance: Towards the Predictive Uncertainty Quantification of Free-Form Large Language Models
- **作者**: Duan, Jinhao and Cheng, Hao and Wang, Shiqi and Zavalny, Alex and Wang, Chenan and Xu, Renjing and Kailkhura, Bhavya and Xu, Kaidi
- **期刊**: Proc. Annu. Meet. Assoc. Comput. Linguist.
- **年份**: 2024
- **卷期**: 1 ()
- **页码**: 5050-5063
- **DOI**: 
- **摘要**: Large Language Models (LLMs) show promising results in language generation and instruction following but frequently “hallucinate”, making their outputs less reliable. Despite Uncertainty Quantification’s (UQ) potential solutions, implementing it accurately within LLMs is challenging. Our research introduces a simple heuristic: not all tokens in auto-regressive LLM text equally represent the underlying meaning, as “linguistic redundancy” often allows a few keywords to convey the essence of long sentences. However, current methods underestimate this inequality when assessing uncertainty, causing tokens with limited semantics to be equally or excessively weighted in UQ. To correct this, we propose Shifting Attention to more Relevant (SAR) components at both token- and sentence-levels for better UQ. We conduct extensive experiments involving a range of popular “off-the-shelf” LLMs, such as Vicuna, WizardLM, and LLaMA-2-chat, with model sizes extending up to 33B parameters. We evaluate various free-form question-answering tasks, encompassing domains such as reading comprehension, science Q&A, and medical Q&A. Our experimental results, coupled with a comprehensive demographic analysis, demonstrate the superior performance of SAR. The code is available at https://github.com/jinhaoduan/SAR.
- **论文中的描述**: J. Duan et al. develop a hallucination quantification approach by reweighting token- and sequence-level relevance.
不确定性量化技术是实现~LLMs~幻觉检测的一种具有应用前景的途径，但对~LLMs~响应开展不确定性评估存在精确性不足的问题，这主要来源于语言的冗余性，即自回归文本生成过程中并非所有词元等价地承载语义信息。针对此，文献\cite{20243917091282}中，Duan~等人提出了一种高相关性注意力转移（Shifting Attention to more Relevant, SAR）机制，通过对词元级别和句子级别的相关性进行重赋权，该方法实现了更精确的不确定性量化，并将量化结果应用在~LLMs~幻觉检测问题上。

### [16] 20240715556058
- **标题**: Enhancing Uncertainty-Based Hallucination Detection with Stronger Focus
- **作者**: Zhang, Tianhang and Qiu, Lin and Guo, Qipeng and Deng, Cheng and Zhang, Yue and Zhang, Zheng and Zhou, Chenghu and Wang, Xinbing and Fu, Luoyi
- **期刊**: Proc. EMNLP
- **年份**: 2023
- **卷期**:  ()
- **页码**: 915-932
- **DOI**: 
- **摘要**: Large Language Models (LLMs) have gained significant popularity for their impressive performance across diverse fields. However, LLMs are prone to hallucinate untruthful or nonsensical outputs that fail to meet user expectations in many real-world applications. Existing works for detecting hallucinations in LLMs either rely on external knowledge for reference retrieval or require sampling multiple responses from the LLM for consistency verification, making these methods costly and inefficient. In this paper, we propose a novel reference-free, uncertainty-based method for detecting hallucinations in LLMs. Our approach imitates human focus in factuality checking from three aspects: 1) focus on the most informative and important keywords in the given text; 2) focus on the unreliable tokens in historical context which may lead to a cascade of hallucinations; and 3) focus on the token properties such as token type and token frequency. Experimental results on relevant datasets demonstrate the effectiveness of our proposed method, which achieves state-of-the-art performance across all the evaluation metrics and eliminates the need for additional information.
- **论文中的描述**: T. Zhang et al. introduce a retrieval-free detector that quantifies hallucinations through token-level uncertainty.
文献\cite{20240715556058}中，Zhang~等人提出了一种无参考的、基于不确定性量化的幻觉检测方法，其核心是一种认知聚焦机制。具体地，这种机制在幻觉检测过程中首先聚焦于包含关键语义信息的核心词元；其次排除历史上下文中潜在的不可靠词元从而阻断其可能诱发的级联幻觉效应；最后分析词元类型和词元频次等固有属性对生成结果可靠性的影响。

### [17] selfcheckgpt
- **标题**: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models
- **作者**: Manakul, Potsawee and Liusie, Adian and Gales, Mark
- **期刊**: Proc. EMNLP
- **年份**: 2023
- **卷期**:  ()
- **页码**: 9004-9017
- **DOI**: 
- **摘要**: Generative Large Language Models (LLMs) such as GPT-3 are capable of generating highly fluent responses to a wide variety of user prompts. However, LLMs are known to hallucinate facts and make non-factual statements which can undermine trust in their output. Existing fact-checking approaches either require access to the output probability distribution (which may not be available for systems such as ChatGPT) or external databases that are interfaced via separate, often complex, modules. In this work, we propose "SelfCheckGPT", a simple sampling-based approach that can be used to fact-check the responses of black-box models in a zero-resource fashion, i.e. without an external database. SelfCheckGPT leverages the simple idea that if an LLM has knowledge of a given concept, sampled responses are likely to be similar and contain consistent facts. However, for hallucinated facts, stochastically sampled responses are likely to diverge and contradict one another. We investigate this approach by using GPT-3 to generate passages about individuals from the WikiBio dataset, and manually annotate the factuality of the generated passages. We demonstrate that SelfCheckGPT can: i) detect non-factual and factual sentences; and ii) rank passages in terms of factuality. We compare our approach to several baselines and show that our approach has considerably higher AUC-PR scores in sentence-level hallucination detection and higher correlation scores in passage-level factuality assessment compared to grey-box methods.
- **论文中的描述**: P. Manakul et al. propose SelfCheckGPT, which assesses hallucinations by sampling multiple black-box LLM responses and measuring their mutual consistency.
事实核查是实现~LLMs~幻觉检测的合理方法，但传统的基于事实核查的方法一方面难以被应用在闭源系统中，另一方面高度依赖外部数据库且通常需要通过结构复杂的独立模块进行交互。为了解决这些问题，文献\cite{selfcheckgpt}中，Manakul~等人提出一种基于简单采样的无资源事实核查机制，命名为~SelfCheckGPT。该方法基于语言模型确切掌握概念内在知识的启发性假设，依据对~LLMs~多次采样结果的一致性评估进行模型幻觉检测。

### [18] su-etal-2024-unsupervised
- **标题**: Unsupervised Real-Time Hallucination Detection based on the Internal States of Large Language Models
- **作者**: Su, Weihang and Wang, Changyue and Ai, Qingyao and Hu, Yiran and Wu, Zhijing and Zhou, Yujia and Liu, Yiqun
- **期刊**: Proc. Annu. Meet. Assoc. Comput. Linguist.
- **年份**: 2024
- **卷期**:  ()
- **页码**: 14379-14391
- **DOI**: 
- **摘要**: Hallucinations in large language models (LLMs) refer to the phenomenon of LLMs producing responses that are coherent yet factually inaccurate. This issue undermines the effectiveness of LLMs in practical applications, necessitating research into detecting and mitigating hallucinations of LLMs. Previous studies have mainly concentrated on post-processing techniques for hallucination detection, which tend to be computationally intensive and limited in effectiveness due to their separation from the LLM’s inference process. To overcome these limitations, we introduce MIND, an unsupervised training framework that leverages the internal states of LLMs for real-time hallucination detection without requiring manual annotations. Additionally, we present HELM, a new benchmark for evaluating hallucination detection across multiple LLMs, featuring diverse LLM outputs and the internal states of LLMs during their inference process. Our experiments demonstrate that MIND outperforms existing state-of-the-art methods in hallucination detection.
- **论文中的描述**: W. Su et al. propose a real-time and annotation-free hallucination detection framework using the internal states of LLMs, termed MIND.
传统的基于后处理范式的~LLMs~幻觉检测方法因为独立于模型的推理过程，存在计算开销大的问题。为了克服这一局限性，文献\cite{su-etal-2024-unsupervised}中，Su~等人提出了一种无需人工标注且直接利用~LLMs~内部隐状态的实时幻觉检测机制，命名为MIND。这一工作同时构建了名为~HELM~的基准评估体系，不仅包含高度多样化的模型输出文本，同时记录了模型在推理过程时内部隐状态的演化轨迹。

### [19] 10.1007/978-3-031-86623-4_13
- **标题**: Detecting Hallucinations in Large Language Model Generation: A Token Probability Approach
- **作者**: Quevedo, Ernesto and Salazar, Jorge Yero and Koerner, Rachel and Rivas, Pablo and Cerny, Tomas
- **期刊**: Proc. ICAI
- **年份**: 2025
- **卷期**:  ()
- **页码**: 154-173
- **DOI**: 
- **摘要**: Concerns regarding the propensity of Large Language Models (LLMs) to produce inaccurate outputs, also known as hallucinations, have escalated. Detecting them is vital for ensuring the reliability of applications relying on LLM-generated content. Current methods often demand substantial resources and rely on extensive LLMs or employ supervised learning with multidimensional features or intricate linguistic and semantic analyses difficult to reproduce and largely depend on using the same LLM that hallucinated. This paper introduces a supervised learning approach employing two simple classifiers utilizing only four numerical features derived from tokens and vocabulary probabilities obtained from other LLM evaluators, which are not necessarily the same. The method yields promising results, surpassing state-of-the-art outcomes in multiple tasks across three different benchmarks. Additionally, we provide a comprehensive examination of the strengths and weaknesses of our approach, highlighting the significance of the features utilized and the LLM employed as an evaluator. We have released our code publicly at this https URL.
- **论文中的描述**: E. Quevedo et al. propose a supervised approach that utilizes an auxiliary detector trained on resource-efficient numerical features, termed SHalluDetect.
为了实现模型无关幻觉检测，文献\cite{10.1007/978-3-031-86623-4_13}中，Quevedo~等人提出了一种基于监督学习的幻觉检测方法，命名为~SHalluDetect，旨在基于大型~LLMs~的无幻觉或少幻觉推理结果评估小型~LLMs~输出的幻觉水平。该方法通过部署两个浅层分类器，以基于上述两种不同规模~LLMs~推理结果中的词元分布构造的四个数值特征为输入，实现跨模型架构的高精度幻觉检测。

### [20] li-etal-2023-halueval
- **标题**: HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models
- **作者**: Li, Junyi and Cheng, Xiaoxue and Zhao, Xin and Nie, Jian-Yun and Wen, Ji-Rong
- **期刊**: Proc. EMNLP
- **年份**: 2023
- **卷期**:  ()
- **页码**: 6449-6464
- **DOI**: 
- **摘要**: Large language models (LLMs), such as ChatGPT, are prone to generate hallucinations, i.e., content that conflicts with the source or cannot be verified by the factual knowledge. To understand what types of content and to which extent LLMs are apt to hallucinate, we introduce the Hallucination Evaluation for Large Language Models (HaluEval) benchmark, a large collection of generated and human-annotated hallucinated samples for evaluating the performance of LLMs in recognizing hallucination. To generate these samples, we propose a ChatGPT-based two-step framework, i.e., sampling-then-filtering. Besides, we also hire some human labelers to annotate the hallucinations in ChatGPT responses. The empirical results suggest that ChatGPT is likely to generate hallucinated content in specific topics by fabricating unverifiable information (i.e., about 19.5% user queries). Moreover, existing LLMs face great challenges in recognizing the hallucinations in texts. While, our experiments also prove that the hallucination recognition can be improved by providing external knowledge or adding reasoning steps.
- **论文中的描述**: J. Li et al. develop a benchmark via sampling-then-filtering and annotation for hallucination analysis.
为了评估~LLMs~在何种内容和何种程度上容易产生幻觉，文献\cite{li-etal-2023-halueval}中，Li~等人构建了一个基准测试，提出了一种基于~ChatGPT~的先采样后过滤的两阶段数据生成框架，通过人工操作对模型响应中潜在的幻觉进行审查和标注，证明通过引入外部事实知识或在模型内部增加显示逻辑推理步骤可以提升模型自身的幻觉识别能力。
