from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Идентификатор")
    name = models.CharField(max_length=50, verbose_name="Наименование")
    price = models.IntegerField(verbose_name="Цена")
    image = models.URLField(verbose_name="Изображение")
    release_date = models.DateTimeField(verbose_name="Дата публикации")
    lte_exists = models.BooleanField(verbose_name="LTE")
    slug = models.SlugField(verbose_name="Ссылка")

    class Meta:
        verbose_name_plural = 'Телефоны'
        ordering = ('-release_date',)
        verbose_name = 'телефон'

    def __str__(self):
        return self.name
