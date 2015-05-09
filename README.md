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

##Super Quick start##

1. Create a new Mezzanine project following the [official instructions](http://mezzanine.jupo.org/docs/overview.html#installation).
Choose to install the set of demonstration pages during the setup process.

1. Add mezzanine_slideshows to your INSTALLED_APPS immediately after your Django apps and before 
   your Mezzanine apps like this :
       INSTALLED_APPS = (  
           ...  
           "mezzanine_slideshows",  
           ...  
        )

2. Run `python manage.py syncdb` to create the mezzanine-slideshows models.

3. Start the development server and visit http://127.0.0.1:8000/admin/ to create a slideshow instance.

4. Navigate to the page on the site to see your gallery displayed after the page text as a slideshow.


##Regular Installation##
