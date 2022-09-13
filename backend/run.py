import json

from flask import jsonify

from api import create_app
from api.lib import db
from api import models
from settings import DATABASE, DB_USER, DB_PASSWORD


app = create_app(DATABASE, DB_USER, DB_PASSWORD)


if __name__ == "__main__":
    app.run(debug=True)
