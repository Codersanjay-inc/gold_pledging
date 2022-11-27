from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=1000)
    mobile = models.CharField(max_length=12)
    ammount = models.IntegerField()
    address = models.TextField()
     

