from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'node_server_endpoint',
    default_args=default_args,
    description='Executa um endpoint em Node',
    schedule_interval=timedelta(days=1),
)

start_task = BashOperator(
    task_id='start_node_server',
    bash_command='node /caminho/para/arquivo.js',
    dag=dag,
)

check_task = BashOperator(
    task_id='check_node_endpoint',
    bash_command='curl http://localhost:3000/',
    retries=3,
    dag=dag,
)

start_task >> check_task
