from setuptools import setup

setup(name = 'asciiiArt',
    version = '0.2 dev', # added user defined lines
    description = 'Ascii "art" from images',
    author = 'Brendon',
    packasges = ['asciiart'],
    install_requires = ['pillow', 'requests'])
