from django.db import models

class EPI(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()
    validade = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.categoria})"