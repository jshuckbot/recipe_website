from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name="recipes")
    description = models.TextField()
    steps = models.TextField()
    time = models.DurationField()
    image = models.ImageField(upload_to="images/", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    @property
    def short_steps(self):
        return truncatechars(self.steps, 100)
