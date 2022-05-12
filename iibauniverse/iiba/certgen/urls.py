from django.urls import path
from .views import Upload, sample

urlpatterns = [
    path('upload', Upload, name='upload' ),
    path('sample', sample, name='sample' ),


]