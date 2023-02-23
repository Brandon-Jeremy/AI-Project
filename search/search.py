# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    Node = problem.getStartState()
    fringe = Stack()
    fringe.push(Node)
    path = []
    visited = [] #holds the nodes we have already visited to prevent visitng them again
    listOfPaths = Stack() #holds the paths taken to reach a certain node
        
    while not fringe.isEmpty():
        node = fringe.pop()
        if problem.isGoalState(node): #checks if this is the goal state
            return path #if yes it returns how to reached this goal state
        for successor,action,cost in problem.getSuccessors(node):
            if problem.isGoalState(successor):
                correctPath = path + [action]
                return correctPath
            if successor not in visited:
                visited.append(successor)
                fringe.push(successor)
                newPath = path + [action]
                listOfPaths.push(newPath)
        path = listOfPaths.pop() 
        
    return [] #return no action (failure)
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    
    Node = problem.getStartState()

    #Check if initial state is goal state
    if(problem.isGoalState(Node)):
        #Return no action since current node is goal so pacman doesn't need to move
        return []
    else:
        #setting up the environment that the search strategy will use
        #Initialize fringe to be the starting unvisited node
        fringe = Queue()
        fringe.push(problem.getStartState())
        
        #Setting up path and reached lists
        path = []
        reached = []
        reached.append(problem.getStartState())

        listOfPaths = Queue()
        #Queue of lists that will hold the path to every node generated
        #Any tume a node gets generated that leads to a new path, it will
        #get added to this list of paths as a new path that the agent can take
        #The last path [-1] should in theory be the final path with the
        #goal state being the last generated node
        
        while not fringe.isEmpty():
            node = fringe.pop()
            for successor,action,cost in problem.getSuccessors(node):
                if problem.isGoalState(successor):
                    correctPath = path + [action]
                    return correctPath
                if successor not in reached:
                    reached.append(successor)
                    fringe.push(successor)
                    newPath = path + [action]
                    listOfPaths.push(newPath)
            path = listOfPaths.pop()

    return []
    #In event of failure, return nothing
    util.raiseNotDefined()
    #Code also works for the 8-tile problem

def uniformCostSearch(problem: SearchProblem):
    from util import PriorityQueue,Queue

    Node = problem.getStartState()
    frontier = PriorityQueue() # ←a priority queue ordered by f , with node as an element
    frontier.push(Node, 0)
    reached = [] # ←a lookup table, with one entry with key problem.INITIAL and value node
    path = []

    listOfPaths = PriorityQueue()
    #I need a way to store all the paths taken by every expanded node. So I will use another priorityQ
    #That will store the paths instead of a node state
    listOfPaths.push(path,0)

    while not frontier.isEmpty():
        #While the frontier is not empty
        Node = frontier.pop()
        currentPath = listOfPaths.pop()
        #Pop a node from the frontier (this node will have the least cost)
        #Pop its respective path
        if problem.isGoalState(Node):
            return currentPath
        if Node not in reached:
            reached.append(Node)
            for child,action,cost in problem.getSuccessors(Node):
                childPath = currentPath + [action]
                childCost = problem.getCostOfActions(childPath)
                if (child not in reached) or (problem.getCostOfActions(childPath)<problem.getCostOfActions(currentPath)):
                    frontier.push(child, childCost)
                    listOfPaths.push(childPath, childCost)
    
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #Pseudocode source: Artificial Intelligence: a Modern Approach, EBook, Global Edition
    #Page 91

    #Setting up the environment for A*

    from util import PriorityQueue
    from util import Queue

    Node = problem.getStartState()
    frontier = PriorityQueue() # ←a priority queue ordered by f , with node as an element
    frontier.push(Node, 0+heuristic(Node,problem))
    #Why 0+nullHeuristic(Node,problem)? 
    #A* works based off f(n)=g(n)+h(n) && g(n) at the root = 0
    reached = [] # ←a lookup table, with one entry with key problem.INITIAL and value node
    path = []

    listOfPaths = PriorityQueue()
    #I need a way to store all the paths taken by every expanded node. So I will use another priorityQ
    #That will store the paths instead of a node state
    listOfPaths.push(path,0+heuristic(Node,problem))

    while not frontier.isEmpty():
        #While the frontier is not empty
        Node = frontier.pop()
        currentPath = listOfPaths.pop()
        #Pop a node from the frontier (this node will have the least cost)
        #Pop its respective path
        if problem.isGoalState(Node):
            return currentPath
        if Node not in reached:
            reached.append(Node)
            for child,action,cost in problem.getSuccessors(Node):
                childPath = currentPath + [action]
                childCost = problem.getCostOfActions(childPath) + heuristic(child,problem)
                if (child not in reached) or (problem.getCostOfActions(childPath)<problem.getCostOfActions(currentPath)):
                    frontier.push(child, childCost)
                    listOfPaths.push(childPath, childCost)
    
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
