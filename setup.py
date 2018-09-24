# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


MINIMAL_DESCRIPTION = '''ASCII art is also known as "computer text art".
    It involves the smart placement of typed special characters or
    letters to make a visual shape that is spread over multiple lines of text.
    Art is a Python lib for text converting to ASCII ART fancy.'''


def get_requires():
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return MINIMAL_DESCRIPTION


setup(
    name='art',
    packages=['art'],
    version='2.2',
    description='ASCII Art Library For Python',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='sepand@qpage.ir',
    url='https://github.com/sepandhaghighi/art',
    keywords="ascii art python3 python text font",
    project_urls={
        'Webpage': 'http://art.shaghighi.ir',
        'Source': 'https://github.com/sepandhaghighi/art',
        'Tracker': 'https://github.com/sepandhaghighi/art/issues',
    },
    install_requires=get_requires(),
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Fonts',
        'Topic :: Text Editors',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities',
        'Topic :: Multimedia',
        'Topic :: Printing',
    ],
    license='MIT',
    include_package_data=True
)
