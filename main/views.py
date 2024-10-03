from django.shortcuts import render, redirect
from main.filters import RecipeFilter
from django_filters.views import FilterView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import send_email
from main.models import Recipe, Review


def home_view(request):
    receipes = Recipe.objects.all()[:9]
    return render(request, 'index.html', {'receipes': receipes})


def about_view(request):
    return render(request, 'about.html')


def receipes_view(request):
    receipes = Recipe.objects.all()
    return render(request, 'receipes.html', {'receipes': receipes})


def recipe_detail(request, pk):
    detail = Recipe.objects.get(id=pk)
    reviews = Review.objects.all()
    return render(request, 'receipe-post.html', {'detail': detail, 'reviews': reviews})


def create_comment(request, pk):
    recipe = Recipe.objects.filter(id=pk).first()
    name = request.POST.get('name')
    subject = request.POST.get('subject')
    email = request.POST.get('email')
    create = Review.objects.create(
        recipe=recipe, name=name, subject=subject, email=email)
    create.save()
    return redirect('receipe', pk)


def search_view(request):
    query = request.GET.get('q')
    if query:
        results = Recipe.objects.filter(name__icontains=query)
    else:
        results = Recipe.objects.none()
    return render(request, 'receipes.html', {'results': results})


class RecipeView(FilterView):
    model = Recipe
    template_name = 'receipes.html'
    context_object_name = 'recipes'
    filterset_class = RecipeFilter
    paginate_by = 6

    def get_filterset(self, filterset_class):
        # Access request.GET correctly without parentheses
        return filterset_class(self.request.GET, queryset=self.get_queryset())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_filterset(self.filterset_class).form
        return context


def breakfast_view(request):
    breakfast = Recipe.objects.all()
    return render(request, 'category/breakfast.html', {'breakfast': breakfast})


def lunch_view(request):
    lunch = Recipe.objects.all()
    return render(request, 'category/lunch.html', {'lunch': lunch})


def dinner_view(request):
    dinner = Recipe.objects.all()
    return render(request, 'category/dinner.html', {'dinner': dinner})


def drinks_view(request):
    drinks = Recipe.objects.all()
    return render(request, 'category/drinks.html', {'drinks': drinks})


def national_view(request):
    national = Recipe.objects.all()
    return render(request, 'category/national.html', {'national': national})


def soups_view(request):
    soups = Recipe.objects.all()
    return render(request, 'category/soups.html', {'soups': soups})


def salads_view(request):
    salads = Recipe.objects.all()
    return render(request, 'category/salads.html', {'salads': salads})


def vegetarian_view(request):
    vegetarian = Recipe.objects.all()
    return render(request, 'category/vegetarian.html', {'vegetarian': vegetarian})


def desserts_view(request):
    desserts = Recipe.objects.all()
    return render(request, 'category/desserts.html', {'desserts': desserts})


@api_view(['GET'])
def send_email_view(request):
    send_email.delay()

    return Response({'status': 'ok'})