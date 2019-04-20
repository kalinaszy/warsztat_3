from django.db import models

# Create your models here.
# Jest to reprezentacja sali w aplikacji. Powinna przechowywać następujące wartości: nazwa, pojemność, dostępność rzutnika.
# Rezerwacja
#
# Ma reprezentować rezerwację sali na dany dzień. Powinien przechowywać następujące dane: datę, id sali, komentarz dodany
# przy rezerwacji.
# Powinna być połączona z obiektem Sala relacją: jedna sala może mieć wiele całodniowych rezerwacji, każdą innego dnia.
class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    capacity = models.IntegerField()
    has_projector = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#class Reservation(models.Model):

