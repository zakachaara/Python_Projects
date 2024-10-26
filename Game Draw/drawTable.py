import numpy as np 
def init_teams(n_teams):
    dict_teams = {}
    teams = []
    for i in range(n_teams):
        j = input("Team "+ str(i+1) + " name ")
        dict_teams[j]= ["-" for t in range(4)]
        teams.append(j)
    return dict_teams , teams

import random

def draw_teams(teams, rounds=4):
    matches = {team: [] for team in teams}
    
    for round_num in range(rounds):
        available_teams = set(teams)  # Teams available for this round
        while available_teams:
            team1 = random.choice(list(available_teams))
            available_teams.remove(team1)
            
            possible_opponents = [t for t in available_teams if t not in matches[team1]]
            if not possible_opponents:  # If no valid opponents, reattempt
                return draw_teams(teams, rounds)  # Start this round from scratch
                
            team2 = random.choice(possible_opponents)
            available_teams.remove(team2)
            
            # Register this match
            matches[team1].append(team2)
            matches[team2].append(team1)
            
    return matches


nbr_teams = int(input("nmbre of teams :"))
teams_dict , teams = init_teams(nbr_teams)

draw_teams(teams)