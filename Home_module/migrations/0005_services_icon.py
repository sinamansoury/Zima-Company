# Generated by Django 5.1 on 2024-09-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_module', '0004_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ایکون'),
        ),
    ]
