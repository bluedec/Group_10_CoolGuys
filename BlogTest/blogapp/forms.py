from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Comment

class UserRegisterForm(UserCreationForm):
	username= forms.CharField(label='',max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
	email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '' }))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '' }))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '' }))

	class Meta:
		model = User
		fields  = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields}


#class CommentForm(forms.ModelForm):
#      class Meta:
#        model = Comment
#        fields = '__all__'
#
#        widgets ={
#            'user': forms.TextInput(attrs={'class': 'form-control'}),
#            'content': forms.Textarea(attrs={'class': 'form-control'}),
#        }


#class CommentForm(forms.ModelForm):
#   class Meta:
#        model = Comment
#        fields = ('user', 'post', 'content')
#        
#        widgets = {
#            'user': forms.TextInput(attrs={'value': '', 'id':'author'}),
#            'post': forms.TextInput(attrs={'value': '', 'id':'post'}),
			
#            'content': forms.Textarea(attrs={'class': 'form-control'}),
#        }

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')
		labels= {
			'body':'',
		}

		widgets = {
			#'name': forms.TextInput(attrs={'class': 'form-control'}),
			'name':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu comentario' }),			
			
		}

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'hi',
        }
))
