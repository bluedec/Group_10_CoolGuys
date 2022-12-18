from django.urls import path
from . import views
from .views import all_events
app_name = 'events'

urlpatterns = [
    path('calendar/', views.events, name='cal'),
    path('calendar/<int:year>/<str:month>/', views.events, name='calendar'),
    path('events/', views.all_events, name='list-events'),
    path('events/category/<int:eventcategory_id>/', views.event_category, name='event_category'),
    path('all_events', all_events, name='all_events'),
    
]