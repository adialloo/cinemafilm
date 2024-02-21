# tests/test_api.py

from app import get_movies


def test_get_movies():
    url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=46f3de7d1fd8790343c98572d954a595'
    movies = get_movies(url)
    assert movies is not None
