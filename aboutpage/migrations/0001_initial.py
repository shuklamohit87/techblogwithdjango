# Generated by Django 4.2 on 2023-06-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques1', models.TextField()),
                ('ques2', models.TextField()),
                ('ques3', models.TextField()),
                ('ques4', models.TextField()),
                ('ques5', models.TextField()),
            ],
        ),
    ]
