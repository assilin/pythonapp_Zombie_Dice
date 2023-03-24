# Zombie Dice
#### Video Demo: <https://youtu.be/aM_h5PCMNd8>
#### Description:
This project is based on popular board game **Zombie Dice** by Steve Jackson.
I hope you're familiar with this game, but you can check the rules [here](http://www.sjgames.com/dice/zombiedice/img/ZDRules_English.pdf), and there are a lot of videos on [YouTube](https://www.youtube.com/results?search_query=zombie+dice) as well.


I tried to repeat all the steps, that happen during the real game:
* choice of number of players (i.e. number of non-player character)
* random order of players at the table (how would you sit with friends in the pub)
* all steps during one turn:
    * taking random dices from the jar
    * rolling the dices
    * making the decision including the game strategy for the non-player character
* table entry with game results
* saving highscore in CSV file
* some phrases just for fun

#### How to play:
1. Enter your name
2. Choose number of players
3. And try to enjoy the game!
You should use **enter** for rolling dices and when you're asked, or input something to pass your turn


> Each turn presented in such wayc(each word means you threw away, and what color was the dice):

[![game-process.png](https://i.postimg.cc/43fF8nJ2/game-process.png)](https://postimg.cc/75RVhHJS)


> At the end of each round you'll see table with the results:

[![table.png](https://i.postimg.cc/DwbNWRx5/table.png)](https://postimg.cc/K1xfwpSg)


> Name of the winner:

[![winner.png](https://i.postimg.cc/grbZgXPx/winner.png)](https://postimg.cc/PvKJxqJH)


> And top ten high score from CSV file:

[![top-ten.png](https://i.postimg.cc/Bnc5K51L/top-ten.png)](https://postimg.cc/hXv7Fdsc)


#### What I used:
In this project I tried to use all the themes from the **CS50’s Introduction to Programming with Python** and something more:
* loops, conditionals, exceptions etc.
* global variables, lists, dictionaries, tuples
* functions and classes
* and some pip-installable libraries


##### Libraries:
1. **random** for randomize process of taking dices and rolling dices
2. **csv** for working with CSV files
3. **tabulate** for the tables themselves
4. **colorama** for using color font
5. **datetime** for fixing date and time in highscore file
6. **time** for making all the action of NPC just a little slower
7. in early version, which was written on my PC, I used **keyboard** library, in order to use keyboard for rolling dices or passing ypur turn, but i couldn't find the way install it in Codespases :(

#### How it works:
1. **main()** function defines the order of implementation the algorithm:
    * short introducing
    * name and number of players input
    * generation of a list of players
    * short rule explanation
    * creating the loop with every round till somebody win
    * showing intermediate result after each round
    * announcement of the winner
    * writing the highscore file and showing top ten players of all time
2. **one_round()** function calls one of two subclasses *OneTurnPlayer* or *OneTurnComp*, depending on whose turn. These subclasses inherit the characteristics of the class *OneTurn*, which defines tho whole game process during one round:d
    * definition number of dices "in hand"
    * imitate process of rolling dices
    * asking some actions from user (if it's user's turn)
    * imitate actions of NPC
    * returning the result (as a list of dictionaries with name and score of each player)
    * getting intermediate high score in order to correct NPC's game strategy

#### And finally:
To make game a little interesting I used the [researching](https://arxiv.org/abs/1406.0351) of Heather L. Cook and David G. Taylor from Department of Mathematics, Computer Science, and Physics, Roanoke College, Salem, which describes an optimal play strategy, which formed the basis for NPC's strategy in my project.
