📊 UNCTAD Economic Data Analysis & Visualization

This project focuses on cleaning, analyzing, visualizing, and deploying UNCTAD economic indicator data using Python.
The workflow includes outlier removal, train–test splitting, exploratory data analysis (EDA), and an interactive Streamlit dashboard.

🚀 Project Overview

The goal of this project is to:

Identify independent and dependent variables

Clean real-world economic data (null values & outliers)

Perform exploratory data analysis

Split the dataset into training and testing sets

Build clear and meaningful visualizations

Deploy insights using Streamlit

This project is ideal for demonstrating data analytics, visualization, and deployment skills.

🧠 Dataset Description

Source: UNCTAD (United Nations Conference on Trade and Development)

File: UNCTAD_DE.csv

Records: 8,156 rows

Features: 39 columns

Key Column Used:

OBS_VALUE → Economic measurement (Dependent Variable)

TIME_PERIOD → Year (Independent Variable)

🔍 Variables Used
Dependent Variable

OBS_VALUE

Represents the economic indicator value (numeric)

Independent Variable

TIME_PERIOD

Time dimension (year)

These variables were selected for trend analysis and forecasting readiness.

🧹 Data Cleaning Steps

Converted OBS_VALUE to numeric

Removed null values

Removed outliers using the Interquartile Range (IQR) method

Converted TIME_PERIOD into numeric format

✂️ Train–Test Split

Training Set: 80%

Testing Set: 20%

Method: train_test_split from scikit-learn

Random State: 42 (for reproducibility)

📈 Visualizations Created
1️⃣ Trend Over Time

Line chart showing economic indicator changes across years

2️⃣ Distribution of Values

Histogram displaying the spread of OBS_VALUE

These charts help identify patterns, trends, and anomalies in the data.

🖥️ Streamlit Application

An interactive dashboard was built using Streamlit, allowing users to:

Explore cleaned data

Visualize trends dynamically

Understand distributions interactively

To run the Streamlit app:
streamlit run app.py

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

Streamlit

Google Colab / Jupyter Notebook

📁 Project Structure
├── UNCTAD_DE.csv
├── data_preprocessing.ipynb
├── visualization.ipynb
├── app.py
├── README.md

🎯 Key Learnings

Handling real-world economic datasets

Outlier detection using statistical methods

Creating clear, meaningful visualizations

Preparing data for machine learning workflows

Deploying analytics with Streamlit

👤 Author

Sehan Balajee Pilli
Master’s Student – Data Analytics & Artificial Intelligence
📍 Germany

⭐ Future Improvements

Add more independent variables

Implement forecasting models

Enhance Streamlit UI with filters & selectors

Deploy app on Streamlit Cloud
