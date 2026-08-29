# Results Summary — run `20260711-120007-quick-d566a2`


### Dataset 1 - Mendeley Data (D1)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CatBoost | Gradient Boosting | 0.9786 | 0.9617 | 0.9944 | 0.9778 | 0.9645 | 0.0355 | 0.0056 | 0.9577 | 0.9572 | 0.9987 | 98.5446 | 0.0738 |
| Random Forest | Bagging Ensemble | 0.9759 | 0.9615 | 0.9887 | 0.9749 | 0.9645 | 0.0355 | 0.0113 | 0.9521 | 0.9518 | 0.9975 | 1.5256 | 0.0944 |
| Extra Trees | Bagging Ensemble | 0.9759 | 0.9719 | 0.9774 | 0.9746 | 0.9746 | 0.0254 | 0.0226 | 0.9518 | 0.9517 | 0.9988 | 1.2375 | 0.0623 |
| XGBoost | Gradient Boosting | 0.9733 | 0.9563 | 0.9887 | 0.9722 | 0.9594 | 0.0406 | 0.0113 | 0.9470 | 0.9465 | 0.9985 | 5.3934 | 0.0355 |
| Logistic Regression | Linear/Probabilistic | 0.9733 | 0.9665 | 0.9774 | 0.9719 | 0.9695 | 0.0305 | 0.0226 | 0.9465 | 0.9464 | 0.9915 | 0.1373 | 0.0040 |
| LightGBM | Gradient Boosting | 0.9679 | 0.9714 | 0.9605 | 0.9659 | 0.9746 | 0.0254 | 0.0395 | 0.9357 | 0.9356 | 0.9985 | 8.7638 | 0.2070 |
| SVM | Base Non-Linear | 0.9599 | 0.9355 | 0.9831 | 0.9587 | 0.9391 | 0.0609 | 0.0169 | 0.9208 | 0.9198 | 0.9930 | 3.9241 | 0.7691 |
| Decision Tree | Base Non-Linear | 0.9545 | 0.9444 | 0.9605 | 0.9524 | 0.9492 | 0.0508 | 0.0395 | 0.9090 | 0.9089 | 0.9548 | 0.3802 | 0.0046 |
| KNN | Base Non-Linear | 0.9439 | 0.9382 | 0.9435 | 0.9408 | 0.9442 | 0.0558 | 0.0565 | 0.8874 | 0.8874 | 0.9809 | 0.0045 | 0.6938 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.5909 | 0.8158 | 0.1751 | 0.2884 | 0.9645 | 0.0355 | 0.8249 | 0.2307 | 0.1454 | 0.6133 | 0.0361 | 0.0357 |


### Dataset 2 - Oriola Kolawole (D2)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XGBoost | Gradient Boosting | 0.9519 | 0.9463 | 0.9652 | 0.9557 | 0.9364 | 0.0636 | 0.0348 | 0.9033 | 0.9030 | 0.9863 | 5.3779 | 0.0170 |
| LightGBM | Gradient Boosting | 0.9439 | 0.9412 | 0.9552 | 0.9481 | 0.9306 | 0.0694 | 0.0448 | 0.8870 | 0.8869 | 0.9871 | 4.5925 | 0.1530 |
| CatBoost | Gradient Boosting | 0.9385 | 0.9320 | 0.9552 | 0.9435 | 0.9191 | 0.0809 | 0.0448 | 0.8764 | 0.8761 | 0.9842 | 118.9814 | 0.0638 |
| Extra Trees | Bagging Ensemble | 0.9358 | 0.9492 | 0.9303 | 0.9397 | 0.9422 | 0.0578 | 0.0697 | 0.8713 | 0.8711 | 0.9830 | 2.1001 | 0.1236 |
| Random Forest | Bagging Ensemble | 0.9358 | 0.9538 | 0.9254 | 0.9394 | 0.9480 | 0.0520 | 0.0746 | 0.8717 | 0.8712 | 0.9838 | 2.5753 | 0.1315 |
| Decision Tree | Base Non-Linear | 0.9091 | 0.9073 | 0.9254 | 0.9163 | 0.8902 | 0.1098 | 0.0746 | 0.8171 | 0.8169 | 0.9078 | 0.9801 | 0.0082 |
| Logistic Regression | Linear/Probabilistic | 0.8957 | 0.8857 | 0.9254 | 0.9051 | 0.8613 | 0.1387 | 0.0746 | 0.7904 | 0.7895 | 0.9319 | 0.3261 | 0.0057 |
| SVM | Base Non-Linear | 0.8904 | 0.8922 | 0.9055 | 0.8988 | 0.8728 | 0.1272 | 0.0945 | 0.7793 | 0.7792 | 0.9649 | 5.2928 | 1.0465 |
| KNN | Base Non-Linear | 0.8824 | 0.9110 | 0.8657 | 0.8878 | 0.9017 | 0.0983 | 0.1343 | 0.7654 | 0.7643 | 0.9370 | 0.0046 | 0.1317 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.7005 | 0.9083 | 0.4925 | 0.6387 | 0.9422 | 0.0578 | 0.5075 | 0.4770 | 0.4192 | 0.8490 | 0.0494 | 0.0563 |


