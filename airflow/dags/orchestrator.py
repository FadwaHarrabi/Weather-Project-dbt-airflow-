from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
import sys


sys.path.append('/opt/airflow')

def safe_main_collable():
    from api_request.insert_records import main

    return main()
default_args = {
    'owner': 'fadwa',
    'depends_on_past': False,
    'email_on_failure': False,}
dag=DAG(
   dag_id='weather_api_dbt_orchestrator',
   default_args=default_args,
   schedule=timedelta(hours=8),
   start_date=datetime(2024, 1, 1),
   catchup=False

)

with  dag:
    task1=PythonOperator(
        task_id='ingest_weather_data',
        python_callable=safe_main_collable



    )

    task2=DockerOperator(
        task_id='transform_weather_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(
                source='C:/Users/user/Desktop/dbt airflow pstgres projects/Project12026-01-08/Weather-Data-Project/dbt/my_project',
                target='/usr/app',
                type='bind'
            ),
            Mount(
                source='C:/Users/user/Desktop/dbt airflow pstgres projects/Project12026-01-08/Weather-Data-Project/dbt/profiles.yml',
                target='/root/.dbt/profiles.yml',
                type='bind'
            )
        ],

        network_mode='weather-data-project_my_network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success')
    task1>>task2