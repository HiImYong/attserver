from django.db import models

# Create your models here.

class Clients(models.Model):
    class Meta: db_table = "clients"
    name = models.CharField(max_length=30)
    userId = models.CharField(max_length=30)
    userPw = models.CharField(max_length=30)
    
class LastTime(models.Model):
    class Meta: db_table = "last_time"
    userId = models.CharField(max_length=30, unique=1)
    lastTime = models.TimeField()
    