### Dataset 3 - Joakim Arvidsson (D3)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Extra Trees | Bagging Ensemble | 0.9893 | 0.9915 | 0.9972 | 0.9943 | 0.8696 | 0.1304 | 0.0028 | 0.9045 | 0.9034 | 0.9943 | 0.2774 | 0.0493 |
| LightGBM | Gradient Boosting | 0.9893 | 0.9943 | 0.9943 | 0.9943 | 0.9130 | 0.0870 | 0.0057 | 0.9073 | 0.9073 | 0.9985 | 0.3286 | 0.0513 |
| CatBoost | Gradient Boosting | 0.9866 | 0.9860 | 1.0000 | 0.9929 | 0.7826 | 0.2174 | 0.0000 | 0.8784 | 0.8711 | 0.9995 | 7.8833 | 0.0097 |
| Random Forest | Bagging Ensemble | 0.9866 | 0.9887 | 0.9972 | 0.9929 | 0.8261 | 0.1739 | 0.0028 | 0.8791 | 0.8767 | 0.9982 | 0.4169 | 0.0424 |
| XGBoost | Gradient Boosting | 0.9866 | 0.9915 | 0.9943 | 0.9929 | 0.8696 | 0.1304 | 0.0057 | 0.8820 | 0.8818 | 0.9985 | 0.2128 | 0.0105 |
| KNN | Base Non-Linear | 0.9840 | 0.9887 | 0.9943 | 0.9915 | 0.8261 | 0.1739 | 0.0057 | 0.8561 | 0.8551 | 0.9736 | 0.0015 | 0.0569 |
| Decision Tree | Base Non-Linear | 0.9813 | 0.9886 | 0.9915 | 0.9900 | 0.8261 | 0.1739 | 0.0085 | 0.8347 | 0.8345 | 0.9088 | 0.0180 | 0.0015 |
| SVM | Base Non-Linear | 0.9786 | 0.9804 | 0.9972 | 0.9887 | 0.6957 | 0.3043 | 0.0028 | 0.7990 | 0.7890 | 0.9768 | 0.2265 | 0.0337 |
| Logistic Regression | Linear/Probabilistic | 0.9759 | 0.9777 | 0.9972 | 0.9873 | 0.6522 | 0.3478 | 0.0028 | 0.7709 | 0.7570 | 0.9610 | 0.0250 | 0.0012 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.2032 | 0.9818 | 0.1538 | 0.2660 | 0.9565 | 0.0435 | 0.8462 | 0.0749 | 0.0157 | 0.8643 | 0.0053 | 0.0025 |


