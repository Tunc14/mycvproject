from django.db import models

class Hakkimda(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    adress= models.CharField(max_length=100)
    mail= models.CharField(max_length=50)
    promotion=models.CharField(max_length=250)
    photo=models.CharField(max_length=50)

class Deneyim(models.Model):
    title=models.CharField(max_length=20)
    mission=models.CharField(max_length=20) 
    company=models.CharField(max_length=20)
    caption=models.CharField(max_length=20)

class Egitim(models.Model):
    title=models.CharField(max_length=20)
    school=models.CharField(max_length=20) 
    section=models.CharField(max_length=20)
    caption=models.CharField(max_length=20)

class Yetenek(models.Model):
    title=models.CharField(max_length=20)
    Yetenekler=models.CharField(max_length=20) 
    caption=models.CharField(max_length=20)

class Sertifikalar(models.Model):
    title=models.CharField(max_length=20)
    certificas=models.CharField(max_length=250) 
    caption=models.CharField(max_length=20)

class Beceriler(models.Model):
    title=models.CharField(max_length=20)
    skills=models.CharField(max_length=20) 
    caption=models.CharField(max_length=20)

