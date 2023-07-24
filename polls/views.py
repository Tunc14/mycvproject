from django.shortcuts import render
from .models import Hakkimda,Deneyim,Egitim,Yetenek,Beceriler,Sertifikalar

def index(request):
    content ={
        "hakkimda":Hakkimda.object.all(),
        "deneyimler":Deneyim.object.all(),
        "egitimler":Egitim.object.all(),
        "yetenekeler":Yetenek.object.all(),
        "sertifikalar":Sertifikalar.object.all(),
        "beceriler":Beceriler.object.all(),
    }
    return render(request,"index.html",content)
