from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    data = models.DateField(auto_now=True)
    content = models.CharField(max_length=1000)
