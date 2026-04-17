from django.db import models

class Material(models.Model):
    # Definindo opções fixas (Boas práticas para evitar erros de digitação dos usuários)
    CATEGORIAS_CHOICES = [
        ('ALIMENTOS', 'Alimentos não perecíveis'),
        ('VESTUARIO', 'Roupas e Calçados'),
        ('HIGIENE', 'Produtos de Higiene Pessoal'),
        ('EQUIPAMENTOS', 'Equipamentos (Cadeiras de rodas, muletas, etc)'),
        ('OUTROS', 'Outros'),
    ]

    ESTADO_CHOICES = [
        ('NOVO', 'Novo'),
        ('BOM', 'Usado (Em bom estado)'),
        ('REPARO', 'Usado (Precisa de pequenos reparos)'),
    ]

    # Criando as colunas da tabela
    nome = models.CharField(max_length=150, verbose_name="Nome do Material")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES, verbose_name="Categoria")
    quantidade = models.IntegerField(verbose_name="Quantidade em Estoque")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, verbose_name="Estado de Conservação")
    
    # Textos longos para detalhes e histórico
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações Adicionais")
    
    # Preenche a data e hora automaticamente no momento do cadastro
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    # Como o material vai se "apresentar" quando listado
    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades"
# Create your models here.
