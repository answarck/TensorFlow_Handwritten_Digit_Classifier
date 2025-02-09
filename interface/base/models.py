from django.db import models

class Column(models.Model):
    drawn = models.BooleanField(default=False)
