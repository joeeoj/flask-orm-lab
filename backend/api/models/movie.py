from api.lib.db import build_from_record
import api.models as models
class Movie:
    columns = ['id', 'title', 'studio', 
    'runtime', 'description', 'release_date', 'year']
    __table__ = 'movies'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.columns: setattr(self, k, v)

    def actors(self, conn):
        cursor = conn.cursor()
        sql_statement = """select actors.* from movies 
        join movie_actors
        on movie_actors.movie_id = movies.id 
        join actors on movie_actors.actor_id = actors.id
        where movies.id = %s
        """
        cursor.execute(sql_statement, (self.id,))
        actors = cursor.fetchall()
        return [build_from_record(models.Actor, actor) for actor in actors]

    def to_json(self, conn):
        actors = self.actors(conn)
        actors_json = [actor.__dict__ for actor in actors]
        movie_dict = self.__dict__
        movie_dict['actors'] = actors_json
        return movie_dict
