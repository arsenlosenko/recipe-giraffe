from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from api.models import Recipe
from frontend.forms import RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = "frontend/recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "frontend/recipe_detail.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    success_url = reverse_lazy('frontend:list-recipes')
    template_name = "frontend/recipe_create.html"

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        return initial


class RegisterUserView(CreateView):
    template_name = 'frontend/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('frontend:list-recipes')
