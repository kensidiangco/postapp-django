from django.db import models

# Create your models here.

class Post(models.Model):
	nickname = models.CharField(max_length=20, blank=False)
	post_text = models.CharField(max_length=100, blank=True)
	image = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)