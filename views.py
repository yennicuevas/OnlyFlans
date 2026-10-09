
from django.shortcuts import render
from .models import Flan,Sucursal
from django.http import HttpResponseRedirect
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def indice(request):   
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    return render(request, 'about.html')

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    usuario_nombre = request.user.get_username() or "cliente"
    return render(request, 'welcome.html', {'flanes': flanes_privados,'usuario': usuario_nombre})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    return render(request, 'contactanos.html', {'form': form})

def exito(request):
    return render( request, 'success.html')

def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente Gracias por visitarnos. Esperamos verte pronto de vuelta.")
    return redirect('/?bye=1')

def sucursales(request):
    locales = Sucursal.objects.all()
    return render(request,'sucursales.html', {'locales' : locales})


