About Dataset
🧾 Dataset Description

This dataset is designed for malware detection research using machine learning techniques and is based on static analysis of Microsoft Windows Portable Executable (PE) files.

The data consists of 79 numerical features extracted from different structural components of PE files, including various headers and sections defined in the official Windows PE format specification. These features represent low-level metadata and structural characteristics of executable files and are commonly used in academic and industrial malware analysis.

Each sample in the dataset corresponds to a single Windows executable file, labeled as either malicious or benign, making the dataset suitable for binary classification tasks.

📦 Feature Extraction**

All features were extracted through static analysis, meaning that executable files were analyzed without being executed. This approach is safer, faster, and widely adopted in real-world malware detection systems.

The extracted features are derived from standard PE file components such as:

*DOS Header
*File Header1.
*Optional Header
*Section-related metadata

A detailed explanation of the PE file structure and all related fields can be found in the official Microsoft documentation:

👉 Microsoft PE and COFF Specification**
https://learn.microsoft.com/en-us/windows/win32/debug/pe-format

This dataset does not redefine or modify any PE fields; it strictly follows the official specification provided by Microsoft.

🎯 Intended Use Cases

This dataset can be used for:

Malware vs. benign file classification
Benchmarking machine learning algorithms
Feature selection and importance analysis
Academic research and student projects
Comparative studies between traditional ML and advanced models
It is especially suitable for experimenting with algorithms such as:

Logistic Regression
Random Forest
Gradient Boosting (XGBoost, LightGBM, CatBoost)
Support Vector Machines
**
⚠️ Important Notes**

This dataset is intended for research and educational purposes only.
The dataset relies solely on static features and does not include behavioral or dynamic analysis.
Malware samples are labeled based on their known status at the time of dataset creation.
The dataset does not contain executable files, only extracted numerical features, ensuring safety for users.
**
📊 Dataset Characteristics**

Data type: Tabular (CSV)
Number of features: 79
Target variable: Binary (Malware / Benign)
Analysis type: Static malware analysis
Operating system: Microsoft Windows
📚 References

Microsoft Documentation – PE File Format
https://learn.microsoft.com/en-us/windows/win32/debug/pe-format