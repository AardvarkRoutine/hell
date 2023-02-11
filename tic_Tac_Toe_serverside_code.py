from flask import Flask, request, jsonify

app = Flask(__name__)
games = {}

@app.route('/create_game', methods=['POST'])
def create_game():
    # Spieler X erstellt das Spiel
    player_x = request.remote_addr
    game_id = len(games) + 1
    games[game_id] = {'player_x': player_x, 'player_o': None, 'board': ['-', '-', '-', '-', '-', '-', '-', '-', '-']}
    return jsonify({'game_id': game_id})

@app.route('/join_game/<int:game_id>', methods=['POST'])
def join_game(game_id):
    if game_id not in games:
        return jsonify({'error': 'Spiel nicht gefunden'}), 404
    if games[game_id]['player_o'] is not None:
        return jsonify({'error': 'Spiel ist bereits voll'}), 400
    player_o = request.remote_addr
    games[game_id]['player_o'] = player_o
    return jsonify({'game_id': game_id})

@app.route('/make_move/<int:game_id>', methods=['POST'])
def make_move(game_id):
    if game_id not in games:
        return jsonify({'error': 'Spiel nicht gefunden'}), 404
    if games[game_id]['player_o'] is None:
        return jsonify({'error': 'Spiel ist nicht voll'}), 400
    player = request.remote_addr
    if player != games[game_id]['player_x'] and player != games[game_id]['player_o']:
        return jsonify({'error': 'Ungültiger Spieler'}), 400
    move = request.json.get('move')
    if move is None or not (0 <= move <= 8):
        return jsonify({'error': 'Ungültiger Zug'}), 400
    board = games[game_id]['board']
    if board[move] != '-':
        return jsonify({'error': 'Feld bereits besetzt'}), 400
    if player == games[game_id]['player_x']:
        board[move] = 'X'
    else:
        board[move] = 'O'
    winner = check_winner(board)
    if winner is not None:
        return jsonify({'winner': winner})
    return jsonify({'board': board})

def check_winner(board):
    # Überprüfen Sie hier, ob ein Spieler gewonnen hat
    return None # Kein Sieger

if __name__ == '__main__':
    app.run()
