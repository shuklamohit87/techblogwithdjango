# Generated by Django 4.2 on 2023-05-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.FileField(default=None, max_length=250, upload_to='course/'),
        ),
    ]
