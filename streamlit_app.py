import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data/insurance.csv")

# Estimate Premium (based on risk factors from amount paid)
df["estimated_premium"] = df["amount"] * np.where(df["smoker"] == "yes", 1.2, 1.0) * np.where(df["age"] > 50, 1.1, 1.0)

# Prepare features
df_encoded = pd.get_dummies(df[["age", "bmi", "smoker"]], drop_first=True)

# Train regression model
X = df_encoded
y = df["estimated_premium"]
model = LinearRegression()
model.fit(X, y)

# Streamlit App UI
st.title("Insurance Premium Estimator & Claims Insights")

# Section 1: Predict Estimated Premium
st.header("1. Predict Your Estimated Premium")
age = st.slider("Age", 18, 65, 30)
bmi = st.slider("BMI", 15, 55, 30)
smoker = st.selectbox("Smoker", ["yes", "no"])
smoker_yes = 1 if smoker == "yes" else 0

sample_input = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "smoker_yes": [smoker_yes]
})

predicted_premium = model.predict(sample_input)[0]
st.subheader(f"Estimated Premium: ₦{predicted_premium:,.2f}")

# Section 2: Smoking Status vs Estimated Premium
st.header("2. Average Estimated Premium by Smoking Status")
st.bar_chart(df.groupby("smoker")["estimated_premium"].mean())

# Section 3: Claims vs Age (Interactive)
st.header("3. Claims vs Age (Interactive)")
fig2 = px.scatter(df, x="age", y="amount", title="Actual Claims (₦) vs Age")
st.plotly_chart(fig2)

# Section 4: Premium Summary Table
st.header("4. Premium Summary Table")
st.dataframe(df[["age", "bmi", "smoker", "amount", "estimated_premium"]].head(10))

# Section 5: Insurance Plan Commentary
st.header("5. Insurance Plan Commentary")
insurance_type = st.selectbox("Select Insurance Type", ["Basic", "Enhanced", "Comprehensive"])
if insurance_type == "Enhanced":
    st.write("✅ Enhanced plans provide broader coverage than Basic plans.")
elif insurance_type == "Basic":
    st.write("⚠️ Basic plans have limited coverage and fewer benefits.")
else:
    st.write("💡 Comprehensive plans offer full-spectrum protection.")

# Display user input summary
st.write(f"Selected Age: {age}, BMI: {bmi}, Smoker: {smoker}, Plan Type: {insurance_type}")

