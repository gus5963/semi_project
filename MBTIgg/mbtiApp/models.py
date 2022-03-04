from django.db import models

# Create your models here.
class Mbti(models.Model):
    mbti_id = models.CharField(max_length=4,primary_key=True)
    defi = models.CharField(max_length=50)
    profile = models.TextField()