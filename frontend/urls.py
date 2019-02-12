from django.urls import path
from django.views.generic.base import RedirectView

from frontend.views import RecipeListView, RecipeDetailView

app_name = 'frontend'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name="frontend:list-recipes"), name="home"),
    path('recipes/', RecipeListView.as_view(), name="list-recipes"),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail')
]
