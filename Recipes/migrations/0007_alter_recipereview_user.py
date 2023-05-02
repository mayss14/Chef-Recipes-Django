# Generated by Django 4.1.7 on 2023-05-01 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recipes', '0006_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipereview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
