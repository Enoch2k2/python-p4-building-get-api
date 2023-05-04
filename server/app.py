#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return "Index for Game/Review/User API"


@app.route('/games')
def games():
    # games = [{
    #     "title": game.title,
    #     "genre": game.genre,
    #     "platform": game.platform,
    #     "price": game.price
    # } for game in Game.query.all()]
    games = [game.to_dict() for game in Game.query.all()]

    response = make_response(
        games,
        200
    )

    return response


@app.route("/games/<int:id>")
def game(id):
    game = Game.query.filter(Game.id == id).first().to_dict()

    return make_response(
        game,
        200
    )


if __name__ == '__main__':
    app.run(port=5555, debug=True)
