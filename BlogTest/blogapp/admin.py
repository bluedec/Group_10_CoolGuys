from django.contrib import admin
from .models import Post, Tag, Category, About, Link, Comment
admin.site.site_header = 'Administración del Blog'
admin.site.index_title = 'Panel de Cotrol'
admin.site.site_title = 'Blog'

# Register your models here.

# Post
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'category', 'published', 'author', 'created', 'post_tags')
    ordering = ('author', '-created')
    search_fields = ('title', 'author__username', 'category__name')
    list_filter = ('author', 'category__name', 'tags')

    #trampita para filtrar por etiquetas, ya la relacion de tags es de muchos a muchos

    def post_tags(self, obj):
        return ' - '.join([t.name for t in obj.tags.all().order_by('name')])

    
    post_tags.short_description = 'Etiquetas'
    

admin.site.register(Post, PostAdmin)

# Etiquetas
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Tag, TagAdmin)



# Categorias
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')
admin.site.register(Category, CategoryAdmin)

# About

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('description', 'created')

admin.site.register(About, AboutAdmin)

# Redes Sociales

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'key', 'url', 'icon')

admin.site.register(Link, LinkAdmin)

# Comentarios
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'body')
    list_display = ('name', 'post', 'body', 'date_added' )
admin.site.register(Comment, CommentAdmin)