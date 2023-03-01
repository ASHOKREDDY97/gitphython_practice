from django.db import models

class EmployeeDeatils(models.Model):
    name = models.CharField(max_length=200)
    salary = models.IntegerField()
    id = models.IntegerField(primary_key=True, null= False)
    email_id = models.EmailField()

    def __str__(self):
        return self.name
