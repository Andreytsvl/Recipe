# Generated by Django 5.1.1 on 2024-11-03 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название рецепта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('preparation_steps', models.TextField(verbose_name='Шаги приготовления')),
                ('cooking_time', models.IntegerField(verbose_name='Время приготовления (минуты)')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec.category', verbose_name='Категория')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rec.recipe', verbose_name='Рецепт')),
            ],
            options={
                'unique_together': {('recipe', 'author', 'category')},
            },
        ),
    ]