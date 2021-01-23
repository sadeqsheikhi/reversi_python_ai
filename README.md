# Reversi(othello) Implementation in Python With AI Apponent
the code is implemented in python flask web framework


## Description Of Modules:
#### reversi.py
the rule of the Othello game and methods that need it.

#### AIHelper.py
Helper interfface class for the AI

        $1. available moves (board, player)
        $2. get_resulting_board -> (board, player, coord)
        $3. player pools (board, player)
        $4. check if game has ended (board

#### reversiai.py
AI algoritim and heuristics

        $1. get next move ( board, player)
        $2. minimax algorotim (board, depth, player)
        $3. game heuristic (board)

#### server.py
UI of project is write in the Flask framework, so you can start the project with this file.

#### tests_worked.py
This File Is For Unit Testing different components of the application.

#### Satic Directory
This Directory Static file for the UI 

## Algorithm
In the mathematical area of game theory, a minimax theorem is a theorem providing conditions that guarantee that the max–min inequality is also an equality. The first theorem in this sense is von Neumann's minimax theorem from 1928, which was considered the starting point of game theory. Since then, several generalizations and alternative versions of von Neumann's original theorem have appeared in the literature [link](https://en.wikipedia.org/wiki/Minimax_theorem)

## Heuristic function
Games like Othello, which have proven to fit in well with computer game playing strategies, have spawned a lot of research in this direction. Though numerous computer Othello players have been designed, and have beaten human world champions, it is not very clear as to how the various Othello heuristics interact.  This paper implements and examines various heuristics, in an attempt to make observations about the interplay  between  the  heuristics,  and  how  well  each heuristic contributes as a whole.  Identifying heuristics that contribute immensely to Othello game-play implies that more processor cycles could be allocated in that direction to enhance the quality of play.  Due to the complexity of accurate calculations, most heuristics tend to approximate. Like a typical stability heuristic, that approximates stability, instead of accurately calculating it. By realizing the importance of the stability heuristic, it enables one to decide the amount of time to spend in such a function. [link](https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf)

## what are the dependencies:
install flask and uuid packages first and then run server.py file
` $ pip install Flask uuid `
## RUN
` $ python server.py `

## License

MIT 2021
