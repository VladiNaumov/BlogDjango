from django.contrib import admin
from .models import Post

""" admin.py – здесь мы регистрируем модели для добавления их в систему администрирования Django 
(использование сайта администрирования Django не является обязательным); """

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
