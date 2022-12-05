from django.urls import path
from . import views
from .views import home, post, author, dates, category, about, register, AddCommentView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #Pagina de inicio
    path('', home, name='home'),

    #Pagina filtrado de author
    path('author/<int:author_id>', author, name='author'),

    #Pagina filtrado de fecha
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),

    #Detalle del post
    path('post/<int:post_id>', post, name='post'),

    #Pagina de filtrado por Categorias
    path('category/<int:category_id>', category, name='category'),

    #Pagina about
    path('about/', about, name='about'),

    #Pagina Registro
    path('register/', views.register, name='register'),

    #Pagina login/logout
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    #Pagina Comentario
    #path('post/<int:id>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),






]
