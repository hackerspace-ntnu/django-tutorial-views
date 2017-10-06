from django.db import models

class Clicker(models.Model):
    clicks = models.PositiveIntegerField(default=0)
    name = models.CharField(default="Clicker", max_length=50, primary_key=True)

    def __str__(self):
        return self.name + " - " + str(self.clicks)
