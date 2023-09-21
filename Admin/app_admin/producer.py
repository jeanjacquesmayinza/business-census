import pika
import json

# Connexion avec le broker rabbitmq
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
    # Etablir la connecion
    channel = connection.channel()
    # Création exchange 
    channel.exchange_declare('pme_control', durable=True, exchange_type='topic')
    # Création de la queue user
    channel.queue_declare(queue='user')
    #Lier la queue user avec l"exchange pme_control
    channel.queue_bind(exchange='pme_control', queue='user', routing_key='user')
    print('Connexion et configuration du canal RabbitMQ réussies.')

except pika.exceptions.AMQPError as e:
    print('Une erreur s\'est produite lors de la connexion à RabbitMQ :', str(e))

# Fonction de publication de message
def publish_message(message):
    body = json.dumps(message)
    channel.basic_publish(exchange='pme_control', routing_key='user', body=body)
    print("Message envoyé au broker.")