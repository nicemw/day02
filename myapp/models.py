from django.db import models

# Create your models here.
class joke(models.Model):
    j_content = models.CharField(max_length=128)
