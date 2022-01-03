from blogs.models import Post
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class HomeView(View):
	def get(self, request):
		context = {
			'posts': Post.objects.filter(status="publish")[:3]
		}
		return render(request, 'core/index.html', context)

