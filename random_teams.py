'''
I created this program for my on going volleyball tournament. It randomly picks 8 teams from 16 total teams and puts
them in two different groups of 8 teams each
'''

import random


def random_team(q):
    group_A = ['Team 1', 'Team 2', 'Team 3', 'Team 4', 'Team 5', 'Team 6', 'Team 7', 'Team 8']
    group_B = ['Team 9', 'Team 10', 'Team 11', 'Team 12', 'Team 13', 'Team 14', 'Team 15', 'Team 16']
    group_1 = []
    group_2 = []

    team = list(q)

    group_1 = random.sample(team, len(group_A))
    for i in group_1:
        if i in group_1:
            team.remove(i)
    # print("Teams in Group 1 are {0}".format(Group_1))

    group_2 = random.sample(team, len(group_B))
    # print("Teams in Group 2 are {0}".format(Group_2))
    # print("Teams in Group 1 are {0} \nTeams in Group 2 are {1}".format(Group_1, Group_2))

    return print(f"Teams in Group 1 are {group_1} \nTeams in Group 2 are {group_2}")


q = [str(input("Please insert Team 1: ")),
     str(input("Please insert Team 2: ")),
     str(input("Please insert Team 3: ")),
     str(input("Please insert Team 4: ")),
     str(input("Please insert Team 5: ")),
     str(input("Please insert Team 6: ")),
     str(input("Please insert Team 7: ")),
     str(input("Please insert Team 8: ")),
     str(input("Please insert Team 9: ")),
     str(input("Please insert Team 10: ")),
     str(input("Please insert Team 11: ")),
     str(input("Please insert Team 12: ")),
     str(input("Please insert Team 13: ")),
     str(input("Please insert Team 14: ")),
     str(input("Please insert Team 15: ")),
     str(input("Please insert Team 16: ")),
     ]

random_team(q)
