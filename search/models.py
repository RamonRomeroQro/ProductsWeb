import uuid
from django.db import models
# Create your models here.

import os

#modelo de datos_pais

class Country(models.Model):
    name=models.CharField(verbose_name='País', null=True, blank=True, max_length=200)
    def __str__(self):
        return self.name

# Modelo de datos_estado

class State(models.Model):
    name=models.CharField(verbose_name='Estado', null=True, blank=True, max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#Modelo de datos_ciudad aka Municipio

class County(models.Model):
    name=models.CharField(verbose_name='Ciudad', null=True, blank=True, max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Place(models.Model):
    retrievedID = models.CharField(verbose_name='retrievedID', primary_key=True, max_length=100)
    name= models.CharField(verbose_name='Nombre', null=True, blank=True, max_length=200)
    address= models.CharField(verbose_name='Dirección', null=True, blank=True, max_length=500)
    latitude = models.FloatField(verbose_name='Latitude', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Longitude', null=True, blank=True)
    county = models.ForeignKey(County, verbose_name='Ciudad', on_delete=models.CASCADE,  null=True, blank=True)



    def __str__(self):
        return self.name


class Product(models.Model):
    description= models.CharField(verbose_name='Nombre', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.descripcion

class ProductPlaceStatus(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)




    possibleStatus = (
        (1, 'Desconocido'),
        (2, 'Reabasteciendo'),
        (3, 'Agotado'),
        (4, 'Poca Disponibilidad'),
        (5, 'Alta Disponibilidad'),
    )
    currentStatus  = models.IntegerField(verbose_name='Estado Actual', choices=possibleStatus, default=1)
    #selection field Viable, Desconocido, Agotado, Refill, Atascado
    #TimeStamp last update
    created_date = models.DateTimeField(verbose_name='Fecha de Creación ',   null=True, blank=True, auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name='Fecha de Modificación ',  null=True, blank=True, auto_now=True)



class Report(models.Model):
    changeProductPlaceStatus = models.ForeignKey(ProductPlaceStatus, on_delete=models.CASCADE)
    possibleStatus = (
        (1, 'Desconocido'),
        (2, 'Reabasteciendo'),
        (3, 'Agotado'),
        (4, 'Poca Disponibilidad'),
        (5, 'Alta Disponibilidad'),
    )
    suggestedStatus = models.IntegerField(verbose_name='Estado', choices=possibleStatus, default=1)

    moreInformation = models.CharField(verbose_name='Más Información', null=True, blank=True, max_length=1000)
    created_date = models.DateTimeField(verbose_name='Fecha de Creación ', null=True, blank=True, auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name='Fecha de Modificación ', null=True, blank=True, auto_now=True)




