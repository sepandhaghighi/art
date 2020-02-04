#!/bin/bash
set -e
set -x


IS_IN_TRAVIS=false
PYTHON_COMMAND=python
PIP_COMMAND=pip

if [ "$TRAVIS_OS_NAME" == "osx" ]
then
	PYTHON_COMMAND=python3
	PIP_COMMAND=pip3
fi
 
if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
then
     IS_IN_TRAVIS=true
fi
 
$PYTHON_COMMAND otherfile/version_check.py
$PYTHON_COMMAND otherfile/font_check.py
$PYTHON_COMMAND -m art testcov2

if [ "$IS_IN_TRAVIS" = 'false' ] || [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
then
     $PYTHON_COMMAND -m vulture art/ otherfile/ setup.py art_profile.py --min-confidence 65 --exclude=__init__.py --sort-by-size
     $PYTHON_COMMAND -m bandit -r art -s B311
	 $PYTHON_COMMAND -m pydocstyle --match='(?!test).*\.py'
	 codecov
fi


$PYTHON_COMMAND -m cProfile -s cumtime art_profile.py
$PIP_COMMAND uninstall art
$PIP_COMMAND install art --upgrade