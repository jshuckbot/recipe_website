from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render

from recipeapp import models as recipeapp_models
from recipeapp.forms import RecipeForm


@login_required
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

    return render(request, "recipeapp/create_recipe.html", {"form": form, "section": "create_recipe"})


@login_required
def detail_recipe(request, recipe_id):
    recipe = get_object_or_404(recipeapp_models.Recipe, pk=recipe_id)
    return render(request, "recipeapp/detail_recipe.html", {"recipe": recipe})


@login_required
def random_recipes(request):
    recipes = recipeapp_models.Recipe.objects.all()
    user_recipes = recipes.filter(author__username=request.user.username)[:5]
    rand_recipes = recipes.order_by("?")[:5]
    # print(request.user.id)
    return render(
        request,
        "recipeapp/random_recipes.html",
        {"user_recipes": user_recipes, "section": "dashboard", "rand_recipes": rand_recipes},
    )


@login_required
def user_recipes(request, user_id):
    recipes = recipeapp_models.Recipe.objects.filter(author=user_id)
    return render(request, "recipeapp/user_recipes.html", {"recipes": recipes})
