#TO DO:
#*1 Check for issue of big win bringing down the average, big loss bringing up the average
#*2 Adjust formula if need be based on 1
#*3 figure out env solution
#*4 Add comments
#*5 Clean up file
#*6 Set default values for variables if not defined in .env (week = 18/17, year = 2021)
#*7 Try Sqrt, other roots
#*8 Get default non-.env values working
#*9 create .env.default and .gitignore
#10*Create README, mention need to install python_dotenv

#*11 Take into account overtime
#*12 Clean up README
#*13 Rename the variables to more sensical/intelligdent names, such as using rating score in particular
#*14 Push to Github (make more official repo after adding in git ignore, cleaning everything up, remove this top list)

#*15 Separate API call into separate file
#*16 Export into data.json file or some other format
#*17 Import exported data file into webpage
#*18 Add in compatibility for ties


#*19 Clean up how data is stored, such as variable with each game/ratings versus total ratings. Maybe combine into one variable? Add to export to data.json
#20 Create prod react app (use different name than fold). Create graphic design for displaying the data, including:
#A
#-rankings
#-click to expand(?) list of rating for each game
#-explanation of methodology
#-make it pretty
#-clean up react directory
#B
#-go to rankings for previous weeks?
#-predictions for next week's games
#-predictions for past games, whether they ended up being correct, and total record for predictions over the season (also figure out what week to start predictions for)

#21. Use date to calculate week??
#22. Compatibility with previous seasons, including teams in different locations, for seasons before 2000? - figure out if there were any other team abbreviation changes for teams after 2000 besides LA and LV teams
#23 Figure our why calls for 2020, week 1 2017 are failing; Handle when future weeks/games are included in the range that haven't been played yet


import requests
import time
import math
import os
from dotenv import load_dotenv
import json

# Load values in .env and assign to variables. For setting weeks_passed variable, if week 12 has ended and week 13 is next, weeks passed should be set to 12
load_dotenv()

def get_env(key, default): 
    value = os.getenv(key)
    if value is None:
        return default
    return value

api_key = os.getenv('API_KEY')
weeks_passed = int(get_env('WEEK', 8))
year = int(get_env('YEAR', 2021))
year_str = str(year)

#Pulls data from the api for each of the weeks that has passed, waiting 2 seconds to avoid triggering the api limit of no more than 1 call each second. The returned data is converted into a usable form, and the relevant data is grabbed from it and turned into an array, containing the two opponents for each game and the points scored by each.
games = []
for i in range(weeks_passed):
    week = str(i + 1)
    url = "http://api.sportradar.us/nfl/official/trial/v7/en/games/" + year_str + "/REG/" + week + "/schedule.json?api_key=" + api_key
    response = requests.get(url)
    games_json = response.json()
    time.sleep(2)
    for game in games_json["week"]["games"]:
        overtime = "OT" if (len(game["scoring"]["periods"]) > 4) else ""
        games.append([game["home"]["alias"],game["scoring"]["home_points"],game["away"]["alias"],game["scoring"]["away_points"],overtime])
#print(games)

