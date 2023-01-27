from setuptools import setup

setup(
    name="spongebob-cli",
    version="2.00",

    install_requires=[
        "prettytable",
        "beautifulsoup4",
        "requests",
        "argparse"
        ],

    scripts=[
        "spongebob-cli",
    ]
)