from __future__ import unicode_literals

from django.contrib import admin

from mezzanine_slideshows.models import Slideshow


class SlideshowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slideshow, SlideshowAdmin)

