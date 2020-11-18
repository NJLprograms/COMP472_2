from aenum import Enum, NoAlias
import Cost

# aenum supports same valued enumerations without aliasing those with the same value

class Move(Enum):

  _settings_ = NoAlias

  UP = Cost.REGULAR
  DOWN = Cost.REGULAR
  LEFT = Cost.REGULAR
  RIGHT = Cost.REGULAR
  WRAP_LEFT = Cost.WRAP
  WRAP_RIGHT = Cost.WRAP
  DIAGONAL = Cost.DIAGONAL
  DIAG_WRAP = Cost.DIAGONAL

# Possible moves for empty slot at each index
moves = {
  0: [Move.UP, Move.LEFT, Move.WRAP_RIGHT, Move.DIAGONAL, Move.DIAG_WRAP],
  1: [Move.UP, Move.LEFT, Move.RIGHT],
  2: [Move.UP, Move.LEFT, Move.RIGHT],
  3: [Move.UP, Move.RIGHT, Move.WRAP_LEFT, Move.DIAGONAL, Move.DIAG_WRAP],
  4: [Move.DOWN, Move.LEFT, Move.WRAP_RIGHT, Move.DIAGONAL, Move.DIAG_WRAP],
  5: [Move.DOWN, Move.LEFT, Move.RIGHT],
  6: [Move.DOWN, Move.LEFT, Move.RIGHT],
  7: [Move.DOWN, Move.RIGHT, Move.WRAP_LEFT, Move.DIAGONAL, Move.DIAG_WRAP]
}