from django.db import models
from datetime import date, datetime

# Create your models here.

class Book(models.Model):
    STATE = (
        ('Confirmada', 'Confirmada'),
        ('Checkin', 'Checkin'),
        ('Checkout', 'Checkout'),
    )
    number_book = models.IntegerField(verbose_name="Número de habitación", null=True, blank=True)
    date_start = models.DateField(verbose_name="Fecha de entrada", auto_now_add=False, auto_now=False, blank=True, null=True)
    date_end = models.DateField(verbose_name="Fecha de salida", auto_now_add=False, auto_now=False, blank=True, null=True)
    days = models.IntegerField(verbose_name="Días")
    n_persons = models.IntegerField(verbose_name="Número de personas")
    total_price = models.IntegerField(verbose_name="Precio Total")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    surname = models.CharField(max_length=50, verbose_name="Apellidos")
    email = models.EmailField(verbose_name="Correo electrónico")
    name_of_card = models.CharField(max_length=50, verbose_name="Nombre de la tarjeta")
    credit_card_number = models.IntegerField(verbose_name="Número de tarjeta")
    State = models.CharField(max_length=10, choices=STATE, null=True, blank=True)
    notes = models.TextField(verbose_name='Notas', null=True, blank=True)
    locator = models.CharField(max_length=32, verbose_name="Localizador", null=True, blank=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return self.name

