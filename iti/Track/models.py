from django.db import models

# Create your models here.
class Track (models.Model):
    track_id=models.AutoField(primary_key=True)
    track_name=models.CharField(max_length=100,null=False)
    track_capacity=models.IntegerField()