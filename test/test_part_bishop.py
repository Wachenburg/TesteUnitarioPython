from src.board import Board
from src.color import Color
from src.part import Bishop

# python -m pip install pytest pytest-mock
# python -m pytest


#1 testa movimento para o bispo com uma peça no seu caminho
def test_move_bishop_Blocked():
  board = Board()
  part1 = Bishop(Color.WHITE)
  part2 = Bishop(Color.WHITE)
  board.put(0, 0, part1)
  board.put(1, 1, part2)
  part1.recalc(board, 0, 0)
  assert len(part1._positions) == 0


#2 testa movimento do bispo com uma peça do oponente no seu caminho
def test_move_bishop_Unblocked():
  board = Board()
  part1 = Bishop(Color.WHITE)
  part2 = Bishop(Color.BLACK)
  board.put(1, 1, part2)
  board.put(0, 0, part1)
  part1.recalc(board, 0, 0)
  assert len(part1._positions) == 1


#3 testa movimento do bispo no centro do tabuleiro
def test_move_bishop_Center():
  board = Board()
  part1 = Bishop(Color.WHITE)
  board.put(4, 4, part1)
  part1.recalc(board, 4, 4)
  assert len(part1._positions) == 13


#4 testa bloqueio do movimento horizontal do bispo
def test_bishop_side_movements():
  board = Board()
  part1 = Bishop(Color.WHITE)
  board.put(4, 4, part1)
  part1.recalc(board, 4, 4)
  assert (4, 3) not in [(pos._x, pos._y) for pos in part1._positions]
  assert (4, 5) not in [(pos._x, pos._y) for pos in part1._positions]


#5 testa bloqueio do movimento vertical do bispo
def test_bishop_vertical_movements():
  board = Board()
  part1 = Bishop(Color.WHITE)
  board.put(4, 4, part1)
  part1.recalc(board, 4, 4)
  assert (3, 4) not in [(pos._x, pos._y) for pos in part1._positions]
  assert (5, 4) not in [(pos._x, pos._y) for pos in part1._positions]
