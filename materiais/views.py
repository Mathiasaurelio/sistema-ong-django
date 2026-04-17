from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from .forms import MaterialForm

# --- Lógica da Tela de Estoque ---
def lista_materiais(request):
    materiais_no_banco = Material.objects.all()
    contexto = {'materiais': materiais_no_banco}
    return render(request, 'materiais/lista_materiais.html', contexto)

# --- Lógica da Tela de Cadastro ---
def cadastrar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_materiais')
    else:
        form = MaterialForm()

    contexto = {'form': form}
    return render(request, 'materiais/cadastro_material.html', contexto)

# --- Lógica da Tela de Edição ---
def editar_material(request, id):
    material = get_object_or_404(Material, id=id)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('lista_materiais')
    else:
        form = MaterialForm(instance=material)

    contexto = {'form': form}
    return render(request, 'materiais/cadastro_material.html', contexto)

# --- Lógica da Tela de Exclusão (A QUE ESTAVA FALTANDO!) ---
def excluir_material(request, id):
    material = get_object_or_404(Material, id=id)

    if request.method == 'POST':
        material.delete() # O comando que apaga do banco de dados
        return redirect('lista_materiais')

    contexto = {'material': material}
    return render(request, 'materiais/confirmar_exclusao.html', contexto)