from blogs.models import Post
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .forms import CreatePostForm

class IndexView(View):
	def get(self, request):
		object_list = Post.objects.filter(author=request.user.pk)
		paginator = Paginator(object_list, 6)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context = {'page_obj': page_obj}
		return render(request, 'dashboard/index.html', context)

class AddPostView(View):
	def get(self, request):
		form = CreatePostForm()
		context = {'form': form}
		return render(request, 'dashboard/create_post.html', context)

	def post(self, request):
		form = CreatePostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect("dashboard:index")

		else:
			return redirect("dashboard:add_post")



class DeletePostView(View):
	def get(self, request, slug):
		post = get_object_or_404(Post, slug=slug)
		post.delete()

		return redirect('dashboard:index')

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'dashboard/update_post.html'
	fields = ['title', 'slug', 'text', 'status']