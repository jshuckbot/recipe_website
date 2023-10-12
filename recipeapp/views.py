from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

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
