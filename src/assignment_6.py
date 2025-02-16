from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime, timedelta

default_args = {
    "owner": "manvi",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "start_date": datetime(2024, 5, 7),
}

with DAG("sensor_dag",
         start_date=datetime(2024, 5, 1),
         schedule_interval="@daily",
         default_args=default_args,
         catchup=False) as dag:

    is_forex_available = HttpSensor(
        task_id="is_forex_rate_available",
        http_conn_id="forex_api",
        endpoint="marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )
