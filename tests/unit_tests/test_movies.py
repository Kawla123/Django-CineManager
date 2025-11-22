# tests/unit_tests/testes_movies.py

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviesproject.settings")
django.setup()

import pytest
from movie_app.models import Movie
from movie_app.forms import MovieForm
from django.urls import reverse
from django.test import Client





# Test minimal pour vérifier que pytest fonctionne
def test_dummy():
    assert True

# Test du modèle Movie
@pytest.mark.unit
def test_movie_creation():
    movie = Movie(title="Test Movie", description="Description", release_year=2025, new=True)
    assert movie.title == "Test Movie"
    assert movie.description == "Description"
    assert movie.release_year == 2025
    assert movie.new is True

# Test du formulaire MovieForm valide (image optionnelle)
@pytest.mark.unit
def test_movie_form_valid():
    form_data = {
        "title": "Film Form Test",
        "description": "Formulaire test",
        "release_year": 2025,
        "new": True
    }
    form = MovieForm(data=form_data)
    # Maintenant le formulaire devrait être valide car l'image est optionnelle
    if not form.is_valid():
        print(f"Erreurs du formulaire: {form.errors}")
    assert form.is_valid()

# Test du formulaire MovieForm

