#!/usr/bin/python3
# test_addition.py

# importation du module multiply du package src/calculatrice.py
import sys

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/src")
from calculatrice import multiply

sys.path.append("/mnt/c/Users/Utilisateur/Desktop/bak_projet/2_docker_python_jenkins/python_docker_jenkins_git/mydev1/lib/python3.8/site-packages")
import pytest

def test_multiply():
    result = multiply(3, 4)
    assert result == 10


def test_multiply_string():
    with pytest.raises(TypeError):
        multiply("string", 4)