from django.db import models
# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media',null=True,blank=True)
    deadline=models.DateField(null=True,blank=True)
    project_url = models.CharField(max_length=200,null=True,blank=True)
    comment=models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True)


class Services(models.Model):
    name = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media',null=True,blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class Lavozim(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media',null=True,blank=True)
    lavozim=models.ForeignKey(Lavozim,on_delete=models.CASCADE)
    project_url = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

class Contact(models.Model):
    name =models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    subject=models.CharField(max_length=30)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now=True)


class Subscribe(models.Model):
    gmail=models.EmailField(max_length=40)