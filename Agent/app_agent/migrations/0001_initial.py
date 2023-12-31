# Generated by Django 4.2.5 on 2023-09-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_PME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('fullAddress', models.CharField(max_length=200, verbose_name='Adresse complète')),
                ('entrepreneur', models.CharField(max_length=100, verbose_name='Entrepreneur')),
                ('NumberOfEmployees', models.IntegerField(verbose_name="Nombre d'employés")),
                ('regulation', models.CharField(choices=[('conforme', 'Conforme'), ('non_conforme', 'Non conforme')], max_length=100, verbose_name='Régulation')),
                ('activity', models.BooleanField(default=False, verbose_name='En activité')),
                ('creationDate', models.DateField(verbose_name='Date de création')),
            ],
            options={
                'verbose_name': 'Modèle PME',
                'verbose_name_plural': 'Modèles PME',
            },
        ),
    ]
