from django.db import models

#this is a test purpose

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esalary=models.FloatField()

    def __str__(self):
        return self.ename


