from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	postedBy = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
	post_text = models.CharField(max_length=100, blank=True)
	image = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name="likers", blank=True)

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
	comment = models.CharField(max_length=500, blank=False, null=False)
	date_created = models.DateTimeField(auto_now_add=True)