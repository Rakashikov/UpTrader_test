from django.db import models
from django.utils.text import slugify

from config import settings


class Menu(models.Model):
    title = models.CharField(max_length=50, verbose_name="Menu Title")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Menu Slug")

    class Meta:
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Menu, self).save(*args, **kwargs)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name="Menu")
    title = models.CharField(max_length=50, verbose_name="Menu Item Title")
    slug = models.SlugField(max_length=50, unique=True, blank=True, verbose_name="Menu Item Slug")
    url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Menu Item URL")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='children', verbose_name="Parent Menu Item",)

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.url is None:
            self.url = settings.DEFAULT_DOMAIN + self.slug
            print(self.url)
        super(MenuItem, self).save(*args, **kwargs)
