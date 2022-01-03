from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comment)
	