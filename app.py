from flask import Flask, render_template
import requests

app = Flask(__name__)

api_key = 'KEY_api'

# URL de l'API TMDb pour récupérer la liste des films actuellement au cinéma
now_playing_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1'

movie_details_base_url = 'https://api.themoviedb.org/3/movie/'

@app.route('/')
def home():
    movies = get_movies(now_playing_url)
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    movie_details_url = f'{movie_details_base_url}{movie_id}?api_key={api_key}&language=fr-FR'
    movie_details = get_movie_details(movie_details_url)
    return render_template('movie_details.html', movie=movie_details)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

def get_movies(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        return movies
    else:
        return None

def get_movie_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        movie_details = response.json()
        return movie_details
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
