from django.db import models
from Account.models import Account
from .models import *

class Trainee(models.Model):
    trainee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    id_obj = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True) 
    image = models.ImageField(upload_to='.images/', null=True, blank=True)


    def get_account_id(self):
        return self.id_obj.id if self.id_obj else 'No Account'