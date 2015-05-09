#mezzanine-slideshows#

mezzanine-slideshows is for use with the [Mezzanine CMS](http://mezzanine.jupo.org/). It allows the placement of 
Mezzanine Galleries within other Mezzanine Pages as slideshows.


##Requirements##

mezzanine-slideshows requires that the following python apps be installed:

* Mezzanine 3.1 (and its dependencies)
* South - for database migrations (optional)

##Installation##

The easiest method is to install directly from pypi using [pip](http://www.pip-installer.org/) by 
running the command below:

    $ pip install mezzanine_slideshows

##Super Quick Start##

These instructions will allow you to place Mezzanine Galleries *at the end* of other Mezzanine Pages as slideshows.
If you wish to place the galleries at any other place please follow the Regular Setup instructions.

1. Create a new Mezzanine project following the [official instructions](http://mezzanine.jupo.org/docs/overview.html#installation).
Choose to install the set of demonstration pages during the setup process.

1. Add mezzanine_slideshows to INSTALLED_APPS in settings.py immediately after your Django apps and before 
   your Mezzanine apps:

    ```python
    INSTALLED_APPS = (
        ...
        "mezzanine_slideshows",
        ...
        )
    ```

1. Add the following to TEMPLATE_CONTEXT_PROCESSORS in settings.py:

    ```python
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        "mezzanine_slideshows.context_processors.get_slideshows"
        )
    ``` 

1. Run `python manage.py migrate mezzanine_slideshows` to create the mezzanine-slideshows models.

1. Start the development server and visit http://127.0.0.1:8000/admin/ to create a slideshow instance.

1. Navigate to the page on the site to see your gallery displayed after the page text as a slideshow.


##Regular Setup##

1. Add mezzanine_slideshows as an app in your project like this:

    ```python
    INSTALLED_APPS = (
        ...
        "mezzanine_slideshows"
        )
    ```

1. Add the following template context processor in settings.py:

    ```python
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        "mezzanine_slideshows.context_processors.get_slideshows"
        )
    ``` 

1. Run `python manage.py migrate mezzanine_slideshows` to create the mezzanine-slideshows models.

1. In the header of your *base.html* file after ``<link rel="stylesheet" href="{% static "css/bootstrap-theme.css" %}">``
add the following two lines:
    ```html
    <link rel="stylesheet" href="{% static "mezzanine-slideshows/css/mezzanine-slideshow.css" %}">
    <link rel="stylesheet" href="{% static "mezzanine/css/magnific-popup.css" %}">
    ```

1. At the end of your *base.html* file, just after `{% include "includes/footer_scripts.html" %}`, add the following
two lines:
    ```html
    <script src="{% static "mezzanine-slideshows/js/mezzanine-slideshow.js" %}"></script>
    <script src="{% static "mezzanine-slideshows/js/jquery.magnific-popup.js" %}"></script>
    ```

1. This step is key. Without it no slideshows will appear. Add the following code to any place you wish a template to 
check whether a slideshow should be displayed, and then display it:
    ```django
    {% include "includes/mezzanine_slideshows.html" %}
    ```