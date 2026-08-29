# Results Summary — run `20260618-155816-full-7f40fe`


### Dataset 1 - Mendeley Data (D1)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XGBoost | Gradient Boosting | 0.9861 | 0.9761 | 0.9951 | 0.9855 | 0.9780 | 0.0220 | 0.0049 | 0.9723 | 0.9722 | 0.9979 | 3.7873 | 0.0123 |
| Random Forest | Bagging Ensemble | 0.9792 | 0.9667 | 0.9902 | 0.9783 | 0.9692 | 0.0308 | 0.0098 | 0.9585 | 0.9583 | 0.9981 | 1.2536 | 0.0479 |
| CatBoost | Gradient Boosting | 0.9769 | 0.9577 | 0.9951 | 0.9761 | 0.9604 | 0.0396 | 0.0049 | 0.9543 | 0.9537 | 0.9984 | 69.2491 | 0.0176 |
| LightGBM | Gradient Boosting | 0.9769 | 0.9665 | 0.9854 | 0.9758 | 0.9692 | 0.0308 | 0.0146 | 0.9538 | 0.9536 | 0.9986 | 2.7055 | 0.0202 |
| Extra Trees | Bagging Ensemble | 0.9769 | 0.9665 | 0.9854 | 0.9758 | 0.9692 | 0.0308 | 0.0146 | 0.9538 | 0.9536 | 0.9990 | 1.2678 | 0.0594 |
| Logistic Regression | Linear/Probabilistic | 0.9745 | 0.9709 | 0.9756 | 0.9732 | 0.9736 | 0.0264 | 0.0244 | 0.9490 | 0.9490 | 0.9892 | 0.3204 | 0.0060 |
| SVM | Base Non-Linear | 0.9606 | 0.9393 | 0.9805 | 0.9594 | 0.9427 | 0.0573 | 0.0195 | 0.9221 | 0.9213 | 0.9956 | 7.8683 | 0.9799 |
| KNN | Base Non-Linear | 0.9491 | 0.9420 | 0.9512 | 0.9466 | 0.9471 | 0.0529 | 0.0488 | 0.8980 | 0.8979 | 0.9834 | 0.0124 | 0.3319 |
| Decision Tree | Base Non-Linear | 0.9421 | 0.9245 | 0.9561 | 0.9400 | 0.9295 | 0.0705 | 0.0439 | 0.8846 | 0.8842 | 0.9428 | 0.5435 | 0.0037 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.5972 | 0.8444 | 0.1854 | 0.3040 | 0.9692 | 0.0308 | 0.8146 | 0.2526 | 0.1606 | 0.6265 | 0.0608 | 0.0231 |


### Dataset 2 - Oriola Kolawole (D2)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LightGBM | Gradient Boosting | 0.9656 | 0.9744 | 0.9614 | 0.9678 | 0.9705 | 0.0295 | 0.0386 | 0.9310 | 0.9309 | 0.9965 | 5.8239 | 0.0131 |
| CatBoost | Gradient Boosting | 0.9628 | 0.9691 | 0.9614 | 0.9652 | 0.9643 | 0.0357 | 0.0386 | 0.9252 | 0.9251 | 0.9943 | 115.9628 | 0.0104 |
| XGBoost | Gradient Boosting | 0.9585 | 0.9676 | 0.9547 | 0.9611 | 0.9628 | 0.0372 | 0.0453 | 0.9166 | 0.9165 | 0.9951 | 10.4996 | 0.0078 |
| Random Forest | Bagging Ensemble | 0.9563 | 0.9792 | 0.9387 | 0.9585 | 0.9767 | 0.0233 | 0.0613 | 0.9133 | 0.9124 | 0.9938 | 3.9589 | 0.0224 |
| Extra Trees | Bagging Ensemble | 0.9549 | 0.9791 | 0.9361 | 0.9571 | 0.9767 | 0.0233 | 0.0639 | 0.9106 | 0.9095 | 0.9928 | 2.8216 | 0.0280 |
| Decision Tree | Base Non-Linear | 0.9420 | 0.9455 | 0.9467 | 0.9461 | 0.9364 | 0.0636 | 0.0533 | 0.8833 | 0.8833 | 0.9416 | 1.7986 | 0.0025 |
| SVM | Base Non-Linear | 0.9398 | 0.9513 | 0.9361 | 0.9436 | 0.9442 | 0.0558 | 0.0639 | 0.8792 | 0.8791 | 0.9835 | 62.8365 | 2.3705 |
| Logistic Regression | Linear/Probabilistic | 0.9277 | 0.9299 | 0.9361 | 0.9330 | 0.9178 | 0.0822 | 0.0639 | 0.8544 | 0.8544 | 0.9651 | 1.8177 | 0.0036 |
| KNN | Base Non-Linear | 0.9191 | 0.9443 | 0.9028 | 0.9231 | 0.9380 | 0.0620 | 0.0972 | 0.8387 | 0.8378 | 0.9724 | 0.0287 | 0.3440 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.6834 | 0.9120 | 0.4554 | 0.6075 | 0.9488 | 0.0512 | 0.5446 | 0.4547 | 0.3883 | 0.8492 | 0.1807 | 0.0191 |


