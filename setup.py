#!/usr/bin/env python

from setuptools import find_packages, setup
from pygus import __version__


with open("README.md") as readme_file:
    long_description = readme_file.read()


tests_require = [
    "mock>=1.0.1",
    "nose>=1.3.3",
    "vcrpy>=1.10.3",
]


setup(
    name="pygus",
    version=__version__,
    description="Twitter library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Michal Dyzma",
    author_email="pygus@googlegroups.com",
    url="",
    project_urls={
        "Documentation": "https://pygus.readthedocs.io",
        "Issue Tracker": "https://github.com/mdyzma/pygus/issues",
        "Source Code": "https://github.com/mdyzma/pygus",
    },
    download_url="https://pypi.org/project/pygus/",
    packages=find_packages(exclude=["tests", "examples"]),
    install_requires=[
        "requests>=2.11.1,<3",
        "requests_oauthlib>=1.0.0,<2",
    ],
    keywords="gus library",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    zip_safe=True,
)
