from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='database'),
    path('table/data/', views.data, name='data'),
    path('author/', views.author, name='author'),
]
