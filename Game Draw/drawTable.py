import numpy as np 
def init_teams(n_teams):
    dict_teams = {}
    teams = []
    for i in range(n_teams):
        j = input("Team "+ str(i+1) + " name ")
        dict_teams[j]= ["-" for t in range(4)]
        teams.append(j)
    return dict_teams , teams
def draw(dict_teams , team):
    teams = team[:]
    t = len(teams)
    r = 0 
    while r < 4*t:
        j = np.random.randint(0,len(teams))
        k = np.random.randint(0,len(teams))
        teamA = teams[j]
        teamB = teams[k]
        while "-" not in dict_teams[teamA] :
            j = np.random.randint(0,len(teams))
            teamA = teams[j]
        
        while "-" not in dict_teams[teamB] or teamA == teamB or teamB in dict_teams[teamA] :
            k = np.random.randint(0,len(teams))
            teamB = teams[k]
        print(teamA , teamB)

        a = dict_teams[teamA].index("-")
        b = dict_teams[teamB].index("-")
        dict_teams[teamA][a] = teamB
        dict_teams[teamB][b] = teamA
        if "-" not in dict_teams[teamA] :
            teams.remove(teamA)
        if "-" not in dict_teams[teamB] :
            teams.remove(teamB)
        print(teams)
        r+=2
    return dict_teams

nbr_teams = int(input("nmbre of teams :"))
teams_dict , teams = init_teams(nbr_teams)

draw(teams_dict, teams)