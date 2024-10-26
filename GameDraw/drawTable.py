# import numpy as np
import streamlit as st
import pandas as pd
import random

def init_teams(n_teams):
    dict_teams = {}
    teams = []
    for i in range(n_teams):
        j = st.text_input(f"Team {i+1}name ")
        dict_teams[j]= ["-" for t in range(4)]
        teams.append(j)
    return dict_teams , teams

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

# Function to format matches as a DataFrame
def format_matches(matches):
    data = []
    for team, opponents in matches.items():
        for opponent_info in opponents:
            if len(opponent_info) == 2:  # Ensure we have both opponent and round number
                opponent, round_num = opponent_info
                data.append({"Round": round_num, "Team 1": team, "Team 2": opponent})
    df = pd.DataFrame(data) 
    return df

# Main code for Streamlit app
nbr_teams = st.number_input("nmbre of teams :")
if nbr_teams != 0 :
    teams_dict , teams = init_teams(nbr_teams)


rounds = 4  # Number of rounds

st.title("Football Match Draw Results are Available")
if teams != None :
    matches = draw_teams(teams, rounds)
    df_matches = format_matches(matches)
if df_matches != None:
st.write("Here are the match results for each round:")
st.table(df_matches)

