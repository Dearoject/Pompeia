from django.db import models

class Albarà(models.Model):
    data = models.DateField(auto_now_add = True)
    número = models.PositiveIntegerField()
    client = models.PositiveIntegerField()

class DescriptorLlibre(models.Model):
    ISBN = models.PositiveIntegerField(primary_key=True)
    títol = models.CharField(max_length = 20)
    autor = models.CharField(max_length = 20)

class ConcretLlibre(models.Model):
    descriptor = models.ForeignKey(DescriptorLlibre, on_delete = models.PROTECT)
    editorial = models.CharField(max_length = 20)
    preu = models.DecimalField(max_digits = 10, decimal_places = 2)
    tapa = models.CharField(max_length = 1, default = 'P',
            choices = (
                ('P', 'Paper'),
                ('C', 'Carto'),
            ))

class Llibre(models.Model):
    albarà = models.ForeignKey(Albarà, on_delete = models.PROTECT)
    llibre = models.ForeignKey(ConcretLlibre, on_delete = models.PROTECT)
    estat = models.CharField(max_length = 1, default = 'E',
            choices = (
                ('I', 'Entrant'),
                ('S', 'En venta'),
                ('V', 'Venut'),
                ('R', 'Retornat'),
            ))
