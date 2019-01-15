#!/bin/bash
if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
	brew update
	brew install openssl readline
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv
    pyenv install $PYTHON
    export PYENV_VERSION=$PYTHON
    export PATH="/Users/travis/.pyenv/shims:${PATH}"
    pyenv local $PYTHON
	exit 0
fi