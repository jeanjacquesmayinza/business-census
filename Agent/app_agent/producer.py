import pika
import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='rabbitmq',
        port=5672,
        virtual_host='/',
        credentials=credentials,
        heartbeat=600,
        blocked_connection_timeout=300
    )
)

try:
    channel = connection.channel()
    channel.exchange_declare('pme_control', durable=True, exchange_type='topic')
    channel.queue_declare(queue='pme')
    channel.queue_bind(exchange='pme_control', queue='pme', routing_key='pme')
    print('Connexion et configuration du canal RabbitMQ réussies.')

except pika.exceptions.AMQPError as e:
    print('Une erreur s\'est produite lors de la connexion à RabbitMQ :', str(e))


def publish_message(message):
    body = json.dumps(message)
    channel.basic_publish(exchange='pme_control', routing_key='pme', body=body)
    print("Message envoyé au broker.")