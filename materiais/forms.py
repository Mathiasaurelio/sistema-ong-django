from django import forms
from .models import Material, Movimentacao

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome', 'categoria', 'estado', 'observacoes']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['material',  'tipo', 'quantidade']