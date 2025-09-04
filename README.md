# 📊 Customer Churn Analysis – Cell2Cell Dataset
### Final Year BCA Data Analytics Project

This project analyzes **customer churn** using the **Cell2Cell telecom dataset**, which contains over 50 features about customer demographics, billing behavior, handset details, and service usage.  
The business objective is to identify which customers are most likely to leave (“churn”) and understand the factors that drive churn, so telecom companies can take proactive retention actions.  

Adopted a **multi-tool approach**:  
- Excel → quick exploration and pivot dashboards  
- SQL → structured queries and data cleaning  
- Python → predictive modeling and machine learning  
- Power BI → interactive and executive-style dashboard  

---

## 📑 Deliverables

### 🔹 Excel Dashboard
- Pivot-based dashboard analyzing churn by Income Group, Marital Status, and Homeownership.  
- Includes Average Monthly Revenue and Average Customer Care Calls by churn.  
- All Excel dashboards are stored in the **`dashboard/` folder**.  

📂 Go to: [dashboard/](./dashboards/)

---

### 🔹 SQL Analysis
- SQL scripts for creating cleaned views, handling missing values, and building indexes.  
- Queries for churn % by demographics and averages for revenue/care calls.  
- All `.sql` scripts are stored in the **`SQL/` folder**.  

📂 Go to: [SQL/](./sql/)

---

### 🔹 Python Modeling
- Jupyter notebooks covering:  
  - Exploratory Data Analysis (EDA)  
  - Data Cleaning & Preprocessing  
  - Model Training & Evaluation (LogReg, RandomForest)  
  - Risk Scoring (churn probabilities + deciles)  
- Outputs (clean CSVs, metrics) saved in **`data/clean/`** and **`report/`**.  
- Notebooks are stored in the **`notebooks/` folder**.  

📂 Go to: [notebooks/](./notebooks/) | [data/clean/](./data/cleaned/)

---

### 🔹 Power BI Dashboard
- Interactive dashboard with:  
  - Churn % by Income Group, Marital Status, and Homeownership  
  - Average Monthly Revenue vs. Churn  
  - Average Customer Care Calls vs. Churn  
- Includes a slicer for churn status and consistent red/green risk colors.  
- Power BI files (`.pbix`, `.pdf`) are stored in the **`dashboard/`** and **`report/`** folders.  

📂 Go to: [dashboard/](./dashboards/) | [report/](./report/)

---

## 📌 Key Insights
- Churn is higher in certain **income groups** and **marital statuses**.  
- **Churned customers** bring in less revenue but contact support more often.  
- Model separates customers into **risk deciles**, enabling targeted retention.  

---

## 🛠️ Tools & Stack
- **Excel** – Pivot Tables & Dashboarding  
- **SQL (SQLite)** – Data cleaning, indexing, querying  
- **Python** – Pandas, Scikit-learn, Matplotlib, Seaborn  
- **Power BI** – Interactive reporting & executive dashboard  

---

📌 *This repo shows a complete data analytics pipeline: raw data → descriptive insights → predictive modeling → interactive reporting.*
