import os
from setuptools import find_packages, setup

from django_log_to_telegram import name

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name=name,
    version='2020.01.23',
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3 (GPLv3)',  # example license
    description='a simple logger that sends 500 exceptions to a Telegram bot of your choice.',
    long_description=README,
    url='',
    author='Luigi Mazari Villanova',
    author_email='luigi.mazari@cnr.it',
    install_requires=[
        "Django>1.9",
        "requests",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Scientific/Engineering',
    ],
)
