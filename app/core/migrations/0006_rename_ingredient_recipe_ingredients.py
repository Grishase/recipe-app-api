# Generated by Django 4.0.10 on 2023-05-18 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ingredient_recipe_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]
