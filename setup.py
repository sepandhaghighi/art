# -*- coding: utf-8 -*-
from setuptools import setup


def get_requires():
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    with open("README.md") as r :
        description = "\n"
        description += r.read()
    with open("CHANGELOG.md") as c:
        description += "\n"
        description += c.read()
    return description


setup(
    name='art',
    packages=['art'],
    version='1.0',
    description='ASCII Art Library For Python',
    long_description='''ASCII art is also known as "computer text art".
    It involves the smart placement of typed special characters or
    letters to make a visual shape that is spread over multiple lines of text.
    Art is a Python lib for text converting to ASCII ART fancy.'''
                     + read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='sepand@qpage.ir',
    url='https://github.com/sepandhaghighi/art',
    download_url='https://github.com/sepandhaghighi/art/tarball/v1.0',
    keywords="ascii art python3 python text font",
    project_urls={
        'Webpage': 'http://art.shaghighi.ir',
        'Source': 'https://github.com/sepandhaghighi/art',
    },
    install_requires=get_requires(),
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Fonts',
    ],
    license='MIT',
    include_package_data=True
)
