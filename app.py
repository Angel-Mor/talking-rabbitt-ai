import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Talking Rabbitt", page_icon="🐇", layout="wide")

st.title("Talking Rabbitt 🐇")
st.subheader("Conversational AI for Supply Chain Intelligence")

st.write("Upload logistics data and ask questions to generate AI-powered insights.")

uploaded_file = st.file_uploader("Upload Logistics Data (CSV)", type=["csv"])

if uploaded_file:
    
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df)

    st.write("### Ask a question about the data")
    question = st.text_input("Example: Which warehouse has the most shipments?")

    if question:

        q = question.lower()

        if "shipment" in q or "most shipments" in q:

            result = df.loc[df["Shipments"].idxmax()]

            st.success(
                f"📦 **Insight:** {result['Warehouse']} warehouse handled the highest shipments with **{result['Shipments']} deliveries**, indicating strong operational throughput."
            )

            fig = px.bar(
                df,
                x="Warehouse",
                y="Shipments",
                color="Shipments",
                title="Shipment Volume by Warehouse",
            )

            st.plotly_chart(fig, use_container_width=True)

        elif "delay" in q and "highest" in q:

            result = df.loc[df["DelayRate"].idxmax()]

            st.warning(
                f"⚠️ **Alert:** {result['Warehouse']} warehouse has the highest delay rate at **{result['DelayRate']}%**, which may indicate operational inefficiencies."
            )

            fig = px.bar(
                df,
                x="Warehouse",
                y="DelayRate",
                color="DelayRate",
                title="Delay Rate by Warehouse",
            )

            st.plotly_chart(fig, use_container_width=True)

        elif "lowest delay" in q or "least delay" in q:

            result = df.loc[df["DelayRate"].idxmin()]

            st.success(
                f"✅ **Performance Insight:** {result['Warehouse']} warehouse has the lowest delay rate at **{result['DelayRate']}%**, indicating efficient logistics operations."
            )

            fig = px.bar(
                df,
                x="Warehouse",
                y="DelayRate",
                color="DelayRate",
                title="Delay Rate Comparison",
            )

            st.plotly_chart(fig, use_container_width=True)

        else:

            st.info(
                "Try asking questions like:\n\n"
                "- Which warehouse has the most shipments?\n"
                "- Which warehouse has the highest delay?\n"
                "- Which warehouse has the lowest delay?"
            )
