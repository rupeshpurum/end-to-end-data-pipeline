from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.ingestion.s3_ingest import ingest_s3_data
from src.transformations.clean_data import clean_data
from src.transformations.aggregate_data import aggregate_data

default_args = {
    "owner": "data_engineer",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
}

def run_pipeline():
    df = ingest_s3_data()
    df_clean = clean_data(df)
    df_agg = aggregate_data(df_clean)
    df_agg.to_csv("data/final_output.csv", index=False)
    print("Pipeline completed successfully!")

with DAG(
    "etl_pipeline_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task_pipeline = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_pipeline
    )
