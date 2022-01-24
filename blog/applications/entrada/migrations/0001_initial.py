# Generated by Django 4.0.1 on 2022-01-19 21:28

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('short_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre corto')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('resume', models.TextField(verbose_name='Resumen')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contenido')),
                ('public', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='Entry', verbose_name='Imagen')),
                ('portada', models.BooleanField(default=False)),
                ('in_home', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False, max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrada.category')),
                ('tag', models.ManyToManyField(to='entrada.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
    ]
