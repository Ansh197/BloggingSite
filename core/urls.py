from django.urls import path
from core.views import landingPage

urlpatterns = [
    path('',landingPage),
]