from setuptools import setup

setup(
   name='combes',
   version='0.0.2',
   description='',
   author='Robin Guignard-Perret',
   author_email='',
   packages=setuptools.find_packages(),
   scripts=['bin/combes'],
   install_requires=['click'],
)
