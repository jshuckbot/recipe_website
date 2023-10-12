from django.urls import path

from recipeapp import views

app_name = "recipeapp"

urlpatterns = [path("create_recipe/", views.create_recipe, name="create_recipe")]
