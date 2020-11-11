from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100) #informo o titulo e o max de caracteres
    descricao = models.TextField(blank=True, null=True) #informo a descrição que pode ficar em branco e nulo
    data_evento = models.DateTimeField(verbose_name='data do evento') #informo para o usuário colocar o dia do evento
    data_criacao = models.DateTimeField(auto_now=True) #me retorna a hora que foi criado o evento.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento' #informo o nome da tabela

    def __str__(self):
        return self.titulo #mudando o nome do evento para o titulo informado

