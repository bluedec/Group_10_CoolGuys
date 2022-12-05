from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from .forms import UserRegisterForm, CommentForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect


#def home(request):
#    return render(request, 'home.html', {})

def home(request):
    posts_page = Paginator(Post.objects.filter(published=True), 6)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)

    list_posts = Post.objects.all()
    paginator = Paginator(list_posts, 3)
    current_page = page
    pages = range(1, posts.paginator.num_pages + 1)

    return render(request, 'home.html', {'posts':posts, "pages": pages, "current_page": current_page })

    
# Detalle del post
def post(request, post_id):
    #post = Post.objects.get(id=post_id)
    #try:
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.filter(active=True)
        new_comment = None

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
                return HttpResponseRedirect(reverse('post', args=(post_id, )))
        else:
            comment_form = CommentForm()

        return render(request, 'detail.html', {'post':post, 'comments':comments, 'new_comment':new_comment,'comment_form':comment_form})
    #except:
    #    return render(request, '404.html')
        



 
    
    

    

#Filtrado por categoria
def category(request, category_id):
    #try:
        category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=category_id)
        return render(request, 'category.html', {'category':category, 'posts':posts})
    #except:
    #    return render(request, '404.html')


#Filtrado por autor
def author(request, author_id):
    try:
        author = get_object_or_404(User, id=author_id)
        return render(request, 'author.html', {'author':author})
    except:
        return render(request, '404.html') 
      

#Filtrado por fecha 

def dates(request, month_id, year_id):

    meses ={
        1:'Enero',
        2:'Febrero',
        3:'Marzo',
        5:'Abril',
        5:'Mayo',
        6:'Junio',
        7:'Julio',
        8:'Agosto',
        9:'Septiembre',
        10:'Octubre',
        11:'Noviembre',
        12:'Diciembre',
    }
    if month_id > 12 or month_id < 1:
        return render(request, '404.html')
    posts = Post.objects.filter(published=True, created__month=month_id, created__year=year_id)
    return render(request, 'dates.html', {'posts':posts, 'month':meses[month_id], 'year':year_id })


def about(request):
    return render(request, 'about.html',)


# Registro de usurarios

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }    
    return render(request, 'register.html', context)


# Comentarios
#class AddCommentView(CreateView):
#    model = Comment
#    form_class = CommentForm
#    template_name = 'add_comment.html'

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')



    
    
   





    
