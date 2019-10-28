from django.db import models
class Name(models.Model):
    name = models.TextField(default='')
class Item(models.Model):
    text = models.TextField(default='')
    name = models.ForeignKey(Name,on_delete=models.CASCADE,default=None)

# Create your models here.
