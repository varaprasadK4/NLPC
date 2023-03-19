# Generated by Django 4.1.7 on 2023-03-15 14:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='none', max_length=100)),
                ('Email', models.EmailField(default='none', max_length=100)),
                ('Number', phonenumber_field.modelfields.PhoneNumberField(blank='False', max_length=128, region=None)),
                ('password', models.CharField(default='none', max_length=100)),
                ('c_password', models.CharField(default='none', max_length=100)),
            ],
        ),
    ]
