from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import UserSerializer, GroupSerializer, \
EdificioSerializer, DepartamentoSerializer

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

def index(request):

    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios, 'numero_edificios': len(edificios)}
    return render(request, 'index.html', informacion_template)


def obtener_edificio(request, id):

    edificio = Edificio.objects.get(pk=id)
    informacion_template = {'edificio': edificio}
    return render(request, 'obtener_edificio.html', informacion_template)


def crear_edificio(request):

    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_edificio.html', diccionario)


def editar_edificio(request, id):

    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_edificio.html', diccionario)


def eliminar_edificio(request, id):

    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)


def crear_departamento(request):

    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_departamento.html', diccionario)


def editar_departamento(request, id):

    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_departamento.html', diccionario)

def eliminar_departamento(request, id):

    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

def crear_departamento_edificio(request, id):

    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'crear_departamento_edificio.html', diccionario)

# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EdificioViewSet(viewsets.ModelViewSet):

    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
