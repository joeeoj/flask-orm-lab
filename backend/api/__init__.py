from flask import Flask, jsonify
from api.lib.db import find_all, get_db, find
from api.models import Actor, Movie
import psycopg2

def create_app(database, user, password):
    app = Flask(__name__)
    app.config['DATABASE'] = database
    app.config['DB_USER'] = user
    app.config['DB_PASSWORD'] = password

    @app.route('/')
    def home():
        return 'Welcome to the movies api'

    @app.route('/actors')
    def actors():
        conn = get_db()
        actors = find_all(Actor, conn)
        actor_dicts = [actor.to_json(conn) for actor in actors]
        return jsonify(actor_dicts)

    @app.route('/actors/<id>')
    def actor(id):
        conn = get_db()
        actor = find(Actor, id, conn)
        return jsonify(actor.to_json(conn))

    @app.route('/movies')
    def movies():
        conn = get_db()
        movies = find_all(Movie, conn)
        movie_dicts = [movie.to_json(conn) for movie in movies]
        return jsonify(movie_dicts)

    @app.route('/movies/<id>')
    def movie(id):
        conn = get_db()
        movie = find(Movie, id, conn)
        return jsonify(movie.to_json(conn))
    
    return app