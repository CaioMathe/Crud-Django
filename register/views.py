from django.shortcuts import render, redirect
from .models import Cadas
from register.forms import ClientForm


def list_registered(request):
    clientes = Cadas.objects.all()
    return render(request, 'index-client.html', {'clientes': clientes})


def create_register(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_registered')

    return render(request, 'client-form.html', {'form': form})


def update_register(request, id):
    client = Cadas.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('list_registered')

    return render(request, 'client-form.html', {'form': form, 'client': client})


def delete_register(request, id):
    cliente = Cadas.objects.get(id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('list_registered')

    return render(request, 'delete-confirm.html', {'cliente': cliente})


