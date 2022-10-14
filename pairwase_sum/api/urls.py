from django.urls import path

from api.views import calculate

urlpatterns = [
    path('v1/calculate/', calculate)
]