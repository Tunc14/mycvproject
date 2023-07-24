from django.contrib import admin
from .models import Hakkimda,Deneyim,Egitim,Yetenek,Beceriler,Sertifikalar
admin.site.register(Hakkimda)
admin.site.register(Beceriler)
admin.site.register(Yetenek)
admin.site.register(Deneyim)
admin.site.register(Egitim)
admin.site.register(Sertifikalar)

