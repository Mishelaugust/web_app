from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dietary_needs = models.CharField(max_length=200)
    medical_conditions = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")