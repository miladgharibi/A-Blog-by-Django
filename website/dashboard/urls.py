from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('add-post/', views.AddPostView.as_view(), name='add_post'),
	path('delete-post/<str:slug>/', views.DeletePostView.as_view(), name='delete_post'),
	path('edit-post/<str:slug>/', views.UpdatePostView.as_view(), name='update_post'),
]