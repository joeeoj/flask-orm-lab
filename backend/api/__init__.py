from flask import Flask, jsonify
from api import models
from api.lib import db


def create_app(database, user, password):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database,
        DB_USER=user,
        DB_PASSWORD=password,
    )

    @app.route("/")
    def index():
        return "Welcome to the movies api"

    @app.route("/actors")
    def actors():
        conn = db.get_db()
        all_actors = db.find_all(models.Actor, conn)
        return jsonify([a.to_json(conn) for a in all_actors])

    @app.route("/actors/<int:id>")
    def get_actor(id):
        conn = db.get_db()
        actor = db.find(models.Actor, id, conn)
        return jsonify(actor.to_json(conn))

    @app.route("/movies")
    def movies():
        conn = db.get_db()
        all_movies = db.find_all(models.Movie, conn)
        return jsonify([m.to_json(conn) for m in all_movies])

    @app.route("/movies/<int:id>")
    def get_movie(id):
        conn = db.get_db()
        movie = db.find(models.Movie, id, conn)
        return jsonify(movie.to_json(conn))

    return app
