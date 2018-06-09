from django.urls import path, include
from . import views

 
urlpatterns = [
    path('', views.TradingView.as_view(), name='get'),
]
