import streamlit as st
import pandas as pd

st.title("Talking Rabbitt 🐇")
st.subheader("Conversational AI for Supply Chain Intelligence")

uploaded_file = st.file_uploader("Upload Logistics Data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df)

    question = st.text_input("Ask a question about the data")

    if question:
        if "shipments" in question.lower():
            result = df.loc[df['Shipments'].idxmax()]
            st.success(f"{result['Warehouse']} warehouse handled the highest shipments.")
