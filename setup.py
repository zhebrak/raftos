# coding: utf-8

from setuptools import setup


__version__ = '0.2.3'

short_description = 'Raft replication in Python'
requirements = [req.strip() for req in open('requirements.txt').readlines()]
crypto_reqs = [req.strip() for req in open('requirements-cryptography.txt').readlines()]

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
    install_requires=requirements,
    extras_require={
        'cryptography': crypto_reqs,
    },
    include_package_data=True,
    classifiers=[],
)
