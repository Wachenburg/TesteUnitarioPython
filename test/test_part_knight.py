from src.board import Board
from src.color import Color
from src.part import Knight

# python -m pip install pytest pytest-mock
# python -m pytest


#1 testa movimento para o cavalo bloqueado
def test_move_knight_Blocked():
  board = Board()
  part1 = Knight(Color.WHITE)
  part2 = Knight(Color.WHITE)
  part3 = Knight(Color.WHITE)
  board.put(0, 0, part1)
  board.put(1, 2, part2)
  board.put(2, 1, part3)
  part1.recalc(board, 0, 0)
  assert len(part1._positions) == 0


#2 testa movimento do cavaleiro no centro do tabuleiro
def test_move_knight_Center():
  board = Board()
  part1 = Knight(Color.WHITE)
  board.put(4, 4, part1)
  part1.recalc(board, 4, 4)
  assert len(part1._positions) == 8

#3 testa movimento do cavaleiro no centro com 2 espaços 
#bloqueados por aliados e 2 com oponentes nele
def test_move_knight_Center_2():
  board = Board()
  part1 = Knight(Color.WHITE)
  part2 = Knight(Color.WHITE)
  part3 = Knight(Color.WHITE)
  part4 = Knight(Color.BLACK)
  part5 = Knight(Color.BLACK)
  board.put(4,4,part1)
  board.put(3,2,part2)
  board.put(5,2,part3)
  board.put(6,3,part4)
  board.put(2,3,part5)
  part1.recalc(board, 4, 4)
  assert len(part1._positions) == 6
  

#4 testa movimento do cavaleiro para fora do tabuleiro
#fazendo o L para baixo à esquerda
def test_move_knight_out_board():
  board = Board()
  part1 = Knight(Color.WHITE)
  board.put(1, 7, part1) # casa inicial do cavalo branco

  part1.recalc(board, 1, 7)

  # 0, 9 é fora do tabuleiro
  
  assert (0, 9) not in [(pos._x, pos._y) for pos in part1._positions]

#5 testa o movimento do cavaleiro com peças em sua volta 
#mas não em casas que ele pode ir
def test_move_surrounded_by_pieces():
  board = Board()
  part1 = Knight(Color.WHITE)
  part2 = Knight(Color.WHITE)
  part3 = Knight(Color.WHITE)
  part4 = Knight(Color.WHITE)
  part5 = Knight(Color.WHITE)
  part6 = Knight(Color.WHITE)
  part7 = Knight(Color.WHITE)
  part8 = Knight(Color.WHITE)
  part9 = Knight(Color.WHITE)
  board.put(4, 4, part1)
  board.put(3, 3, part2)
  board.put(4, 3, part3)
  board.put(5, 3, part4)
  board.put(3, 4, part5)
  board.put(5, 4, part6)
  board.put(3, 5, part7)
  board.put(4, 5, part8)
  board.put(5, 5, part9)
  part1.recalc(board, 4, 4)
  assert len(part1._positions) == 8


