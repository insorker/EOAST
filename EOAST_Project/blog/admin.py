from django.contrib import admin
from .models import Post, Category, Tag, Picture, Notice


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'author', 'excerpt', 'body', 'category', 'tags', 'picture']


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'body']
    fields = ['title', 'body', 'picture']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Picture)
admin.site.register(Post, PostAdmin)
admin.site.register(Notice, NoticeAdmin)
