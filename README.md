# 📊 Customer Churn Analysis – Cell2Cell Dataset
### Final Year BCA Data Analytics Project

This project analyzes **customer churn** using the **Cell2Cell telecom dataset**, which contains over 50 features about customer demographics, billing behavior, handset details, and service usage.  
The business objective is to identify which customers are most likely to leave (“churn”) and understand the factors that drive churn, so telecom companies can take proactive retention actions.  

We adopted a **multi-tool approach**:  
- Excel → quick exploration and pivot dashboards  
- SQL → structured queries and data cleaning  
- Python → predictive modeling and machine learning  
- Power BI → interactive and executive-style dashboard  

---

## 📑 Deliverables

### 🔹 Excel Dashboard
**Goal:** Build an initial descriptive view of churn patterns using pivot tables and charts.  
**What’s included:**  
- Churn % by **Income Group**, **Marital Status**, and **Homeownership**  
- Comparison of **Average Monthly Revenue** between churners and non-churners  
- Comparison of **Average Customer Care Calls** between churners and non-churners  
- Combined into a clean, single-page Excel dashboard  

📂 [Download Excel Dashboard](dashboard/cell2cell_dashboard.xlsx)

---

### 🔹 SQL Analysis
**Goal:** Practice structured querying and indexing to extract churn insights.  
**What’s included:**  
- SQL scripts for creating views, cleaning missing values, and handling data types  
- Indexes built on important fields (`Churn`, `IncomeGroup`, `MaritalStatus`, `Homeownership`)  
- Queries calculating churn % by demographic groups  
- Queries summarizing **Average Revenue** and **Customer Care Calls** split by churn  

📂 [View SQL Scripts](SQL/)

---

### 🔹 Python Modeling
**Goal:** Build an end-to-end predictive modeling pipeline.  
**What’s included:**  
- **Exploratory Data Analysis (EDA):** distributions, missing values, correlations  
- **Data Preprocessing:** handling unknowns, encoding categorical variables, scaling numerics  
- **Model Training:** Logistic Regression & Random Forest, with cross-validation  
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score, ROC-AUC  
- **Risk Scoring:** Generating churn probabilities and customer decile segmentation  
- **Outputs:** confusion matrices, ROC/PR curves, validation metrics CSV, churn-scored holdout dataset  

📂 [Notebooks](notebooks/) | [Artifacts & Outputs](data/clean/)

---

### 🔹 Power BI Dashboard
**Goal:** Deliver a polished, interactive dashboard for decision-makers.  
**What’s included:**  
- **Churn % by Income Group** (gradient-colored, sorted by churn risk)  
- **Churn % by Marital Status** (yes/no/unknown comparison)  
- **Churn % by Homeownership** (donut view of known vs unknown)  
- **Average Monthly Revenue by Churn** (solid red/green for loss vs retention)  
- **Average Customer Care Calls by Churn** (solid red/green)  
- Slicer for Churn → allows interactive filtering  
- Exported in both `.pbix` (editable) and `.pdf` (shareable report)  

📂 [Download Power BI File (.pbix)](dashboard/cell2cell_powerbi.pbix)  
📂 [View Dashboard (PDF)](report/cell2cell_powerbi_dashboard.pdf)

---

## 📌 Key Insights
- Churn is concentrated in certain **income groups** and **marital statuses**.  
- **Churned customers generate less monthly revenue** but **contact support more often**.  
- Machine learning model highlights churners can be segmented into **risk deciles**, enabling targeted retention campaigns.  

---

## 🛠️ Tools & Technologies
- **Excel** (Pivot Tables, Dashboarding)  
- **SQL (SQLite, DB Browser)** for querying & indexing  
- **Python**: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Joblib  
- **Power BI** for interactive visual analytics  

---

📌 *This repository demonstrates a complete analytics pipeline: raw data → descriptive insights → predictive modeling → interactive reporting.*
