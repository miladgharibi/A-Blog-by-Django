from re import search
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, ListView
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.core.paginator import Paginator


class PostListView(View):
	def get(self, request):
		if not request.GET.get('search'):
			queryset = Post.objects.filter(status='publish')
			paginator = Paginator(queryset, 6)
			page_number = request.GET.get('page')
			page_obj = paginator.get_page(page_number)

			context = {
				'page_obj': page_obj
			}
		else:
			search_query = request.GET.get('search')
			queryset = Post.objects.filter(status='publish').filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
			paginator = Paginator(queryset, 6)
			page_number = request.GET.get('page')
			page_obj = paginator.get_page(page_number)

			context = {
				'page_obj': page_obj
			}
		return render(request, 'blogs/index.html', context)


class PostDetailView(View):
	def get(self, request, slug):
		post = get_object_or_404(Post, slug=slug)
		comments = Comment.objects.filter(post=post)

		context = {
			'object': post,
			'comment_list': comments
		}
		return render(request, 'blogs/detail.html', context)


	def post(self, request, slug):
		comment_author = get_object_or_404(User, username=request.user.username)
		comment_text = request.POST.get('comment-text')
		post_pk = request.POST.get('post_pk')
		comment_post = get_object_or_404(Post, slug=slug)
		
		Comment.objects.create(author=comment_author, post=comment_post,text=comment_text)

		return redirect('blogs:list')