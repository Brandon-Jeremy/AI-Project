# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        # mby these could be useful for new custom eval? 
        # successorGameState = currentGameState.generatePacmanSuccessor(action)
        # newPos = successorGameState.getPacmanPosition()
        # newFood = successorGameState.getFood()
        # newGhostStates = successorGameState.getGhostStates()
        # newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        def newUtil(gameState):
            position = gameState.getPacmanPosition()
            pellets = gameState.getFood().asList()

            nearestScaredGhost = float('inf')
            nearestPellet = float('inf')
            if pellets:
                for pellet in pellets:
                    distance = manhattanDistance(position, pellet)
                    if distance < nearestPellet:
                        nearestPellet = distance
            # for nst in newScaredTimes:
            #     if(nst>0):
            #         #ghost is scared here
            #         nearestScaredGhost=min(nearestScaredGhost,nst)


            score = gameState.getScore()

            # foodVal = 10
            # scaredval = 20 #test case vals
            #use new scared time here maybe to compute eval to chase ghost
            evaluation = 1.0 / nearestPellet + score
            #customeval with weights on remaining ghosts did not work, aim was to get pacman to chase ghosts when they are scared
            return evaluation

        # Determine the action that maximizes the expected utility for Pacman
        def max_utility(gameState, depth):
            if gameState.isWin():
                return newUtil(gameState)
            if gameState.isLose():
                return newUtil(gameState)
            if (depth+1) == self.depth: #testing needs to be done with different values. 3 is very slow, might be worse in the lab
                return newUtil(gameState)
            #These conditions are used to check if the game is in its final stage 
            #The game can conlcude in 3 different ways, either winning, losing or when the depth 
            #is higher than the specified depth designated in the multiAgent code.

            max_value = float('-inf')
            pacman_actions = gameState.getLegalActions(0)
            #List of pacman actions stored to loop through and check which would yield a better outcome
            for action in pacman_actions:
                successor_state = gameState.generateSuccessor(0, action)
                current_expectation = min_utility(successor_state, depth+1, 1)
                # Update max_value if the expected value is greater
                max_value = max(max_value, current_expectation)
            return max_value

        # Determine the minimum expected utility for the ghosts
        def min_utility(gameState, depth, agent_index):
            if gameState.isWin():
                return newUtil(gameState)
            if gameState.isLose():
                return newUtil(gameState)
            actions = gameState.getLegalActions(agent_index)
            max_expectation = 0
            #try to emulate chance node here but it won't really work without having real values to comfortably assume prob for each state
            num_actions = len(actions)
            for action in actions:
                successor_state = gameState.generateSuccessor(agent_index, action)
                if agent_index == (gameState.getNumAgents() - 1):
                    current_expectation = max_utility(successor_state, depth)
                else:
                    current_expectation = min_utility(successor_state, depth, agent_index + 1)
                max_expectation += current_expectation
            if num_actions == 0:
                return 0
            return (max_expectation+0.0) / (num_actions+0.0)


        # Get the legal actions for the root node
        actions = gameState.getLegalActions(0)

        # Initialize variables for the best action and its expected utility
        best_action = None
        best_score = float('-inf')

#
        # Evaluate each action and choose the one with the highest expected utility
        for action in actions:
            # Generate the successor state for the current action
            successor_state = gameState.generateSuccessor(0, action)
            # Compute the expected utility of the successor state using min_utility
            score = min_utility(successor_state, 0, 1)
            # Update the best action and its expected utility if necessary
            if score > best_score:
                best_action = action
                best_score = score

        # Return the best action based off nesw&stop vals. Should be a string so if best_action fails here it cud be bc of that
        #none val shouldn't cause an issue though
        return best_action


        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: Similar idea to phase 1 where manhattan distance is used as the heuristic for picking the closest food for the pacman to eat
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
