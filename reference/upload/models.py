from django.db import models


class Img(models.Model):
    id = models.AutoField(primary_key = True)
    img = models.ImageField(upload_to = "img")
