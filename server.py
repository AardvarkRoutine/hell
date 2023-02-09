from flask import Flask, request

app = Flask(__name__)

board = ["_" for x in range(9)]
player = "X"

def check_game_over():
    # Check rows
    for i in range(0, 9, 3):
        row = board[i:i+3]
        if row[0] == row[1] == row[2] and row[0] != "_":
            return row[0]

    # Check columns
    for i in range(3):
        column = [board[i], board[i+3], board[i+6]]
        if column[0] == column[1] == column[2] and column[0] != "_":
            return column[0]

    # Check diagonals
    diagonal1 = [board[0], board[4], board[8]]
    diagonal2 = [board[2], board[4], board[6]]
    if (diagonal1[0] == diagonal1[1] == diagonal1[2] and diagonal1[0] != "_") or (
        diagonal2[0] == diagonal2[1] == diagonal2[2] and diagonal2[0] != "_"
    ):
        return diagonal1[0]

    # Check if all cells are filled
    if "_" not in board:
        return "Tie"

    # Game is not over
    return None

@app.route("/")
def home():
    return "Welcome to the Tic Tac Toe API!"

@app.route("/status", methods=["GET"])
def get_status():
    game_over = check_game_over()
    if game_over:
        return f"{game_over} won the game!", 200

    return f"{player}'s turn. Board: {','.join(board)}", 200

@app.route("/play", methods=["POST"])
def play():
    global player
    position = int(request.form["position"])
    if board[position] == "_":
        board[position] = player
        game_over = check_game_over()
        if game_over:
            return f"{game_over} won the game!", 200

        player = "O" if player == "X" else "X"

        return f"{player}'s turn. Board: {','.join(board)}", 200

    return "Invalid move!", 400

if __name__ == "__main__":
    app.run()