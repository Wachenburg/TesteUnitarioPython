# https://www.alt-codes.net/chess-symbols.php
from src.color import Color


class Position:
  _x: int
  _y: int

  def __init__(self, x, y):
    self._x = x
    self._y = y

  def __str__(self):
    return "(" + str(self._x) + ", " + str(self._y) + ")"


# classe abstrata
class Part:

  _name: str
  _mark_white: str
  _mark_black: str
  _color: Color
  _positions: list[Position]

  def __init__(self, name, color):
    self._name = name
    self._color = color
    self._positions = []

  def __str__(self):
    return self._mark_white \
      if(self._color == Color.WHITE) \
      else self._mark_black


class Knight(Part):
  _mark_white = "♘"
  _mark_black = "♞"

  def __init__(self, color):
    Part.__init__(self, "Cavalo", color)

  def recalc(self, board, x, y):
    self._positions = []

    #cima esquerda
    ulx = x - 1
    uly = y - 2
    if (ulx >= 0 and uly >= 0
        and (board.get_peca(ulx, uly) is None
             or board.get_peca(ulx, uly)._color != self._color)):
      pos = Position(ulx, uly)
      self._positions.append(pos)

    #cima direita
    urx = x + 1
    ury = y - 2
    if (urx <= 7 and ury >= 0
        and (board.get_peca(urx, ury) is None
             or board.get_peca(urx, ury)._color != self._color)):
      pos = Position(urx, ury)
      self._positions.append(pos)

    #direita cima
    rux = x + 2
    ruy = y - 1
    if (rux >= 0 and ruy >= 0
        and (board.get_peca(rux, ruy) is None
             or board.get_peca(rux, ruy)._color != self._color)):
      pos = Position(rux, ruy)
      self._positions.append(pos)

    #direita baixo
    rbx = x + 2
    rby = y + 1
    if (rbx <= 7 and rby <= 7
        and (board.get_peca(rbx, rby) is None
             or board.get_peca(rbx, rby)._color != self._color)):
      pos = Position(rbx, rby)
      self._positions.append(pos)

    #baixo direita
    brx = x + 1
    bry = y + 2
    if (brx <= 7 and bry <= 7
        and (board.get_peca(brx, bry) is None
             or board.get_peca(brx, bry)._color != self._color)):
      pos = Position(brx, bry)
      self._positions.append(pos)

    #baixo esquerda
    blx = x - 1
    bly = y + 2
    if (blx >= 0 and bly <= 7
        and (board.get_peca(blx, bly) is None
             or board.get_peca(blx, bly)._color != self._color)):
      pos = Position(blx, bly)
      self._positions.append(pos)

    #esquerda baixo
    lbx = x - 2
    lby = y + 1
    if (lbx >= 0 and lby <= 7
        and (board.get_peca(lbx, lby) is None
             or board.get_peca(lbx, lby)._color != self._color)):
      pos = Position(lbx, lby)
      self._positions.append(pos)

    #esquerda cima
    lux = x - 2
    luy = y - 1
    if (lux >= 0 and luy >= 0
        and (board.get_peca(lux, luy) is None
             or board.get_peca(lux, luy)._color != self._color)):
      pos = Position(lux, luy)
      self._positions.append(pos)


