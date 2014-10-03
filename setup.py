from setuptools import setup, find_packages
import os
import re

if os.environ.get('USER', '') == 'vagrant':
    del os.link

setup(
    name='dcitools',
    version=open('VERSION.txt').read().strip(),
    author='Ronan Delacroix',
    author_email='ronan.delacroix@gmail.com',
    packages=find_packages(where='.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={}, #{'mypkg': ['data/*.dat']},
    scripts=[],
    license=open('LICENCE.txt').read().strip(),
    description='Digital Cinema related collection of tools for Python',
    long_description=open('README.md').read().strip(),
    include_package_data=True,
    install_requires=[r.strip() if ('git+' not in r) else re.sub(r".*egg=(.*)", "", r).strip() for r in open('requirements.txt').readlines()],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: Proprietary',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
)