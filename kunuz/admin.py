from django.contrib import admin
from .models import *


from django.apps import apps# all other models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}



# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created', 'views']
#     prepopulated_fields = {'slug': ('title',)}

