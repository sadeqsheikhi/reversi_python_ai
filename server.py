from flask import Flask, render_template, request
from uuid import uuid4
from json import dumps, loads
from re import sub as replace
from time import sleep

# local imports
from reversi import Reversi, Coord
from reversiai import ReversiAI
from aihelper import AIHelper, FormatConverter

app = Flask(__name__)

# this will be filled when games are played
games = {}


def filter(_dict, keys):
    return {key: _dict.get(key) for key in keys}


def union(first_dict, second_dict):
    return dict(list(first_dict.items()) + list(second_dict.items()))


def new_token():
    return uuid4().hex


def new_game(name, has_ai):
    global games
    index = new_token()
    game = {"id": index, "black": name,
            "black_token": new_token(), "ai": has_ai, "game": Reversi()}
    if has_ai:
        game['white'] = 'AI'
    games[index] = game
    return union(public_game_info(game, True),
                 {"black_token": game["black_token"]})


def public_game_info(game, additional_info=False):
    data = filter(game, ['id', 'white', 'black'])

    if additional_info:
        return union(data, game['game'].game_info())

    return data


# nsdr 
@app.route('/')
def root():
    return app.send_static_file('client.html')

# @app.route('/style.css')
# def style():
#     return app.send_static_file('style.css')

# @app.route('/script.js')
# def script():
#     return app.send_static_file('script.js')


@app.route('/game/<id>')
def game(id):
    try:
        return dumps(public_game_info(games[id], True))
    except KeyError as e:
        return '', 404


@app.route('/games')
def all_games():
    return dumps([public_game_info(game) for game in games.values()])


@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    has_ai = {"false": 0, "true": 1}[request.form.get('ai')]
    return dumps(new_game(name, has_ai))


@app.route('/play', methods=['POST'])
def play():
    data = request.form
    game = games[str(data.get('id'))]
    player = game['game'].game_info()['player']
    idx = int(data.get('idx'))
    if data.get(player + '_token') == game[player + '_token']:
        game['game'].play(Coord(idx // 8, idx % 8))
        if game['ai']:
            while game['game'].game_info()['player'] == 'white':
                board = FormatConverter.game_to_ai_board(game['game'].board)
                game['game'].play(ReversiAI.get_next_move(board, 'w'))

    return dumps(public_game_info(game, True))


@app.route('/join', methods=['POST'])
def join():
    data = request.form
    game = games[str(data.get('id'))]
    if game.get('white') is None:
        game['white'] = data.get('name')
        game['white_token'] = new_token()
        return dumps(filter(game, ['id', 'white', 'black', 'white_token']))


if __name__ == '__main__':
    app.run(debug=True)
