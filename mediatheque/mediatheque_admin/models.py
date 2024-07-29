from django.db import models


# Create your models here.

class Emprunteur(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_creation = models.DateField(auto_now_add=True)
    bloque = models.BooleanField(default=False)

    def statut_emprunteur(self):
        if self.bloque == 1:
            return 'red'
        else:
            return 'green'
    def __str__(self):
        return self.first_name