from src.board import Board
from src.color import Color
from src.part import Pawn, Queen


#1 testa movimentação da rainha no centro
def test_move_queen_center():
  board = Board()
  part1 = Queen(Color.WHITE)
  board.put(4, 4, part1)
  part1.recalc(board, 4, 4)
  assert len(part1._positions) == 27

#2 testa movimentacao da rainha se bloqueada na diagonal
def test_move_queen_if_blocked_on_diagonals():
  board = Board()
  part1 = Queen(Color.WHITE)
  part2 = Pawn(Color.WHITE)
  board.put(0, 7, part1)
  board.put(1, 7, part2)
  part1.recalc(board, 0, 7)
  assert len(part1._positions) == 14

#3 testa movimentacao da rainha bloqueada aos lados
def test_move_queen_if_blocked_on_sides():
  board = Board()
  part1 = Queen(Color.WHITE)
  part2 = Pawn(Color.WHITE)
  part3 = Pawn(Color.WHITE)
  board.put(0, 7, part1)
  board.put(1, 6, part2)
  board.put(1, 7, part3)
  part1.recalc(board, 0, 7)
  assert len(part1._positions) == 7

#4 testa movimentacao da rainha caso totalmente bloqueada
def test_move_queen_block_all_sides():
  board = Board()
  part1 = Queen(Color.WHITE)
  part2 = Pawn(Color.WHITE)
  part3 = Pawn(Color.WHITE)
  part4 = Pawn(Color.WHITE)
  board.put(0, 0, part1)
  board.put(1, 1, part2)
  board.put(1, 0, part3)
  board.put(0, 1, part4)
  part1.recalc(board, 0, 0)
  assert len(part1._positions) == 0