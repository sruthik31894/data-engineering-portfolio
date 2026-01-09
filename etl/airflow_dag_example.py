from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="sample_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id="run_python_etl",
        python_callable=lambda: print("ETL executed")
    )

    run_etl