### Dataset 4 - AM (D4)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CatBoost | Gradient Boosting | 0.9920 | 0.9894 | 1.0000 | 0.9947 | 0.9684 | 0.0316 | 0.0000 | 0.9788 | 0.9786 | 0.9908 | 11.3364 | 0.0102 |
| LightGBM | Gradient Boosting | 0.9893 | 0.9859 | 1.0000 | 0.9929 | 0.9579 | 0.0421 | 0.0000 | 0.9718 | 0.9714 | 0.9925 | 0.4600 | 0.0186 |
| Random Forest | Bagging Ensemble | 0.9866 | 0.9824 | 1.0000 | 0.9911 | 0.9474 | 0.0526 | 0.0000 | 0.9647 | 0.9641 | 0.9924 | 0.4594 | 0.0440 |
| XGBoost | Gradient Boosting | 0.9840 | 0.9823 | 0.9964 | 0.9893 | 0.9474 | 0.0526 | 0.0036 | 0.9575 | 0.9571 | 0.9949 | 0.2420 | 0.0111 |
| Extra Trees | Bagging Ensemble | 0.9813 | 0.9789 | 0.9964 | 0.9876 | 0.9368 | 0.0632 | 0.0036 | 0.9504 | 0.9497 | 0.9909 | 0.3371 | 0.0522 |
| Decision Tree | Base Non-Linear | 0.9679 | 0.9751 | 0.9821 | 0.9786 | 0.9263 | 0.0737 | 0.0179 | 0.9148 | 0.9147 | 0.9542 | 0.0464 | 0.0011 |
| KNN | Base Non-Linear | 0.9652 | 0.9683 | 0.9857 | 0.9769 | 0.9053 | 0.0947 | 0.0143 | 0.9072 | 0.9067 | 0.9665 | 0.0017 | 0.0280 |
| SVM | Base Non-Linear | 0.9545 | 0.9645 | 0.9749 | 0.9697 | 0.8947 | 0.1053 | 0.0251 | 0.8790 | 0.8788 | 0.9633 | 0.3405 | 0.0639 |
| Logistic Regression | Linear/Probabilistic | 0.9412 | 0.9673 | 0.9534 | 0.9603 | 0.9053 | 0.0947 | 0.0466 | 0.8472 | 0.8469 | 0.9506 | 0.0292 | 0.0013 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.4144 | 0.9839 | 0.2186 | 0.3578 | 0.9895 | 0.0105 | 0.7814 | 0.2436 | 0.1187 | 0.9298 | 0.0046 | 0.0029 |


### Cross-Dataset Transfer (concept-drift proxy)

| Source | Target | Model | Family | common_features | Accuracy | Precision | Recall | F1-Score | MCC | AUC-ROC |
|---|---|---|---|---|---|---|---|---|---|---|
| D3 | D4 | XGBoost | Gradient Boosting | 51 | 0.6720 | 0.8608 | 0.6672 | 0.7518 | 0.3117 | 0.7497 |
| D3 | D4 | LightGBM | Gradient Boosting | 51 | 0.6489 | 0.8411 | 0.6514 | 0.7342 | 0.2587 | 0.7174 |
| D3 | D4 | CatBoost | Gradient Boosting | 51 | 0.7824 | 0.8771 | 0.8231 | 0.8492 | 0.4630 | 0.8265 |
| D3 | D4 | Random Forest | Bagging Ensemble | 51 | 0.7764 | 0.9183 | 0.7679 | 0.8364 | 0.5119 | 0.8076 |
| D3 | D4 | Extra Trees | Bagging Ensemble | 51 | 0.6270 | 0.7887 | 0.6815 | 0.7312 | 0.1364 | 0.6639 |
| D3 | D4 | Decision Tree | Base Non-Linear | 51 | 0.5701 | 0.8602 | 0.5045 | 0.6360 | 0.2336 | 0.6328 |
| D3 | D4 | SVM | Base Non-Linear | 51 | 0.7447 | 0.7688 | 0.9398 | 0.8457 | 0.1774 | 0.8318 |
| D3 | D4 | KNN | Base Non-Linear | 51 | 0.6814 | 0.7895 | 0.7798 | 0.7847 | 0.1723 | 0.5775 |
| D3 | D4 | Logistic Regression | Linear/Probabilistic | 51 | 0.8821 | 0.9370 | 0.9023 | 0.9193 | 0.7025 | 0.9170 |
| D3 | D4 | Gaussian Naive Bayes | Linear/Probabilistic | 51 | 0.2907 | 0.5582 | 0.2264 | 0.3221 | -0.2808 | 0.4715 |
| D4 | D3 | XGBoost | Gradient Boosting | 51 | 0.7891 | 0.9404 | 0.8273 | 0.8802 | 0.0302 | 0.3392 |
| D4 | D3 | LightGBM | Gradient Boosting | 51 | 0.6184 | 0.9264 | 0.6439 | 0.7598 | -0.0598 | 0.3067 |
| D4 | D3 | CatBoost | Gradient Boosting | 51 | 0.8033 | 0.9421 | 0.8419 | 0.8892 | 0.0474 | 0.3677 |
| D4 | D3 | Random Forest | Bagging Ensemble | 51 | 0.7741 | 0.9403 | 0.8104 | 0.8705 | 0.0273 | 0.3701 |
| D4 | D3 | Extra Trees | Bagging Ensemble | 51 | 0.9003 | 0.9455 | 0.9482 | 0.9469 | 0.1380 | 0.4607 |
| D4 | D3 | Decision Tree | Base Non-Linear | 51 | 0.8376 | 0.9410 | 0.8820 | 0.9106 | 0.0438 | 0.5295 |
| D4 | D3 | SVM | Base Non-Linear | 51 | 0.8922 | 0.9500 | 0.9342 | 0.9420 | 0.1825 | 0.5131 |
| D4 | D3 | KNN | Base Non-Linear | 51 | 0.6678 | 0.9469 | 0.6837 | 0.7941 | 0.0590 | 0.5847 |
| D4 | D3 | Logistic Regression | Linear/Probabilistic | 51 | 0.8069 | 0.9409 | 0.8471 | 0.8915 | 0.0370 | 0.5618 |
| D4 | D3 | Gaussian Naive Bayes | Linear/Probabilistic | 51 | 0.1423 | 0.9897 | 0.0856 | 0.1576 | 0.0643 | 0.7376 |


