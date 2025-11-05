from django import forms
from app_cad_usuarios.models import EPI, Colaborador, Emprestimo

class EPIForm(forms.ModelForm):
    class Meta:
        model = EPI
        fields = ['nome', 'categoria', 'quantidade', 'validade']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'matricula', 'setor', 'cargo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'setor': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'epi', 'quantidade']
        widgets = {
            'colaborador': forms.Select(attrs={'class': 'form-select'}),
            'epi': forms.Select(attrs={'class': 'form-select'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

