from django.urls import path
from .views import Upload, Send

urlpatterns = [
    path('', Upload, name='upload' ),
    path('send', Send, name='send')
]