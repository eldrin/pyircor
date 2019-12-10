#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy==1.17.4',
    'numba==0.46.0',
    'scipy==1.3.3'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Jaehun Kim",
    author_email='jaehun.j.kim@gmail.com',
    python_requires='>=3.5, <3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python implementation of the R package `ircor`",
    # entry_points={
    #     'console_scripts': [
    #         'pyircor=pyircor.cli:main',
    #     ],
    # },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyircor',
    name='pyircor',
    packages=find_packages(include=['pyircor', 'pyircor.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/eldrin/pyircor',
    version='0.2.0',
    zip_safe=False,
)
