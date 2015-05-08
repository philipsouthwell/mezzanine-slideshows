====================
mezzanine-slideshows
====================

mezzanine-slideshows is an app which allows the user to select galleries to appear at the bottom
of other pages as slideshows.

Documentation coming to readthedocs.com

Quick start
-----------

1. Add "mezzanine-slideshows" to your INSTALLED_APPS after your Django apps and before your Mezzanine apps
   like this:

    INSTALLED_APPS = (
        ...
        "django.contrib.staticfiles",
        "mezzanine_slideshows",
        "mezzanine.boot",
        ...
    )

3. Run `python manage.py migrate` to create the mezzanine-slideshows models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a slideshow.