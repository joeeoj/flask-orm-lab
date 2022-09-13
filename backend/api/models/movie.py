from api.lib import db
from api import models


class Movie:
    __table__ = "movies"

    columns = ["id", "title", "studio", "runtime", "description", "release_date", "year"]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"'{k}' not in columns!")
            setattr(self, k, v)

    def actors(self, conn):
        query_str = """
        SELECT *
        FROM actors a
        JOIN movie_actors ma
            ON a.id = ma.actor_id
        WHERE
            ma.movie_id = %s
        """
        cursor = conn.cursor()
        cursor.execute(query_str, (self.id,))
        actors = cursor.fetchall()
        return db.build_from_records(models.Actor, actors)

    def to_json(self, conn):
        """Returns dict of movie attributes along with an actors key with all actors in the movie"""
        d = self.__dict__
        d["actors"] = [a.__dict__ for a in self.actors(conn)]
        return d
