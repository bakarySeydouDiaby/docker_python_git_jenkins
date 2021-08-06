#!/usr/bin/python3
# test_addition.py

# importation du module add du package src/calculatrice.py
import sys

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/src")
from calculatrice import add

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/mydev1/lib/python3.8/site-packages")
import pytest

def test_add():
    result = add(3, 4)
    assert result == 7

def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)