from setuptools import setup, find_packages

setup(
    name='RPistepper',
    version='0.3a1',
    description='RPistepper is a library control stepper motors using a Raspberry Pi and a transistor array',
    long_description=open('README.rst').read(),
    url='https://github.com/luxedo/RPistepper',
    author='Luiz Eduardo Nishino Gomes do Amaral',
    author_email='luizamaral306@gmail.com',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='RPi ULN2803A stepper motor',
    packages=find_packages(exclude=['RPi']),
    scripts=['bin/rpistepper'],
    install_requires=['RPi.GPIO>=0.5.8'],
)
