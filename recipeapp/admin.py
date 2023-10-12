from django.contrib import admin

from recipeapp import models as recipeapp_models


@admin.register(recipeapp_models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "short_description", "short_steps", "time", "image", "author", "created"]
    list_filter = ["title", "created"]


@admin.register(recipeapp_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
