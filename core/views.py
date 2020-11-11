from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.
# def index(request):
#     return redirect('/agenda')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    response = {'eventos':evento}
    return render(request, 'agenda.html', response)

#def Consulta(request,titulo_evento):
    #consulta = Evento.objects.get(titulo= titulo_evento)
    #return HttpResponse(consulta)