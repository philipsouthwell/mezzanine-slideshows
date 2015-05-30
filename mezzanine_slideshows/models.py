from django.db import models

from mezzanine.pages.models import RichTextPage
from mezzanine.galleries.models import Gallery


class Slideshow(models.Model):
    page = models.OneToOneField(RichTextPage)
    gallery = models.ForeignKey(Gallery)
    slideshow_title = models.CharField(max_length=30, blank=True,
                                       help_text="A brief description of the slideshow")
    slideshow_description = models.TextField(max_length=100, blank=True,
                                             help_text="A fuller description of the slideshow")

    class Meta:
        verbose_name = "Slideshow"
        verbose_name_plural = "Slideshows"

    def __str__(self):
        return self.page.title
