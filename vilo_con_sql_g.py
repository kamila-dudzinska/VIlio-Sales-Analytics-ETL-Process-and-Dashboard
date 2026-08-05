"""
Created on Sun Jul 26 10:00:28 2026

@author: Kamila Dudzińska

The script establish the connection between Python Pandas and SQl Lite Database.
It extracts data from a cleaned csv file and loads into a SQLite table.
This completes the finals 'Load' stage of ETL pipeline for future querying. 
        
"""

# %%

import sqlite3
import pandas as pd

def load_clean_data(path):
    return pd.read_csv(path)

def load_to_sql(df, db_path):
    conn = sqlite3.connect(db_path)
    
    df.to_sql('Vilo_Store',
              conn,
              if_exists='replace',
              index='False')
    
    conn.close()
    print('Data loaded into SQL.')
    
if __name__ =='__main__':
    new_path = r'C:\Users\lila_\Desktop\GitHub\tp_big\vilo_store_clean.csv'
    db_path = r'C:\Users\lila_\Desktop\GitHub\tp_big\vilo_store.db'
    
    df = load_clean_data(new_path)
    load_to_sql(df, db_path)
    
    
    
    
    
    
    
    
    