import json

from api.lib import db
from api import models


class Actor:
    __table__ = "actors"

    columns = ["id", "name"]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"'{k}' not in columns!")
            setattr(self, k, v)

    def movies(self, conn):
        query_str = """
        SELECT *
        FROM movies m
        JOIN movie_actors ma
            ON m.id = ma.movie_id
        WHERE
            ma.actor_id = %s
        """
        cursor = conn.cursor()
        cursor.execute(query_str, (self.id,))
        movies = cursor.fetchall()
        return db.build_from_records(models.Movie, movies)

    def to_json(self, conn):
        """Returns dict of movie attributes along with an actors key with all actors in the movie"""
        d = self.__dict__
        d["movies"] = [a.__dict__ for a in self.movies(conn)]
        return d
