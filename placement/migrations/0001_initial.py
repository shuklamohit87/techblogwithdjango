# Generated by Django 4.2 on 2023-06-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='placeStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentimg', models.FileField(default=None, max_length=250, upload_to='placestudents/')),
                ('studentname', models.CharField(max_length=50)),
                ('studentprofile', models.CharField(max_length=50)),
                ('studentpacakage', models.CharField(max_length=50)),
                ('studentcompany', models.CharField(max_length=50)),
            ],
        ),
    ]
