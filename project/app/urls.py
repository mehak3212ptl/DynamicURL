
from django.urls import path
from .views import *

urlpatterns = [
    # path('home/',home,name='home'),
    # path('integer/<int:pk>',integer, name='integer'),
    # path('string/<str:id>',string, name='string'),
    # path('slug/<slug:pkid>',slug123, name='slug'), 
    # path('path/<path:abc>',path123, name='path')

    path('comb/<int:ab>/<str:abc>/<slug:abcd>',full,name='comb')

]