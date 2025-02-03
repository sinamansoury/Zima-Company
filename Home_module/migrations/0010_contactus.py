# Generated by Django 5.1 on 2024-09-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_module', '0009_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('fullname', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('is_read_by_admin', models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')),
                ('message', models.TextField(verbose_name='متن تماس با ما')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')),
                ('response', models.TextField(blank=True, null=True, verbose_name='پاسخ ادمین')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
