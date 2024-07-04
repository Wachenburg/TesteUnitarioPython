from src.board import Board
from src.color import Color


#1 testa se o tabuleiro tem as 64 casas padrões
def test_board_columns_and_lines():
  board = Board()
  assert board._NUM_COLUMNS == 8
  assert board._NUM_LINES == 8

#2 testa se a quantidade de peças está correta
def test_board_pieces():
  board = Board()
  board.reset()
  countEmpty = 0
  countWhite = 0
  countBlack = 0
  for i in range(board._NUM_LINES):
    for j in range(board._NUM_COLUMNS):
      if board.get_peca(i, j) is None:
        countEmpty += 1

      if board.get_peca(i, j) is not None:
        if board.get_peca(i, j)._color == Color.WHITE:
          countWhite += 1
        if board.get_peca(i, j)._color == Color.BLACK:
          countBlack += 1
        
  assert countEmpty == 32
  assert countWhite == 16
  assert countBlack == 16

#3 testa se a quantidade de peças de cada tipo foi alocada corretamente
def test_board_type_pieces():
  board = Board()
  board.reset()
  countBishop = 0
  countRook = 0
  countKnight = 0
  countQueen = 0
  countKing = 0
  countPawn = 0
  for i in range(board._NUM_LINES):
    for j in range(board._NUM_COLUMNS):
      if board.get_peca(i, j) is not None:
        if board.get_peca(i, j)._name == "Peão":
          countPawn += 1
        if board.get_peca(i, j)._name == "Rock":
          countRook += 1
        if board.get_peca(i, j)._name == "Cavalo":
          countKnight += 1
        if board.get_peca(i, j)._name == "Bispo":
          countBishop += 1
        if board.get_peca(i, j)._name == "King":
          countKing += 1
        if board.get_peca(i, j)._name == "Rainha":
          countQueen += 1
        
  assert countPawn == 16
  assert countRook == 4
  assert countKnight == 4
  assert countBishop == 4
  assert countKing == 2
  assert countQueen == 2