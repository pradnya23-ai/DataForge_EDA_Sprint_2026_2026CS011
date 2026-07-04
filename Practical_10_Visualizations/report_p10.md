# Practical 10 - Visualizations

Placeholder report for the visualizations practical# Practical 10: Python Visual EDA and Student-Built Automation App

## Objective
To perform Visual Exploratory Data Analysis (EDA) using Python and develop an automated EDA application using Streamlit.

## Tasks Completed

### Part A – Visual EDA

Created the following visualizations:

1. Histogram of Sales
2. Boxplot of Sales
3. Bar Chart of Sales by Category
4. Line Chart of Monthly Sales Trend
5. Scatter Plot of Sales
6. Correlation Heatmap
7. Missing Value Chart
8. Grouped Comparison Chart (Sales by Region)

All charts were saved in the outputs/plots folder.

## Observations

1. Sales values are unevenly distributed with most transactions in the lower range.
2. The boxplot indicates the presence of several high-value outliers.
3. Technology category generated the highest sales.
4. Sales changed over different months, showing an overall upward trend.
5. Scatter plot shows variation in sales without a strong linear pattern.
6. Numeric columns have weak to moderate correlations.
7. Missing values are very low after data cleaning.
8. The West region recorded the highest total sales.

---

## Part B – Automation App

### Requirement
Developed a Streamlit application that automates basic Exploratory Data Analysis for any uploaded CSV dataset.

### Features

- Upload CSV file
- Display dataset shape
- Display column names
- Display data types
- Show missing value summary
- Generate numeric summary statistics
- Display histogram
- Display boxplot
- Display correlation heatmap
- Show top and bottom records
- Automatic dataset insights

### Technology Used

- Python
- Pandas
- Matplotlib
- Streamlit

### Outcome

The application successfully automates the initial EDA process and provides quick statistical summaries and visualizations, reducing manual effort during data analysis.

## Conclusion

Practical 10 was completed successfully by creating multiple visualizations and developing a functional Streamlit-based automated EDA application capable of generating useful insights from uploaded datasets.