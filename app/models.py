from django.db import models

# Create your models here.

class Usuario(models.Model):
    data_nascimento = models.DateField
    cpf = models.CharField('CPF', unique=True, max_length=11)
    endereco = models.CharField('Endereço Completo', max_length=255)

class Doacao(models.Model):
    valor = models.DecimalField('Valor da doação', max_digits=10, decimal_places=2)
    confirmacao = models.BooleanField('Pagamento confirmado ?', default=False)
