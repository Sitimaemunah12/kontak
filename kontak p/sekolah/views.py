from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    var_nama = "Siti Maemunah"
    contex = {
        "nama":var_nama,
    }
    return render(request, "majesti/index.html", contex)

def base(request):
    return render(request, "base.html")
