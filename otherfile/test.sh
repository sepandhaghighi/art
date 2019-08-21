set -e
set -x


IS_IN_TRAVIS=false

python otherfile/version_check.py
python otherfile/font_check.py

if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
then
     IS_IN_TRAVIS=true
fi

if [ "$IS_IN_TRAVIS" = 'false' ] || [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      python -m vulture --min-confidence 80 --exclude=art,build,.eggs --sort-by-size .
      python -m bandit -r art -s B311
	  python -m pydocstyle --match='(?!test).*\.py'
	  python -m art testcov2
	  codecov
  else
	  python -m art testcov
  fi
python -m cProfile -s cumtime art_profile.py