#To speed up the program and to avoid putting hits toward the api limit, this is a copy of the games array after week 7 that would be created by the above code. The api call loop can be commented out, and this uncommented
#games = [['TB', 31, 'DAL', 29], ['TEN', 13, 'ARI', 38], ['HOU', 37, 'JAC', 21], ['CIN', 27, 'MIN', 24], ['IND', 16, 'SEA', 28], ['BUF', 16, 'PIT', 23], ['DET', 33, 'SF', 41], ['WAS', 16, 'LAC', 20], ['CAR', 19, 'NYJ', 14], ['ATL', 6, 'PHI', 32], ['KC', 33, 'CLE', 29], ['NO', 38, 'GB', 3], ['NYG', 13, 'DEN', 27], ['NE', 16, 'MIA', 17], ['LA', 34, 'CHI', 14], ['LV', 33, 'BAL', 27], ['WAS', 30, 'NYG', 29], ['JAC', 13, 'DEN', 23], ['MIA', 0, 'BUF', 35], ['CLE', 31, 'HOU', 21], ['CHI', 20, 'CIN', 17], ['PHI', 11, 'SF', 17], ['CAR', 26, 'NO', 7], ['IND', 24, 'LA', 27], ['PIT', 17, 'LV', 26], ['NYJ', 6, 'NE', 25], ['ARI', 34, 'MIN', 33], ['TB', 48, 'ATL', 25], ['LAC', 17, 'DAL', 20], ['SEA', 30, 'TEN', 33], ['BAL', 36, 'KC', 35], ['GB', 35, 'DET', 17], ['HOU', 9, 'CAR', 24], ['CLE', 26, 'CHI', 6], ['JAC', 19, 'ARI', 31], ['KC', 24, 'LAC', 30], ['BUF', 43, 'WAS', 21], ['TEN', 25, 'IND', 16], ['PIT', 10, 'CIN', 24], ['NE', 13, 'NO', 28], ['NYG', 14, 'ATL', 17], ['DET', 17, 'BAL', 19], ['LV', 31, 'MIA', 28], ['DEN', 26, 'NYJ', 0], ['LA', 34, 'TB', 24], ['MIN', 30, 'SEA', 17], ['SF', 28, 'GB', 30], ['DAL', 41, 'PHI', 21], ['CIN', 24, 'JAC', 21], ['NO', 21, 'NYG', 27], ['PHI', 30, 'KC', 42], ['BUF', 40, 'HOU', 0], ['DAL', 36, 'CAR', 28], ['MIN', 7, 'CLE', 14], ['MIA', 17, 'IND', 27], ['NYJ', 27, 'TEN', 24], ['CHI', 24, 'DET', 14], ['ATL', 30, 'WAS', 34], ['LA', 20, 'ARI', 37], ['SF', 21, 'SEA', 28], ['GB', 27, 'PIT', 17], ['DEN', 7, 'BAL', 23], ['NE', 17, 'TB', 19], ['LAC', 28, 'LV', 14], ['SEA', 17, 'LA', 26], ['ATL', 27, 'NYJ', 20], ['HOU', 22, 'NE', 25], ['TB', 45, 'MIA', 17], ['CAR', 18, 'PHI', 21], ['JAC', 19, 'TEN', 37], ['PIT', 27, 'DEN', 19], ['MIN', 19, 'DET', 17], ['CIN', 22, 'GB', 25], ['WAS', 22, 'NO', 33], ['LV', 9, 'CHI', 20], ['LAC', 47, 'CLE', 42], ['DAL', 44, 'NYG', 20], ['ARI', 17, 'SF', 10], ['KC', 20, 'BUF', 38], ['BAL', 31, 'IND', 25], ['PHI', 22, 'TB', 28], ['JAC', 23, 'MIA', 20], ['DET', 11, 'CIN', 34], ['WAS', 13, 'KC', 31], ['CAR', 28, 'MIN', 34], ['IND', 31, 'HOU', 3], ['NYG', 11, 'LA', 38], ['BAL', 34, 'LAC', 6], ['CHI', 14, 'GB', 24], ['CLE', 14, 'ARI', 37], ['DEN', 24, 'LV', 34], ['NE', 29, 'DAL', 35], ['PIT', 23, 'SEA', 20], ['TEN', 34, 'BUF', 31], ['CLE', 17, 'DEN', 14], ['TEN', 27, 'KC', 3], ['NE', 54, 'NYJ', 13], ['BAL', 17, 'CIN', 41], ['GB', 24, 'WAS', 10], ['MIA', 28, 'ATL', 30], ['NYG', 25, 'CAR', 3], ['LV', 33, 'PHI', 22], ['LA', 28, 'DET', 19], ['TB', 38, 'CHI', 3], ['ARI', 31, 'HOU', 5], ['SF', 18, 'IND', 30], ['SEA', 10, 'NO', 13], ['ARI', 21, 'GB', 24], ['BUF', 26, 'MIA', 11], ['ATL', 13, 'CAR', 19], ['CLE', 10, 'PIT', 15], ['NYJ', 34, 'CIN', 31], ['IND', 31, 'TEN', 34], ['DET', 6, 'PHI', 44], ['CHI', 22, 'SF', 33], ['HOU', 22, 'LA', 38], ['SEA', 31, 'JAC', 7], ['LAC', 24, 'NE', 27], ['NO', 36, 'TB', 27], ['DEN', 17, 'WAS', 10], ['MIN', 16, 'DAL', 20], ['KC', 20, 'NYG', 17]]

