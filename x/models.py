from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name;
