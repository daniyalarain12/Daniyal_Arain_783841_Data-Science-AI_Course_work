# Breast Cancer Classification & Pipeline Optimization

A production-grade binary classification project developed in Python using Scikit-Learn. This project analyzes clinical biopsy records to predict whether a breast mass tumor is **Malignant** or **Benign**. It implements an optimal, leakage-free modeling architecture and highlights the impact of L1 (Lasso) and L2 (Ridge) regularization on model generalization.

## 🛠️ Key Technical Features
* **Leakage-Free Architecture:** Implements a Scikit-Learn `Pipeline` pairing `StandardScaler` feature transformations and estimators together, systematically preventing data leakage during validation splits.
* **Hyperparameter Optimization:** Utilizes `GridSearchCV` to run exhaustive cross-validation searches across candidate regularization strengths (`C`) and stopping tolerances (`tol`).
* **Rigorous Evaluation Matrices:** Evaluates baseline models against regularized variants across Accuracy, Precision, Recall, and F1-Score to ensure high clinical reliability.

## 📊 Dataset Metadata
* **Dataset:** Breast Cancer Dataset (Kaggle)
* **Observations:** 569 patient biopsies
* **Total Features:** 30 continuous numeric attributes representing cellular dimensions (radius, perimeter, area, smoothness, concavity, etc.)
* **Target Layout:** `diagnosis` (Malignant = 1, Benign = 0)

---

## 📈 Model Performance Benchmarks

The hyperparameter optimization process selected **Ridge Logistic Regression** as the champion configuration, improving overall classification accuracy and precision metrics:

| Model | Best Parameters | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression (Baseline)** | N/A | 0.9737 | 0.9762 | 0.9535 | 0.9647 |
| **Ridge Logistic Regression** | `{'C': 1, 'tol': 0.001}` | **0.9825** | **0.9767** | **0.9767** | **0.9767** |
| **Lasso Logistic Regression** | `{'C': 1, 'tol': 1e-05}` | 0.9737 | 0.9762 | 0.9535 | 0.9647 |

### 🔍 Key Findings & Analytical Takeaways
1. **GridSearchCV Evaluation:** Adding an L2 regularization penalty (`C=1`, `tol=0.001`) via grid search effectively penalized unnecessary coefficient variances, reducing model overfitting and lifting generalization test accuracy by **0.88%**.
2. **Clinical Sensitivity (Recall Boost):** Crucially for a medical application, the tuned Ridge model forced the Recall rate up from **95.35% to 97.67%**, successfully reducing critical False Negatives down to just 1 case out of 114 test patients.
3. **Confusion Matrix Breakdown:** On the out-of-sample test split, the production pipeline achieved **112 correct diagnoses** (70 True Negatives, 42 True Positives) and only committed **2 minor errors** across the entire matrix layout.

---

## 💻 Repository Structure
```text
├── Breast_cancer_dataset.csv               # Target dataset containing structural cell entries
├── Breast-Cancer-Pipeline-Tuning.ipynb     # Main Jupyter Notebook with pipeline and grid execution blocks
└── README.md                               # Project documentation and performance summaries
```

## 🚀 Getting Started & Execution

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Install the necessary machine learning and plotting dependencies:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```
3. Open and run the Jupyter Notebook session:
   ```bash
   jupyter notebook Assignment.ipynb
   ```
