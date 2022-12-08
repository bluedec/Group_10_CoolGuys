from django.urls import path
from . import views

urlpatterns = [
    path('events/<int:year>/<str:month>/', views.events, name='events'),
]