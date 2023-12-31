# Generated by Django 4.2 on 2023-06-23 08:54

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postcategories', '0004_alter_postcategories_category_title'),
        ('certificaterequest', '0003_choosecenter_alter_certificaterequest_center'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Contact Number', max_length=31)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificaterequest.choosecenter')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postcategories.postcategories')),
            ],
        ),
    ]
