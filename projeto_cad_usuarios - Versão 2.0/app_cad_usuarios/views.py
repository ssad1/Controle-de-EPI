from django.shortcuts import render, redirect, get_object_or_404
from .models import EPI
from django.contrib import messages

# Listar todos os EPIs
def lista_epis(request):
    epis = EPI.objects.all().order_by('nome')
    return render(request, 'epis/lista.html', {'epis': epis})

# Criar novo EPI
def criar_epi(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        validade = request.POST.get('validade')
        observacoes = request.POST.get('observacoes')

        EPI.objects.create(
            nome=nome,
            categoria=categoria,
            quantidade=quantidade,
            validade=validade or None,
            observacoes=observacoes
        )
        return redirect('lista_epis')

    return render(request, 'epis/form.html')

# Editar EPI existente
def editar_epi(request, id):
    epi = get_object_or_404(EPI, id=id)

    if request.method == 'POST':
        epi.nome = request.POST.get('nome')
        epi.categoria = request.POST.get('categoria')
        epi.quantidade = request.POST.get('quantidade')
        epi.validade = request.POST.get('validade') or None
        epi.observacoes = request.POST.get('observacoes')
        epi.save()
        return redirect('lista_epis')

    return render(request, 'epis/form.html', {'epi': epi})

# Remover EPI
def deletar_epi(request, id):
    epi = get_object_or_404(EPI, id=id)
    if request.method == 'POST':
        nome = epi.nome
        epi.delete()
        messages.success(request, f'EPI "{nome}" foi excluído com sucesso!')
        return redirect('lista_epis')
    return render(request, 'epis/confirmar_delete.html', {'epi': epi})

