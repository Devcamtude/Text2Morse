from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_text_to_morse, name='convert_text_to_morse'),
]
