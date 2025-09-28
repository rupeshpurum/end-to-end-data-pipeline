# End-to-End Data Pipeline

## Project Overview
This project demonstrates a fully automated **data pipeline** that ingests, transforms, and loads data from multiple sources into analytics-ready storage. It covers **batch** and **near real-time processing** using Python, PySpark, Airflow, Snowflake, and Kafka.

## Problem Statement
Telecom companies generate large volumes of data from multiple sources. This pipeline provides **cleaned, aggregated, and enriched data** for analytics dashboards and reporting, ensuring **data quality, scalability, and maintainability**.

## Architecture
![Architecture Diagram](docs/architecture_diagram.png)

**Flow:**
1. Ingest data from S3, APIs, and Snowflake
2. Apply transformations and enrichments
3. Load data into analytics tables / Elasticsearch / S3
4. Monitor via Airflow DAGs

## Tech Stack
- **Programming:** Python, PySpark  
- **Orchestration:** Apache Airflow  
- **Data Storage:** Snowflake, S3, Elasticsearch  
- **Data Quality:** Great Expectations  
- **Messaging / Streaming:** Kafka  
- **Testing:** Pytest  

## Features
- Batch and near real-time ingestion
- Modular ETL pipelines
- Data validation and quality checks
- Orchestrated DAGs with retries and notifications

## Setup & Installation
```bash
# Clone the repo
git clone https://github.com/username/end-to-end-data-pipeline.git
cd end-to-end-data-pipeline

# Setup environment
bash setup.sh

# Install dependencies
pip install -r requirements.txt
