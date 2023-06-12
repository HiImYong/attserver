from django.db import models

# Create your models here.

class Clients(models.Model):
    class Meta: db_table = "clients"
    name = models.CharField(max_length=30)
    userId = models.CharField(max_length=30)
    userPw = models.CharField(max_length=30)
    