#games = [['TB', 31, 'DAL', 29, ''], ['TEN', 13, 'ARI', 38, ''], ['HOU', 37, 'JAC', 21, ''], ['CIN', 27, 'MIN', 24, 'OT'], ['IND', 16, 'SEA', 28, ''], ['BUF', 16, 'PIT', 23, ''], ['DET', 33, 'SF', 41, ''], ['WAS', 16, 'LAC', 20, ''], ['CAR', 19, 'NYJ', 14, ''], ['ATL', 6, 'PHI', 32, ''], ['KC', 33, 'CLE', 29, ''], ['NO', 38, 'GB', 3, ''], ['NYG', 13, 'DEN', 27, ''], ['NE', 16, 'MIA', 17, ''], ['LA', 34, 'CHI', 14, ''], ['LV', 33, 'BAL', 27, 'OT'], ['WAS', 30, 'NYG', 29, ''], ['JAC', 13, 'DEN', 23, ''], ['MIA', 0, 'BUF', 35, ''], ['CLE', 31, 'HOU', 21, ''], ['CHI', 20, 'CIN', 17, ''], ['PHI', 11, 'SF', 17, ''], ['CAR', 26, 'NO', 7, ''], ['IND', 24, 'LA', 27, ''], ['PIT', 17, 'LV', 26, ''], ['NYJ', 6, 'NE', 25, ''], ['ARI', 34, 'MIN', 33, ''], ['TB', 48, 'ATL', 25, ''], ['LAC', 17, 'DAL', 20, ''], ['SEA', 30, 'TEN', 33, 'OT'], ['BAL', 36, 'KC', 35, ''], ['GB', 35, 'DET', 17, ''], ['HOU', 9, 'CAR', 24, ''], ['CLE', 26, 'CHI', 6, ''], ['JAC', 19, 'ARI', 31, ''], ['KC', 24, 'LAC', 30, ''], ['BUF', 43, 'WAS', 21, ''], ['TEN', 25, 'IND', 16, ''], ['PIT', 10, 'CIN', 24, ''], ['NE', 13, 'NO', 28, ''], ['NYG', 14, 'ATL', 17, ''], ['DET', 17, 'BAL', 19, ''], ['LV', 31, 'MIA', 28, 'OT'], ['DEN', 26, 'NYJ', 0, ''], ['LA', 34, 'TB', 24, ''], ['MIN', 30, 'SEA', 17, ''], ['SF', 28, 'GB', 30, ''], ['DAL', 41, 'PHI', 21, ''], ['CIN', 24, 'JAC', 21, ''], ['NO', 21, 'NYG', 27, 'OT'], ['PHI', 30, 'KC', 42, ''], ['BUF', 40, 'HOU', 0, ''], ['DAL', 36, 'CAR', 28, ''], ['MIN', 7, 'CLE', 14, ''], ['MIA', 17, 'IND', 27, ''], ['NYJ', 27, 'TEN', 24, 'OT'], ['CHI', 24, 'DET', 14, ''], ['ATL', 30, 'WAS', 34, ''], ['LA', 20, 'ARI', 37, ''], ['SF', 21, 'SEA', 28, ''], ['GB', 27, 'PIT', 17, ''], ['DEN', 7, 'BAL', 23, ''], ['NE', 17, 'TB', 19, ''], ['LAC', 28, 'LV', 14, ''], ['SEA', 17, 'LA', 26, ''], ['ATL', 27, 'NYJ', 20, ''], ['HOU', 22, 'NE', 25, ''], ['TB', 45, 'MIA', 17, ''], ['CAR', 18, 'PHI', 21, ''], ['JAC', 19, 'TEN', 37, ''], ['PIT', 27, 'DEN', 19, ''], ['MIN', 19, 'DET', 17, ''], ['CIN', 22, 'GB', 25, 'OT'], ['WAS', 22, 'NO', 33, ''], ['LV', 9, 'CHI', 20, ''], ['LAC', 47, 'CLE', 42, ''], ['DAL', 44, 'NYG', 20, ''], ['ARI', 17, 'SF', 10, ''], ['KC', 20, 'BUF', 38, ''], ['BAL', 31, 'IND', 25, 'OT'], ['PHI', 22, 'TB', 28, ''], ['JAC', 23, 'MIA', 20, ''], ['DET', 11, 'CIN', 34, ''], ['WAS', 13, 'KC', 31, ''], ['CAR', 28, 'MIN', 34, 'OT'], ['IND', 31, 'HOU', 3, ''], ['NYG', 11, 'LA', 38, ''], ['BAL', 34, 'LAC', 6, ''], ['CHI', 14, 'GB', 24, ''], ['CLE', 14, 'ARI', 37, ''], ['DEN', 24, 'LV', 34, ''], ['NE', 29, 'DAL', 35, 'OT'], ['PIT', 23, 'SEA', 20, 'OT'], ['TEN', 34, 'BUF', 31, ''], ['CLE', 17, 'DEN', 14, ''], ['TEN', 27, 'KC', 3, ''], ['NE', 54, 'NYJ', 13, ''], ['BAL', 17, 'CIN', 41, ''], ['GB', 24, 'WAS', 10, ''], ['MIA', 28, 'ATL', 30, ''], ['NYG', 25, 'CAR', 3, ''], ['LV', 33, 'PHI', 22, ''], ['LA', 28, 'DET', 19, ''], ['TB', 38, 'CHI', 3, ''], ['ARI', 31, 'HOU', 5, ''], ['SF', 18, 'IND', 30, ''], ['SEA', 10, 'NO', 13, ''], ['ARI', 21, 'GB', 24, ''], ['BUF', 26, 'MIA', 11, ''], ['ATL', 13, 'CAR', 19, ''], ['CLE', 10, 'PIT', 15, ''], ['NYJ', 34, 'CIN', 31, ''], ['IND', 31, 'TEN', 34, 'OT'], ['DET', 6, 'PHI', 44, ''], ['CHI', 22, 'SF', 33, ''], ['HOU', 22, 'LA', 38, ''], ['SEA', 31, 'JAC', 7, ''], ['LAC', 24, 'NE', 27, ''], ['NO', 36, 'TB', 27, ''], ['DEN', 17, 'WAS', 10, ''], ['MIN', 16, 'DAL', 20, ''], ['KC', 20, 'NYG', 17, ''], ['IND', 45, 'NYJ', 30, ''], ['CAR', 6, 'NE', 24, ''], ['JAC', 9, 'BUF', 6, ''], ['NO', 25, 'ATL', 27, ''], ['NYG', 23, 'LV', 16, ''], ['BAL', 34, 'MIN', 31, 'OT'], ['CIN', 16, 'CLE', 41, ''], ['DAL', 16, 'DEN', 30, ''], ['MIA', 17, 'HOU', 9, ''], ['PHI', 24, 'LAC', 27, ''], ['KC', 13, 'GB', 7, ''], ['SF', 17, 'ARI', 31, ''], ['LA', 16, 'TEN', 28, ''], ['PIT', 29, 'CHI', 27, '']]


