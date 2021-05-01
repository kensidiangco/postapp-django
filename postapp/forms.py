from django import forms
from .models import Post

class postForms(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('nickname', 'post_text', 'image')
		widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder':'Your nickname',
                'class':'nickname',
                'required': '',
            }),
            'post_text': forms.Textarea(attrs={
                'class':'post_text',
                'placeholder':"Write your thoughts",
            }),
            'image': forms.FileInput(attrs={
                'class':'image__field',
                'required': '',
            }),}