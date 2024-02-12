from django.urls import path
from hellodjango import views

urlpatterns = [
    path('', views.hellodjango, name='hellodjango'),
]
