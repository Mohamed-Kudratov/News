from django.contrib import admin

from news.models import ContactModel, CategoryModel, NewsModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'created_at']
    search_fields = ['title']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description', 'content', 'category', 'created_at']
