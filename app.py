import streamlit as st
import pandas as pd

st.title("Talking Rabbitt 🐇")
st.subheader("Conversational AI for Supply Chain Intelligence")

uploaded_file = st.file_uploader("Upload Logistics Data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about the data")

    if question:

        q = question.lower()

        if "shipment" in q or "most shipments" in q:
            result = df.loc[df["Shipments"].idxmax()]
            st.success(f"{result['Warehouse']} warehouse handled the highest shipments ({result['Shipments']}).")

        elif "delay" in q or "highest delay" in q:
            result = df.loc[df["DelayRate"].idxmax()]
            st.success(f"{result['Warehouse']} warehouse has the highest delay rate ({result['DelayRate']}%).")

        elif "lowest delay" in q:
            result = df.loc[df["DelayRate"].idxmin()]
            st.success(f"{result['Warehouse']} warehouse has the lowest delay rate ({result['DelayRate']}%).")

        else:
            st.info("Try asking about shipments or delays.")
