from django import forms

from api.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'user']
        widgets = {'user': forms.HiddenInput()}
