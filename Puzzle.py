from typing import Final
import Moves
import Cost

class Puzzle:
  GOAL_STATE: Final = "1 2 3 4 5 6 7 0"
  GOAL_STATE_ODD: Final = "1 3 5 7 2 4 6 0"
  GOAL_PUZZLE_MAP: Final = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '0': 7}
  GOAL_PUZZLE_MAP_ODD: Final = {'1': 0, '3': 1, '5': 2, '7': 3, '2': 4, '4': 5, '6': 6, '0': 7}
  VERTICAL_SHIFT: Final = 4
  EMPTY_SLOT: Final = '0'
  TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT = 0,3,4,7

  def __init__(self, puzzle, cost=0, lastMove=None):
    """ The Puzzle class: Puzzle()
    
    This class defines the Puzzle entity. The constructor accepts a input string of the puzzle.

    Example: "1 2 3 4 5 6 7 0"
    """
    super().__init__()

    # transforms the puzzle string to a puzzle dictionary with index as value
    puzzle = puzzle.split()
    puzzleMap = {}
    for index, value in enumerate(puzzle):
      puzzleMap[value] = index
    #

    self.height = 0
    self.lastAppliedMove = None
    self.puzzle = puzzleMap
    self.cost = cost
    self.lastMove = lastMove

    
    
  def getPuzzle(self):
    """ getPuzzle(): Dict

    Returns the Puzzle in the form of a dictionary
    """
    return self.puzzle

  def isGoalState(self):
    """ isGoalState(): Boolean

    Returns True if this instance's puzzle dictionary is the goal state
    """
    return self.puzzle == Puzzle.GOAL_PUZZLE_MAP or self.puzzle == Puzzle.GOAL_PUZZLE_MAP_ODD

  def get(self, index: int):
    """ get(index: int): String

    Returns the value at the specified index
    """
    for key, value in self.puzzle.items():
      if value == index:
        return key

  def getIndexOf(self, item: str):
    """ getIndexOf(item: String): int

    Returns the index of the specified item
    """
    return self.puzzle[item]

  def swap(self, item1: str, item2: str):
    """ swap(item1: String, item2: String): void

    Swap the values of the two specified keys in the puzzle Dict
    """
    temp = self.puzzle[item1]
    self.puzzle[item1] = self.puzzle[item2]
    self.puzzle[item2] = temp
    return

  def regularMove(self, move: Moves.Move):
    """ regularMove(move: Move)

    Performs a regular move that is described by the enum value passed in.
    (e.g. puzzle.regularMove(Move.UP) will move the corresponding piece up into
    the empty slot.) 
    """
    emptySlotIndex = self.getIndexOf(Puzzle.EMPTY_SLOT)
    indexOfItemToMove = self.getIndexOf(Puzzle.EMPTY_SLOT) # Initial placeholder

    if move.name == Moves.Move.UP.name:
      indexOfItemToMove = emptySlotIndex + Puzzle.VERTICAL_SHIFT
    elif move.name == Moves.Move.DOWN.name:
      indexOfItemToMove = emptySlotIndex - Puzzle.VERTICAL_SHIFT
    elif move.name == Moves.Move.LEFT.name:
      indexOfItemToMove = emptySlotIndex + 1
    elif move.name == Moves.Move.RIGHT.name:
      indexOfItemToMove = emptySlotIndex - 1
    else:
      raise Exception('Illegal parameter. Must provide a regular move enum.')
      return


    self.swap(Puzzle.EMPTY_SLOT, self.get(indexOfItemToMove))
    self.cost += Cost.REGULAR

  def moveDiagonal(self):
    emptySlotIndex = self.getIndexOf(Puzzle.EMPTY_SLOT)

    if emptySlotIndex == Puzzle.TOP_LEFT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(5))
    elif emptySlotIndex == Puzzle.TOP_RIGHT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(6))
    elif emptySlotIndex == Puzzle.BOTTOM_LEFT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(1))
    elif emptySlotIndex == Puzzle.BOTTOM_RIGHT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(2))
    else:
      raise Exception('Empty slot not @ corner position. Illegal move.')
      return

    self.cost += Cost.DIAGONAL

  def moveDiagonalWrap(self):
    emptySlotIndex = self.getIndexOf(Puzzle.EMPTY_SLOT)

    if emptySlotIndex == Puzzle.TOP_LEFT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(7))
    elif emptySlotIndex == Puzzle.TOP_RIGHT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(4))
    elif emptySlotIndex == Puzzle.BOTTOM_LEFT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(3))
    elif emptySlotIndex == Puzzle.BOTTOM_RIGHT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(0))
    else:
      raise Exception('Empty slot not @ corner position. Illegal move.')
      return

    self.cost += Cost.DIAGONAL

  def wrapLeft(self):
    emptySlotIndex = self.getIndexOf(Puzzle.EMPTY_SLOT)

    if emptySlotIndex == Puzzle.TOP_RIGHT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(Puzzle.TOP_LEFT))
    elif emptySlotIndex == Puzzle.BOTTOM_RIGHT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(Puzzle.BOTTOM_LEFT))
    else:
      raise Exception('Cannot wrap left, invalid position.')
      return

    self.cost += Cost.WRAP

  def wrapRight(self):
    emptySlotIndex = self.getIndexOf(Puzzle.EMPTY_SLOT)

    if emptySlotIndex == Puzzle.TOP_LEFT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(Puzzle.TOP_RIGHT))
    elif emptySlotIndex == Puzzle.BOTTOM_LEFT:
      self.swap(Puzzle.EMPTY_SLOT, self.get(Puzzle.BOTTOM_RIGHT))
    else:
      raise Exception('Cannot wrap right, invalid position.')
      return

    self.cost += Cost.WRAP

  def move(self, move: Moves.Move):
    self.lastAppliedMove = move
    
    if move.name == Moves.Move.UP.name or move.name == Moves.Move.DOWN.name or move.name == Moves.Move.LEFT.name or move.name == Moves.Move.RIGHT.name:
      self.regularMove(move)
      self.lastMove = "regular"
    elif move.name == Moves.Move.WRAP_LEFT.name:
      self.wrapLeft()
      self.lastMove = "wrapping"
    elif move.name == Moves.Move.WRAP_RIGHT.name:
      self.wrapRight()
      self.lastMove = "wrapping"
    elif move.name == Moves.Move.DIAGONAL.name:
      self.moveDiagonal()
      self.lastMove = "diagonal"
    elif move.name == Moves.Move.DIAG_WRAP.name:
      self.moveDiagonalWrap()
      self.lastMove = "diagonal"

    return self

  def getPossibleMoves(self):
    indexOfEmptySlot = self.getIndexOf(Puzzle.EMPTY_SLOT)
    return Moves.moves[indexOfEmptySlot]

  def hasEmptyCornerSlot(self):
    """ hasEmptyCornerSlot()

    Returns True if the empty slot is in a corner position
    """
    emptySlot = self.getIndexOf(Puzzle.EMPTY_SLOT)
    return emptySlot == Puzzle.BOTTOM_LEFT or emptySlot == Puzzle.BOTTOM_RIGHT or emptySlot == Puzzle.TOP_LEFT or emptySlot == Puzzle.TOP_RIGHT

  def getPuzzleStringForm(self):
    """ getPuzzleStringForm()

    Returns the string form of the puzzle. For example,
    _________
    |0 1 2 3 |
    |4 5 6 7 |
    ---------
    will return "0 1 2 3 4 5 6 7"
    """
    sortedPuzzleDictByIndex = {value: index for value, index in sorted(self.getPuzzle().items(), key=lambda item: item[1])}
    puzzleStringForm = ""
    for value in sortedPuzzleDictByIndex.keys():
      puzzleStringForm += (value + " ")
    
    return puzzleStringForm.rstrip()

  def __str__(self):
    return self.getPuzzleStringForm()

  def copy(self):
    return Puzzle(str(self), self.cost)

  def getMoves(self):
    if self.lastMove == "regular":
      return Cost.REGULAR
    if self.lastMove == "wrapping":
      return Cost.WRAP
    if self.lastMove == "diagonal":
      return Cost.DIAGONAL

