import time
from Puzzle import Puzzle

def UCS(puzzle: Puzzle):
  """ UCS(puzzle: Puzzle)

  Runs a uniform cost search on a Puzzle
  """

  open_list = []
  open_list.append(puzzle)

  closed_list = []

  currentNode = puzzle

  solution = open("0_ucs_solutions.txt", "a")
  solution.write("0 0 "+str(currentNode)+"\n")
  start_time = time.time()

  while bool(open_list):
    if len(open_list) == 0:
        raise Exception('Failure: Open list is empty and no solution was found.')
        return

    if currentNode.isGoalState():
      return currentNode

    possibleMoves = currentNode.getPossibleMoves() # e.g. [Move.UP, Move.Left, Move.Right]

    nodes = [currentNode.copy().move(move) for move in possibleMoves] # list of nodes after applied possible moves
    sorted_nodes = sorted(nodes, key=lambda node: node.cost) # same list, sorted based on move cost
    open_list.remove(currentNode)
    closed_list.append(currentNode)
    open_list = sorted([*sorted_nodes, *open_list], key=lambda node: node.cost)

    currentNode = open_list[0]
    solution.write(str(currentNode.tile)+" "+str(Puzzle.getMoveCost(currentNode))+" "+str(currentNode)+"\n")

  solution.write(str(currentNode.cost)+" "+str(time.time() - start_time))
  solution.close()