### Dataset 3 - Joakim Arvidsson (D3)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LightGBM | Gradient Boosting | 0.9940 | 0.9964 | 0.9971 | 0.9968 | 0.9467 | 0.0533 | 0.0029 | 0.9485 | 0.9485 | 0.9961 | 0.6560 | 0.0061 |
| Random Forest | Bagging Ensemble | 0.9936 | 0.9957 | 0.9975 | 0.9966 | 0.9360 | 0.0640 | 0.0025 | 0.9453 | 0.9453 | 0.9974 | 4.0013 | 0.0113 |
| XGBoost | Gradient Boosting | 0.9936 | 0.9959 | 0.9973 | 0.9966 | 0.9387 | 0.0613 | 0.0027 | 0.9455 | 0.9454 | 0.9944 | 0.6047 | 0.0018 |
| CatBoost | Gradient Boosting | 0.9931 | 0.9950 | 0.9977 | 0.9963 | 0.9253 | 0.0747 | 0.0023 | 0.9408 | 0.9406 | 0.9962 | 12.2618 | 0.0025 |
| Extra Trees | Bagging Ensemble | 0.9916 | 0.9945 | 0.9966 | 0.9955 | 0.9173 | 0.0827 | 0.0034 | 0.9279 | 0.9278 | 0.9947 | 2.5941 | 0.0173 |
| Decision Tree | Base Non-Linear | 0.9904 | 0.9955 | 0.9943 | 0.9949 | 0.9333 | 0.0667 | 0.0057 | 0.9196 | 0.9196 | 0.9638 | 0.4675 | 0.0003 |
| KNN | Base Non-Linear | 0.9867 | 0.9914 | 0.9945 | 0.9929 | 0.8720 | 0.1280 | 0.0055 | 0.8854 | 0.8852 | 0.9674 | 0.0086 | 0.2412 |
| SVM | Base Non-Linear | 0.9708 | 0.9732 | 0.9962 | 0.9846 | 0.5920 | 0.4080 | 0.0038 | 0.7223 | 0.7038 | 0.9657 | 38.9867 | 0.1795 |
| Logistic Regression | Linear/Probabilistic | 0.9656 | 0.9703 | 0.9937 | 0.9819 | 0.5467 | 0.4533 | 0.0063 | 0.6675 | 0.6495 | 0.9454 | 0.1256 | 0.0002 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.1793 | 0.9957 | 0.1248 | 0.2217 | 0.9920 | 0.0080 | 0.8752 | 0.0881 | 0.0165 | 0.8542 | 0.0270 | 0.0010 |


### Dataset 4 - AM (D4)

| Model | Family | Accuracy | Precision | Recall | F1-Score | Specificity | FPR | FNR | MCC | Cohen Kappa | AUC-ROC | Training Time (s) | Inference ms/sample |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LightGBM | Gradient Boosting | 0.9924 | 0.9908 | 0.9990 | 0.9949 | 0.9731 | 0.0269 | 0.0010 | 0.9799 | 0.9797 | 0.9981 | 0.9132 | 0.0061 |
| CatBoost | Gradient Boosting | 0.9921 | 0.9905 | 0.9990 | 0.9947 | 0.9721 | 0.0279 | 0.0010 | 0.9792 | 0.9791 | 0.9967 | 15.0540 | 0.0025 |
| XGBoost | Gradient Boosting | 0.9916 | 0.9902 | 0.9986 | 0.9944 | 0.9711 | 0.0289 | 0.0014 | 0.9779 | 0.9777 | 0.9984 | 0.8790 | 0.0022 |
| Random Forest | Bagging Ensemble | 0.9913 | 0.9898 | 0.9986 | 0.9942 | 0.9701 | 0.0299 | 0.0014 | 0.9772 | 0.9770 | 0.9981 | 3.8457 | 0.0118 |
| Extra Trees | Bagging Ensemble | 0.9893 | 0.9885 | 0.9973 | 0.9928 | 0.9661 | 0.0339 | 0.0027 | 0.9718 | 0.9716 | 0.9964 | 2.1735 | 0.0246 |
| Decision Tree | Base Non-Linear | 0.9865 | 0.9881 | 0.9938 | 0.9910 | 0.9651 | 0.0349 | 0.0062 | 0.9644 | 0.9643 | 0.9799 | 0.5475 | 0.0004 |
| KNN | Base Non-Linear | 0.9781 | 0.9833 | 0.9873 | 0.9853 | 0.9511 | 0.0489 | 0.0127 | 0.9422 | 0.9422 | 0.9851 | 0.0078 | 0.1995 |
| SVM | Base Non-Linear | 0.9679 | 0.9710 | 0.9863 | 0.9786 | 0.9143 | 0.0857 | 0.0137 | 0.9148 | 0.9143 | 0.9799 | 30.5418 | 0.2484 |
| Logistic Regression | Linear/Probabilistic | 0.9518 | 0.9678 | 0.9675 | 0.9676 | 0.9063 | 0.0937 | 0.0325 | 0.8735 | 0.8735 | 0.9727 | 0.1854 | 0.0002 |
| Gaussian Naive Bayes | Linear/Probabilistic | 0.3699 | 0.9891 | 0.1551 | 0.2682 | 0.9950 | 0.0050 | 0.8449 | 0.2040 | 0.0832 | 0.9294 | 0.0280 | 0.0014 |


