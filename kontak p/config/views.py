from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from sekolah.models import sekolah
from siswa.models import siswa
from perusahaan.models import Perusahaan
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    
    return render(request, "aplikasi/index.html")

# def sekolah(request):
#     return render(request, "aplikasi/sekolah.html")

@login_required(login_url=settings.LOGIN_URL)
def data (request):
    
    sekolahs = sekolah.objects.all()
    
    konteks = {
        'sekolahs' : sekolahs
        
    }
    return render(request, 'aplikasi/sekolah.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def datasiswa (request):
    
    siswas = siswa.objects.all()
    
    konteks = {
        'siswas' : siswas
        
    }
    return render(request, 'aplikasi/siswa.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def dataperusahaan (request):
    
    perusahaans = Perusahaan.objects.all()
    
    konteks = {
        'perusahaans' : perusahaans
        
    }
    return render(request, 'aplikasi/perusahaan.html', konteks)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

