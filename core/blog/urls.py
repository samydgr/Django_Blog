from django.urls import path
from .views import indexView
urlpatterns = [
    path('about/', indexView,name = "fbv-test"),
    
    ]
