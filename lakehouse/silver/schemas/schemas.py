# Databricks notebook source
spark.sql("CREATE CATALOG IF NOT EXISTS silver_ciber")

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS silver_ciber.historical_market")

# COMMAND ----------


