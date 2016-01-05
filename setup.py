import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-psql-estimate',
    version='0.1',
    packages=['psql_estimate'],
    include_package_data=True,
    license='MIT License',  # example license
    description='Estimate expensive COUNTs on postgres',
    long_description=README,
    url='http://github.com/czartur/django-psql-estimate',
    author='Artur Czepiel',
    author_email='czepiel.artur@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
