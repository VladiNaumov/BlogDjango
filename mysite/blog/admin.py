from django.contrib import admin
from .models import Post, Comment, Author, New

""" admin.py – здесь мы регистрируем модели для добавления их в систему администрирования Django 
(использование сайта администрирования Django не является обязательным); """

# admin.site.register(Author)
admin.site.register(New)

"""
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    
"""

@admin.register(Author)
class NewAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','date_of_birth', 'date_of_death')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


