# Generated by Django 4.2 on 2023-06-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactpage', '0003_rename_googlemap_contactdata_googlemap1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]