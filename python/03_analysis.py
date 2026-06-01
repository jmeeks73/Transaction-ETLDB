#6. Transaction Type Analysis

type_summary = df_clean.groupby(
    "transaction_type"
)["transaction_amount"].agg(
    total_transactions="count",
    avg_amount="mean",
    total_amount="sum"
).round(2)

print(type_summary)

              total_transactions  avg_amount  total_amount
transaction_type                                              
Deposit                          316      797.60     252042.62
Transfer                         374      780.15     291776.55
Withdrawal                       310      733.37     227346.12

# 7 Fraud Analysis

fraud_summary = df_clean.groupby(
    "fraud_flag"
)["transaction_amount"].agg(
    total_transactions="count",
    avg_amount="mean",
    total_amount="sum"
).round(2)

print(fraud_summary)

          total_transactions  avg_amount  total_amount
fraud_flag                                              
False                      519      755.88     392301.39
True                       481      787.66     378863.90

# 8 Device Analysis

device_summary = df_clean.groupby(
    "device_used"
)["transaction_amount"].agg(
    total_transactions="count",
    avg_amount="mean",
    total_amount="sum"
).round(2)

print(device_summary)

    total_transactions  avg_amount  total_amount
device_used                                              
Desktop                     479      768.18     367956.16
Mobile                      521      773.91     403209.13

