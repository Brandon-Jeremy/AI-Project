# AI-Project
Phase 1
Documentation: 
Q1) DFS
The algorithm starts by setting up a stack called a fringe with the starting node as the only element. The algorithm then enters a loop that continues
until either the fringe is empty or a goal state is found. In each iteration of the loop, the algorithm takes the last node in the fringe and generates
its successors. For each successor, the algorithm checks if it is the goal state. If it is, it returns the path from the initial state to the goal state.
Otherwise, it adds the successor to the fringe and the path to that successor to a list called listOfPaths. At the end of each iteration, the algorithm
updates the current path to the next path in the listOfPaths. The algorithm repeats this process until either the fringe is empty or a goal state is found.
If the fringe becomes empty before a goal state is found, the algorithm returns an empty path.

Q3) UCS
The uniformCostSearch function searches for the optimal path from the start state to the goal state, where each action has a cost associated with it.
It does this by maintaining a priority queue of nodes to be explored, where the priority is given to the node with the lowest cost so far. It also maintains
a lookup table of nodes that have been explored already. At each step, it takes the node with the lowest cost from the frontier and checks if it is the goal
state. If it is, it returns the path taken to reach this state. If it is not, it adds the node to the lookup table and generates its successors.
For each successor, it computes the cost of the path to get there and if the successor has not been explored yet or if the cost to get to the successor is lower
than the cost already known, it adds the successor to the frontier with the new cost and updates the path to the successor in the listOfPaths.
The algorithm continues until either the frontier is empty (in which case it returns failure) or the goal state is found.

Q7) Eating All the Dots
The function foodHeuristic is used to estimate the cost to reach the goal state in the FoodSearchProblem. The goal of the FoodSearchProblem is
for Pacman to eat all the food in the grid. The function calculates the farthest distance from Pacman's current position to any food dot in the grid, which
Pacman will eat last. The distance is estimated using the mazeDistance function, which calculates the shortest distance through the maze from Pacman's current
position to each food dot. If the distance from Pacman's current position to a food dot has been previously computed, the function retrieves the value from
the problem.heuristicInfo dictionary. If not, the function computes the distance and stores it in the problem.heuristicInfo dictionary for future use.
The estimated cost returned by this function is used by the A* search algorithm to guide the search towards the goal state.

Q8) Suboptimal Search
The function findPathToClosestDot finds the path to the closest dot (food pellet) from the current position of Pacman in a Pacman game. It takes in the current
game state and extracts useful information like Pacman's starting position, the location of food pellets, and the walls in the game.
It then creates an instance of the AnyFoodSearchProblem class using the current game state and uses Breadth First Search (BFS) to find the shortest
path to the closest food pellet. Finally, it returns the path obtained from BFS which will be a list of actions that Pacman needs to take in order
to reach the closest food pellet.
The function isGoalState is used to determine if the current state of Pacman is a goal state or not. The input parameter is Pacman's current position.
The function checks whether Pacman is currently on a food dot. If Pacman's current position is on a food dot, then the function returns True, indicating
that Pacman has achieved the goal state. Otherwise, the function returns False, indicating that Pacman needs to move to a different position to reach a food
dot and achieve the goal state.