# A list of all 32 NFL teams, matching the team codes used in the data source. Note that the Rams were LA, while the Chargers were LAC, and Jacksonville was JAC rather than JAX like is used in some places. Before 2020, Raiders are OAK rather than LV. Before 2017, Chargers are SD rather than LAC. Before 2016, Rams are STL rather than LA. Team codes before then stay constant for a while, but ranges for far before 2016 haven't been added. 
teams = []

if year >= 2020:
    teams=["DAL","PHI","WAS","NYG","GB","CHI","MIN","DET","NO","CAR","ATL","TB","SEA","SF","LA","ARI","NE","MIA","BUF","NYJ","CIN","BAL","PIT","CLE","TEN","IND","JAC","HOU","DEN","LAC","LV","KC"]

elif 2017 <= year <= 2019: 
    teams=["DAL","PHI","WAS","NYG","GB","CHI","MIN","DET","NO","CAR","ATL","TB","SEA","SF","LA","ARI","NE","MIA","BUF","NYJ","CIN","BAL","PIT","CLE","TEN","IND","JAC","HOU","DEN","LAC","OAK","KC"]

elif year == 2016:
    teams=["DAL","PHI","WAS","NYG","GB","CHI","MIN","DET","NO","CAR","ATL","TB","SEA","SF","LA","ARI","NE","MIA","BUF","NYJ","CIN","BAL","PIT","CLE","TEN","IND","JAC","HOU","DEN","SD","OAK","KC"]

