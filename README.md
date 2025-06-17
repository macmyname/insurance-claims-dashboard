# 🧾 Insurance Claims Analysis & Premium Estimator

This project explores a dataset of insurance claims using Python and builds a tool to estimate insurance premiums based on user characteristics. It includes both a detailed Jupyter notebook for analysis and a live interactive dashboard built with Streamlit.

The dataset used in this project is sourced from [Kaggle].  
It contains insurance-related fields such as age, BMI, smoker status, and amount (claims incurred).  

## 🔍 What’s Inside

### 1. Jupyter Notebook (`analysis.ipynb`)
A complete walkthrough of the dataset:
- Data cleaning and preprocessing
- Feature engineering (e.g., adjusted premiums based on age and smoker status)
- Exploratory data analysis (EDA)
- Linear regression model to predict insurance premiums
- Insightful observations and charts

### 2. Streamlit App (`streamlit_app.py`)
An interactive web dashboard where users can:
- Enter their age, BMI, and smoking status to estimate premium
- View average premiums by smoker type
- Explore a scatter plot showing claims vs age
- See a summary table of sample policyholders
- Select insurance coverage type (Basic, Enhanced, Comprehensive) to view general advice

📍 **Live Dashboard**: [streamlit link]

## 📊 Key Features

- **Interactive Widgets**: Sliders, dropdowns, and dynamic outputs
- **Data Visualization**: Uses both Matplotlib and Plotly to visualize claims and trends
- **Machine Learning**: Linear regression predicts personalized insurance premiums
- **User-Friendly Design**: Tailored content based on user input

## 💾 Dataset
The dataset (`insurance.csv`) contains:
- Age, sex, BMI, smoking status, region
- Amount (claims incurred)

## 🛠️ Tech Tools
- Python
- Pandas, NumPy
- Scikit-learn (for regression)
- Matplotlib & Plotly
- Streamlit

## 🚀 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/macmyname/insurance-claims-dashboard.git
   
2. Install the dependencies
   ```bash
   pip install -r requirements.txt

3. Launch the dashboard
   ```bash
   streamlit run streamlit_app.py

🗂️ Files Included
insurance.csv - Main dataset
analysis.ipynb - Initial analysis & modeling
streamlit_app.py - Dashboard app
README.md - This file
requirements.txt - Python packages

👤 Author:
Motunrayo Awe
_www.linkedin.com/in/motunrayo-awe-mac_
Focused on data-driven insights in insurance, claims, and health analytics.

📝 Notes:
Dataset used includes amount (claims incurred), not actual premiums.
"Basic", "Enhanced", and "Comprehensive" insurance types are illustrative only.
Adjusted premiums are based on age and smoker status.
