from setuptools import setup, find_packages
from os.path import join, dirname

__here__ = dirname(__file__)
with open(join(__here__,'README.md')) as f:
    long_description = f.read()

setup(
    name='GeoDeepDive-tools',
    version='0.1a0',
    description='Tools for working with GeoDeepDive sentence data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/davenquinn/GeoDeepDive-tools',
    author='Daven Quinn',
    author_email='daven.quinn@wisc.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='nlp geology stratigraphy science data-mining',
    packages=find_packages(),
    install_requires=[],
)
