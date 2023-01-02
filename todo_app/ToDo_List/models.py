from django.db import models

# Create your models here.
class ToDo(models.Model):
    title=models.CharField(max_length=50)
    discription=models.TextField(max_length=50)
    complete=models.BooleanField(max_length=20)







