#! /usr/bin/env python

import setuptools

from business_rules import __version__ as version

with open('HISTORY.rst') as f:
    history = f.read()

description = 'Python DSL for setting up business intelligence rules that can be configured without code'

setuptools.setup(
    name='business-rules',
    version=version,
    description='{0}\n\n{1}'.format(description, history),
    author='Venmo',
    author_email='open-source@venmo.com',
    url='https://github.com/alternativshik/business-rules',
    packages=['business_rules'],
    license='MIT',
)
