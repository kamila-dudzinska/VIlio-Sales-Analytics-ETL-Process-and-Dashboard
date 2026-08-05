"""
Created on Sun Jul 25 11:00:28 2026

@author: Kamila Dudzińska

The ETL process extract raw data, cleans missing or incorrrect values and 
extracts the clean dataset into a new .csv file.
The pipeline ensures data quality before analysis. 
        
"""


# %%
import pandas as pd

def load(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    
    #duplicates cleaning
    df = df.drop_duplicates()
    
    #NaN filling
    df = df.fillna({
        'Discount': 0,
        'Quantity':0,
        'Profit':0,
        'Sales':'NA'
        })
    
    #Data Types conversion
    df['Postal Code'] = pd.to_numeric(df['Postal Code'],
                                    errors='coerce')
    df['Order ID'] = df['Order ID'].astype(str)
    df['Order Date'] = pd.to_datetime(df['Order Date'],
                                      errors='coerce')
    
    df['Ship Date'] = pd.to_datetime(df['Ship Date'],
                                     errors = 'coerce')
    
    df['Sales'] = pd.to_numeric(df['Sales'],
                                errors = 'coerce')
    df['Quantity'] = pd.to_numeric(df["Quantity"],
                                   errors='coerce')
    df['Dicount'] = pd.to_numeric(df['Discount'],
                                  errors = 'coerce')
    df['Profit'] = pd.to_numeric(df['Profit'],
                                 errors='coerce')
    
    
    #konkretny format daty -zmiana na europejski
    df['Order Date'] = df['Order Date'].dt.strftime('%d/%m/%Y')
    df['Ship Date'] = df['Ship Date'].dt.strftime('%d.%m.%Y')
    
    return df

def save_processed(df, path):
    df.to_csv(path, index=False)
    
if __name__ == '__main__':
    raw_path = r'C:\Users\lila_\Desktop\GitHub\tp_big\vilo_store.csv'
    new_path = r'C:\Users\lila_\Desktop\GitHub\tp_big\vilo_store_clean.csv'
    
    df = load(raw_path)
    df_clean = clean_data(df)
    save_processed(df_clean,
                   new_path)
    
    print('Data preprocessing completed')
    
    
    
    
    
    