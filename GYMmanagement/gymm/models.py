from django.db import models

class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=130)
    phone=models.CharField(max_length=100)
    desc=models.TextField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


# Create your models here.
