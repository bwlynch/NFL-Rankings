## NFL Rankings

### Overview

This projects aims to create a simple ranking of NFL football teams based on the which teams a team beats and loses to, and by what margins. The idea is that rather than look at the number of wins and losses to instead look at the quality of the teams they're winning or losing against and how close they are playing those teams. For each game, a team is given a rating by taking the square root of the margin of victory, and adding or subtracting it from the rating of their opponent depending on whether they won or lost the game. So for example if a team beats an opponent who has rating of 64 by 9 points, the team's rating for that game would be 64 + sqrt(9), or 64+3, so 67. Each team then gets an overall rating for the season based on the average of the ratings they received for each of the games they played. Each team starts with the same rating, and then this process is repeated multiple times, using the ratings of each team in the previous round for calculating the ratings in the current round. Eventually after a number of rounds, the season ratings for each team converge on a single number. (To make the ratings easier to read and interpret, the margins are increased by a factor of 10, and teams start with a rating of 50). 

### Installation

Required Packages:
The only required python package to run the rankings is dotenv. The two commands below install pip, and then use pip to install dotenv.

```
sudo apt install python3-pip
pip install python_dotenv
```

### Update Rankings

To update the rankings, run `python3 rank.py`. See the .env.default for the variables to define. You will need to get a free api key by creating an account at https://sportradar.us/, and add the key to the .env file under the variable API_KEY. The year the rankings are run for is defined by the variable YEAR=, and it will calculate all games up through including the week defined by the variable WEEK.

