from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'manvi',
    'start_date': datetime(2024, 5, 8),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG object
dag = DAG(
    'trigger_dag_run_demo',
    default_args=default_args,
    description='A DAG to trigger another DAG using TriggerDagRunOperator',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Define task using TriggerDagRunOperator
trigger_task = TriggerDagRunOperator(
    task_id='trigger_another_dag',
    trigger_dag_id='demo_dag',
    dag=dag,
)
