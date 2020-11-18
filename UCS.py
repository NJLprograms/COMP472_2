
from Puzzle import Puzzle

def UCS(puzzle: Puzzle):
    """ UCS(puzzle: Puzzle)

  Runs a uniform cost search on a Puzzle
  """

    openList = {}
    openList[str(puzzle)] = puzzle

    closedList = {}

    currentNode = puzzle

    while bool(openList):
        print(str(currentNode))
        if len(openList) == 0:
            raise Exception('Failure: Open list is empty and no solution was found.')
        return

    if currentNode.isGoalState():
      return currentNode

    if str(currentNode) in closedList:
      raise Exception('No solution found. State ' + str(currentNode) + ' is in the closed list.')

    ### Step: Remove node n with the smallest h(n) from open list and place n in closed list
    possibleMoves = currentNode.getPossibleMoves() # e.g. [Move.UP, Move.Left, Move.Right]

    nodes = [currentNode.copy().move(move) for move in possibleMoves] # list of nodes after applied possible moves
    
    # Remove successor nodes which have already been visited
    for node in nodes:
      if str(node) in closedList:
        nodes.remove(node)
    # Remove duplicates

    nodes = sorted(nodes, key=lambda node: node.cost) # same list, sorted based on move cost

    for node in nodes:
      openList[str(node)] = node

    del openList[str(currentNode)]
    closedList[str(currentNode)] = currentNode
    ### Step done

    # currentNode points to puzzle deep copy with lowest h(n)
    currentNode = openList[next(iter(openList))]
  
    return str(currentNode)




