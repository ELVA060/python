import pandas as pd
import os
from ..decoratos.decoratos import timeit, logit

@logit
@timeit
def load_data(data_path):
    if data_path.endswith(".csv"):
        df=pd.read_csv(data_path)
    elif data_path.endswith("xlsx"):
        df=pd.read_excel(data_path)
    else: raise ValueError("Unsupported file format")
    print("Data loaded succesfully")
    return df
@logit
@timeit
def clean_data(df):
    # Assuming the 'price' column contains prices as strings with currency symbols, e.g., "$123.45"
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    print("Data cleaned successfully")
    return df
@logit
@timeit
def  analyze_data(df):
    print("Basic data Analysis:")
    print(df.describe())
    print("\nProducts with highest prices:")
    highestPrices=df.nlargest(5,"prices")
    print(highestPrices)
    return highestPrices
@logit
@timeit
def save_clean_data(df, output_path):
   
    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False)  
    elif output_path.endswith(".xlsx"):
        df.to_excel(output_path, index=False)  
    else:
        raise ValueError("Unsupported file format")  
    print(f"Clean data saved to {output_path}")

def load_data(data_path):
    
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Unsupported file format")
    print("Data loaded successfully")
    return df

def clean_data(df):
    
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    df = df.dropna()  
    df['title'] = df['title'].str.strip()  
    df['description'] = df['description'].str.strip() 
    
    print("Data cleaned successfully")
    return df

def analyze_data(df):
    
    print(df.describe())  
    print(df.info())  
    print(df.head())  

if __name__ == "__main__":
   
    data_path = "data/raw/products.csv"  
    output_path = "data/processed/cleaned_products.csv"  
    
    df = load_data(data_path)  
    df = clean_data(df)  
    analyze_data(df)  
    
    os.makedirs("data/processed", exist_ok=True)  
    save_clean_data(df, output_path)