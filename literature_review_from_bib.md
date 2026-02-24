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
- **摘要**: *(待添加)*
- **论文中的描述**: Li et al. propose a lightweight and generalizable model for battery SOH estimation that integrates the pretraining-finetuning paradigm with pruned convolutional neural network.

### [2] 9372902
- **标题**: Estimating State of Charge for xEV Batteries Using 1D Convolutional Neural Networks and Transfer Learning
- **作者**: Bhattacharjee, Arnab and Verma, Ashu and Mishra, Sukumar and Saha, Tapan K.
- **期刊**: IEEE Trans. Veh. Technol.
- **年份**: 2021
- **卷期**: 70 (4)
- **页码**: 3123-3135
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Bhattacharjee et al. utilize finetune 1D CNN to facilitate state estimation for varying battery chemistries.

### [3] 9343713
- **标题**: Predictive Battery Health Management With Transfer Learning and Online Model Correction
- **作者**: Che, Yunhong and Deng, Zhongwei and Lin, Xianke and Hu, Lin and Hu, Xiaosong
- **期刊**: IEEE Trans. Veh. Technol.
- **年份**: 2021
- **卷期**: 70 (2)
- **页码**: 1269-1277
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Che et al. introduce an online self-calibrating model for RUL prediction based on Gaussian process regression, long short-term memory neural network, and a pretraining-finetuning strategy.

### [4] LIU2025115347
- **标题**: Battery state of health estimation using a novel BiLSTM-Mamba2 network with differential voltage features and transfer learning
- **作者**: Yunong Liu and Yuefeng Liu and Hongyu Shen and Liuxu Ding
- **期刊**: J. Energy Storage
- **年份**: 2025
- **卷期**: 110 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Liu et al. fine-tune a bidirectional long short-term memory (BiLSTM)-Mamba2 model based on differential voltage features to achieve SOH estimation across batteries with different operating conditions and electrode materials.

### [5] D2EE01676A
- **标题**: Real-time personalized health status prediction of lithium-ion batteries using deep transfer learning
- **作者**: Ma, Guijun and Xu, Songpei and Jiang, Benben and Cheng, Cheng and Yang, Xin and Shen, Yue and Yang, Tao and Huang, Yunhui and Ding, Han and Yuan, Ye
- **期刊**: Energy Environ. Sci.
- **年份**: 2022
- **卷期**: 15 ()
- **页码**: 4083-4094
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Ma et al. propose a real-time personalized battery degradation modeling framework named CRNN, based on convolutional-recurrent neural network, achieving joint prediction of SOH and RUL across operating conditions.

### [6] wang2024physics
- **标题**: Physics-informed neural network for lithium-ion battery degradation stable modeling and prognosis
- **作者**: Wang, Fujin and Zhai, Zhi and Zhao, Zhibin and Di, Yi and Chen, Xuefeng
- **期刊**: Nat. Commun.
- **年份**: 2024
- **卷期**: 15 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Wang et al. propose a physics-informed neural network (PINN) for battery degradation modeling and achieve cross-dataset battery health state prediction using the pretraining-finetuning paradigm.

### [7] 10886998
- **标题**: Robust State of Health Estimation for Heterogeneous Batteries With Privacy Preserving
- **作者**: Wang, Tianjing and Zhang, Zhijun and Tao, Yuechuan and Dong, Zhao Yang
- **期刊**: IEEE Trans. Veh. Technol.
- **年份**: 2025
- **卷期**: 74 (6)
- **页码**: 8921-8937
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Wang et al. propose a decentralized framework to achieve robust SOH estimation across heterogeneous battery datasets.

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

### [15] TAN2024103725
- **标题**: Forecasting battery degradation trajectory under domain shift with domain generalization
- **作者**: Ruifeng Tan and Xibin Lu and Minhao Cheng and Jia Li and Jiaqiang Huang and Tongyi Zhang
- **期刊**: Energy Storage Mater.
- **年份**: 2024
- **卷期**: 72 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Tan et al. design a meta learning-based domain generalization method named MAGNet. It couples a two-phase meta-optimization strategy (training/testing cycles) with RUL-driven health prediction, enforcing domain-invariant representation learning through task-aligned gradient synchronization.

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
- **摘要**: *(待添加)*
- **论文中的描述**: H. Peng et al. design a cross-dataset diagnostic LLM, termed BearLLM.

