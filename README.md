Sales Data Analysis using Python (Pandas + Matplotlib)

This project analyzes monthly sales data from a CSV file and visualizes the results with bar charts. It demonstrates the use of Pandas for data handling and Matplotlib for visualization.

Project Files

analyze_sales.py – Main Python script

sales_data.csv – Dataset used

requirements.txt – List of Python dependencies

monthly_sales.png – Generated bar chart (output)

.gitignore – Ignore unnecessary files (like venv, cache)

Dataset Overview

The dataset includes:

Date – Date of sales transaction

Sales – Amount of sales recorded

Data is aggregated month-wise to show total sales across the year.

Technologies Used

Python

Pandas

Matplotlib

Workflow

Load the sales dataset (CSV)

Convert date column into datetime format

Extract month names from dates

Calculate monthly total sales using groupby

Print results to terminal

Generate and save a bar chart of monthly sales

Sample Results

January: 2150

February: 2650

March: 2190

April: 3000

May: 3550

June: 3000

July: 4000

August: 3950

September: 4250

October: 4550

November: 4750

December: 4950

Generated chart:

How to Run

Clone the repo:

git clone https://github.com/your-username/sales-data-analysis.git
cd sales-data-analysis


Install dependencies:

pip install -r requirements.txt


Run the script:

python analyze_sales.py

Future Improvements

Add more datasets (e.g., multiple years)

Include moving averages for trend analysis

Build a Flask/Streamlit dashboard

Add forecasting models (ARIMA, Prophet, etc.)

Author

Faiz Azam
BS Artificial Intelligence
Sindh Madressatul Islam University
Email: faiyz.azam@gmail.com

Tags

#Python #Pandas #Matplotlib #DataAnalysis #AIProjects