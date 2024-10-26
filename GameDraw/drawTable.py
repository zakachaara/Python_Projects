import numpy as np
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
      data.append([team]+opponents)
    data = np.array(data)
    df = pd.DataFrame(data , columns=["team"]+[f"round {i+1}" for i in range(len(opponents))] , index=[f"match_{j}" for j in range(1,len(matches)+1)]) 
    return df

def color_columns(val):
    if val.name == "Round 1":
        return ["background-color: lightblue"] * len(val)
    elif val.name == "Round 2":
        return ["background-color: lightcoral"] * len(val)
    elif val.name == "Round 3":
        return ["background-color: lightred"] * len(val)
    return [""] * len(val)

def hover_style():
    return {
        "selector": "tbody tr:hover",
        "props": [("background-color", "#e0e0e0")]
    }
# Main Streamlit application
st.title("Football Match Draw System")

# Step 1: Get user input for teams
teams_input = st.text_input("Enter team names separated by commas (e.g., Team A, Team B, Team C)")
rounds_input = st.number_input("Enter the number of rounds", min_value=1, step=1, value=4)

# Step 2: Check if teams are provided
if teams_input:
    teams = [team.strip() for team in teams_input.split(",") if team.strip()]
    rounds = int(rounds_input)

    # Step 3: Run draw only if teams and rounds are valid
    if len(teams) >= 2:
        matches = draw_teams(teams, rounds)
        df_matches = format_matches(matches)
        styled_df = df_matches.style.apply(color_columns, axis=0).set_table_styles([hover_style()])
        st.write("Here are the match results for each round:")
        st.table(df_matches)
    else:
        st.error("Please enter at least two teams.")
else:
    st.warning("Please enter team names to generate the draw.")