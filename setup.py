import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mezzanine-slideshows',
    version='0.2.1',
    packages=['mezzanine_slideshows'],
    include_package_data=True,
    license='BSD License',
    description='A simple mezzanine app which allows the placement of a mezzanine Gallery within any other mezzanine Page as a slideshow ',
    long_description=README,
    url='https://github.com/philipsouthwell/mezzanine-slideshows',
    author='Philip Southwell',
    author_email='phil@zoothink.com',
    keywords=['django', 'mezzanine'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Mezzanine',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

