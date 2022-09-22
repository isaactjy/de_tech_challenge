from airflow import DAG, utils
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import dailyexports.sales as sales

default_args = {
    'owner': 'isaac',
    'depends_on_past': False,
    'start_date': utils.dates.days_ago(2),
    'email': ['teojyiz@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
    dag_id = 'dailyexports',
    description = 'Process daily data.',
    catchup=False,
    schedule_interval = '0 1 * * *',
    default_args = default_args,
) as dag:
    get_sales = PythonOperator(
        task_id = 'get_sales',
        python_callable = sales.getSales
    )