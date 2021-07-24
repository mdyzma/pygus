# PyGUS

Python wrapper for GUS REST API.

## Installation

The easiest way to install the latest version from PyPI is by using pip:

    pip install pygus

You can also clone the repository from GitHub and install the latest development version:

    git clone https://github.com/mdyzma/pygus.git
    cd pygus
    pip install .

Alternatively, install directly from the GitHub repository:

    pip install git+https://github.com/mdyzma/pygus.git

Python >=3.8 are supported.

## Development

Setting up development environment

### Virtualenv Mac/Linux

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install - r requirements.txt

### Poetry Mac/Linux

    poetry install
    poetry shell

## Testing

To run tests manually runthis command  in project root folder:

    pytest

### Documentation

To build documentation

1. clone this repository
2. cd `pygus/docs` folder
3. run:

    make html

## Links

- [PyGUS Documentation](https://pytest.readthedocs.io/en/latest/)
- [GUS API Documentation (PL)](https://api.stat.gov.pl)
