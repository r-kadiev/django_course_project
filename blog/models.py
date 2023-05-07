from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    slug = models.SlugField(verbose_name="URL", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
