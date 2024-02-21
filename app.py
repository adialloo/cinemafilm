from flask import Flask, render_template ,request
import requests

app = Flask(__name__)

api_key = '46f3de7d1fd8790343c98572d954a595'

now_playing_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}'

movie_details_base_url = 'https://api.themoviedb.org/3/movie/'

@app.route('/')
def home():
    lang = request.args.get('lang', 'en-US')  # Récupère la langue à partir de l'URL
    movies = get_movies(f'{now_playing_url}&language={lang}')
    return render_template('index.html', movies=movies, lang=lang)


@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    lang = request.args.get('lang', 'en-US')  
    movie_details_url = f'{movie_details_base_url}{movie_id}?api_key={api_key}&language={lang}'
    movie_details = get_movie_details(movie_details_url)
    return render_template('movie_details.html', movie=movie_details, lang=lang)


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

def get_movies(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        for movie in movies:
            movie['poster_path'] = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
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
    app.run(host='0.0.0.0', port=5000, debug=True)