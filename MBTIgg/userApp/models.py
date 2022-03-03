from django.db import models
from django.db.models import Q
from mbtiApp.models import *

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    mbti_id = models.ForeignKey(Mbti,on_delete=models.CASCADE, db_column='mbti_id')
    birth = models.DateField()
    pwd = models.CharField(max_length=60)
    gender = models.CheckConstraint(check=Q(gender__in='M' or 'F'), name='gender')