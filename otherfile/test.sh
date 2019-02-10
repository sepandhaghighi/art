set -e
set -x

python -m art testcov
python version_check.py
python -m vulture --min-confidence 80 --exclude=art,build,.eggs --sort-by-size .
python -m bandit -r art -s B311
python -m cProfile -s cumtime art_profile.py