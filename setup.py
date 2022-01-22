from setuptools import setup

setup(
   name='spongebob-cli',
   version='1.0',
   install_requires=["termcolor", "BeautifulSoup4"], 
   scripts=[
            'spongebob-cli',
           ]
)
