# Databricks notebook source
source_table = 'silver_ciber.historical_market__normalized.open_historical'
destination_table = 'silver_ciber.historical_market.open_historical'

# COMMAND ----------

open_normalized = spark.sql(f'''
    SELECT
        open.*
    FROM
        {source_table} AS open
''')
open_normalized.createOrReplaceTempView('open_normalized')

# COMMAND ----------

open_derived = spark.sql(f'''
    SELECT
        o.*,
        (o.close - o.open) / o.open         AS daily_return,
        o.high - o.low                      AS high_low_range,
        o.high - GREATEST(o.open, o.close)  AS upper_wick,
        LEAST(o.open, o.close) - o.low      AS lower_wick
    FROM
        open_normalized AS o                            
''')

open_derived.createOrReplaceTempView('open_derived')

# COMMAND ----------

spark.sql(f'''
    INSERT OVERWRITE {destination_table}
    BY NAME
    SELECT *
    FROM open_derived
''')
