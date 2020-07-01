from django.shortcuts import render, redirect
from vendas.models import Vendas
from vendas.forms import VendasForm


def list_vendas(request):
    vendas = Vendas.objects.all()
    return render(request, 'vendas.html', {'vendas': vendas})


def create_vendas(request):
    form = VendasForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_vendas')

    return render(request, 'vendas-form.html', {'form': form})


def update_vendas(request, id):
    vendas = Vendas.objects.get(id=id)
    form = VendasForm(request.POST or None, instance=vendas)

    if form.is_valid():
        form.save()
        return redirect('list_vendas')

    return render(request, 'vendas-form.html', {'form': form, 'vendas': vendas})


def delete_vendas(request, id):
    vendas = Vendas.objects.get(id=id)

    if request.method == 'POST':
        vendas.delete()
        return redirect('list_vendas')

    return render(request, 'vendas-delete-confirm.html', {'vendas': vendas})
