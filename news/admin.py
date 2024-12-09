from django.contrib import admin
from .models import *



@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_display_links = ('name', 'created_at',)
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}
    list_editable = ['is_active',]



    
@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_active')
    list_display_links = ('name', 'created_at',)



@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'created_at', 'views', 'is_active')
    list_display_links = ('category', 'title', 'created_at')
    search_fields = ('category', 'title',)
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('views', )
    filter_horizontal = ('tag',)