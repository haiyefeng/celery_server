from kombu import Exchange, Queue
from config import settings

amqp_dsn = settings.amqp_dsn
broker_url = str(amqp_dsn)
result_backend = str(settings.backend_dsn)


task_queues = (
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("add", Exchange("add"), routing_key="add"),
)

task_routes = {"celery_tasks.tasks.add": {"queue": "add", "routing_key": "add"}}


broker_connection_retry_on_startup = True
