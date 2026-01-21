from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
import sys


sys.path.append('/opt/airflow/api_request')

def safe_main_collable():
    from api_request.insert_records import main

    return main()
default_args = {
    'owner': 'fadwa',
    'depends_on_past': False,
    'email_on_failure': False,}
dag=DAG(
   dag_id='orchestrator',
   default_args=default_args,
   schedule=timedelta(minutes=1),
   start_date=datetime(2026, 1, 1),
   catchup=False

)

with  dag:
    task1=PythonOperator(
        task_id='ingest_weather_data_task',
        python_callable=safe_main_collable



    )

