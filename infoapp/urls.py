from django.urls import path, include
from infoapp import views

urlpatterns = [
    path('', views.info_view,name='getinfo'),

]
