import pika
from django.core.management.base import BaseCommand
import json
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'RabbitMQ started consuming'

    def handle(self, *args, **options): 
        credentials = pika.PlainCredentials('guest', 'guest')
        connection  = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='rabbitmq',
                port=5672,
                virtual_host='/',
                credentials=credentials,
                heartbeat=600,
                blocked_connection_timeout=300
            )
        )
        channel = connection.channel()
        channel.basic_consume(queue='user', on_message_callback=self.get_user, auto_ack=True)

        self.stdout.write(
                self.style.SUCCESS("Le consommateur a commencé....")
            )
        channel.start_consuming()
        connection.close()

    def get_user(ch, method, properties, body, b):
        data = b.decode('utf-8')
        message = json.loads(data)
        username = message["username"]
        lastname = message["lastname"]
        firstname = message["firstname"]
        password = message["password"]
        if username and lastname and firstname and password :
            user = User.objects.create_user(username=username, last_name=lastname, first_name=firstname, password=password)
            print("Enregistrement réussie.")
        print("[-] Message reçu !")