else:
    teams=["DAL","PHI","WAS","NYG","GB","CHI","MIN","DET","NO","CAR","ATL","TB","SEA","SF","STL","ARI","NE","MIA","BUF","NYJ","CIN","BAL","PIT","CLE","TEN","IND","JAC","HOU","DEN","SD","OAK","KC"]


#Create a dictionary for the iterations of the ranking, with a dictionary within each iteration listing the rating for each team. Also initializes the first iteration where each team starts with a rating of 50
rank = {}
rank[0] = {}
rank[0]['ranks'] = {}
for i in teams:
    rank[0]['ranks'][i] = 50


#Checks for and removes cases where a team wins by more than 14 points but the game rating is bring down their overall average rating, or similarly where a team loses by 14 points but the game rating is bringing up their overall average rating
def extremes_test(team, ratings, new_ratings):
    adjust = 0
    for m in range(len(ratings)):
        n = m - adjust
        if ((((new_ratings[team][n]['p_for'] - new_ratings[team][n]['p_against']) > 14) and (ratings[n] < (sum(ratings)/len(ratings)))) or (((new_ratings[team][n]['p_for'] - new_ratings[team][n]['p_against']) < -14) and (ratings[n] > (sum(ratings)/len(ratings))))):
            new_ratings[team].pop(n)
            ratings.pop(n)
            adjust += 1
    return(adjust, ratings, new_ratings)


#Function that generates one round of the rankings. It is called multiple times to produce the multiple iterations of the rankings.
def rank_calc(rank,teams,games):
    new_rank = {}
    new_rank['ranks'] = {}
    new_rank['games'] = {}
    new_ratings = {}
    for team in teams:
        ratings = []
        new_ratings[team] = []
        
        #Grabs the data for each game
        for j in games:
            team1 = j[0]
            score1 = j[1]
            team2 = j[2]
            score2 = j[3]
            #diff = score1 - score2
            if score1 == score2:
                diff = 0
            #If the game goes into overtime (but didn't end in a tie), the difference is overriden to 1, the same as if the game was won by a 1 point margin. This keeps the margin from being artificially inflated with a game that was tied at the end of regular time, but makes sure the winning team is rewarded for the win.
            elif j[4] == "OT":
                diff = 1;
            elif (score1 - score2) > 0:
                diff = 10 * math.sqrt(score1 - score2)
            else:
                diff = -10 * math.sqrt(score2 - score1)

            #Checks if the current team was in the current game, and if so creates a rating for that game, equal to the opponent's rating plus the margin of victory/loss.
            if team1 == team:
                game_rating = rank[team2] + diff
                ratings.append(game_rating)
                new_ratings[team].append({'p_for': score1, 'p_against': score2, 'opp': team2, 'game_rating': round(game_rating,1)})
            if team2 == team:
                game_rating = rank[team1] - diff
                ratings.append(game_rating)
                new_ratings[team].append({'p_for': score2, 'p_against': score1, 'opp': team1, 'game_rating': round(game_rating,1)})

        #Checks for and removes outlying ratings skewing the data - see comment next to function
        adjust = 1
        while adjust > 0:
            adjust, ratings, new_ratings = extremes_test(team,ratings,new_ratings)

       #Assigns the average of the ratings for the team as it's new rating in the next iteration of the rankings
        if len(ratings) > 0:
            new_rank['ranks'][team] = (sum(ratings)/len(ratings))
    new_rank['games'] = new_ratings
    return(new_rank)


