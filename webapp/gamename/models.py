from django.db import models

class Gametitle(models.Model):
    title = models.TextField()
    content = models.TextField()
