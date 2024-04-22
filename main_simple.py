import os
from flask import Flask, send_from_directory
import pandas as pd
from supabase import create_client, Client
from sqlalchemy import create_engine
from waitress import serve

app = Flask(__name__)

@app.get("/")
def root():
    return {"message": "OK"}

if __name__=="__main__":
    app.run()
