from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from datetime import date,time,datetime,timedelta

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100) #informo o titulo e o max de caracteres
    local_evento = models.CharField(max_length=50)  # campo para local do evento
    descricao = models.TextField(blank=True, null=True) #informo a descrição que pode ficar em branco e nulo
    data_evento = models.DateTimeField(verbose_name='data do evento') #informo para o usuário colocar o dia do evento
    data_criacao = models.DateTimeField(auto_now=True) #me retorna a hora que foi criado o evento.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #mostrar usuários cadastrados import funçao django

    class Meta:
        db_table = 'evento' #informo o nome da tabela

    def __str__(self):
        return self.titulo #mudando o nome do evento para o titulo informado

    def get_data_criacao(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True #Retorna se está realmente atrasado, Retorne se for menor que a data de agora
        else:
            return False