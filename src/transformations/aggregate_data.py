import pandas as pd

def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    # Example: aggregate by 'category' column
    aggregated = df.groupby("category").agg({"value": "sum"}).reset_index()
    print("Aggregated Data:")
    print(aggregated.head())
    return aggregated

if __name__ == "__main__":
    df = pd.read_csv("data/sample_data.csv")
    aggregate_data(df)
