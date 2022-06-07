from setuptools import setup

setup(
    name="spongebob-cli",
    version="1.1",
    install_requires=[
        "termcolor",
        "BeautifulSoup4",
        "prettytable",
        "youtube-dl",
        "halo",
        "requests",
    ],
    scripts=[
        "spongebob-cli",
        "func.py",
    ],
)
