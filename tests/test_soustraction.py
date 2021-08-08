#!/usr/bin/python3
# test_addition.py

# importation du module substract du package src/calculatrice.py
import sys

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/src")
from calculatrice import subtract

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/mydev1/lib/python3.8/site-packages")
import pytest

def test_subtract_positive():
    result = subtract(4, 3)
    assert result == 10


def test_subtract_negative():
    result = subtract(3, 4)
    assert result == -1


def test_subtract_string():
    with pytest.raises(TypeError):
        subtract("string", 4)