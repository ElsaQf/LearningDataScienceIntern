# 建模过程
## 数据预处理
## 特征工程
1. 特征分箱，WOE,IV
2. importance值（与树模型相关，rf,xgboost,lightgbm）
3. onehot,labelencoder
## 模型
1. 线性相关
2. 树模型相关
## 调参，模型评估，策略检验，模型稳定性
1. KFold, cv网格搜索
2. 模型评价指标：auc, 混淆矩阵，acc, pre, tpr, fpr, f1
3. 策略评估：ks, lift
4. 稳定性指标：psi
