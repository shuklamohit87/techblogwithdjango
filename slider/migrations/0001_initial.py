# Generated by Django 4.2 on 2023-05-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.FileField(default=None, upload_to='slider/')),
                ('slider_tag', models.CharField(max_length=100)),
                ('slider_title', models.TextField(max_length=150)),
                ('slider_button', models.CharField(max_length=50)),
            ],
        ),
    ]