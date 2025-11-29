# Databricks notebook source
dbutils.widgets.text("alpaca_key", "")
dbutils.widgets.text("alpaca_secret", "")
dbutils.widgets.text("symbol", "")
dbutils.widgets.text("start_date", "")
dbutils.widgets.text("end_date", "")
dbutils.widgets.text("timeframe", "")
dbutils.widgets.text("limit", "")

# COMMAND ----------

API_KEY = dbutils.widgets.get("alpaca_key")
API_SECRET = dbutils.widgets.get("alpaca_secret")
symbol = dbutils.widgets.get("symbol")
start_date = dbutils.widgets.get("start_date")
end_date = dbutils.widgets.get("end_date")
timeframe = dbutils.widgets.get("timeframe")
limit = dbutils.widgets.get("limit")

# COMMAND ----------

import requests
import pandas as pd
from datetime import datetime, timedelta

# COMMAND ----------

BASE_URL = "https://data.alpaca.markets/v2/stocks/"

url = f"{BASE_URL}bars?symbols={symbol}&timeframe={timeframe}&start={start_date}&end={end_date}&limit={limit}&adjustment=raw&feed=sip"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": API_SECRET
}

response = requests.get(url, headers=headers)

data = response.json().get("bars", [])

df = pd.DataFrame(data)

df["bronze_timestamp"] = datetime.now()

# COMMAND ----------

spark_df = spark.createDataFrame(df)
spark_df.write.mode("overwrite").option("overwriteSchema", "true").format("delta").saveAsTable("bronze_ciber.alpaca_historical_bars.open")
