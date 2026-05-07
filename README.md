# Retail Sales Analytics Dashboard

## Project Overview

This project demonstrates an end-to-end Retail Sales Analytics workflow using Python, SQL, SQLite, and Tableau. The objective of the project is to analyze retail sales data, generate business insights, and build an interactive dashboard for decision-making.

The project includes:

* Data cleaning and ETL processing using Python and Pandas
* SQL analysis using SQLite
* KPI generation and business reporting
* Interactive Tableau dashboard creation
* GitHub project documentation and version control

---

# Business Problem

Retail businesses generate large amounts of transactional sales data daily. Business stakeholders need a centralized analytics solution to:

* Monitor sales performance
* Identify top-performing products
* Analyze profitability
* Compare regional performance
* Track business KPIs
* Support operational and strategic decision-making

This project simulates a real-world retail analytics workflow used by data analysts and business intelligence teams.

---

# Tools & Technologies Used

| Tool / Technology     | Purpose                             |
| --------------------- | ----------------------------------- |
| Python                | ETL and data processing             |
| Pandas                | Data cleaning and transformations   |
| SQLite                | SQL query execution                 |
| DB Browser for SQLite | Database management                 |
| Tableau Public        | Dashboard and data visualization    |
| Git & GitHub          | Version control and project hosting |

---

# Project Structure

```text
retail_sales_analytics_project/
│
├── data/
│   ├── raw/
│   │   └── retail_sales_raw.csv
│   ├── clean_sales.csv
│   └── monthly_kpi_summary.csv
│
├── src/
│   └── etl_pipeline.py
│
├── sql/
│   ├── 01_schema.sql
│   └── 02_queries.sql
│
├── dashboard/
│   └── retail_sales_dashboard.twbx
│
└── README.md
```

---

# ETL Process

The ETL pipeline was developed using Python and Pandas.

## Steps Performed

### 1. Data Extraction

* Loaded raw retail sales CSV data using Pandas.

### 2. Data Cleaning

* Removed missing values
* Standardized column names
* Converted date columns into proper datetime format
* Generated derived fields such as:

  * order_year
  * order_month
  * profit_margin

### 3. Data Transformation

Calculated:

* sales_amount
* cost_amount
* profit_amount
* profit_margin

### 4. Data Loading

Exported cleaned datasets:

* clean_sales.csv
* monthly_kpi_summary.csv

---

# SQL Analysis

SQLite was used to perform analytical queries on the cleaned retail sales dataset.

## SQL Queries Implemented

### 1. Total Sales and Profit by Month and Region

Analyzed monthly sales and profit performance across regions.

### 2. Top Selling Products

Identified products generating the highest revenue.

### 3. Profit Margin by Product Category

Compared profitability across product categories.

### 4. Customer Order Analysis

Calculated total orders and revenue per customer.

### 5. Average Discount Analysis

Analyzed average discount percentages across product categories.

### 6. Regional Product Performance

Compared sales and profitability by region and category.

---

# Tableau Dashboard

An interactive Tableau dashboard was created to visualize key business metrics and insights.

## Dashboard Features

### KPI Cards

* Total Sales
* Total Profit
* Total Orders
* Profit Margin

### Visualizations

* Monthly Sales Trend
* Sales by Region
* Top Products Analysis
* Profit by Category

### Interactive Filters

* Region Filter
* Product Category Filter

---

# Key Insights

* The West region generated the highest sales revenue.
* Electronics products contributed significantly to total sales.
* Profitability varied across product categories.
* Interactive filtering enabled dynamic regional and category analysis.

---

# How to Run the Project

## Step 1 — Clone Repository

```bash
git clone https://github.com/sowmya536/retail-sales-analytics-dashboard.git
```

## Step 2 — Navigate to Project Folder

```bash
cd retail-sales-analytics-dashboard
```

## Step 3 — Install Dependencies

```bash
pip install pandas
```

## Step 4 — Run ETL Pipeline

```bash
python3 src/etl_pipeline.py
```

## Step 5 — Execute SQL Queries

* Open DB Browser for SQLite
* Import clean_sales.csv
* Execute queries from:

```text
sql/02_queries.sql
```

## Step 6 — Open Tableau Dashboard

Open:

```text
dashboard/retail_sales_dashboard.twbx
```

---

# Future Enhancements

Potential improvements for future versions:

* Larger multi-month datasets
* Real-time streaming analytics
* Predictive sales forecasting
* Automated Airflow pipelines
* Cloud deployment using AWS or Azure
* Advanced KPI monitoring

---

# Author

Sowmya Banala

GitHub:

[https://github.com/sowmya536](https://github.com/sowmya536)
