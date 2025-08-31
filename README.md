# CustomerChurn-Cell2Cell
Final Year Project — Customer Churn Prediction using the Cell2Cell Dataset
- `/data/raw` — raw datasets (Cell2Cell train & holdout uploaded here)
## 📊 Excel (Dashboard)  
The Excel dashboard provides a quick overview of churn patterns through pivot tables and charts.  

- Visualized churn % across key groups: **Income Group, Marital Status, Homeownership, Average Revenue, Customer Care Calls**.  
- Combined into one dashboard with positive (No Churn = green) and negative (Churn = red) color coding.  

📂 File: [excel_dashboard.xlsx](./dashboard/excel_dashboard.xlsx)  

---

## 🗄️ SQL (Queries & Indexing)  
SQL scripts were used for exploration, cleaning, and summarization.  

- Created cleaned view `v_cell2cell_clean` with proper datatypes.  
- Added indexes on `Churn`, `IncomeGroup`, `MaritalStatus`, `Homeownership`, and `CustomerCareCalls`.  
- Wrote queries for churn % by demographics, average revenue, and average care calls.  

📂 Folder: [SQL/](./SQL/)  
- Contains all `.sql` scripts.  

---

## 🐍 Python (Notebooks & Modeling)  
Python notebooks were used for data cleaning, analysis, and churn prediction modeling.  

- **[01_eda.ipynb](./notebooks/01_eda.ipynb)** → Exploratory Data Analysis (churn distribution ≈29%, key features, missing values).  
- **[02_cleaning.ipynb](./notebooks/02_cleaning.ipynb)** → Data preprocessing (imputation, grouping rare categories, preprocessing pipeline).  
- **[03_modeling.ipynb](./notebooks/03_modeling.ipynb)** → Random Forest model:  
  - Validation (threshold = 0.50): Accuracy ≈ 69%, Precision ≈ 44%, Recall ≈ 31%, ROC-AUC ≈ 0.66.  
  - Evaluated F1-optimal (~0.38) and Top-20% (~0.50) thresholds.  
  - Produced BI-ready scored datasets with churn probabilities and deciles.  

**Key Outputs:**  
- Metrics: [validation_metrics.csv](./artifacts/validation_metrics.csv)  
- Thresholds: [thresholds.json](./artifacts/thresholds.json)  
- Scored datasets: [holdout_scored.csv](./data/clean/holdout_scored.csv), [validation_scored_with_deciles.csv](./data/clean/validation_scored_with_deciles.csv)  
- Visuals: [ROC Curve](./report/roc_curve.png), [PR Curve](./report/pr_curve.png), [Confusion Matrix (default)](./report/confusion_matrix_default.png), [F1](./report/confusion_matrix_f1.png), [Top-20%](./report/confusion_matrix_top20.png)  

