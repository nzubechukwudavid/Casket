# CHAPTER FIVE: SUMMARY, RECOMMENDATION AND CONCLUSION

## 5.1 Summary
This research investigated the performance and computational efficiency of static ransomware and malware detection using ensemble machine learning on tabular Portable Executable (PE) header data. Operating under the "Green AI" paradigm, the core objective was to demonstrate that lightweight machine learning ensembles running on CPU-only commodity hardware can match or exceed the performance of published deep learning (DL) models trained on expensive, energy-intensive GPU infrastructure.

To achieve this aim, the study systematically addressed and successfully accomplished each of the key research objectives established for this investigation:

1.  **Compilation and Preprocessing of Structurally Independent PE Header Datasets:**
    This was achieved by assembling and preprocessing 58,547 total samples across four distinct repositories, representing raw-byte representations (Dataset 1: Moreira et al., and Dataset 2: Oriola Kolawole) and parsed header/directory metadata (Dataset 3: Joakim Arvidsson, and Dataset 4: AM). Preprocessing successfully removed identifier metadata, mapped multiclass labels to binary targets, and standardized features using stratified 80:20 splits to strictly prevent preprocessing data leakage.
2.  **Implementation and Benchmarking of Diverse Algorithmic Paradigms:**
    Ten machine learning models representing four algorithmic families were successfully implemented and trained: Gradient Boosting (LightGBM, XGBoost, CatBoost), Bagging Ensembles (Random Forest, Extra Trees), Base Non-Linear (Decision Trees, SVM, KNN), and Linear/Probabilistic models (Logistic Regression, Gaussian Naive Bayes) for binary classification.
3.  **Comprehensive Performance Comparison Across Exhaustive Evaluation Metrics:**
    All ten models were evaluated on each dataset using exactly eleven metrics (summarized in Tables 4.2–4.5). The benchmarking confirmed that tree-based gradient boosting models outperform all other families. Specifically, **LightGBM** achieved an outstanding F1-score of **0.9968** and an overall accuracy of **0.9940%** on Dataset 3, while **XGBoost** achieved the highest F1-score of **0.9855** on Dataset 1.
4.  **Rigorous Robustness and Consistency Evaluation Under Cross-Validation and Concept Drift:**
    Consistency was verified through 5-fold stratified cross-validation and cross-dataset transfer tests. Cross-validation confirmed the high stability of gradient boosting models (F1 standard deviation $\le 0.0087$). Cross-dataset transfer (testing on Dataset 4 with models trained on Dataset 3, and vice versa, using 51 shared features) acted as a proxy for concept drift, demonstrating that simple linear classifiers (Logistic Regression) and highly randomized tree models (Extra Trees) generalize best under domain shift.
5.  **Comparative Profiling of Computational Efficiency Against Literature Baselines:**
    Profiling confirmed that LightGBM minimizes the training footprint (under 1 second on CPU), inference latency (0.006 ms/sample), and model size (under 250 KB). A comparative analysis against the literature confirmed that the proposed CPU-only classifiers systematically outperform GPU-trained models (e.g., LightGBM on Dataset 2 achieved **96.56%** accuracy, outperforming **Xception ColSeq CNN**'s 93.73% and **LSTM**'s 93.25%), successfully validating the Green AI advantage.


---

## 5.2 Recommendation
Based on the findings and computational analysis of this study, the following recommendations are proposed for endpoint security design and future research:

1.  **Prioritization of Lightweight Tree Ensembles for Endpoints:** 
    For active malware monitoring on consumer-grade and corporate endpoint devices, security developers should prioritize gradient boosting ensembles—specifically **LightGBM**—over deep neural networks or support vector machines. LightGBM combines near-perfect accuracy with microsecond inference latency (0.006 ms/sample) and a highly compact storage footprint (under 250 KB), making it ideal for background execution without causing user-perceived performance degradation.
2.  **Utilization of Parsed Metadata Features over Raw Bytes:** 
    When designing static detection engines, parsed structural PE header fields (such as those in Datasets 3 and 4) should be preferred over raw byte-frequency sequences. Structuring the feature space into named optional-header and section-directory metadata yields F1-scores exceeding 0.99, compared to raw byte-level F1-scores which capped around 0.96–0.98.
3.  **Strict Avoidance of Preprocessing Data Leakage:** 
    It is recommended that security evaluation frameworks strictly partition training and testing data *before* performing feature standardization. Fitting standardizers on the entire dataset leaks out-of-sample statistical parameters (mean and variance) into the training sets, resulting in overly optimistic accuracy metrics that fail to generalize in real-world settings.
4.  **Integration of Cross-Dataset Generalization Checks:** 
    Academic and industrial evaluations of malware classifiers should incorporate cross-dataset transfer tests rather than relying solely on cross-validation. Evaluating models on independent databases (such as Dataset 3 to Dataset 4) reveals the true degradation caused by concept drift and database bias, providing a more realistic measure of real-world deployment performance.

---

## 5.3 Conclusion
In conclusion, this study has successfully demonstrated the feasibility and superiority of Green AI in static ransomware and malware detection. By leveraging lightweight ensemble machine learning on tabular PE-header data, the need for energy-intensive GPU acceleration is completely bypassed. 

The primary contribution of this research is the empirical and statistical validation that tree-based gradient boosting models (like LightGBM and XGBoost) running on commodity CPUs can outperform complex, GPU-bound Deep Learning architectures (such as Xception ColSeq CNNs and LSTMs) on identical raw-byte and structured PE-header representations. This finding shifts the paradigm of static malware detection, proving that endpoint security solutions do not need to trade computational resources or energy efficiency to achieve state-of-the-art classification performance.
