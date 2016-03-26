from django.db import models

class Regulation(models.Model):
    title = models.CharField(max_length=250)
    media = models.FileField()

