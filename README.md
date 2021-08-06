# docker_python_git_jenkins

## resume :
==========

nous allons développer une calculatrice simple en Python, 
écrire des tests pour celle-ci en utilisant le framework pytest 
et utiliser un container Jenkins pour récupérer le dépôt depuis GitHub 
et exécuter les tests à l'intérieur d'un nouveau conteneur Docker lancé par Jenkins. 
L'ensemble du dépôt est disponible sur : https://github.com/varunkumar032/python-test-calculator

## Example testing python code with pytest

Ther src repository contains a python package with two files :
- __init__.py
- calculatrice.py : a simple python script to perform add/sustract/multiply/divide
The src repository contains aloso anotehr directory : tests

the tests directory contains 5 files : 

- __init__.py
- test_addition.py
- test_multiplication.py
- test_soustraction.py
- test_division.py
