from django import forms
from blogs.models import Post


class CreatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'cover', 'slug' , 'text', 'status']


