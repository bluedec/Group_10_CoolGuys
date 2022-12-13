from django.urls import path
from . import views
app_name = 'events'

urlpatterns = [
    path('<int:year>/<str:month>/', views.events, name='events'),
    path('events/', views.all_events, name='list-events'),
    path('events/category/<int:eventcategory_id>/', views.event_category, name='event_category'),
]