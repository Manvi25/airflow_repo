from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args={
    'owner':'manvi',
    'start_date': datetime(2024,5,8),
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

dag= DAG(
    dag_id= 'bash_operator_dag',
    default_args= default_args,
    description='Perform some actions using bash operator',
    schedule_interval= timedelta(days=1)
)
# Define tasks using BashOperator
#print the current date using the date command.
task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)
# lists files in the home directory using ls -l ~
task2 = BashOperator(
    task_id='list_files_in_home',
    bash_command='ls -l ~',
    dag=dag,
)
# checking  disk space using df -h.
task3 = BashOperator(
    task_id='check_disk_space',
    bash_command='df -h',
    dag=dag,
)

# display system information using uname -a.
task4 = BashOperator(
    task_id='show_system_info',
    bash_command='uname -a',
    dag=dag,
)

# Defining  task dependencies
task1 >> task2 >> task3 >> task4

