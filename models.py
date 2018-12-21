from django.db import models

class Categories_woman(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название")
    text = models.TextField(verbose_name=u"Описание", default="")

    def __str__(self):
        return self.name


class Subcategories_woman(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название")
    price = models.IntegerField(verbose_name=u"Цена (сом)")
    number_of_copies = models.IntegerField(verbose_name=u"Количество экземпляров")
    composition = models.CharField(max_length=200, verbose_name=u"Состав",  default="")
    text = models.TextField(verbose_name=u"Описание", default="")
    mark = models.CharField(max_length=100, verbose_name=u"Качество", default=" ")
    color = models.CharField(max_length=100, verbose_name=u"Расцветки", default="")
    image = models.ImageField(null = True, blank = True, upload_to='images', verbose_name=u"Картинка")
    name_сategories = models.ForeignKey(Categories_woman, on_delete=models.CASCADE)

    def __str__(self):
        return self.name