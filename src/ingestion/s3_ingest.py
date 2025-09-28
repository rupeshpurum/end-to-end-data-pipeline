import pandas as pd
import boto3
import os

# S3 Configuration
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = "sample-bucket"
FILE_KEY = "sample_data.csv"

def ingest_s3_data():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    
    response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
    df = pd.read_csv(response['Body'])
    print("S3 Data Ingested:")
    print(df.head())
    return df

if __name__ == "__main__":
    ingest_s3_data()