#movimentacao rainha
class Queen(Part):
  _mark_white = "♕"
  _mark_black = "♛"

  def __init__(self, color):
    Part.__init__(self, "Rainha", color)

  def recalc(self, board, x, y):
    #validar se esta é a lógica
    self._positions = []

    #diagonal cima esquerda
    bx = x - 1
    by = y - 1
    while (bx >= 0 and by >= 0):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx - 1
      by = by - 1
      
    #diagonal baixo esquerda
    bx = x - 1
    by = y + 1
    while (bx >= 0 and by <= 7):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx - 1
      by = by + 1

    #diagonal cima direita
    bx = x + 1
    by = y - 1
    while (bx <= 7 and by >= 0):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx + 1
      by = by - 1

    #diagonal cima esquerda
    bx = x + 1
    by = y + 1
    while (bx <= 7 and by <= 7):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx + 1
      by = by - 1

    #movimento cima
    xt = x - 1
    while (xt >= 0):
      part = board.get_peca(xt, y)
      if (part is None):
        pos = Position(xt, y)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(xt, y)
          self._positions.append(pos)
        break
      xt = xt - 1

    #motivmento baixo
    xt = x + 1
    while (xt <= 7):
      part = board.get_peca(xt, y)
      if (part is None):
        pos = Position(xt, y)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(xt, y)
          self._positions.append(pos)
        break
      xt = xt + 1

    #movimento esquerda
    yt = y - 1
    while (yt >= 0):
      part = board.get_peca(x, yt)
      if (part is None):
        pos = Position(x, yt)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(x, yt)
          self._positions.append(pos)
        break
      yt = yt - 1

    #movimento direita
    yt = y + 1
    while (yt <= 7):
      part = board.get_peca(x, yt)
      if (part is None):
        pos = Position(x, yt)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(x, yt)
          self._positions.append(pos)
        break
      yt = yt + 1


#fim movimentacao rainha


#movimentacao rei
class King(Part):
  _mark_white = "♔"
  _mark_black = "♚"

  def __init__(self, color):
    Part.__init__(self, "King", color)

  def recalc(self, board, x, y):
    #print(self._name, x, y)

    self._positions = []
    # Movimentos possíveis do rei
    possible_moves = [
         (x - 1, y),  # cima
        (x + 1, y),  # baixo
        (x, y - 1),  # esquerda
        (x, y + 1),  # direita
        (x - 1, y - 1),  # diagonal cima-esquerda
        (x - 1, y + 1),  # diagonal cima-direita
        (x + 1, y - 1),  # diagonal baixo-esquerda
        (x + 1, y + 1)  # diagonal baixo-direita
    ]

    for move in possible_moves:
      xt, yt = move
      if 0 <= xt <= 7 and 0 <= yt <= 7:
        part = board.get_peca(xt, yt)
        if part is None or part._color != self._color:
          pos = Position(xt, yt)
          self._positions.append(pos)


#fim movimentacao rei


class Bishop(Part):
  _mark_white = "♗"
  _mark_black = "♝"

  def __init__(self, color):
    Part.__init__(self, "Bispo", color)

  def recalc(self, board, x, y):
    #validar se esta é a lógica
    self._positions = []

    #diagonal cima esquerda
    bx = x - 1
    by = y - 1
    while (bx >= 0 and by >= 0):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx - 1
      by = by - 1
    #diagonal baixo esquerda
    bx = x - 1
    by = y + 1
    while (bx >= 0 and by <= 7):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx - 1
      by = by + 1

    #diagonal cima direita
    bx = x + 1
    by = y - 1
    while (bx <= 7 and by >= 0):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx + 1
      by = by - 1

    #diagonal cima esquerda
    bx = x + 1
    by = y + 1
    while (bx <= 7 and by <= 7):
      part = board.get_peca(bx, by)
      if (part is None):
        pos = Position(bx, by)
        self._positions.append(pos)
      else:
        if (part._color == self._color):
          break
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(bx, by)
          self._positions.append(pos)
        break
      bx = bx + 1
      by = by - 1


#for p in self._positions:
#  print(str(p))


class Rock(Part):
  _mark_white = "♖"
  _mark_black = "♜"

  def __init__(self, color):
    Part.__init__(self, "Rock", color)

  def recalc(self, board, x, y):

    #print(self._name, x, y)

    self._positions = []
    #movimento cima
    xt = x - 1
    while (xt >= 0):
      part = board.get_peca(xt, y)
      if (part is None):
        pos = Position(xt, y)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(xt, y)
          self._positions.append(pos)
        break
      xt = xt - 1
    #motivmento baixo
    xt = x + 1
    while (xt <= 7):
      part = board.get_peca(xt, y)
      if (part is None):
        pos = Position(xt, y)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(xt, y)
          self._positions.append(pos)
        break
      xt = xt + 1
    #movimento esquerda
    yt = y - 1
    while (yt >= 0):
      part = board.get_peca(x, yt)
      if (part is None):
        pos = Position(x, yt)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(x, yt)
          self._positions.append(pos)
        break
      yt = yt - 1
    #movimento direita
    yt = y + 1
    while (yt <= 7):
      part = board.get_peca(x, yt)
      if (part is None):
        pos = Position(x, yt)
        self._positions.append(pos)
      else:
        # peca de cores diferentes
        if (part._color != self._color):
          pos = Position(x, yt)
          self._positions.append(pos)
        break
      yt = yt + 1

    #for p in self._positions:
    #  print(str(p))


