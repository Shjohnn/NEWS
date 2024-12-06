from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ContentInline(admin.StackedInline):
    model = Content
    extra = 1


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'reading_time', 'category', 'published', 'views', 'comments', 'created_at',)
    list_filter = ('category', 'published')
    search_fields = ('name', 'tag')
    date_hierarchy = 'created_at'
    inlines = [ContentInline, CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'email', 'created_at', 'article')
    list_filter = ('article', 'author')
    search_fields = ('article', 'author', 'email')
    date_hierarchy = 'created_at'



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone_number','created_at')
    list_filter = ('name','email','phone_number', 'subject' ,'message','created_at',)
    list_filter=('name', 'phone_number','email',)
    search_fields = ('name', 'phone_number','email','message',)


@admin.register(Newsletter)
class NewslatterAdmin(admin.ModelAdmin):
    list_display = ('email',)



