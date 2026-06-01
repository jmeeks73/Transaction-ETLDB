#1. Install Packages

!pip install sqlalchemy pyodbc pandas


#2 Python ETL Code and Import Libraries

import pandas as pd
from sqlalchemy import create_engine

# Extract
df = pd.read_csv("transaction_data.csv")

print(df.shape)
print(df.head())

