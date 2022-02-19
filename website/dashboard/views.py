from blogs.models import Post
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

def data_validation(*args):
	items = [True if item != '' else False for item in args]
	return all(items)

class IndexView(LoginRequiredMixin, View):
	def get(self, request):
		object_list = Post.objects.filter(author=request.user.pk)
		paginator = Paginator(object_list, 6)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context = {'page_obj': page_obj}
		return render(request, 'dashboard/index.html', context)

class AddPostView(LoginRequiredMixin, View):
	def get(self, request):
		context = {}
		return render(request, 'dashboard/create_post.html',context)

	def post(self, request):
		title = request.POST.get('title')
		slug = request.POST.get('slug')
		text = request.POST.get('text')
		status = request.POST.get('status')
		author = request.user

		if data_validation(title, slug, text, status):
			post = Post(
				title=title,
				slug=slug,
				text=text,
				author=request.user
			)
			post.save()
			return redirect('dashboard:index')

		return redirect('dashboard:add_post')


class DeletePostView(LoginRequiredMixin, View):
	def get(self, request, slug):
		post = get_object_or_404(Post, slug=slug)
		post.delete()

		return redirect('dashboard:index')

class UpdatePostView(LoginRequiredMixin, View):
	def get(self, request, slug):
		post = get_object_or_404(Post, slug=slug)
		if request.user == post.author:
			context = {
				'form':post
			}
			return render(request, 'dashboard/update_post.html', context)
		return redirect('core:home')


	def post(self, request, slug):
		post = get_object_or_404(Post, slug=slug)
		if request.user == post.author:
			post.title = request.POST.get('title')
			post.slug = request.POST.get('slug')
			post.text = request.POST.get('text')
			post.status = request.POST.get('status')
			post.save()

			return redirect("dashboard:index")
		return redirect("dashboard:index")