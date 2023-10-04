from django.db import models

class school_store_app(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)