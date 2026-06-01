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

Engine created

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1 AS test_connection"))
    print(result.fetchone())

(1,)

C:\Users\jpmee\AppData\Local\Temp\ipykernel_18412\2902609802.py:1: SAWarning: Unrecognized server version info '17.0.1115.1'.  Some SQL Server features may not function properly.
  with engine.connect() as conn:
