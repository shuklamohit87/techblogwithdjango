# Generated by Django 4.2 on 2023-05-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_image', models.ImageField(upload_to='')),
                ('course_title', models.CharField(max_length=50)),
            ],
        ),
    ]
