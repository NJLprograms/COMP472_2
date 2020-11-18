from Puzzle import Puzzle

def inCorrectRow(item: str, currentIndex: int):
  """

  Returns boolean
  """
  correctIndex = int(item) - 1
  if item == Puzzle.EMPTY_SLOT:
    correctIndex = 7
  
  if correctIndex < 4:
    # Upper row
    # Returns true if in upper row
    return currentIndex < 4
  elif correctIndex >= 4:
    return currentIndex >= 4

def inCorrectColumn(item: str, currentIndex: int):
  """

  Returns boolean
  """
  correctIndex = int(item) - 1 # 4
  if item == Puzzle.EMPTY_SLOT:
    correctIndex = 7

  if correctIndex >= 4:
    return currentIndex == correctIndex or currentIndex == correctIndex - 4
  else:
    return currentIndex == correctIndex or currentIndex == correctIndex + 4

    

def h1(puzzle: Puzzle):
  """ Heuristic #1
  
  Returns the number of tiles out of row + number of tiles out of column
  """
  count = 0
  for item, index in puzzle.getPuzzle().items():
    if not inCorrectRow(item, index):
      count += 1

    if not inCorrectColumn(item, index):
      count += 1

  return count

def h2(puzzle: Puzzle):
  print