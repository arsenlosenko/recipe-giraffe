from django.urls import path

from frontend.views import RecipeListView, RecipeDetailView

app_name = 'frontend'
urlpatterns = [
    path('r/', RecipeListView.as_view(), name="list-recipes"),
    path('r/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail')
]
