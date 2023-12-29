from django.db import models

# Create your models here.

class Botique(models.Model):
    name = models.CharField(max_length = 190,null = True)
    phone_nember = models.CharField(max_length = 190,null = True)
    location = models.CharField(max_length = 190,null = True)

    def __str__(self):
        return self.name
    

class Client(models.Model):
    name =  models.CharField(max_length = 190,null = True)
    Email = models.CharField(max_length = 190,null = True)  
    phone = models.CharField(max_length = 190,null = True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length = 190,null = True)  

    def __str__(self):
        return self.name




class Demand(models.Model):
    STATUS = (
        ('resu','resu'),
        ('in progress','in progress'),
        ('perd','perd')
    )
    botique = models.ForeignKey(Botique,null = True,on_delete = models.SET_NULL)
    client = models.ForeignKey(Client,null = True,on_delete = models.SET_NULL)
    tags =models.ManyToManyField(Tag)
    pris = models.FloatField(null = True)
    data_created = models.DateTimeField(auto_now_add = True,null = True)
    status = models.CharField(max_length = 190,null = True,choices = STATUS)    
















