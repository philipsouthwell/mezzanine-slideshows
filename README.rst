mezzanine-slideshows
====================

mezzanine-slideshows is for use with the `Mezzanine
CMS <http://mezzanine.jupo.org/>`__. It allows the placement of
Mezzanine Galleries within other Mezzanine Pages as slideshows.

Requirements
------------

mezzanine-slideshows requires that the following python apps be
installed:

-  Python 3.4
-  Mezzanine 3.1 (and its dependencies)
-  Django 1.7 +  (this app uses the django migrations framework)

Installation
------------

The easiest method is to install directly from pypi using
`pip <http://www.pip-installer.org/>`__ by running the command below:

::

    $ pip install mezzanine-slideshows

Super Quick Start
-----------------

These instructions are for instant setup with the Mezzanine demonstration installation and
allow you to place Mezzanine Galleries *at the end* of other Mezzanine Pages as slideshows.
If you are using anything other than the standard templates provided with a fresh Mezzanine
install or wish to place the galleries at any place other than the end of pages please
follow the Regular Setup instructions below.

1. Create a new Mezzanine project following the `official
   instructions <http://mezzanine.jupo.org/docs/overview.html#installation>`__.

2. Add mezzanine\_slideshows to INSTALLED\_APPS in settings.py
   immediately after your Django apps and before your Mezzanine apps:

   .. code:: python

       INSTALLED_APPS = (
           ...
           "mezzanine_slideshows",
           ...
           )

3. Add the following to TEMPLATE\_CONTEXT\_PROCESSORS in settings.py:

   .. code:: python

       TEMPLATE_CONTEXT_PROCESSORS = (
           ...
           "mezzanine_slideshows.context_processors.get_slideshows"
           )

4. Run ``python manage.py migrate mezzanine_slideshows`` to create the
   mezzanine-slideshows models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a slideshow instance.

6. Navigate to the page on the site to see your gallery displayed after
   the page text as a slideshow.


Regular Setup
-------------

1. Add mezzanine\_slideshows as an app in your project like this:

   .. code:: python

       INSTALLED_APPS = (
           ...
           "mezzanine_slideshows"
           )

2. Add the following template context processor in settings.py:

   .. code:: python

       TEMPLATE_CONTEXT_PROCESSORS = (
           ...
           "mezzanine_slideshows.context_processors.get_slideshows"
           )

3. Run ``python manage.py migrate mezzanine_slideshows`` to create the
   mezzanine-slideshows models.

4. In the header of your base.html file after the other css files add the lines

   .. code:: html

       <link rel="stylesheet" href="{% static "mezzanine/css/magnific-popup.css" %}">
       <link rel="stylesheet" href="{% static "mezzanine-slideshows/css/owl.carousel.css" %}">
       <link rel="stylesheet" href="{% static "mezzanine-slideshows/css/owl.theme.css" %}">


5. At the end of your *base.html* file, just after

   .. code:: html

        {% include "includes/footer_scripts.html" %}

   add the following three lines:

   .. code:: html

        <script src="{% static "mezzanine-slideshows/js/owl.carousel.js" %}"></script>
        <script src="{% static "mezzanine-slideshows/js/jquery.magnific-popup.js" %}"></script>


6. This step is key. Without it no slideshows will appear. Add the following code to any place
   you wish a template to check whether a slideshow should be displayed. If a slideshow is dues
   to show on that page it will be displayed at that place in the template:

   .. code:: html

        {% include "includes/mezzanine_slideshows.html" %}


