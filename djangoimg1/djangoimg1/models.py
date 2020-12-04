from django.db import models
 
Class djangoimg1(models.Model):
      title = models.CharField(max_length=120)
      img = models.ImageField(upload_to='photos/')
