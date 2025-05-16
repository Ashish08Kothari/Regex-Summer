import pandas as pd
import mysql.connector
import os

# === Configuration ===
host = 'host_name'
port = 'port_number'
user = 'user_name'         # 🔁 Replace with your MySQL username
password = 'your_password'     # 🔁 Replace with your MySQL password
database = 'your_database'     # 🔁 Replace with your database name
table_name = 'your_table'      # 🔁 Replace with the table name you want to export

# === Connect to MySQL ===
conn = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# === Read table into pandas DataFrame ===
query = f"SELECT * FROM {table_name}"
df = pd.read_sql(query, conn)

# === Save DataFrame to Desktop ===
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, f"{table_name}_export.csv")
df.to_csv(output_file, index=False)

print(f"✅ Table '{table_name}' saved to: {output_file}")

# === Close the connection ===
conn.close()
