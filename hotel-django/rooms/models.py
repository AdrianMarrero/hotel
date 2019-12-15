from django.db import models

# Create your models here.
class Room(models.Model):
    ROOMS_TYPES = (
        ('1', 'Individual'),
        ('2', 'Doble'),
        ('3', 'Triple'),
        ('4', 'Cuadruple'),
    )
    name_room = models.CharField(max_length=50, verbose_name="Nombre de la habitación")
    room_type = models.CharField(max_length=1, choices=ROOMS_TYPES,  verbose_name="Tipo")
    number_room = models.IntegerField(primary_key=True, verbose_name="Número de Habitación")
    price_room = models.IntegerField( verbose_name="Precio")
    image = models.ImageField(upload_to="rooms", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"
        ordering = ["number_room"]

    def __str__(self):
        return self.name_room