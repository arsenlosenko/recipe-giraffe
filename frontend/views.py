from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from api.models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "frontend/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "frontend/recipe_detail.html"


class RegisterUserView(CreateView):
    template_name = 'frontend/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('frontend:list-recipes')
