from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
# from logging import logging

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'http_request_dag',
    default_args=default_args,
    description='Chama uma API externa',
    # tag=['tagHere'],
    # schedule_interval=timedelta(minutes=1),
    # schedule_interval=timedelta(hours=1),
)


# api_url = 'http://localhost:3333/'
api_url = 'https://pokeapi.co/api/v2/pokemon/ditto'
responseData = ""

call_task = SimpleHttpOperator(
    task_id='server_node',
    http_conn_id='nome_conexao_pokemon_2', # Opctional
    # endpoint=api_url,
    endpoint="",
    method='GET',
    headers={},
    # data='{"parametro1": "valor1", "parametro2": "valor2"}',
    dag=dag,
)

store_task = BashOperator(
    task_id='store_external_data',
    bash_command='echo {{ task_instance.xcom_pull(task_ids="server_node") }}',
    # logging.info("output")
    dag=dag,
)

call_task >> store_task

