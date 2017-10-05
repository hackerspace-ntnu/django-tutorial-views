from django.db import models

class Clicker(models.Model):
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.clicks)
