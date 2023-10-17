from django.urls import path

from recipeapp import views

app_name = "recipeapp"

urlpatterns = [
    path("create_recipe/", views.create_recipe, name="create_recipe"),
    path("detail_recipe/<int:recipe_id>", views.detail_recipe, name="detail_recipe"),
    path("user_recipes/<int:user_id>", views.user_recipes, name="user_recipes"),
    path("edit_recipe/<int:recipe_id>", views.edit_recipe, name="edit_recipe"),
    path("", views.random_recipes, name="random_recipes"),
]
