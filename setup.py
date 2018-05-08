# -*- coding: utf-8 -*-
from setuptools import setup
def get_requires():
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))

setup(
    name='art',
    packages=['art'],
    version='0.9',
    description='ASCII Art Collection In Python',
    long_description='ASCII Art Collection In Python',
    author='Sepand Haghighi',
    author_email='sepand@qpage.ir',
    url='https://github.com/sepandhaghighi/art',
    download_url='https://github.com/sepandhaghighi/art/tarball/v0.9',
    keywords="ascii art python3 python text font",
    project_urls={
        'Webpage': 'http://pycm.shaghighi.ir',
        'Source': 'https://github.com/sepandhaghighi/pycm',
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
