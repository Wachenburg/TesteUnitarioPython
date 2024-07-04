from src.board import Board
from src.color import Color
from src.part import Rock

# python -m pip install pytest pytest-mock
# python -m pytest

#1 Testa o movimento da torre sendo bloqueado por um aliado
#e com um oponente em outro
def test_part_rock_recalc_ex3():
  board = Board()
  part1 = Rock(Color.WHITE)
  part2 = Rock(Color.WHITE)
  part3 = Rock(Color.BLACK)
  board.put(0, 0, part1)
  board.put(0, 1, part2)
  board.put(1, 0, part3)
  part1.recalc(board, 0, 0)
  assert len(part1._positions) == 1

#2 Testa o movimento da torre sendo bloqueado por aliado em todos os lados
def test_part_rock_recalc_ex2():
  board = Board()
  part1 = Rock(Color.WHITE)
  part2 = Rock(Color.WHITE)
  part3 = Rock(Color.WHITE)
  board.put(0, 0, part1)
  board.put(0, 1, part2)
  board.put(1, 0, part3)
  part1.recalc(board, 0, 0)
  assert len(part1._positions) == 0

#3 Testa o movimento da torre sendo bloqueado apenas na vertical
def test_part_rock_recalc_ex1():
  board = Board()
  part_w = Rock(Color.WHITE)
  part_b = Rock(Color.BLACK)
  board.put(0, 0, part_w)
  board.put(0, 1, part_b)
  part_w.recalc(board, 0, 0)
  assert len(part_w._positions) == 8

#4 Testa o movimento da torre sem ser bloqueado
def test_part_rock_recalc_empty():
  board = Board()
  part = Rock(Color.WHITE)
  part.recalc(board, 0, 0)
  assert len(part._positions) == 14

#5 Testa se o construtor da torre funciona corretamente
def test_part_rock_ctor():

  colors = [Color.WHITE, Color.BLACK]

  for c in colors:
    part = Rock(c)
    assert part._mark_black == "♜"
    assert part._mark_white == "♖"
    assert part._color == c
    assert part._name == "Rock"
    assert part._positions == []