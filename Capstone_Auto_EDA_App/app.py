import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Superstore EDA Automation", layout="wide")

st.title("📊 Superstore EDA Automation App")
st.write("Upload a CSV file to perform automatic Exploratory Data Analysis (EDA).")

# -------------------------------
# Upload CSV
# -------------------------------
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv(uploaded_file)

    # -------------------------------
    # Dataset Shape
    # -------------------------------
    st.header("Dataset Shape")
    st.write(df.shape)

    # -------------------------------
    # Column Names
    # -------------------------------
    st.header("Column Names")
    st.write(df.columns.tolist())

    # -------------------------------
    # Data Types
    # -------------------------------
    st.header("Data Types")
    st.write(df.dtypes)

    # -------------------------------
    # Missing Values
    # -------------------------------
    st.header("Missing Values")
    st.write(df.isnull().sum())

    # -------------------------------
    # Numeric Summary
    # -------------------------------
    st.header("Numeric Summary")
    st.write(df.describe())

    # -------------------------------
    # Automatic Insights (Extra Feature)
    # -------------------------------
    if "Sales" in df.columns:

        st.header("📌 Automatic Insights")

        st.success(f"Total Sales : {df['Sales'].sum():,.2f}")
        st.info(f"Average Sales : {df['Sales'].mean():,.2f}")
        st.warning(f"Maximum Sale : {df['Sales'].max():,.2f}")
        st.error(f"Minimum Sale : {df['Sales'].min():,.2f}")

    # -------------------------------
    # Top 10 Sales
    # -------------------------------
    if "Sales" in df.columns:

        st.header("Top 10 Sales")
        st.dataframe(df.nlargest(10, "Sales"))

        st.header("Bottom 10 Sales")
        st.dataframe(df.nsmallest(10, "Sales"))

    # -------------------------------
    # Histogram
    # -------------------------------
    if "Sales" in df.columns:

        st.header("Histogram of Sales")

        fig, ax = plt.subplots(figsize=(7,4))
        ax.hist(df["Sales"], bins=20)
        ax.set_title("Sales Distribution")
        ax.set_xlabel("Sales")
        ax.set_ylabel("Frequency")

        st.pyplot(fig)

    # -------------------------------
    # Bar Chart
    # -------------------------------
    if "Category" in df.columns and "Sales" in df.columns:

        st.header("Sales by Category")

        fig, ax = plt.subplots(figsize=(7,4))

        df.groupby("Category")["Sales"].sum().plot(kind="bar", ax=ax)

        ax.set_xlabel("Category")
        ax.set_ylabel("Total Sales")

        st.pyplot(fig)

    # -------------------------------
    # Correlation Heatmap
    # -------------------------------
    numeric_df = df.select_dtypes(include="number")

    if len(numeric_df.columns) > 1:

        st.header("Correlation Heatmap")

        fig, ax = plt.subplots(figsize=(8,6))

        corr = numeric_df.corr()

        img = ax.imshow(corr)

        plt.colorbar(img)

        ax.set_xticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=90)

        ax.set_yticks(range(len(corr.columns)))
        ax.set_yticklabels(corr.columns)

        st.pyplot(fig)

    # -------------------------------
    # Missing Value Chart
    # -------------------------------
    st.header("Missing Value Chart")

    fig, ax = plt.subplots(figsize=(8,4))

    df.isnull().sum().plot(kind="bar", ax=ax)

    ax.set_ylabel("Missing Count")

    st.pyplot(fig)

    # -------------------------------
    # Sales by Segment
    # -------------------------------
    if "Segment" in df.columns and "Sales" in df.columns:

        st.header("Sales by Segment")

        fig, ax = plt.subplots(figsize=(7,4))

        df.groupby("Segment")["Sales"].sum().plot(kind="bar", ax=ax)

        ax.set_ylabel("Total Sales")

        st.pyplot(fig)

    # -------------------------------
    # Download Dataset (Extra Feature)
    # -------------------------------
    st.header("Download Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="processed_dataset.csv",
        mime="text/csv"
    )

else:

    st.info("Please upload a CSV file to begin the analysis.")