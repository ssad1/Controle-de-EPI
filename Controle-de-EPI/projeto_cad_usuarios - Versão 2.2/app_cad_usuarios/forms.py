from django import forms
from app_cad_usuarios.models import EPI, Colaborador, Emprestimo


class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nome', 'categoria', 'quantidade', 'validade']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'setor', 'cargo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'setor': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'epi', 'quantidade', 'data_emprestimo', 'data_devolucao', 'status']
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-select'}),
            'epi': forms.Select(attrs={'class': 'form-select'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'data_emprestimo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_devolucao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # SE É UM NOVO EMPRÉSTIMO, restringimos os status permitidos
        if not self.instance.pk:  # Criando → só podem estes:
            status_permitidos = ['emprestado', 'em_uso', 'fornecido']
            self.fields['status'].choices = [
                (k, v) for k, v in Emprestimo.STATUS_CHOICES if k in status_permitidos
            ]

    def clean(self):
        cleaned_data = super().clean()
        data_emprestimo = cleaned_data.get("data_emprestimo")
        data_devolucao = cleaned_data.get("data_devolucao")
        
        if data_devolucao and data_emprestimo:
            if data_devolucao < data_emprestimo:
                self.add_error("data_devolucao", "A data de devolução não pode ser antes da data de empréstimo.")
    
        return cleaned_data
