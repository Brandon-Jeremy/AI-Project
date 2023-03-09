# AI-Project
Phase 1
Documentation:

<h1>Q1 - DFS:</h1>
The algorithm starts by setting up a stack called a fringe with the starting node as the only element. The algorithm then enters a loop that continues
until either the fringe is empty or a goal state is found. In each iteration of the loop, the algorithm takes the last node in the fringe and generates
its successors. For each successor, the algorithm checks if it is the goal state. If it is, it returns the path from the initial state to the goal state.
Otherwise, it adds the successor to the fringe and the path to that successor to a list called listOfPaths. At the end of each iteration, the algorithm
updates the current path to the next path in the listOfPaths. The algorithm repeats this process until either the fringe is empty or a goal state is found.
If the fringe becomes empty before a goal state is found, the algorithm returns an empty path.

<h1>Q2 - BFS:</h1>
BFS starts off by an early goal check to ensure that we are not already on the goal state. If not, we set up all data structures we need such as a listofpaths queue and a fringe queue that work in unison to check if the node we are expanding leads to the correct path. In every node we check, we are also storing in parallel, the path we took to get there. That way, when we deqeue, we also obtain the correct path for the respective node. Additionally, an early goal check is done for the node after expansion.
<h1>Q3 - UCS:</h1>
The uniformCostSearch function searches for the optimal path from the start state to the goal state, where each action has a cost associated with it.
It does this by maintaining a priority queue of nodes to be explored, where the priority is given to the node with the lowest cost so far. It also maintains
a lookup table of nodes that have been explored already. At each step, it takes the node with the lowest cost from the frontier and checks if it is the goal
state. If it is, it returns the path taken to reach this state. If it is not, it adds the node to the lookup table and generates its successors.
For each successor, it computes the cost of the path to get there and if the successor has not been explored yet or if the cost to get to the successor is lower
than the cost already known, it adds the successor to the frontier with the new cost and updates the path to the successor in the listOfPaths.
The algorithm continues until either the frontier is empty (in which case it returns failure) or the goal state is found.

<h1>Q4 - A*:</h1>
A* uses the same logic as that found in UCS. The difference here is that the A* algorithm uses a heuristic to enhance the computation to find a short path to the goal state. Having said that, A* uses the concept of storing nodes and their respective path costs along with the heuristic added to the priority queue. Dequeue the node with the lowest priority queue as the data structure is initially setup to be a min heap to do just that. The goal check is done after popping/dequeuing each node from the priority queue.

<h1>Q5 - Corners Problem:</h1>
To solve the corners problem, we first need to change the initializer. According to the outputs from the problems 1-4 the state state returned must be in a certain format which we decided to follow for the following problem. The state is stored by storing in a tuple the starting position along with a list containing the corners which is initially empty [].
To check the goalstate, we simply check the node that we are currently at and see if it belongs to one of the 4 corners of the maze. If it isn't, move on otherwise check if it's been added to the tuple's list of corners. If not, add it otherwise move on. Finally check if the size of the list if 4 (4 being the max corners in a maze) then return true len==4.
To get successors, we follow the logic of the code provided to us and simpy check if the boolean of the .walls[][] returns true or not. If not, then the action is a valid one and we can return it as part of the successors. To do this we simply check if that successor is a corner and if so, append it to the list of corners for the successors. Finally return the successor.

<h1>Q6 - cornersHeuristics:</h1>
The corner heuristic simply uses the manhattanDistance from the util.py file in order to find the maxDistance. The reason max was chosen since it provides a closer approximation to the true cost.

<h1>Q7 - Eating All the Dots:</h1>
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

