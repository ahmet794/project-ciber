# Databricks notebook source
spark.sql(f'''
    CREATE OR REPLACE TABLE silver_ciber.historical_market.open_historical (
        symbol STRING
            COMMENT 'Ticker',
        trading_date DATE
            COMMENT 'Trading Date',
        open DECIMAL(10,2)
            COMMENT 'Day Opening Price',
        high DECIMAL(10,2)
            COMMENT 'Day Highest Price',
        low DECIMAL(10,2)
            COMMENT 'Day Lowest Price',
        close DECIMAL(10,2)
            COMMENT 'Day Closing Price',
        share_volume BIGINT
            COMMENT 'Volume Traded',
        volume_weighted_average_price DECIMAL(10,2)
            COMMENT 'Volume Weighted Average Price',
        number_of_trades BIGINT
            COMMENT 'Number of Trades',
        daily_return DECIMAL(10,2)
            COMMENT '(Close - Open)/Open)',
        high_low_range DECIMAL(10,2)
            COMMENT '(High - Low)',
        upper_wick DECIMAL (10,2)
            COMMENT 'High - MAX(Open, Close)',
        lower_wick DECIMAL (10,2)
            COMMENT 'MIN(Open, Close) - Low',
        bronze_timestamp TIMESTAMP
            COMMENT 'Ingestion Timestamp'
    )         
''')
