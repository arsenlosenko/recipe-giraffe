from django.views.generic import ListView, DetailView

from api.models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "frontend/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "frontend/recipe_detail.html"
