from project_settings import DATABASE
import psycopg2
import pandas as pd


def get_data_by_year(year):
    conn = psycopg2.connect(**DATABASE)
    cursor = conn.cursor()
    query = f'SELECT * FROM select_rows_by_year({year})'
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return pd.DataFrame(rows, columns=columns)


def get_data():
    table_name = 'weather_data'
    conn = psycopg2.connect(**DATABASE)
    cursor = conn.cursor()
    query = f'SELECT * FROM {table_name}'
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return pd.DataFrame(rows, columns=columns)


def check_correlation(correlation):
    if abs(correlation) > 0.5:
        return 'Korelacja silna'
    elif 0 < abs(correlation) <= 0.5:
        return 'Korelacja słaba'
    return 'Brak korelacji'


def get_values_by_year_and_months(year, start_month, end_month):
    conn = psycopg2.connect(**DATABASE)
    cursor = conn.cursor()
    query = f'SELECT * FROM select_rows_by_year_and_months({year},{start_month},{end_month})'
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return pd.DataFrame(rows, columns=columns)
