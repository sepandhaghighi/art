from distutils.core import setup
setup(
  name = 'art',
  packages = ['art'],
  version = '0.5',
  description = 'ASCII Art Collection In Python',
  long_description='ASCII Art Collection In Python',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/art',
  download_url = 'https://github.com/sepandhaghighi/art/tarball/v0.5',
  keywords = ['ascii', 'art', 'python3','python','text'],
  install_requires=[
	  'codecov',
      ],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Topic :: Text Processing :: Fonts',
    ],
  license='MIT',
)
