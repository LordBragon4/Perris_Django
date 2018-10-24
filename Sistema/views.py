from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.template import loader, RequestContext
from .forms import RegistrarPersona
from .forms import RegistrarMascota
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"Index",
    }
    return HttpResponse(plantilla.render(contexto,request))

def registro(request):
    form=RegistrarPersona(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        u=User.objects.create_user(data.get("rutPersona"),data.get("mailPersona"),data.get("passwordPersona"))
        u.save()
    form=RegistrarPersona()
    return render(request,"Registro.html",{'form':form,})
    
def upload_image_view(request):
    if request.method == 'POST':
        form = RegistrarMascota(request.POST)
        if form.is_valid():
            form.save()
            message = "Imagen subida correctamente!"
    else:
        form = RegistrarMascota()

    return render(request, 'lala.html', {'form':form,})

