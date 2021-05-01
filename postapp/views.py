from django.shortcuts import render, redirect
from .forms import postForms
from .models import Post

def post(request):
	posts = Post.objects.all()

	form = postForms()
	if request.method == 'POST':
		form = postForms(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('post')

	return render(request, 'post.html', {'form':form, 'posts':posts})

def about(request):
	form = postForms()
	if request.method == 'POST':
		form = postForms(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('post')
	return render(request, 'about.html', {'form':form})