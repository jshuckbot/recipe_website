from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render

from recipeapp import models as recipeapp_models
from recipeapp.forms import RecipeForm


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.cleaned_data["image"]

            if image is not None:
                FileSystemStorage(location="media/images/").save(image.name, image)
            form.save()
    else:
        form = form = RecipeForm()

    return render(request, "recipeapp/create_recipe.html", {"form": form})


def detail_recipe(request, recipe_id):
    recipe = get_object_or_404(recipeapp_models.Recipe, pk=recipe_id)
    return render(request, "recipeapp/detail_recipe.html", {"recipe": recipe})
