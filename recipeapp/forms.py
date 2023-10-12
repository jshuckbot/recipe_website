from django import forms

from recipeapp import models as recipeapp_models


class RecipeForm(forms.ModelForm):
    class Meta:
        model = recipeapp_models.Recipe
        fields = ["title", "category", "description", "steps", "time", "image", "author"]
        labels = {
            "title": "Название",
            "category": "Категория",
            "description": "Описание",
            "steps": "Шаги приготовления",
            "time": "Время приготовления",
            "image": "Изображение",
            "author": "Автор",
        }
