from src.ingestion.s3_ingest import ingest_s3_data

def test_s3_ingest():
    df = ingest_s3_data()
    assert df.shape[0] > 0
    assert "category" in df.columns
