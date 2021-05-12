from django.urls import path

from . import views

urlpatterns = [
    path('', views.trending_lang, name='trending_lang'),
]