### Cross-Dataset Transfer (concept-drift proxy)

| Source | Target | Model | Family | common_features | Accuracy | Precision | Recall | F1-Score | MCC | AUC-ROC |
|---|---|---|---|---|---|---|---|---|---|---|
| D3 | D4 | XGBoost | Gradient Boosting | 51 | 0.6924 | 0.8873 | 0.6722 | 0.7649 | 0.3725 | 0.7711 |
| D3 | D4 | LightGBM | Gradient Boosting | 51 | 0.6489 | 0.8411 | 0.6514 | 0.7342 | 0.2587 | 0.7174 |
| D3 | D4 | CatBoost | Gradient Boosting | 51 | 0.7824 | 0.8771 | 0.8231 | 0.8492 | 0.4630 | 0.8265 |
| D3 | D4 | Random Forest | Bagging Ensemble | 51 | 0.7764 | 0.9183 | 0.7679 | 0.8364 | 0.5119 | 0.8076 |
| D3 | D4 | Extra Trees | Bagging Ensemble | 51 | 0.6270 | 0.7887 | 0.6815 | 0.7312 | 0.1364 | 0.6639 |
| D3 | D4 | Decision Tree | Base Non-Linear | 51 | 0.5701 | 0.8602 | 0.5045 | 0.6360 | 0.2336 | 0.6328 |
| D3 | D4 | SVM | Base Non-Linear | 51 | 0.7447 | 0.7688 | 0.9398 | 0.8457 | 0.1774 | 0.8318 |
| D3 | D4 | KNN | Base Non-Linear | 51 | 0.6814 | 0.7895 | 0.7798 | 0.7847 | 0.1723 | 0.5775 |
| D3 | D4 | Logistic Regression | Linear/Probabilistic | 51 | 0.8821 | 0.9370 | 0.9023 | 0.9193 | 0.7025 | 0.9170 |
| D3 | D4 | Gaussian Naive Bayes | Linear/Probabilistic | 51 | 0.2907 | 0.5582 | 0.2264 | 0.3221 | -0.2808 | 0.4715 |
| D4 | D3 | XGBoost | Gradient Boosting | 51 | 0.7737 | 0.9386 | 0.8116 | 0.8705 | 0.0133 | 0.3305 |
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
| D1 | XGBoost | Gradient Boosting | 0.9655 | 0.0057 | 0.9671 | 0.0054 | 5 | 2157 |
| D1 | LightGBM | Gradient Boosting | 0.9704 | 0.0036 | 0.9717 | 0.0034 | 5 | 2157 |
| D1 | CatBoost | Gradient Boosting | 0.9677 | 0.0087 | 0.9689 | 0.0084 | 5 | 2157 |
| D1 | Random Forest | Bagging Ensemble | 0.9621 | 0.0077 | 0.9638 | 0.0073 | 5 | 2157 |
| D1 | Extra Trees | Bagging Ensemble | 0.9629 | 0.0068 | 0.9648 | 0.0063 | 5 | 2157 |
| D1 | Decision Tree | Base Non-Linear | 0.9272 | 0.0084 | 0.9309 | 0.0077 | 5 | 2157 |
| D1 | SVM | Base Non-Linear | 0.9430 | 0.0150 | 0.9453 | 0.0145 | 5 | 2157 |
| D1 | KNN | Base Non-Linear | 0.9300 | 0.0114 | 0.9337 | 0.0112 | 5 | 2157 |
| D1 | Logistic Regression | Linear/Probabilistic | 0.9488 | 0.0118 | 0.9513 | 0.0114 | 5 | 2157 |
| D1 | Gaussian Naive Bayes | Linear/Probabilistic | 0.3150 | 0.0288 | 0.6013 | 0.0139 | 5 | 2157 |
| D2 | XGBoost | Gradient Boosting | 0.9686 | 0.0028 | 0.9665 | 0.0030 | 5 | 6978 |
| D2 | LightGBM | Gradient Boosting | 0.9707 | 0.0011 | 0.9686 | 0.0012 | 5 | 6978 |
| D2 | CatBoost | Gradient Boosting | 0.9682 | 0.0016 | 0.9659 | 0.0017 | 5 | 6978 |
| D2 | Random Forest | Bagging Ensemble | 0.9606 | 0.0014 | 0.9583 | 0.0015 | 5 | 6978 |
| D2 | Extra Trees | Bagging Ensemble | 0.9583 | 0.0023 | 0.9559 | 0.0027 | 5 | 6978 |
| D2 | Decision Tree | Base Non-Linear | 0.9400 | 0.0020 | 0.9351 | 0.0020 | 5 | 6978 |
| D2 | SVM | Base Non-Linear | 0.9394 | 0.0038 | 0.9355 | 0.0037 | 5 | 6978 |
| D2 | KNN | Base Non-Linear | 0.9194 | 0.0037 | 0.9154 | 0.0039 | 5 | 6978 |
| D2 | Logistic Regression | Linear/Probabilistic | 0.9277 | 0.0030 | 0.9219 | 0.0031 | 5 | 6978 |
| D2 | Gaussian Naive Bayes | Linear/Probabilistic | 0.5953 | 0.0180 | 0.6766 | 0.0086 | 5 | 6978 |
| D3 | XGBoost | Gradient Boosting | 0.9955 | 0.0009 | 0.9915 | 0.0017 | 5 | 8000 |
| D3 | LightGBM | Gradient Boosting | 0.9958 | 0.0009 | 0.9921 | 0.0017 | 5 | 8000 |
| D3 | CatBoost | Gradient Boosting | 0.9947 | 0.0010 | 0.9901 | 0.0019 | 5 | 8000 |
| D3 | Random Forest | Bagging Ensemble | 0.9949 | 0.0011 | 0.9904 | 0.0021 | 5 | 8000 |
| D3 | Extra Trees | Bagging Ensemble | 0.9945 | 0.0015 | 0.9897 | 0.0029 | 5 | 8000 |
| D3 | Decision Tree | Base Non-Linear | 0.9925 | 0.0013 | 0.9859 | 0.0024 | 5 | 8000 |
| D3 | SVM | Base Non-Linear | 0.9837 | 0.0014 | 0.9691 | 0.0027 | 5 | 8000 |
| D3 | KNN | Base Non-Linear | 0.9908 | 0.0010 | 0.9826 | 0.0019 | 5 | 8000 |
| D3 | Logistic Regression | Linear/Probabilistic | 0.9835 | 0.0025 | 0.9688 | 0.0049 | 5 | 8000 |
| D3 | Gaussian Naive Bayes | Linear/Probabilistic | 0.2779 | 0.0164 | 0.2134 | 0.0102 | 5 | 8000 |
| D4 | XGBoost | Gradient Boosting | 0.9941 | 0.0014 | 0.9911 | 0.0022 | 5 | 8000 |
| D4 | LightGBM | Gradient Boosting | 0.9941 | 0.0012 | 0.9912 | 0.0019 | 5 | 8000 |
| D4 | CatBoost | Gradient Boosting | 0.9945 | 0.0017 | 0.9918 | 0.0025 | 5 | 8000 |
| D4 | Random Forest | Bagging Ensemble | 0.9932 | 0.0012 | 0.9899 | 0.0019 | 5 | 8000 |
| D4 | Extra Trees | Bagging Ensemble | 0.9908 | 0.0017 | 0.9863 | 0.0027 | 5 | 8000 |
| D4 | Decision Tree | Base Non-Linear | 0.9888 | 0.0006 | 0.9834 | 0.0009 | 5 | 8000 |
| D4 | SVM | Base Non-Linear | 0.9791 | 0.0018 | 0.9686 | 0.0027 | 5 | 8000 |
| D4 | KNN | Base Non-Linear | 0.9824 | 0.0029 | 0.9738 | 0.0043 | 5 | 8000 |
| D4 | Logistic Regression | Linear/Probabilistic | 0.9736 | 0.0035 | 0.9605 | 0.0052 | 5 | 8000 |
| D4 | Gaussian Naive Bayes | Linear/Probabilistic | 0.3157 | 0.0354 | 0.3935 | 0.0196 | 5 | 8000 |


### Green-AI Headline

- Best model: **LightGBM** on **D3** — Accuracy 0.9940, F1 0.9968, trained in 0.66s on CPU-only commodity endpoint; no GPU/TPU acceleration used.

- Compare against DL baselines in `config.DL_BASELINES` (e.g. Xception ColSeq 98.20% / 93.73%), all GPU-trained.
