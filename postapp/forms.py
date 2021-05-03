from django import forms
from .models import Post, Comment

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class UserCreateForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','email','password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder':'Username',
                'class': 'form-control form-control-user',
                'autocapitalize':'none',
                'id':'username',
            }),
            'email': forms.TextInput(attrs={
                'type': 'email',
                'placeholder':'Email',
                'class': 'form-control',
                'required': '',
      }),
    }
    
    def __init__(self, *args, **kwargs):
        
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': ("New password"),
            'class': ("form-control form-control-user"),
        })
        
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': ("Confirm password"),
            'class': ("form-control form-control-user"),
        })

class postForms(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('post_text', 'image')
		widgets = {
            'post_text': forms.Textarea(attrs={
                'class':'post_text',
                'placeholder':"Write your thoughts",
            }),
            'image': forms.FileInput(attrs={
                'class':'image__field',
                'required': '',
            }),}

class postCommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.TextInput(attrs={
                'class':'comment__input',
                'placeholder':"Say something about this post.",
            }),}