from src.board import Board
from src.color import Color
from src.part import King, Pawn

# python -m pip install pytest pytest-mock
# python -m pytest
  
#1 testa possiveis movimentos do Rei para qualquer lado estando no meio do tabuleiro
def test_move_options_king_is_on_center():
  board = Board()
  part = King(Color.WHITE)
  board.put(4, 4, part)
  part.recalc(board, 4, 4)
  assert len(part._positions) == 8
  

#2 testa movimento do Rei para frente no inicio do jogo
def test_move_king_forward_with_pawn():
  board = Board()
  part = King(Color.BLACK)
  part2 = Pawn(Color.BLACK)
  board.put(4, 0, part)  
  board.put(4, 1, part2) 

  part.recalc(board, 4, 0)

  # Verificar qtde posicoes pode pular, indicando que o rei não pode mover para frente
  assert len(part._positions) == 4
  

#3 testa possiveis movimentos do Rei para qualquer lado estando rodeado
def test_move_king_surrounded_with_pawn():
  board = Board()
  part = King(Color.BLACK)
  part2 = Pawn(Color.BLACK)
  part3 = Pawn(Color.BLACK)
  part4 = Pawn(Color.BLACK)
  part5 = Pawn(Color.BLACK)
  part6 = Pawn(Color.BLACK)
  part7 = Pawn(Color.BLACK)
  part8 = Pawn(Color.BLACK)
  part9 = Pawn(Color.BLACK)
  
  board.put(4, 4, part)  
  board.put(4, 5, part2)
  board.put(3, 5, part3) 
  board.put(3, 4, part4) 
  board.put(3, 3, part5) 
  board.put(4, 3, part6)
  
  board.put(5, 3, part7)
  board.put(5, 4, part8) 
  board.put(5, 5, part9) 
  
  assert len(part._positions) == 0