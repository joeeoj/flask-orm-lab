from api.lib.db import build_from_record
import api.models as models

class Actor:
    columns = ['id', 'name']
    __table__ = 'actors'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.columns: setattr(self, k, v)

    def movies(self, conn):
        cursor = conn.cursor()
        sql_statement = """select movies.* from movies 
        join movie_actors
        on movie_actors.movie_id = movies.id 
        join actors on movie_actors.actor_id = actors.id
        where actors.id = %s
        """
        cursor.execute(sql_statement, (self.id,))
        movies = cursor.fetchall()
        return [build_from_record(models.Movie, movie) for movie in movies]

    def to_json(self, conn):
        movies = self.movies(conn)
        movies_json = [movie.__dict__ for movie in movies]
        actor_dict = self.__dict__
        actor_dict['movies'] = movies_json
        return actor_dict


