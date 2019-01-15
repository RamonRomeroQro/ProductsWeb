



# XML Retrived from:
# https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-comerciales-de-gasolina-y-diesel-de-cre/resource/bfbe9236-5992-4239-947f-41ef6969e9c1

# To Json thanks to:
# https://codebeautify.org


#echo "Drop DATABASE product; DROP RolE postgres; CREATE DATABASE product;create user postgres with encrypted password 'postgres';grant all privileges on database product to postgres;" > new.sql


from productsWeb.settings import BASE_DIR
from search.models import *
import time

import json
import os

from geopy.geocoders import Nominatim

def fromFileToDataBaseObject(fl):


    #open JSON file
    data = json.loads(open(fl).read())
    total= (data["places"]["place"])

    for i in range(len(total)):
        #retrive elements from JSON file
        name = (data["places"]["place"][i]['name'])
        x = (data["places"]["place"][i]['location']['x'])
        y = (data["places"]["place"][i]['location']['y'])
        address = (data["places"]["place"][i]['location']["address_street"])
        rid = (data["places"]["place"][i]["_place_id"])

        if len(Place.objects.filter(retrievedID=rid))==0:
            al=(str(y)+', '+str(x))

            #CallGeocoder for propper data fillup
            time.sleep(2)

            geolocator = Nominatim(user_agent="gas")
            location = geolocator.reverse(al)

            # Maping of attributes

            lat = ((location.latitude))
            long = ((location.longitude))
            retrievedAddress=(location.address)

            try:
                retrievedCounty = (location.raw["address"]["county"])
            except Exception as e:
                retrievedCounty = "Unknown"








            retrievedState=(location.raw["address"]["state"])
            retrievedCountry=(location.raw["address"]["country"])

            # Creation of data base objects

            # Country creation or get
            try:
                dbCountry = Country.objects.get(name=retrievedCountry)
            except Country.DoesNotExist:
                dbCountry = Country(name=retrievedCountry)
                dbCountry.save()

            # Creation State or get

            try:
                dbState = State.objects.get(name=retrievedState, country=dbCountry.id)
            except State.DoesNotExist:
                dbState = State(name=retrievedState, country_id=dbCountry.id)
                dbState.save()


            # Creation County/City or get

            try:
                dbcounty = County.objects.get(name=retrievedCounty, state=dbState.id)
            except County.DoesNotExist:
                dbcounty = County(name=retrievedCounty, state_id=dbState.id)
                dbcounty.save()



            try:
                pl = Place.objects.get( name=name, address=retrievedAddress, latitude=lat, longitude=long, county_id=dbcounty.id, retrievedID=rid)

            except Place.DoesNotExist:



                pl = Place(name=name, address=retrievedAddress, latitude=lat, longitude=long, county_id=dbcounty.id, retrievedID=rid)
                pl.save()



            try:
                pr = Product.objects.get(description="Gasolina")
            except Product.DoesNotExist:
                pr = Product(description="Gasolina")
                pr.save()

            try:
                r = ProductPlaceStatus.objects.get(product_id=pr.id, place__retrievedID=pl.retrievedID)
                r.currentStatus=1
                r.save()
            except ProductPlaceStatus.DoesNotExist:
                r = ProductPlaceStatus(product_id=pr.id, place_id=pl.retrievedID)
                r.save()



from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'DB Gas MEX'

    def handle(self, *args, **options):
        f=BASE_DIR+'/productsWeb/search/management/files/places.json'
        # if file is not in media root, copy it to there
        fromFileToDataBaseObject(f)

        self.stdout.write(self.style.SUCCESS('Success'+f))
        #echo "Drop DATABASE PRODUCTS; CREATE DATABASE PRODUCTS;create user postgres with encrypted password 'postgres';grant all privileges on database PRODUCTS to postgres;" > new.sql














