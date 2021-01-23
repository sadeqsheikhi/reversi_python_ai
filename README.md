# Reversi(othello) Implementation in Python With AI Apponent

**Reversi Game** Implementation in the python with AI Apponent and Itractive **MinMax** algorithm.

INFO: the code is implemented in python flask web framework

## Description Of Modules:

filename        | Discription 
--------------- |-----------------------------------------------------------
`server.py`     | GUI of project is write in the Flask framework, so you can start the project with this file.             
`reversiai.py`  | AI algorithm and heuristics        
`reversi.py`    | implement the rule of Othello game and methods that need it.             
`aihelper.py`   | Helper interfface class for the AI                 
`tests_worked`  | This File Is For Unit Testing different components of the application                  
`static`        | This Directory contine                


## Algorithm
In the mathematical area of game theory, a minimax theorem is a theorem providing conditions that guarantee that the max–min inequality is also an equality. The first theorem in this sense is von Neumann's minimax theorem from 1928, which was considered the starting point of game theory. Since then, several generalizations and alternative versions of von Neumann's original theorem have appeared in the literature [link](https://en.wikipedia.org/wiki/Minimax_theorem)

## Heuristic function
This heuristic function is actually a collection of several heuristics and calculates the utility value of a board position by assigning different weights to those heuristics. These heuristics take into account the mobility, coin parity, stability and corners-captured aspects of a board configuration. Each heuristic scales its return value from -100 to 100. These values are weighed appropriately to play an optimal game. The various heuristics include:


1. Coin Parity
 
This component of the utility function captures the difference in coins between the max player and the min player. The return value is determined as follows :
```python
Coin Parity Heuristic Value =
	100 * (Max Player Coins - Min Player Coins ) / (Max Player Coins + Min Player Coins)
```

2. Mobility

It attempts to capture the relative difference between the number of possible moves for the max and the min players, with the intent of restricting the opponent’s mobility and increasing one’s own mobility. This value is calculated as follows :
``` python
if ( Max Player Moves + Min Player Moves != 0)
	Mobility Heuristic Value =
		100 * (Max Player Moves - Min Player Moves) / (Max Player Moves + Min Player Moves)
else
	Mobility Heuristic Value = 0
```

3. Corners Captured

Corners hold special importance because once captured, they cannot be flanked by the opponent. They also allow a player to build coins around them and provide stability to the player’s coins. This value is captured as follows :
``` python
if ( Max Player Corners + Min Player Corners != 0)
	Corner Heuristic Value =
		100 * (Max Player Corners - Min Player Corners) / (Max Player Corners + Min Player Corners)
else
	Corner Heuristic Value = 0
```

4. Stability

The stability measure of a coin is a quantitative representation of how vulnerable it is to being flanked. Coins can be classified as belonging to one of three categories: (i) stable, (ii) semi-stable and (iii) unstable.

Stable coins are coins which cannot be flanked at any point of time in the game from the given state. Unstable coins are those that could be flanked in the very next move. Semi-stable coins are those that could potentially be flanked at some point in the future, but they do not face the danger of being flanked immediately in the next move. Corners are always stable in nature, and by building upon corners, more coins become stable in the region.

Weights are associated to each of the three categories, and summed to give rise to a final stability value for the player. Typical weights could be 1 for stable coins, -1 for unstable coins and 0 for semi-stable coins.

The stability value is calculated as follows :
``` python
if ( Max Player Stability Value + Min Player Stability Value != 0)
	Stability  Heuristic Value =
		100 * (Max Player Stability Value - Min Player Stability Value) / (Max Player Stability Value + Min Player Stability Value)
else
	Stability Heuristic Value = 0
```
 [Reference](https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf)

## 

## what are the dependencies:
install flask and uuid packages first and then run server.py file
` $ pip install Flask uuid `
## RUN
` $ python server.py `

## License
MIT 2021
