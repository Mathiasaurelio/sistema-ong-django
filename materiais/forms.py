from django import forms
from .models import Material, Movimentacao, Instituicao
import re

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = Instituicao
        fields = ['nome', 'cnpj', 'endereco', 'telefone', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome):
            raise forms.ValidationError('O nome da instituição deve conter apenas letras e espaços.')
        if len(nome) < 3:
            raise forms.ValidationError('O nome da instituição deve conter pelo menos 3 caracteres.')
        return nome
        
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if not re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', cnpj):
            raise forms.ValidationError('O CNPJ deve estar no formato XX.XXX.XXX/XXXX-XX.')
        if cnpj:
            cnpj_numeros = re.sub(r'\D', '', cnpj)
            if len(cnpj_numeros) != 14:
                raise forms.ValidationError('O CNPJ deve conter 14 dígitos numéricos.')
        return cnpj
    
    def clean_endereco(self):
        endereco = self.cleaned_data.get('endereco')
        if len(endereco) < 5:
            raise forms.ValidationError('O endereço deve conter pelo menos 5 caracteres.')
        return endereco
        
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not re.match(r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', telefone):
            raise forms.ValidationError('O telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.')
        if telefone:
            telefone_numeros = re.sub(r'\D', '', telefone)
            if len(telefone_numeros) < 10 or len(telefone_numeros) > 11:
                raise forms.ValidationError('Telefone inválido.')
        return telefone
    
    email = forms.EmailField(error_messages={'invalid': 'Digite um endereço de e-mail válido.'})

# Formulário para cadastro e edição de materiais
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
    def __init__(self, *args, **kwargs):
        self.material = kwargs.pop('material', None)
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Movimentacao
        fields = ['tipo', 'quantidade']

        