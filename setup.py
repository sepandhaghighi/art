# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


MINIMAL_DESCRIPTION = '''ASCII art is also known as "computer text art".
    It involves the smart placement of typed special characters or
    letters to make a visual shape that is spread over multiple lines of text.
    ART is a Python lib for text converting to ASCII art fancy.'''


def get_dev_requires():
    """Read dev-requirements.txt."""
    requirements = open("dev-requirements.txt", "r").read()
    return [x for x in requirements.split() if x]


def read_description():
    """Read README.md and CHANGELOG.md."""
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
    version='6.1',
    description='ASCII Art Library For Python',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='info@ascii-art.site',
    url='https://github.com/sepandhaghighi/art',
    keywords="ascii art python3 python text font non-ascii printing",
    project_urls={
        'Webpage': 'https://www.ascii-art.site',
        'Source': 'https://github.com/sepandhaghighi/art',
        'Tracker': 'https://github.com/sepandhaghighi/art/issues',
        'Discord': 'https://discord.com/invite/FAAyq3QJqP',
    },
    install_requires=[],
    extras_require={
        "dev": get_dev_requires()
    },
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Text Processing :: Fonts',
        'Topic :: Text Editors',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities',
        'Topic :: Multimedia',
        'Topic :: Printing',
    ],
    license='MIT',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'art = art.__main__:main',
        ]}
)
