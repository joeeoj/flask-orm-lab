class MovieActor:
    columns = ['movie_id', 'actor_id']
    __table__ = 'movie_actors'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.columns: setattr(self, k, v)

