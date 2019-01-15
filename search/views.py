from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from  django.conf import  settings
import json
import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect





#Visualizar partidos en la landing page
def search(request):
    r=ProductPlaceStatus.objects.filter(product__description="Gasolina")
    return render(request, 'lugares/index.html' , { 'results': r })



'''
#Visualizar partidos en la landing page
def explicitSearch(request, nombre_lugar,id_lugar):
    l = get_object_or_404(Lugar, id=id_lugar)
    gkey=settings.GMAPS_API_KEY_JS
    formresena=UsuarioReview(prefix="resena")
    return render(request, 'lugares/details.html' , { 'lugar': l, 'gkey':gkey, 'forma':formresena })
'''
