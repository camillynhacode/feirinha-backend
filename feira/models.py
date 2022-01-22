from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feira(models.Model):
    usuario=models.ForeignKey(
        User, 
        verbose_name="Usuário", 
        on_delete=models.CASCADE
    )
    nome=models.CharField(
        verbose_name="Nome",
        max_length=60,
    )
    data=models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Feira'
        verbose_name_plural = 'Feiras'


class ItemFeira(models.Model):
    feira=models.ForeignKey(
        Feira,
        verbose_name="Feira", 
        on_delete=models.CASCADE
    )
    nome=models.CharField(
        verbose_name="Nome do produto",
        max_length=80,
    )
    quantidade=models.PositiveIntegerField(
        verbose_name="Quantidade",
        default=1
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Item feira'
        verbose_name_plural = 'Itens feira'