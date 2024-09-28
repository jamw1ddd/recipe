from django.urls import path
from .views import home_view, about_view, recipe_detail, receipes_view, breakfast_view, lunch_view, \
                   dinner_view, drinks_view, desserts_view, search_view, vegetarian_view, national_view, \
                   salads_view, soups_view, create_comment, RecipeView


urlpatterns = [
    path('filter/', RecipeView.as_view(), name='filter'),
    path('', home_view, name='home'),
    path('receipes/', receipes_view, name='receipes'),
    path('about/', about_view, name='about'),
    path('search/', search_view, name='search'),
    path('recipe/<int:pk>/', recipe_detail, name='receipe'),
    path('comment/<int:pk>/', create_comment, name='create_comment'),
    path('breakfast/', breakfast_view, name='breakfast'),
    path('lunch/', lunch_view, name='lunch'),
    path('dinner/', dinner_view, name='dinner'),
    path('drinks/', drinks_view, name='drinks'),
    path('desserts/', desserts_view, name='desserts'),
    path('vegetarian/', vegetarian_view, name='vegetarian'),
    path('national/', national_view, name='national'),
    path('soups/', soups_view, name='soups'),
    path('salads/', salads_view, name='salads'),
]
