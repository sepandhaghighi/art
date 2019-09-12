#!/bin/sh
python -m autopep8 art --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose
python -m autopep8 setup.py --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose
python -m autopep8 art_profile.py --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose
python -m autopep8 otherfile --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --verbose
