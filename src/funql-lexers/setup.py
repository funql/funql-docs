#!/usr/bin/env python
"""Setup funql-lexers."""
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
funql=funql_lexers:FunQLLexer
'''

setup(
    name='funql-lexers',
    version='1.0.0',
    description='Pygments lexer package for FunQL.',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.17.2'
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Private :: Do Not Upload',
    ]
)
