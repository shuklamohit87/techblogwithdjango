# Generated by Django 4.2 on 2023-08-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_course_course_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_brouchre',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='course-brouchre/'),
        ),
    ]
