from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView

from frontend.views import RecipeListView, RecipeDetailView, RegisterUserView, RecipeCreateView

app_name = 'frontend'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name="frontend:list-recipes"), name="home"),
    path('recipes/', RecipeListView.as_view(), name="list-recipes"),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/add/', RecipeCreateView.as_view(), name='recipe-create'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
