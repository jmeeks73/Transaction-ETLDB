# ETL Architecture — Transaction ETLDB

## Overview

This project follows an ETL (Extract, Transform, Load) architecture to process transaction data and create business intelligence dashboards using Python, SQL Server, and Power BI.

---

# ETL Process

## 1. Extract

Raw transaction data is collected from CSV files.

### Raw Data Includes:

* Transaction details
* Customer information
* Device usage
* Fraud indicators
* Payment methods
* Geolocation data

The raw files are stored inside:

```text
data/raw/
```

---

## 2. Transform

The raw data is cleaned and transformed using Python and SQL Server.

### Transformation Tasks:

* Remove duplicate records
* Handle missing values
* Standardize column names
* Convert data types
* Create fraud analysis fields
* Prepare data for reporting

Python libraries used:

* Pandas
* SQLAlchemy

SQL transformations include:

* Joins
* Aggregations
* Fraud analysis queries
* Revenue calculations

The cleaned data is stored inside:

```text
data/clean/
```

---

## 3. Load

The transformed data is loaded into SQL Server tables for analysis and reporting.

### Database Used:

```text
TransactionETLDB
```

Tables are connected to Power BI for dashboard creation and business intelligence reporting.

---

# Reporting Layer

Power BI dashboards are used to visualize:

* Total Revenue
* Fraud Transactions
* Transaction Trends
* Device Usage
* Payment Methods
* Network Slice Revenue

---

# Technologies Used

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| Python     | Data cleaning and ETL processing  |
| SQL Server | Database storage and SQL analysis |
| Power BI   | Dashboard reporting               |
| Pandas     | Data transformation               |
| SQLAlchemy | Database connection pipeline      |

---

# Final Outcome

The ETL architecture creates a complete data pipeline that transforms raw transaction data into meaningful business insights and interactive dashboards.

