from .models import EventCategory

# Categorias
def ctx_dic_category(request):
    ctx_event_category = {}
    ctx_event_category['event_categories'] = EventCategory.objects.filter(active=True)

    print(ctx_event_category)

    return ctx_event_category