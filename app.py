import streamlit as st
import pandas as pd

df = pd.read_csv("data/cleaned_sales_data.csv")

st.title("Sales & Customer Analytics Dashboard")

st.metric("Total Revenue", f"₹{df['Sales'].sum():,.0f}")
st.metric("Total Profit", f"₹{df['Profit'].sum():,.0f}")
st.metric("Orders", df["Order_ID"].nunique())