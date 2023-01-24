from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewProducts.as_view(), name='home' ),
]