#Loop through doing iterations of the rankings the number of times set in num_iterations. 20 iterations is enough that the ratings stabilize to the first decimal place.
num_iterations = 20
for i in range(num_iterations):
    rank[i + 1] = rank_calc(rank[i]['ranks'],teams,games)
final_rank = rank[num_iterations - 1]['ranks']

#Can be uncommented out to show how the rating for each team change over the course of iterations. Good for checking the degree to which the rating for each team is converging.
#for i in teams:
#    print("")
#    print(i)
#    for j in range(num_iterations):
#        print(rank[j][i]['ranks'])

#Sorts the final iteration of the ranking from highest to lowest rating
sorted_ranking = sorted(final_rank.items(), key=lambda x: x[1], reverse=True)

#define iterator to count teams in order to provide rank 
rank_num = 0

#Generate ranking of teams from highest to lowest
for i in sorted_ranking:
    rank_num += 1
    team = str(i[0])
    print('{:<5s}{:<5s}{:<12s}'.format(str(rank_num) + ".",team,str(round(i[1], 1))))

    #Uncomment the two lines below to list the games for each time and the rating that game provided toward the average 
    #print(rank[num_iterations - 1]['games'][team])
    #print("")

    #Temporary code checking for cases where a big win is bringing down the rating, or a big loss is bringing it up
    for k in rank[num_iterations - 1]['games'][team]:
        if (k['p_for'] - k['p_against']) > 14:
            if k['game_rating'] < i[1]:
                print(k, i[1])
    for k in rank[num_iterations - 1]['games'][team]:
        if (k['p_for'] - k['p_against']) < -14:
            if k['game_rating'] > i[1]:
                print(k, i[1])


#Fetches next weeks games. Copy the printout of next_week_games to the line below and then comment out everything above to store the data and stop making api calls.
next_week = weeks_passed + 1
url = "http://api.sportradar.us/nfl/official/trial/v7/en/games/" + year_str + "/REG/" + str(next_week) + "/schedule.json?api_key=" + api_key
response = requests.get(url)
future_games_json = response.json()
next_week_games = []
for game in future_games_json["week"]["games"]:
    next_week_games.append([game["home"]["alias"],game["away"]["alias"]])
print(next_week_games)
#next_week_games = [['MIA', 'BAL'], ['WAS', 'TB'], ['PIT', 'DET'], ['TEN', 'NO'], ['DAL', 'ATL'], ['NE', 'CLE'], ['NYJ', 'BUF'], ['IND', 'JAC'], ['LAC', 'MIN'], ['ARI', 'CAR'], ['DEN', 'PHI'], ['GB', 'SEA'], ['LV', 'KC'], ['SF', 'LA']]


projections = []
for game in next_week_games:
    away = final_rank[game[0]]
    home = final_rank[game[1]]
    expected_diff = (((away - home)/10)**2)
    if expected_diff < 0.5:
        expected_diff = 0.5
    else:
        expected_diff = round(expected_diff * 2) / 2
    if (away - home) > 0:
        winner = game[0]
        loser = game[1]
    else:
        winner = game[1]
        loser = game[0]
    print(str(winner) + " is projected to beat " + str(loser) + " by " + str(expected_diff))
    projections.append({"winner": winner, "loser": loser, "expected_diff": expected_diff})


# Export data into data.json
data = {'ranks': sorted_ranking, 'games': rank[num_iterations - 1]['games'], 'projections': projections}
with open('./src/data.json', 'w') as f:
  json.dump(data, f, ensure_ascii=False)

