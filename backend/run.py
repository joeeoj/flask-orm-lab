from api import create_app

app = create_app('imdb_development', 'postgres', 'postgres')

app.run(debug = True)