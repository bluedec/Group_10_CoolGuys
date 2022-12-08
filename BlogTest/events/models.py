from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
event_mode = [
    (1, 'Online'),
    (2, 'Presencial')
]

event_cost =[
    (1, 'Gratuito'),
    (2, 'De Pago')

]


class Event(models.Model):
    name = models.CharField('Nombre', max_length=120)
    Event_date = models.DateTimeField('Fecha del Evento')
    place = models.CharField('Lugar', max_length=120)
    description = models.TextField('Descripcion', blank=True)
    mode = models.IntegerField('Modalidad',
        null=False,
        choices=event_mode
    )
    cost = models.IntegerField('Costo',
        null=False,
        choices=event_cost
    )
    price = models.CharField('Precio', 
        max_length=10,
        blank=True
        )

    def __str__(self):
        return self.name