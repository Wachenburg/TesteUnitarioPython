from src.board import Board
from src.color import Color
from src.part import Pawn

# python -m pip install pytest pytest-mock
# python -m pytest


#1 testa quantas casas o peao tem disponivel para pular a frente no inicio do jogo
def test_part_pawn_recalc_start():
    board = Board()
    part = Pawn(Color.WHITE)
    board.put(6, 6, part)
    part.recalc(board, 6, 6)
    assert len(part._positions) == 2


#2 testa movimento para trás
def test_part_pawn_recalc_back_movement():
    board = Board()
    part = Pawn(Color.WHITE)
    board.put(6, 6, part)

    assert (6, 7) not in [(pos._x, pos._y) for pos in part._positions]

    '''try:
        part.recalc(board, 6, 7)  # Tente realizar um movimento inválido aqui
        raise AssertionError("Movimento inválido. O peão não pode pular para trás.")
    except AssertionError as e:
        assert str(e) == "Movimento inválido. O peão não pode pular para trás."'''

#3 testa movimento para laterais
def test_part_pawn_recalc_side_movement():
    board = Board()
    part = Pawn(Color.WHITE)
    board.put(6, 6, part)

    '''Verifica se o movimento para (5, 6 esquerda) (falso para movimento lateral)
    #assert part.recalc(board, 5, 6) is None

    # Verifica se o movimento para (7, 6 direita) falso para movimento lateral)
    #assert part.recalc(board, 7, 6) is None'''

    assert (5, 6) and (7, 6) not in [(pos._x, pos._y) for pos in part._positions]

#4 testa captura peça branca em peça preta
def test_part_pawn_recalc_capture_black():
    board = Board()
    part1 = Pawn(Color.WHITE)
    part2 = Pawn(Color.BLACK)
    board.put(4, 4, part1)
    board.put(3,3,part2)
    part1._first_move = False
    part1.recalc(board, 4, 4)
    assert len(part1._positions) == 2

#5 testa captura peça preta em peça branca
def test_part_pawn_recalc_capture_white():
    board = Board()
    part1 = Pawn(Color.WHITE)
    part2 = Pawn(Color.BLACK)
    board.put(4, 4, part1)
    board.put(3,3,part2)
    part2._first_move = False
    part1.recalc(board, 3, 3)
    assert len(part1._positions) == 2

#6 testa movimente en passant brancas
def test_en_passant_white():
    board = Board()
    part1 = Pawn(Color.WHITE)
    part2 = Pawn(Color.BLACK)
    board.put(4, 4, part1)
    board.put(3, 4, part2)
    part1._first_move = False
    part1.recalc(board, 4, 4)
    assert len(part1._positions) == 2

#7 testa movimento en passant pretas
def test_en_passant_black():
    board = Board()
    part1 = Pawn(Color.WHITE)
    part2 = Pawn(Color.BLACK)
    board.put(4, 4, part1)
    board.put(3, 4, part2)
    part2._first_move = False
    part2.recalc(board, 3, 4)
    assert len(part2._positions) == 2

#8 testa movimento com peça na frente bloqueando
def test_move_block():
    board = Board()
    part1 = Pawn(Color.WHITE)
    part2 = Pawn(Color.BLACK)
    board.put(4, 4, part1)
    board.put(4, 3, part2)
    part1._first_move = False
    part1.recalc(board, 4, 4)
    assert len(part1._positions) == 0