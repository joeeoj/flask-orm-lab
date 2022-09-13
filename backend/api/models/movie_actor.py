class MovieActor:
    __table__ = "movie_actors"

    columns = ["id", "movie_id", "actor_id"]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.columns:
                raise ValueError(f"'{k}' not in columns!")
            setattr(self, k, v)
