from django.contrib import admin

from main.models import Country, Recipe, Review, Ingredient, Tag, Category

admin.site.register(Country)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Category)
