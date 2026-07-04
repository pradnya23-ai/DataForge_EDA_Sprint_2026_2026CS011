# ===========================
# Practical 8: Data Wrangling
# ===========================

import pandas as pd
import numpy as np
import os

# ---------------------------
# Load Dataset
# ---------------------------
df = pd.read_csv("../Dataset/dataset_raw.csv")   # Change the path if needed

print("Dataset Loaded Successfully!\n")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display column names
print("\nColumns:")
print(df.columns)

# ---------------------------
# Remove Duplicates
# ---------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Before: {duplicates}")

df = df.drop_duplicates()

print(f"Duplicate Rows After: {df.duplicated().sum()}")

# ---------------------------
# Convert Date Columns
# ---------------------------
date_columns = [col for col in df.columns if "Date" in col]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

print("\nDate Columns Converted:")
print(df[date_columns].dtypes)

# ---------------------------
# Feature Engineering
# ---------------------------
if "Order Date" in df.columns:
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month_name()

# ---------------------------
# Missing Values Before
# ---------------------------
print("\nMissing Values Before Filling:")
print(df.isnull().sum())

# Fill categorical columns with "Unknown"
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna("Unknown")

# Fill numeric columns with mean
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    df[col] = df[col].fillna(df[col].mean())

print("\nMissing Values After Filling:")
print(df.isnull().sum())

# ---------------------------
# Create Output Folder
# ---------------------------
os.makedirs("../../01_data/processed", exist_ok=True)

# ---------------------------
# Save Cleaned Dataset
# ---------------------------
output_path = "../../01_data/processed/dataforge_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print(f"Location: {output_path}")

# ---------------------------
# Dataset Information
# ---------------------------
print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows of Cleaned Dataset:")
print(df.head())