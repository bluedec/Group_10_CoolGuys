from .models import About, Link, Category, Post


# Los procesadores de contexto inyectan diccionarios en el archivo base

# About
def ctx_dic_about(request):
    ctx_about = {}

    ctx_about['about'] = About.objects.latest('created')

    return ctx_about


# Categorias
def ctx_dic_category(request):
    ctx_category = {}
    ctx_category['categories'] = Category.objects.filter(active=True)

    return ctx_category

# Archivos
def ctx_dic_history(request):
    ctx_history = {}
    ctx_history['dates'] = Post.objects.dates('created', 'month', order='DESC').distinct()
    return ctx_history

# Redes Sociales
def ctx_dic_link(request):

    ctx_link = {}

    links = Link.objects.all()

    for link in links:
        ctx_link[link.key] = {'url':link.url, 'icon':link.icon}

    return ctx_link