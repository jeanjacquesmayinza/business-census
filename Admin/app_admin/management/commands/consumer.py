import pika
from django.core.management.base import BaseCommand
import json
from app_admin.models import Model_PME

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
        channel.basic_consume(queue='pme', on_message_callback=self.get_pme, auto_ack=True)

        self.stdout.write(
                self.style.SUCCESS("Le consommateur a commencé....")
            )
        channel.start_consuming()
        connection.close()

    def get_pme(ch, method, properties, body, b):
        data = b.decode('utf-8')
        message = json.loads(data)
        name = message["name"]
        fullAddress = message["fullAddress"]
        entrepreneur = message["entrepreneur"]
        creationDate = message["creationDate"]
        NumberOfEmployees = message["NumberOfEmployees"]
        regulation = message["regulation"]
        activity = message["activity"]
        if name and fullAddress and entrepreneur and creationDate and NumberOfEmployees and regulation and activity:
            pme = Model_PME.objects.create(
                name=name,
                fullAddress=fullAddress,
                entrepreneur=entrepreneur,
                creationDate=creationDate,
                NumberOfEmployees=NumberOfEmployees,
                regulation=regulation,
                activity=activity
            )
            pme.save()
            if pme:
                print("Enregistrement réussie.")

        print("[-] Message reçu !")