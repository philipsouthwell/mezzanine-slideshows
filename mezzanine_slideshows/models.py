from django.db import models

from mezzanine.pages.models import RichTextPage
from mezzanine.galleries.models import Gallery


class Slideshow(models.Model):
    page = models.OneToOneField(RichTextPage)
    galleries = models.ManyToManyField(Gallery)

    class Meta:
        verbose_name = "Slideshow"
        verbose_name_plural = "Slideshows"
        app_label = "Slideshows"

    def __str__(self):
        return self.title
