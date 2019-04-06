set -e
set -x

python version_check.py
if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
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