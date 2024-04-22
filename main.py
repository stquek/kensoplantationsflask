import os
from flask import Flask, send_from_directory
import pandas as pd
from supabase import create_client, Client
from sqlalchemy import create_engine
from waitress import serve

db_password = "Yunxuan123!"
current_dir = os.getcwd()

app = Flask(__name__)

@app.get("/download")
def download_excel():
    print("Downloading Excel")
    filename = "Result.xlsx"
    create_engine_str = ("postgresql://postgres.vdqsfnptcoezfgdfmkvg:{0}@aws-0-ap-southeast-1.pooler.supabase.com:"
                         "5432/postgres").format(db_password)
    print("Create Engine Str:", create_engine_str)
    engine = create_engine(create_engine_str)
    conn = engine.connect()
    sql_str = "SELECT * from users_ext"
    stock_df = pd.read_sql_query(sql=sql_str, con=conn.connection)
    print("\nStock Df:")
    stock_df = stock_df.drop(columns=['id', 'created_at'])
    print(stock_df)
    writer = pd.ExcelWriter(filename,engine="xlsxwriter")
    stock_df.to_excel(writer, sheet_name="Result")
    writer.close()

    return send_from_directory(current_dir, filename, as_attachment=True)

@app.get("/test")
def test():
    return {"message": "test OK"}


@app.get("/")
def root():
    return {"message": "OK"}

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)
