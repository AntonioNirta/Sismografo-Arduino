# Copyright 2020 Francesco Apruzzese <cescoap@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from setuptools import setup


setup(
    name='sismografo',
    version='0.1.0',
    description='Sismografo',
    url='https://github.com/AntonioNirta/Sismografo-Arduino',
    author='Antonio Nirta',
    author_email='info@intrageo.it',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python :: 3.6',
        ],
    keywords='sismografo csv',
    license='LGPL',
    packages=['sismografo'],
    install_requires=[
        'pandas',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': ['sismografo=sismografo.sismografo:main'],
        },
    zip_safe=False,
    )
