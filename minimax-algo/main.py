import chess
import chess.engine
import argparse
from movegeneration import next_move
from csv import writer
import chess.svg
from cairosvg import svg2png
import PySimpleGUI as sg

def start(args):
    board = chess.Board()
    user_side = (
        chess.WHITE if input("Start as a [b]lack bead or [w]hite bead? This signifies the evaluator color\n") == "w" else chess.BLACK
    )
    print(render(board))

    if user_side == chess.WHITE:
        board.push(get_move(board))
        print(render(board))

    while not board.is_game_over():
        board.push(next_move(get_depth(args), board, debug=args.debug))
        print(render(board))
        board.push(get_move(board))
        print(render(board))

    print(render(board))
    print(f"\nResult: [w] {board.result()} [b]")


def render(board: chess.Board) -> str:
    svg_image = chess.svg.board(board=board)
    svg2png(bytestring=svg_image,write_to='output.png')
    sg.Window('Chess', [[sg.Image('output.png')]], margins=(100, 50)).read(close=True)

def get_move(board: chess.Board) -> chess.Move:
    move = input(f"\nYour move (Like: {list(board.legal_moves)[0]}):\n")

    for legal_move in board.legal_moves:
        if move == str(legal_move):
            return legal_move
    return get_move(board)

def get_depth(args) -> int:
    return max([1, int(args.depth)])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", default=3, help="Provide an integer (Default: 3)")
    parser.add_argument("--debug", type=bool, default=False, help="Provide a boolean (Default: False)")
    args = parser.parse_args()
    print(args)
    try:
        start(args)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
