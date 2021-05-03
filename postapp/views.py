from django.shortcuts import render, redirect
from .forms import postForms, UserCreateForm, postCommentForms
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

@unauthenticated_user
def register(request):
    
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)
            
            messages.success(request, 'Account successfully created for ' + username)
            return HttpResponseRedirect(reverse('user_login'))
            
        else:
            messages.error(request, form.errors)
            
    return render(request, 'register.html', {'form':form})

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('post'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            messages.error(request, 'Username OR Password not correct!')
            
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('post')

@login_required

def post(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    form = postForms()
    commentForm = postCommentForms()

    if request.method == 'POST' and 'postBTN' in request.POST:
        form = postForms(request.POST, request.FILES)

        if form.is_valid():

            createdPost = form.save(commit=False)
            createdPost.postedBy = request.user
            createdPost.save()

            return redirect('post')

    if request.method == 'POST' and 'commentBTN' in request.POST:
        cForm = postCommentForms(request.POST)

        if cForm.is_valid():
            createdComment = cForm.save(commit=False)

            createdComment.user = request.user
            createdComment.post = Post.objects.get(id=request.POST.get('post'))

            createdComment.save()

            return redirect('post')

    if request.method == 'POST' and 'likeBTN' in request.POST:
        postAW = Post.objects.get(id=request.POST.get('post'))

        form = postForms(request.POST, request.FILES, instance=postAW)
        if form.is_valid():
            updatedPost = form.save(commit=False)
            updatedPost.likes.add(request.user.id)
            updatedPost.save()
            return redirect('post')

    if request.method == 'POST' and 'unlikeBTN' in request.POST:
        postAW = Post.objects.get(id=request.POST.get('post'))

        form = postForms(request.POST, request.FILES, instance=postAW)
        if form.is_valid():
            updatedPost = form.save(commit=False)
            updatedPost.likes.remove(request.user.id)
            updatedPost.save()
            return redirect('post')

    return render(request, 'post.html', {'posts': posts, 'comments': comments, 'form': form, 'commentForm': commentForm})

def about(request):
	form = postForms()
	if request.method == 'POST':
		form = postForms(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('post')
	return render(request, 'about.html', {'form':form})