# Data Dictionary — Transaction ETLDB

| Column Name        | Description                                       |
| ------------------ | ------------------------------------------------- |
| transaction_id     | Unique ID for each transaction                    |
| transaction_amount | Dollar amount of the transaction                  |
| transaction_type   | Type of transaction, such as purchase or transfer |
| transaction_date   | Date the transaction happened                     |
| customer_id        | Unique ID for each customer                       |
| device_used        | Device used to complete the transaction           |
| network_slice      | Network category connected to the transaction     |
| geolocation        | Location connected to the transaction             |
| flag_fraud         | Shows whether the transaction was marked as fraud |
| risk_level         | Fraud risk level, such as low, medium, or high    |

## Summary

This data dictionary explains the main columns used in the Transaction ETLDB project. It helps readers understand what each field means and how the data is used for fraud analysis, revenue tracking, and Power BI dashboard reporting.

