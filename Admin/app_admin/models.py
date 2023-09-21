from django.db import models

REGULATION_CHOICES = [
    ('conforme', 'Conforme'),
    ('non_conforme', 'Non conforme'),
]

class Model_PME(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    fullAddress = models.CharField(max_length=200, verbose_name='Adresse complète')
    entrepreneur = models.CharField(max_length=100, verbose_name='Entrepreneur')
    NumberOfEmployees = models.IntegerField(verbose_name='Nombre d\'employés')
    regulation = models.CharField(max_length=100, choices=REGULATION_CHOICES, verbose_name='Régulation')
    activity = models.BooleanField(default=False, verbose_name="En activité")
    creationDate = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Date de création")

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Modèle PME'
        verbose_name_plural = 'Modèles PME'