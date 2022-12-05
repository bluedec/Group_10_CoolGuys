from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField




# Create your models here.

#class post(models.Model):
#    title = models.CharField(max_length=255)
#    author = models.ForeignKey(User, on_delete=models.CASCADE)
#    body = models.TextField()
    

#    def __str__(self):
#        return self.title + ' | ' + str(self.author) 


#Modelo categoria
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


#Modelo Etiquetas

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name']

    def __str__(self):
        return self.name


#Modelos de autor = usurios registrados => Importar tabla de usuarios


#Modelo de los post

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    exerpt = models.TextField(verbose_name='Bajada')
    #content = models.TextField(verbose_name='contenido')
    content = RichTextUploadingField(verbose_name='contenido')
    image = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name='Imagen')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    #campos con relaciones

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoria')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')



    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title
        


##################################################

# Modelo about
class About(models.Model):
    
    description = models.CharField(max_length=350, verbose_name='Descripción')
    #description = RichTextUploadingField(verbose_name='Descripción')
    #image = models.ImageField(upload_to='about', null=True, blank=True, verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')


    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de Nosotros'
        ordering = ['-created']

    def __str__(self):
        return self.description


# Modelo Link

class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='Key Link')
    name = models.CharField(max_length=120, verbose_name='Red Social')
    url = models.URLField(max_length=350, blank=True, null=True, verbose_name='Enlace')
    icon = models.CharField(max_length=100, null=True, blank=True, verbose_name='Icono')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['-created']

    def __str__(self):
        return self.name 


class ResearchTopic(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()

#Modelo Comentarios

class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name= 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    



	
	
	
    






