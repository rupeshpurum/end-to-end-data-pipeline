import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates and nulls
    df = df.drop_duplicates()
    df = df.dropna()
    
    # Example: standardize column names
    df.columns = [col.strip().lower() for col in df.columns]
    
    print("Data after cleaning:")
    print(df.head())
    return df

if __name__ == "__main__":
    sample_df = pd.read_csv("data/sample_data.csv")
    clean_data(sample_df)
