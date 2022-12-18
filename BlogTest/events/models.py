from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name



event_mode = [
    (1, 'Online'),
    (2, 'Presencial')
]

event_cost =[
    (1, 'Gratuito'),
    (2, 'De Pago')

]


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=120)
    event_date = models.DateTimeField('Fecha del Evento')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de finalizacion')
    place = models.CharField('Lugar', max_length=120)
    description = models.TextField('Descripcion', blank=True)
    image = models.ImageField(upload_to='Event', null=True, blank=True, verbose_name='Imagen')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    published = models.BooleanField(default=False, verbose_name='Publicado')
    event_type = models.CharField(max_length=10, null=True, blank=True, verbose_name='Tipo')

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

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-event_date']

    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='get_event', verbose_name='Categoria', null=True)

    def __str__(self):
        return self.name

