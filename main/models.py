from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Countries'


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
    description = models.TextField(blank=True,null=True)
    prep = models.CharField(max_length=50)
    cook = models.CharField(max_length=50)
    yields = models.CharField(max_length=100, blank=True, null=True)  
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    rating = models.IntegerField(default=0)
    make=RichTextField(blank=True,null=True)
    calories=models.CharField(max_length=255,blank=True,null=True)
    fat=models.CharField(max_length=255,blank=True,null=True)
    carbs=models.CharField(max_length=255,blank=True,null=True)
    protein=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ('-id', )


class Review(models.Model):
    name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(default=1) 
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.ingredients
    