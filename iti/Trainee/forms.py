from django import forms
from django.db import models
from Account.models import Account
from .models import *

class NewTrainee(forms.Form):
    trainee_id = models.AutoField(primary_key=True)
    name = forms.CharField(max_length=100, null=False)
    id_obj = forms.ChoiceField(choices=Account.getall())
    image = models.ImageField(upload_to='.images/', null=True, blank=True)