### [2] VGCDM
- **标题**: Generating HSR Bogie Vibration Signals via Pulse Voltage-Guided Conditional Diffusion Model
- **作者**: Liu, Xuan and Chen, Jinglong and Xie, Jingsong and Chang, Yuanhong
- **期刊**: IEEE Trans. Intell. Transp. Syst.
- **年份**: 2025
- **卷期**: 26 (1)
- **页码**: 116-127
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: X. Liu et al. introduce pulse-voltage embeddings into the diffusion process for controllable vibration synthesis.

### [3] DCGAN
- **标题**: Deep convolutional generative adversarial network with semi-supervised learning enabled physics elucidation for extended gear fault diagnosis under data limitations
- **作者**: Kai Zhou and Edward Diehl and Jiong Tang
- **期刊**: Mech. Syst. Signal Proc.
- **年份**: 2023
- **卷期**: 185 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: K. Zhou et al. develop a balanced generator-discriminator architecture to diagnose gear defects, termed DCGAN.

### [4] WOS:000688310200005
- **标题**: A Hybrid Generalization Network for Intelligent Fault Diagnosis of Rotating Machinery under Unseen Working Conditions
- **作者**: Han, Te and Li, Yan-Fu and Qian, Min
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2021
- **卷期**: 70 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: T. Han et al. propose a hybrid network that combines class constraints with adversarial domain regularization to capture transferable features.

### [5] 10478558
- **标题**: Few-Shot Bearing Fault Diagnosis Via Ensembling Transformer-Based Model With Mahalanobis Distance Metric Learning From Multiscale Features
- **作者**: Vu, Manh-Hung and Nguyen, Van-Quang and Tran, Thi-Thao and Pham, Van-Truong and Lo, Men-Tzung
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2024
- **卷期**: 73 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: M. Vu et al. propose a dual-branch diagnostic framework that enhances fault classification accuracy in sparse-label scenarios.

### [6] QSCGAN
- **标题**: QSCGAN: An Un-Supervised Quick Self-Attention Convolutional GAN for LRE Bearing Fault Diagnosis Under Limited Label-Lacked Data
- **作者**: Wan, Wenqing and He, Shuilong and Chen, Jinglong and Li, Aimin and Feng, Yong
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2021
- **卷期**: 70 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: W. Wan et al. embed self-attention and spectral normalization within generator-discriminator architectures to augment rocket bearing data, termed QSCGAN.

### [7] VQVAE
- **标题**: A generalized network with domain invariance and specificity representation for bearing remaining useful life prediction under unknown conditions
- **作者**: Qing Zheng and Pengtao Teng and Kai Zhang and Guofu Ding and Xuwei Lai and Zhixuan Li and Zhaocheng Yuan
- **期刊**: Knowl.-Based Syst.
- **年份**: 2025
- **卷期**: 310 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Q. Zheng et al. combine degradation stage partitioning and vector quantized augmentation to enrich degradation features, termed VQVAE.

### [8] ZHAO2022108672
- **标题**: Adaptive open set domain generalization network: Learning to diagnose unknown faults under unknown working conditions
- **作者**: Chao Zhao and Weiming Shen
- **期刊**: Reliab. Eng. Syst. Saf.
- **年份**: 2022
- **卷期**: 226 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: C. Zhao et al. employ a triplet loss and a boundary adaptation method to learn compact features and optimal class boundaries.

### [9] 10262196
- **标题**: Domain Adaptation With Multi-Adversarial Learning for Open-Set Cross-Domain Intelligent Bearing Fault Diagnosis
- **作者**: Zhu, Zhixiao and Chen, Guangyi and Tang, Gang
- **期刊**: IEEE Trans. Instrum. Meas.
- **年份**: 2023
- **卷期**: 72 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: Z. Zhu et al. develop an adversarially trained open-set classifier to identify unknown classes and out-of-domain samples.

### [10] 10214410
- **标题**: A Customized Meta-Learning Framework for Diagnosing New Faults From Unseen Working Conditions With Few Labeled Data
- **作者**: Long, Jianyu and Zhang, Rongxin and Chen, Yibin and Zhao, Rong and Yang, Zhe and Huang, Yunwei and Li, Chuan
- **期刊**: IEEE/ASME Trans. Mechatron.
- **年份**: 2024
- **卷期**: 29 (2)
- **页码**: 1363-1373
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: J. Long et al. develop a domain-generalized unseen fault diagnosis method by fusing a meta-learning block with the Mahalanobis metric, termed MLMM.

### [11] ZHANG2023109518
- **标题**: Weighted domain separation based open set fault diagnosis
- **作者**: Xingwu Zhang and Yu Zhao and Xiaolei Yu and Rui Ma and Chenxi Wang and Xuefeng Chen
- **期刊**: Reliab. Eng. Syst. Saf.
- **年份**: 2023
- **卷期**: 239 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: X. Zhang et al. introduce a domain-adaptive approach that disentangles private and shared features to diagnose unseen faults, termed WDSN.

