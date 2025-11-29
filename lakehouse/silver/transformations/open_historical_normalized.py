# Databricks notebook source
source_table = 'bronze_ciber.alpaca_historical_bars.open'
destination_table = 'silver_ciber.historical_market.open_historical'

# COMMAND ----------

open = spark.sql(
    f'''
    SELECT
        o.OPEN.vw AS vw,
        o.OPEN.n AS n,
        o.OPEN.t AS t,
        o.OPEN.o AS o,
        o.OPEN.v AS v,
        o.OPEN.h AS h,
        o.OPEN.l AS l,
        o.OPEN.c AS c,
        bronze_timestamp
    FROM
        {source_table} AS o
    '''
)
open.createOrReplaceTempView('open')

# COMMAND ----------

normalized_open = spark.sql(f'''
    SELECT
        'OPEN'                       AS symbol,
        CAST(o.o AS DECIMAL(10,2))   AS open,
        CAST(o.h AS DECIMAL(10,2))   AS high,
        CAST(o.l AS DECIMAL(10,2))   AS low,
        CAST(o.c AS DECIMAL(10,2))   AS close,
        CAST(o.v AS BIGINT)          AS share_volume,
        CAST(o.vw AS DECIMAL(10,2))  AS volume_weighted_average_price,
        CAST(o.n AS BIGINT)          AS number_of_trades,
        CAST(o.t AS DATE)            AS trading_date
    FROM
        open AS o
''')

normalized_open.createOrReplaceTempView('normalized_open')

# COMMAND ----------

spark.sql(f'''
    INSERT OVERWRITE TABLE {destination_table}
    BY NAME
    SELECT * FROM normalized_open
''')
