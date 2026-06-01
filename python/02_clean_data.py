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

# 4. Check for Missing Values

print(df_clean.isnull().sum())


# 5. Overall Summary

summary = df_clean["transaction_amount"].agg(
    ["count", "mean", "min", "max", "sum"]
).round(2)

print(summary)

