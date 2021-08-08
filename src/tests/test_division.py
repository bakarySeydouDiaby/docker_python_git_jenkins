#!/usr/bin/python3
# test_addition.py

# importation du module divide du package src/calculatrice.py
import sys

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/src")
from calculatrice import divide

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/mydev1/lib/python3.8/site-packages")
import pytest


def test_divide():
    result = divide(3, 2)
    assert result == 1.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(3, 0)


def test_divide_string():
    with pytest.raises(TypeError):
        divide("string", 2)