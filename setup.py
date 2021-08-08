from setuptools import setup, find_packages
from os import path

setup(
    name='polynomial',
    packages = ['polynomial'],
    version='0.14',
    license='AGPLv3',
    description=
    'This is a professional polynomial calculator and analyzer python module.',
    author='Rainbow-Dreamer',
    author_email='1036889495@qq.com',
    url='https://github.com/Rainbow-Dreamer/polynomial',
    download_url=
    'https://github.com/Rainbow-Dreamer/matrixpro/archive/0.14.tar.gz',
    keywords=['matrix', 'mathematics', 'statistics'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    include_package_data=True)