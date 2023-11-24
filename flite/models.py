from django.db import models


class Test(models.Model):
    name = models.CharField('Название', max_length=30, default='')
    description = models.CharField('Описание', max_length=(200))
    photo = models.ImageField('Картинка')
    Price = models.IntegerField(3500)
