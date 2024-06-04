from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Recipes

@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'author','description','ingredients','image']
