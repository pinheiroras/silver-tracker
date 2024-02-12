from django.db import models


class Produto(models.Model):
    UNIDADE_CHOICES = [
        ('unidade', 'Unidade'),
        ('par', 'Par'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    nome_produto = models.CharField(max_length=255)
    unidade = models.CharField(
        max_length=10, choices=UNIDADE_CHOICES, blank=True, null=True)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    margem = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    saldo_estoque = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Calcula automaticamente a margem de lucro ao salvar
        if self.preco_custo and self.preco_venda:
            self.margem = (
                (self.preco_venda - self.preco_custo) / self.preco_custo) * 100
        # Uppercase do código
        self.codigo = self.codigo.upper() if self.codigo else self.codigo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_produto} - {self.codigo}"

    class Meta:
        db_table = 'produto'
