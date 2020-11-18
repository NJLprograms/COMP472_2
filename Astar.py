from Puzzle import Puzzle
from heuristic import h1, h2

def Astar(puzzle: Puzzle, heuristic=h1):
  """ Astar(puzzle: Puzzle)

  Runs an A* algorithm on a Puzzle
  """

  path = []

  open_list = []
  open_list.append(puzzle)

  closed_list = []

  currentNode = puzzle

  while bool(open_list):
    if len(open_list) == 0:
      raise Exception('Failure: Open list is empty and no solution was found.')
      return

    if currentNode.isGoalState():
      return currentNode

    ### Step: Remove node n with the smallest h(n) from open list and place n in closed list
    possibleMoves = currentNode.getPossibleMoves() # e.g. [Move.UP, Move.Left, Move.Right]

    nodes = [currentNode.copy().move(move) for move in possibleMoves] # list of nodes after applied possible moves
    sorted_nodes = sorted(nodes, key=lambda node: heuristic(node) + node.cost) # same list, sorted based on heuristic

    # Increment the height for newly discovered node in the state tree
    for node in nodes:
      node.height += 1

    open_list.remove(currentNode)
    closed_list.append(currentNode)

    open_list = sorted([*sorted_nodes, *open_list], key=lambda node: h1(node) + node.cost)
    currentNode = open_list[0]

    # # insert the node at each respective height. Previous ones at the same height get replaced if there was backtracking
    # try: 
    #   path[currentNode.height] = currentNode.lastAppliedMove.name
    # except:
    #   path.insert(currentNode.height, currentNode.lastAppliedMove.name)
  
  return currentNode
