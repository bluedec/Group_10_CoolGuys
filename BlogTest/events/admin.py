from django.contrib import admin
from .models import Event, EventCategory

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', )
    list_display = ('name', 'event_category', 'published', 'event_date')
    ordering = ('-event_date', )
    search_fields = ('name', 'event_category__name')
    list_filter = ('event_category__name', )

admin.site.register(Event, EventAdmin)



class EventCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')
admin.site.register(EventCategory, EventCategoryAdmin)