class Pawn(Part):
  _mark_white = "♙"
  _mark_black = "♟"
  _positions = []
  _first_move = True

  def __init__(self, color):
    Part.__init__(self, "Peão", color)
    self._positions = []

    self._last_x = None
    self._last_y = None

  def recalc(self, board, x, y):

    # verifica se a peça já foi jogada e desabilita
    # jogada de dois saltos
    if (self._last_x not in [None, x] or self._last_y not in [None, y]):
      self._first_move = False

    self._positions = []

    # encontra movimento de saída com 1 salto
    dy = (y - 1) if self._color == Color.WHITE else (y + 1)
    part = board.get_peca(x, dy)
    if (part is None):
      self._positions.append(Position(x, dy))

    # encontra movimento de saída com 2 saltos
    # (apenas se peça não foi tocada ainda)
    if (self._first_move):
      dy = (y - 2) if self._color == Color.WHITE else (y + 2)
      part = board.get_peca(x, dy)
      if (part is None):
        self._positions.append(Position(x, dy))

    #TODO: calcular jogadas de captura na diagonal
    if (self._color == Color.WHITE
        and (board.get_peca(x - 1, y - 1) is not None
             and board.get_peca(x - 1, y - 1)._color != self._color)):
      self._positions.append(Position(x - 1, y - 1))

    if (self._color == Color.WHITE
        and (board.get_peca(x + 1, y - 1) is not None
             and board.get_peca(x + 1, y - 1)._color != self._color)):
      self._positions.append(Position(x + 1, y - 1))

    if (self._color == Color.WHITE
        and (board.get_peca(x + 1, y + 1) is not None
             and board.get_peca(x + 1, y + 1)._color != self._color)):
      self._positions.append(Position(x + 1, y + 1))

    if (self._color == Color.WHITE
        and (board.get_peca(x - 1, y + 1) is not None
             and board.get_peca(x - 1, y + 1)._color != self._color)):
      self._positions.append(Position(x - 1, y + 1))

    # TODO: calcular jogadas de captura en pasant
    if (board.get_peca(x + 1, y) is not None
        and (self._color == Color.WHITE and board.get_peca(x + 1, y)._name
             == "Peão" and board.get_peca(x + 1, y)._color != self._color
             and board.get_peca(x + 1, y)._first_move)):
      self._positions.append(Position(x + 1, y - 1))

    if (board.get_peca(x - 1, y) is not None
        and (self._color == Color.WHITE and board.get_peca(x - 1, y)._name
             == "Peão" and board.get_peca(x - 1, y)._color != self._color
             and board.get_peca(x - 1, y)._first_move)):
      self._positions.append(Position(x - 1, y - 1))

    if (board.get_peca(x + 1, y) is not None
        and (self._color == Color.BLACK and board.get_peca(x + 1, y)._name
             == "Peão" and board.get_peca(x + 1, y)._color != self._color
             and board.get_peca(x + 1, y)._first_move)):
      self._positions.append(Position(x + 1, y + 1))

    if (board.get_peca(x - 1, y) is not None
        and (self._color == Color.BLACK and board.get_peca(x - 1, y)._name
             == "Peão" and board.get_peca(x - 1, y)._color != self._color
             and board.get_peca(x - 1, y)._first_move)):
      self._positions.append(Position(x - 1, y + 1))
