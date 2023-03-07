from django.urls import path
from django.conf.urls import include
from .views import *


urlpatterns = [
    path('<int:element>/', details),
    path('', tree_get, name='tree_get'),
]