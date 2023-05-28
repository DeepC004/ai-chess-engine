import chess
import chess.engine
import sys


def stockfishEvalFromPosition(position,depth=15):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish")
    board = chess.Board(position)
    print(render(board))
    info = engine.analyse(board, chess.engine.Limit(depth=depth))

    if info["score"].relative.score() is None:
        return 0
    return info["score"].relative.score()

def render(board: chess.Board) -> str:
    board_string = list(str(board))
    uni_pieces = {
        "r": "♖",
        "n": "♘",
        "b": "♗",
        "q": "♕",
        "k": "♔",
        "p": "♙",
        "R": "♜",
        "N": "♞",
        "B": "♝",
        "Q": "♛",
        "K": "♚",
        "P": "♟",
        ".": "·",
    }
    for idx, char in enumerate(board_string):
        if char in uni_pieces:
            board_string[idx] = uni_pieces[char]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []
    for rank in "".join(board_string).split("\n"):
        display.append(f"  {ranks.pop()} {rank}")
    if board.turn == chess.BLACK:
        display.reverse()
    display.append("    a b c d e f g h")
    return "\n" + "\n".join(display)