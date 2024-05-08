from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'manvi',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG object
dag = DAG(
    'demo_dag',
    default_args=default_args,
    description='A demo dag using PyhtonOperator',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)


# Define tasks using PythonOperator
def task1():
    print("Executing task 1")


task1 = PythonOperator(
    task_id='task1',
    python_callable=task1,
    dag=dag,
)

def task2():
    print("Executing task 2")

task2 = PythonOperator(
    task_id='task2',
    python_callable=task2,
    dag=dag,
)


def task3():
    print("Executing task 3")


task3 = PythonOperator(
    task_id='task3',
    python_callable=task3,
    dag=dag,
)

def task4():
    print("Executing task 4")


task4 = PythonOperator(
    task_id='task4',
    python_callable=task4,
    dag=dag,
)


def task5():
    print("Executing task 5")


task5 = PythonOperator(
    task_id='task5',
    python_callable=task5,
    dag=dag,
)

# Define task dependencies
task1 >> task2 >> task3 >> [task4, task5]
