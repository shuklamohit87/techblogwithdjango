# Generated by Django 4.2 on 2023-06-13 12:35

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postcategories', '0004_alter_postcategories_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='post_tittle', unique=True)),
                ('post_tittle', models.CharField(max_length=300)),
                ('post_image', models.FileField(default=None, max_length=250, upload_to='postimages/')),
                ('posted_on', models.DateField()),
                ('posted_by', models.CharField(max_length=100)),
                ('post_content', tinymce.models.HTMLField()),
                ('post_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='postcategories.postcategories')),
            ],
        ),
    ]
