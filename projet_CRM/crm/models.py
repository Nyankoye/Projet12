from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Team(models.Model):
    name = models.CharField('Nom Equipe', max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'


class User(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='users')

    def __str__(self):
        return self.username


class Client(models.Model):
    first_name = models.CharField('Prenom', max_length=200)
    last_name = models.CharField('Nom', max_length=200)
    email = models.EmailField('Adresse mail', max_length=100)
    phone = models.CharField('Fixe', max_length=50, blank=True)
    mobile = models.CharField('Mobile', max_length=50, blank=True)
    company_name = models.CharField('Entreprise', max_length=200)
    date_created = models.DateTimeField('Date de Création', auto_now_add=True)
    date_updated = models.DateTimeField('Date de Modification', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Contract(models.Model):
    date_created = models.DateTimeField('Date de Création', auto_now_add=True)
    date_updated = models.DateTimeField('Date de Modification', auto_now=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField('Montant')
    payment_due = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contracts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracts')

    class Meta:
        verbose_name = 'Contrat'
        verbose_name_plural = 'Contrats'

    def __str__(self):
        return 'Contrat créer par: {} {}'.format(self.user.first_name, self.user.last_name)


class Event(models.Model):
    date_created = models.DateTimeField('Date de Creation', auto_now_add=True)
    date_updated = models.DateTimeField('Date de Modification', auto_now=True)
    attendees = models.IntegerField('Nombre de Participants')
    event_date = models.DateTimeField()
    note = models.TextField(max_length=8192, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='events')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='events')

    class Meta:
        verbose_name = 'Evenement'
        verbose_name_plural = 'Evenements'
