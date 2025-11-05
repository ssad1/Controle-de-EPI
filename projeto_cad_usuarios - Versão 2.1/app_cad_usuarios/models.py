from django.db import models

# ----------------------------
# MODELO DE EPI
# ----------------------------
class EPI(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


# ----------------------------
# MODELO DE COLABORADOR
# ----------------------------
class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    setor = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


# ----------------------------
# MODELO DE EMPRÉSTIMO
# ----------------------------
class Emprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    epi = models.ForeignKey(EPI, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_emprestimo = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.colaborador.nome} → {self.epi.nome}"

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
