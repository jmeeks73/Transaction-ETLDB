#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Install Packages

get_ipython().system('pip install sqlalchemy pyodbc pandas')


# In[17]:


#2 Python ETL Code and Import Libraries

import pandas as pd
from sqlalchemy import create_engine

# Extract
df = pd.read_csv("transaction_data.csv")

print(df.shape)
print(df.head())


# In[14]:


#3. Clean Column Names

df_clean = df.copy()

df_clean.columns = (
    df_clean.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("/", "_")
)

print(df_clean.columns)


# In[18]:


# 4. Check for Missing Values

print(df_clean.isnull().sum())


# In[19]:


# 5. Overall Summary

summary = df_clean["transaction_amount"].agg(
    ["count", "mean", "min", "max", "sum"]
).round(2)

print(summary)


# In[20]:


#6. Transaction Type Analysis

type_summary = df_clean.groupby(
    "transaction_type"
)["transaction_amount"].agg(
    total_transactions="count",
    avg_amount="mean",
    total_amount="sum"
).round(2)

print(type_summary)


# In[21]:


# 7 Fraud Analysis

fraud_summary = df_clean.groupby(
    "fraud_flag"
)["transaction_amount"].agg(
    total_transactions="count",
    avg_amount="mean",
    total_amount="sum"
).round(2)

print(fraud_summary)


# In[22]:


# 8 Device Analysis

device_summary = df_clean.groupby(
    "device_used"
)["transaction_amount"].agg(
    total_transactions="count",
    avg_amount="mean",
    total_amount="sum"
).round(2)

print(device_summary)


# In[33]:


from sqlalchemy import create_engine, text

server = r"JOHNMPC\SQLEXPRESS"
database = "TransactionETLDB"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
    "&TrustServerCertificate=yes"
    "&timeout=5"
)

engine = create_engine(connection_string)

print("Engine created")


# In[34]:


with engine.connect() as conn:
    result = conn.execute(text("SELECT 1 AS test_connection"))
    print(result.fetchone())


# In[ ]:




