from setuptools import setup

setup(
   name='spongebob-cli',
   version='1.1',
   install_requires=["termcolor", "BeautifulSoup4", "prettytable"], 
   scripts=[
            'spongebob-cli',
           ]
)
