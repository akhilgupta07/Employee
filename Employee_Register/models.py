from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullName =  models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    empCode = models.CharField(max_length=20)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)