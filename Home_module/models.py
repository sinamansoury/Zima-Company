from django.db import models

# Create your models here.


class Settings(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='عنوان')
    value = models.CharField(max_length=100, null=True, verbose_name='مقدار')
    value_title = models.CharField(max_length=100, null=True, verbose_name='مفدار نمایشی')
    copyright = models.CharField(max_length=100, null=True, verbose_name='حق کپی رایت')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='عنوان')
    value = models.CharField(max_length=100, null=True, verbose_name='مقدار')
    icon = models.CharField(max_length=100, verbose_name='ایکون',null=True, blank=True)

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.title


class Customers(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='عنوان')
    value = models.CharField(max_length=100, null=True, verbose_name='مقدار')
    icon = models.CharField(max_length=100, verbose_name='ایکون', null=True, blank=True)

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    category = models.CharField(max_length=100, null=True, verbose_name='کتگوری')
    image = models.ImageField(upload_to='images/projects', null=True, verbose_name='عکس')
    value = models.CharField(max_length=100, verbose_name='مقدار', null=True, blank=True)

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'

    def __str__(self):
        return self.category


class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    job = models.CharField(max_length=100, verbose_name='پست')
    image = models.ImageField(upload_to='images/staff', verbose_name='عکس')
    description = models.CharField(max_length=100, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'

    def __str__(self):
        return self.name


