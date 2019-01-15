from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView
from .import views
from .views import *

app_name = 'lugares'
urlpatterns = [
    #show  map
    path('', views.search, name='search'),
    # search per state
   # path('search/<int:lf_state>+<int:lf_county>+<int:lf_status>', views.explicitSearch, name='explicitSearch'),
    # AJAX 1 min 4 update


]