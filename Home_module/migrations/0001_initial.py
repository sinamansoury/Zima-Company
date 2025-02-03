# Generated by Django 5.1 on 2024-09-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('value', models.CharField(max_length=100, verbose_name='مقدار')),
                ('link', models.CharField(max_length=100, verbose_name='لینک')),
                ('value_title', models.CharField(max_length=100, verbose_name='مفدار نمایشی')),
                ('copyright', models.CharField(max_length=100, verbose_name='حق کپی رایت')),
            ],
            options={
                'verbose_name': 'تنظیمات',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
    ]
