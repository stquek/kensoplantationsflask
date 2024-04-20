import os
from flask import Flask, send_from_directory
import pandas as pd
from supabase import create_client, Client
from sqlalchemy import create_engine

# db_password = "Yunxuan123!"
# url = "https://vdqsfnptcoezfgdfmkvg.supabase.co"
# key = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZkcXNmbnB0Y29lemZnZGZta3ZnIiwicm9sZSI6"
#        "ImFub24iLCJpYXQiOjE3MTMxMDQxNDgsImV4cCI6MjAyODY4MDE0OH0.swv_YwbLN6EPxxikubazm-JihQvFRNN7G4QZJHTLnyI")
# Client = create_client(url, key)
# current_dir = os.getcwd()

app = Flask(__name__)

# @app.get("/download")
# def download_excel():
#     print("Downloading Excel")
#     filename = "Result.xlsx"
#     create_engine_str = ("postgresql+psycopg2://postgres.vdqsfnptcoezfgdfmkvg:{0}@aws-0-ap-southeast-1.pooler.supabase.com:"
#                          "5432/postgres").format(db_password)
#     print("Create Engine Str:", create_engine_str)
#     engine = create_engine(create_engine_str)
#     conn = engine.connect()
#     sql_str = "SELECT * from users_ext"
#     stock_df = pd.read_sql_query(sql=sql_str, con=conn.connection)
#     print("\nStock Df:")
#     stock_df = stock_df.drop(columns=['id', 'created_at'])
#     print(stock_df)
#     writer = pd.ExcelWriter(filename,engine="xlsxwriter")
#     stock_df.to_excel(writer, sheet_name="Result")
#     writer.close()

#     return send_from_directory(current_dir, filename, as_attachment=True)

# @app.get("/test")
# def test():
#     return {"message": "test"}


@app.get("/")
def root():
    return {"message": "OK"}
