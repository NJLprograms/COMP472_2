from Puzzle import Puzzle

def indexToCoordinates(index):
  y = 0
  x = 0

  if index > 3 and index < 8:
    y = 1
    x = index - 4
  elif index >= 0 and index <=3:
    y = 0
    x = index
  else:
    raise Exception('number must be between 0-8')

  return {'y': y, 'x': x}


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
  tiles = puzzle.getPuzzle()

  manhattan_distance = 0
  for tile, index in tiles.items():
    correctIndex = int(tile) - 1

    if tile == Puzzle.EMPTY_SLOT:
      correctIndex = 7
    
    coordinate1 = indexToCoordinates(correctIndex)
    coordinate2 = indexToCoordinates(index)

    coordinates = {'y': coordinate1['y'] - coordinate2['y'], 'x': coordinate1['x'] - coordinate2['x']}
    manhattan_distance += coordinates['y']**2 + coordinates['x']**2

  return manhattan_distance



    

    