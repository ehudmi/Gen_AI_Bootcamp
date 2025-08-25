import psycopg2
import requests
import json

connection = psycopg2.connect(
    database="countries",
    user="postgres",
    password="ehudmi1",
    host="localhost",
    port="5433",
)

cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE countries(
               country_id SERIAL PRIMARY KEY,
               country_name VARCHAR(100) NOT NULL,
               capital VARCHAR(100),
               flag_code VARCHAR(100),
               region VARCHAR(100),
               population INTEGER NOT NULL)"""
)
connection.commit()

print("connection was made. Table successfully created")
