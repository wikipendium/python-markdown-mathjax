#! /usr/bin/env python

from setuptools import setup

setup(
    name='mdx_mathjax',
    version='1.0.0',
    description='Tiny python-markdown extension for easier use of MathJax with Markdown',
    py_modules=['mdx_mathjax'],
    install_requires=['markdown>=2.1.1']
)