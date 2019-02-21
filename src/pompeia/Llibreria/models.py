from django.db import models
import datetime

ALBARÀ_CHOICES = (
    ('c', 'Crèdit'),
    ('o', 'Comptat'),
    ('r', 'Retorn'),
    ('d', 'Dipòsit'),
    ('n', 'Novetat'),
)

# No depenen de ningú.
class Encuadernació(models.Model):
    nom = models.CharField(max_length = 20)

class Idioma(models.Model):
    nom = models.CharField(max_length = 20)

class Tema(models.Model):
    nom = models.CharField(max_length = 20)

class Ciutat(models.Model):
    nom = models.CharField(max_length = 100)

class CoŀleccióNom(models.Model):
    nom = models.CharField(max_length = 100)

class Departament(models.Model):
    nom = models.CharField(max_length = 100)

class Editorial(models.Model):
    nom = models.CharField(max_length = 100)

class Observacions(models.Model):
    text = models.TextField()

class Autor(models.Model):
    Primer_nom = models.CharField(max_length = 30)
    Segon_nom = models.CharField(max_length = 30)

class Persona(models.Model):
    Primer_nom = models.CharField(max_length = 30)
    Segon_nom = models.CharField(max_length = 30)

class Traductor(models.Model):
    Primer_nom = models.CharField(max_length = 30)
    Segon_nom = models.CharField(max_length = 30)

# Senzills.
class Adreça(models.Model):
    direcció = models.CharField(max_length = 100)
    ciutat = models.ForeignKey(Ciutat, on_delete = models.PROTECT)

class Coŀlecció(models.Model):
    nom = models.ForeignKey(CoŀleccióNom, on_delete = models.PROTECT)
    número = models.CharField(max_length = 9)

# Interessants.
class Proveïdor(models.Model):
    nom = models.CharField(max_length = 100)
    nif = models.CharField(max_length = 9)
    adreça = models.ForeignKey(Adreça, on_delete = models.PROTECT)
    telèfon = models.CharField(max_length = 20)
    correu_electrònic = models.EmailField()
    representant = models.ForeignKey(Persona, on_delete = models.PROTECT)
    descompte = models.DecimalField(max_digits = 3, decimal_places = 2)

class Albarà(models.Model):
    proveïdor = models.ForeignKey(Proveïdor, on_delete = models.PROTECT)
    data = models.DateField(default = datetime.date.today)
    número = models.CharField(max_length = 20)
    # * client = models.PositiveIntegerField() (?)
    tipus = models.CharField(max_length = 1, choices = ALBARÀ_CHOICES)

class Catàleg(models.Model):
    ISBN = models.CharField(max_length = 13)
    departament = models.ManyToManyField(Departament)
    tema = models.ManyToManyField(Tema)
    títol = models.CharField(max_length = 100)
    autor = models.ForeignKey(Autor, on_delete = models.PROTECT)
    observacions = models.ManyToManyField(Observacions)
    idioma_publicat = models.ForeignKey(Idioma, on_delete = models.PROTECT,
                                  related_name='publicat')
    idioma_origal = models.ForeignKey(Idioma, on_delete = models.PROTECT,
                                  related_name='original', null = True)

class MetaLlibre(models.Model):
    catàleg = models.ForeignKey(Catàleg, on_delete = models.PROTECT)
    tamany_alt = models.DecimalField(max_digits = 2, decimal_places = 1)
    tamany_fons = models.DecimalField(max_digits = 2, decimal_places = 1)
    edició = models.CharField(max_length = 3)
    editorial = models.ForeignKey(Proveïdor, on_delete = models.PROTECT)
    coŀlecció = models.ForeignKey(Coŀlecció, on_delete = models.PROTECT,
                                  null = True)
    traductor = models.ForeignKey(Traductor, on_delete = models.PROTECT,
                                  null = True)
    encuadernació = models.ForeignKey(Encuadernació, on_delete = models.PROTECT)

# Informació realment desitjada.
class Llibre(models.Model):
    albarà = models.ForeignKey(Albarà, on_delete = models.PROTECT)
    meta_llibre = models.ForeignKey(MetaLlibre, on_delete = models.PROTECT)
    preu_venta_públic = models.DecimalField(max_digits = 6, decimal_places = 2)
    venut = models.DateField(default = None, null = True)
