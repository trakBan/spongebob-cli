from setuptools import setup
from pathlib import Path

requirements = Path("requirements.txt").read_text().splitlines()

setup(
    name="spongebob-cli",
    version="1.1",
    install_requires=requirements,
    scripts=[
        "spongebob-cli",
        "func.py",
    ]
)
