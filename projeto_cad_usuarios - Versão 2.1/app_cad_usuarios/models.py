from django.db import models
from django.core.exceptions import ValidationError

# MODELO DE EPI
class EPI(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


# MODELO DE COLABORADOR
class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome}"


# MODELO DE EMPRÉSTIMO
class Emprestimo(models.Model):

    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('em_uso', 'Em Uso'),
        ('fornecido', 'Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    epi = models.ForeignKey(EPI, on_delete=models.CASCADE)

    quantidade = models.PositiveIntegerField()

    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='emprestado'
    )

    # VALIDAÇÕES
    def clean(self):
        
        # Data inválida
        if self.data_devolucao and self.data_devolucao < self.data_emprestimo:
            raise ValidationError("A data de devolução não pode ser antes da data de empréstimo.")
            return False

        # Status proibidos ao criar
        if self.pk is None and self.status in ['danificado', 'perdido', 'devolvido']:
            raise ValidationError("Status inválido no início do empréstimo.")
            return False

        # Quantidade maior que o estoque
        if self.pk is None:
            if self.quantidade > self.epi.quantidade:
                raise ValidationError("Quantidade solicitada maior que a disponível no estoque.")
                return False

        return True

    # SALVAMENTO — ATUALIZA O ESTOQUE
    def save(self, *args, **kwargs):

        #Evite salvar o EPI caso ele não esteja regular.
        if not self.clean(): return

        novo = self.pk is None

        super().save(*args, **kwargs)

        if novo:
            self.epi.quantidade -= self.quantidade
            self.epi.save()

        if self.status == 'devolvido':
            self.epi.quantidade += self.quantidade
            self.epi.save()

    def __str__(self):
        return f"{self.colaborador.nome} → {self.epi.nome}"

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