### [12] 10382502
- **标题**: A Novel Multidomain Contrastive-Coding-Based Open-Set Domain Generalization Framework for Machinery Fault Diagnosis
- **作者**: Lu, Biliang and Zhang, Yingjie and Sun, Qingshuai and Li, Ming and Li, Pude
- **期刊**: IEEE Trans. Ind. Inform.
- **年份**: 2024
- **卷期**: 20 (4)
- **页码**: 6369-6381
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: B. Lu et al. design a contrastive embedding-based diagnostic strategy that jointly preserves domain-specific and domain-invariant features, termed MDCC.

### [13] 20242516270368
- **标题**: How Good Are LLMs at Out-of-Distribution Detection?
- **作者**: Liu, Bo and Zhan, Li-Ming and Lu, Zexin and Feng, Yujie and Xue, Lei and Wu, Xiao-Ming
- **期刊**: Proc. LREC-COLING
- **年份**: 2024
- **卷期**:  ()
- **页码**: 8211-8222
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: B. Liu et al. benchmark LLaMA-series LLMs for undesired input detection and design a cosine distance-based detector using isotropic embeddings, termed LLM-OOD.

### [14] 20251218102787
- **标题**: LLM-Check: Investigating Detection of Hallucinations in Large Language Models
- **作者**: Sriramanan, Gaurang and Bharti, Siddhant and Sadasivan, Vinu Sankar and Saha, Shoumik and Kattakinda, Priyatham and Feizi, Soheil
- **期刊**: Proc. Adv. Neural Inf. Process. Syst.
- **年份**: 2024
- **卷期**: 37 ()
- **页码**: 
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: G. Sriramanan et al. design a compute-efficient detector that leverages the model's internal attention maps, termed LLM-Check.

### [15] 20243917091282
- **标题**: Shifting Attention to Relevance: Towards the Predictive Uncertainty Quantification of Free-Form Large Language Models
- **作者**: Duan, Jinhao and Cheng, Hao and Wang, Shiqi and Zavalny, Alex and Wang, Chenan and Xu, Renjing and Kailkhura, Bhavya and Xu, Kaidi
- **期刊**: Proc. Annu. Meet. Assoc. Comput. Linguist.
- **年份**: 2024
- **卷期**: 1 ()
- **页码**: 5050-5063
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: J. Duan et al. develop a hallucination quantification approach by reweighting token- and sequence-level relevance.

### [16] 20240715556058
- **标题**: Enhancing Uncertainty-Based Hallucination Detection with Stronger Focus
- **作者**: Zhang, Tianhang and Qiu, Lin and Guo, Qipeng and Deng, Cheng and Zhang, Yue and Zhang, Zheng and Zhou, Chenghu and Wang, Xinbing and Fu, Luoyi
- **期刊**: Proc. EMNLP
- **年份**: 2023
- **卷期**:  ()
- **页码**: 915-932
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: T. Zhang et al. introduce a retrieval-free detector that quantifies hallucinations through token-level uncertainty.

### [17] selfcheckgpt
- **标题**: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models
- **作者**: Manakul, Potsawee and Liusie, Adian and Gales, Mark
- **期刊**: Proc. EMNLP
- **年份**: 2023
- **卷期**:  ()
- **页码**: 9004-9017
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: P. Manakul et al. propose SelfCheckGPT, which assesses hallucinations by sampling multiple black-box LLM responses and measuring their mutual consistency.

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

### [19] 10.1007/978-3-031-86623-4_13
- **标题**: Detecting Hallucinations in Large Language Model Generation: A Token Probability Approach
- **作者**: Quevedo, Ernesto and Salazar, Jorge Yero and Koerner, Rachel and Rivas, Pablo and Cerny, Tomas
- **期刊**: Proc. ICAI
- **年份**: 2025
- **卷期**:  ()
- **页码**: 154-173
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: E. Quevedo et al. propose a supervised approach that utilizes an auxiliary detector trained on resource-efficient numerical features, termed SHalluDetect.

### [20] li-etal-2023-halueval
- **标题**: HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models
- **作者**: Li, Junyi and Cheng, Xiaoxue and Zhao, Xin and Nie, Jian-Yun and Wen, Ji-Rong
- **期刊**: Proc. EMNLP
- **年份**: 2023
- **卷期**:  ()
- **页码**: 6449-6464
- **DOI**: 
- **摘要**: *(待添加)*
- **论文中的描述**: J. Li et al. develop a benchmark via sampling-then-filtering and annotation for hallucination analysis.

