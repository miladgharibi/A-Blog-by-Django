from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
def cover_upload_path(instance, filename):
	return f"uploads/{filename}"

class Post(models.Model):
	class StatusChoices(models.TextChoices):
		PUBLISH = _('publish'), 'Publish'
		DRAFT = _('draft'), 'Draft'

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	slug  = models.SlugField(max_length=255)
	cover = models.ImageField(upload_to=cover_upload_path)
	status = models.CharField(max_length=255, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	text = models.TextField()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created']

	def get_absolute_url(self):
		return reverse('dashboard:index')


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text

	class Meta:
		ordering = ['-created']