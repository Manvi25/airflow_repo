from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


# Define default arguments for the DAG
default_args = {
    'owner': 'manvi',
    'start_date': datetime(2024, 5, 8),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'python_operator_dag',
    default_args=default_args,
    description='DAG using PythonOperator',
    schedule_interval=timedelta(days=1),
)

# Define Python functions to be executed by PythonOperator
def print_date():
    print("Executing task: Print Date")
    print(datetime.now())

def calculate_sum():
    print("Executing task: Calculate Sum")
    a = 5
    b = 10
    sum = a + b
    print(f"The sum of {a} and {b} is: {sum}")

def greet_user():
    print("Executing task: Greet User")
    user_name = "Everyone"
    print(f"Hello, {user_name}!")

# Define tasks using PythonOperator
task1 = PythonOperator(
    task_id='print_date_task',
    python_callable=print_date,
    dag=dag,
)

task2 = PythonOperator(
    task_id='calculate_sum_task',
    python_callable=calculate_sum,
    dag=dag,
)

task3 = PythonOperator(
    task_id='greet_user_task',
    python_callable=greet_user,
    dag=dag,
)

# Define task dependencies
task1 >> task2 >> task3
