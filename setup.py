# coding: utf-8

from distutils.core import setup


__version__ = '0.0.2'

short_description = 'Raft replication in Python'

setup(
    name='raftos',
    packages=['raftos'],
    version=__version__,
    description=short_description,
    long_description=short_description,
    author='Alexander Zhebrak',
    author_email='fata2ex@gmail.com',
    license='MIT',
    url='https://github.com/zhebrak/raftos',
    keywords=['python', 'raft', 'replication'],
    include_package_data=True,
    classifiers=[],
)
