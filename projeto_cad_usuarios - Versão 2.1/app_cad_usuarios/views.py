from django.shortcuts import render, redirect, get_object_or_404
from app_cad_usuarios.models import EPI, Colaborador, Emprestimo
from app_cad_usuarios.forms import EPIForm, ColaboradorForm, EmprestimoForm
from django.contrib import messages

# CRUD DE EPIs

def lista_epis(request, check = None):

    q = request.GET.get('q')

    if q:
        epis = EPI.objects.filter(nome__icontains=q)
    else:
        epis = EPI.objects.all()

    return render(request, 'epis/lista.html', {'epis': epis})


def criar_epi(request):
    form = EPIForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'EPI cadastrado com sucesso!')
        return redirect('lista_epis')
    return render(request, 'epis/form.html', {'form': form, 'titulo': 'Cadastrar EPI'})

def editar_epi(request, id):
    epi = get_object_or_404(EPI, id=id)
    form = EPIForm(request.POST or None, instance=epi)
    if form.is_valid():
        form.save()
        messages.success(request, 'EPI atualizado com sucesso!')
        return redirect('lista_epis')
    else:
        form = EPIForm(instance=epi)   # <- CARREGA OS DADOS
    return render(request, 'epis/form.html', {'form': form, 'titulo': 'Editar EPI'})

def deletar_epi(request, id):
    epi = get_object_or_404(EPI, id=id)
    if request.method == 'POST':
        epi.delete()
        messages.success(request, 'EPI removido com sucesso!')
        return redirect('lista_epis')
    return render(request, 'epis/confirmar_delete.html', {'epi': epi})

# CRUD DE COLABORADORES
def lista_colaboradores(request):
    q = request.GET.get('q')
    if q:
        colaboradores = Colaborador.objects.filter(nome__icontains=q)
    else:
        colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores/lista.html', {'colaboradores': colaboradores})


def criar_colaborador(request):
    form = ColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Colaborador cadastrado com sucesso!')
        return redirect('lista_colaboradores')
    return render(request, 'colaboradores/form.html', {'form': form, 'titulo': 'Cadastrar Colaborador'})

def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    form = ColaboradorForm(request.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        messages.success(request, 'Colaborador atualizado com sucesso!')
        return redirect('lista_colaboradores')
    return render(request, 'colaboradores/form.html', {'form': form, 'titulo': 'Editar Colaborador'})

def deletar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador removido com sucesso!')
        return redirect('lista_colaboradores')
    return render(request, 'epis/confirmar_delete.html', {'epi': colaborador})

# CRUD DE EMPRÉSTIMOS
def lista_emprestimos(request):
    q = request.GET.get('q')
    if q:
        emprestimos = Emprestimo.objects.filter(
            Q(colaborador__nome__icontains=q) |
            Q(epi__nome__icontains=q)
        )
    else:
        emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos/lista.html', {'emprestimos': emprestimos})


def criar_emprestimo(request):
    form = EmprestimoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Empréstimo registrado com sucesso!')
        return redirect('lista_emprestimos')
    return render(request, 'emprestimos/form.html', {'form': form, 'titulo': 'Registrar Empréstimo'})

def editar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    form = EmprestimoForm(request.POST or None, instance=emprestimo)
    if form.is_valid():
        form.save()
        messages.success(request, 'Empréstimo atualizado com sucesso!')
        return redirect('lista_emprestimos')
    return render(request, 'emprestimos/form.html', {'form': form, 'titulo': 'Editar Empréstimo'})

def deletar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        emprestimo.delete()
        messages.success(request, 'Empréstimo removido com sucesso!')
        return redirect('lista_emprestimos')
    return render(request, 'epis/confirmar_delete.html', {'epi': emprestimo})

#BARRA DE BUSCAS UNIVERSAL

def buscar_EPI(request):

    caminho = request.GET.get('origin')
    resposta = request.GET.get('w')
    q = request.GET.get('q')

    #processar de onde veio a informação

    match caminho:
        case "/pesquisar/":

        case "/":
            
            epis = EPI.objects.filter(nome = resposta)

            return render(
                request, 
                'epis/lista.html', 
                {
                    'epis': epis
                }
            )
        case "/colaboradores/":
        
            colabs = Colaborador.objects.filter(nome = resposta)

            return render(
                request, 
                'colaboradores/lista.html', 
                {
                    'colaboradores': colabs
                }
            )
        case "/emprestimos/":
        
            emprestimos = Emprestimo.objects.filter(colaborador__nome=resposta)

            return render(
                request, 
                'emprestimos/lista.html', 
                {
                    'emprestimos': emprestimos
                }
            )
        case _:
            return render(
                request, 
                'falha_pesquisa.html'
            )