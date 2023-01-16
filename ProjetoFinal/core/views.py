from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View
import csv


from .models import (Pessoa, 
    Veiculo, 
    MovimentoRotativo, 
    Mensalista,
    MovMensalista, 
)

from .forms import (
    PessoaForm, 
    VeiculoForm,
    MovimentoRotativoForm,
    MensalistaForm,
    MovMensalistaForm
    )
# Create your views here.

def home(request):
    context = {'mensagem' : 'Olá Mundo'}
    return render(request,'core/index.html', context)

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_pessoas')

@login_required        
def pessoa_update(request,id):
    data = {}
    pessoa = Pessoa.objects.get(id = id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)

@login_required
def pessoa_delete(request, id):
    obj = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('core_pessoas')
    else:
        return render(request, 'core/delete_confirm.html',{'obj': obj})

@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_veiculos')

@login_required
def veiculo_update(request,id):
    data = {}
    veiculo = Veiculo.objects.get(id = id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)

@login_required
def veiculo_delete(request, id):
    obj = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('core_veiculos')
    else:
        return render(request, 'core/delete_confirm.html',{'obj': obj})

@login_required
def lista_movrotativos(request):
    mov_rotativo = MovimentoRotativo.objects.all()
    form = MovimentoRotativoForm
    data = {'mov_rotativo': mov_rotativo , 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)

@login_required
def movrotativos_novo(request):
    form = MovimentoRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_movimento_rotativo')

@login_required
def movrotativo_update(request,id):
    data = {}
    mov_rotativo = MovimentoRotativo.objects.get(id = id)
    form = MovimentoRotativoForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_movimento_rotativo')
    else:
        return render(request, 'core/update_movrotativos.html', data)

@login_required
def movrotativo_delete(request, id):
    obj = MovimentoRotativo.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('core_movimento_rotativo')
    else:
        return render(request, 'core/delete_confirm.html',{'obj': obj})

@login_required
def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)

@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mensalista')

@login_required
def mensalista_update(request,id):
    data = {}
    mensalista = Mensalista.objects.get(id = id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)

@login_required
def mensalista_delete(request, id):
    obj = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('core_mensalista')
    else:
        return render(request, 'core/delete_confirm.html',{'obj': obj})

@login_required
def lista_movmensalista(request):
    mov_mensalista = MovMensalista.objects.all()
    form = MovMensalistaForm
    data = {'form':form, 'mov_mensalista': mov_mensalista}
    return render(request, 'core/lista_movmensalista.html', data)

@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_mensalista')

@login_required
def movmensalista_update(request,id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id = id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_movimento_mensalista')
    else:
        return render(request, 'core/update_movimento_mensalista.html', data)

@login_required
def movmensalista_delete(request, id):
    obj = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('core_movimento_mensalista')
    else:
        return render(request, 'core/delete_confirm.html',{'obj': obj})

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):
    def get(self,request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos' : veiculos,
            'request' : request,
        }
        return Render.render('core/relatorio.html', params, 'myfile')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        veiculos = Veiculo.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])

        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])

        return response