### Cross-Validation (mean ± std)

| Dataset | Model | Family | F1 mean | F1 std | Accuracy mean | Accuracy std | folds | n_samples |
|---|---|---|---|---|---|---|---|---|
| D1 | XGBoost | Gradient Boosting | 0.9719 | 0.0066 | 0.9731 | 0.0063 | 5 | 2157 |
| D1 | LightGBM | Gradient Boosting | 0.9739 | 0.0077 | 0.9750 | 0.0074 | 5 | 2157 |
| D1 | CatBoost | Gradient Boosting | 0.9730 | 0.0078 | 0.9740 | 0.0075 | 5 | 2157 |
| D1 | Random Forest | Bagging Ensemble | 0.9660 | 0.0071 | 0.9675 | 0.0069 | 5 | 2157 |
| D1 | Extra Trees | Bagging Ensemble | 0.9669 | 0.0045 | 0.9685 | 0.0043 | 5 | 2157 |
| D1 | Decision Tree | Base Non-Linear | 0.9407 | 0.0054 | 0.9434 | 0.0054 | 5 | 2157 |
| D1 | SVM | Base Non-Linear | 0.9477 | 0.0064 | 0.9499 | 0.0060 | 5 | 2157 |
| D1 | KNN | Base Non-Linear | 0.9328 | 0.0084 | 0.9370 | 0.0071 | 5 | 2157 |
| D1 | Logistic Regression | Linear/Probabilistic | 0.9554 | 0.0067 | 0.9574 | 0.0064 | 5 | 2157 |
| D1 | Gaussian Naive Bayes | Linear/Probabilistic | 0.3227 | 0.0283 | 0.6036 | 0.0120 | 5 | 2157 |
| D2 | XGBoost | Gradient Boosting | 0.9684 | 0.0028 | 0.9662 | 0.0030 | 5 | 6978 |
| D2 | LightGBM | Gradient Boosting | 0.9723 | 0.0029 | 0.9703 | 0.0032 | 5 | 6978 |
| D2 | CatBoost | Gradient Boosting | 0.9698 | 0.0030 | 0.9676 | 0.0032 | 5 | 6978 |
| D2 | Random Forest | Bagging Ensemble | 0.9611 | 0.0036 | 0.9589 | 0.0038 | 5 | 6978 |
| D2 | Extra Trees | Bagging Ensemble | 0.9563 | 0.0022 | 0.9539 | 0.0024 | 5 | 6978 |
| D2 | Decision Tree | Base Non-Linear | 0.9386 | 0.0051 | 0.9335 | 0.0058 | 5 | 6978 |
| D2 | SVM | Base Non-Linear | 0.9411 | 0.0046 | 0.9374 | 0.0052 | 5 | 6978 |
| D2 | KNN | Base Non-Linear | 0.9207 | 0.0064 | 0.9166 | 0.0066 | 5 | 6978 |
| D2 | Logistic Regression | Linear/Probabilistic | 0.9281 | 0.0082 | 0.9226 | 0.0091 | 5 | 6978 |
| D2 | Gaussian Naive Bayes | Linear/Probabilistic | 0.5975 | 0.0048 | 0.6780 | 0.0052 | 5 | 6978 |
| D3 | XGBoost | Gradient Boosting | 0.9957 | 0.0010 | 0.9920 | 0.0018 | 5 | 8000 |
| D3 | LightGBM | Gradient Boosting | 0.9955 | 0.0008 | 0.9915 | 0.0015 | 5 | 8000 |
| D3 | CatBoost | Gradient Boosting | 0.9953 | 0.0008 | 0.9912 | 0.0015 | 5 | 8000 |
| D3 | Random Forest | Bagging Ensemble | 0.9956 | 0.0009 | 0.9918 | 0.0017 | 5 | 8000 |
| D3 | Extra Trees | Bagging Ensemble | 0.9939 | 0.0012 | 0.9885 | 0.0023 | 5 | 8000 |
| D3 | Decision Tree | Base Non-Linear | 0.9932 | 0.0009 | 0.9873 | 0.0017 | 5 | 8000 |
| D3 | SVM | Base Non-Linear | 0.9857 | 0.0016 | 0.9729 | 0.0030 | 5 | 8000 |
| D3 | KNN | Base Non-Linear | 0.9911 | 0.0007 | 0.9832 | 0.0013 | 5 | 8000 |
| D3 | Logistic Regression | Linear/Probabilistic | 0.9834 | 0.0011 | 0.9686 | 0.0021 | 5 | 8000 |
| D3 | Gaussian Naive Bayes | Linear/Probabilistic | 0.2634 | 0.0181 | 0.2044 | 0.0112 | 5 | 8000 |
| D4 | XGBoost | Gradient Boosting | 0.9942 | 0.0008 | 0.9914 | 0.0012 | 5 | 8000 |
| D4 | LightGBM | Gradient Boosting | 0.9951 | 0.0004 | 0.9926 | 0.0006 | 5 | 8000 |
| D4 | CatBoost | Gradient Boosting | 0.9947 | 0.0008 | 0.9921 | 0.0012 | 5 | 8000 |
| D4 | Random Forest | Bagging Ensemble | 0.9931 | 0.0011 | 0.9898 | 0.0016 | 5 | 8000 |
| D4 | Extra Trees | Bagging Ensemble | 0.9915 | 0.0020 | 0.9872 | 0.0030 | 5 | 8000 |
| D4 | Decision Tree | Base Non-Linear | 0.9897 | 0.0029 | 0.9846 | 0.0043 | 5 | 8000 |
| D4 | SVM | Base Non-Linear | 0.9793 | 0.0032 | 0.9689 | 0.0049 | 5 | 8000 |
| D4 | KNN | Base Non-Linear | 0.9800 | 0.0035 | 0.9703 | 0.0052 | 5 | 8000 |
| D4 | Logistic Regression | Linear/Probabilistic | 0.9738 | 0.0026 | 0.9610 | 0.0038 | 5 | 8000 |
| D4 | Gaussian Naive Bayes | Linear/Probabilistic | 0.2636 | 0.0077 | 0.3673 | 0.0043 | 5 | 8000 |


### Green-AI Headline

- Best model: **CatBoost** on **D4** — Accuracy 0.9920, F1 0.9947, trained in 11.34s on CPU-only commodity endpoint; no GPU/TPU acceleration used.

- Compare against DL baselines in `config.DL_BASELINES` (e.g. Xception ColSeq 98.20% / 93.73%), all GPU-trained.
