from django.db import models

from mezzanine.pages.models import RichTextPage
from mezzanine.galleries.models import Gallery


class Slideshow(models.Model):
    title = models.CharField(max_length=30,
                             help_text="The title of your slideshow")
    page = models.OneToOneField(RichTextPage)
    galleries = models.ManyToManyField(Gallery)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Slideshow"
        verbose_name_plural = "Slideshows"
