# Generated by Django 5.0.7 on 2024-07-29 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.country'),
        ),
    ]
