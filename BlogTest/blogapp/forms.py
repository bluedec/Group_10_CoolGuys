from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

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

		widgets = {
			#'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			
		}
