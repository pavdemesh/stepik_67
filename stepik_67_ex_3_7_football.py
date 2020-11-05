n = int(input())

d_wins = dict()
d_loss = dict()
d_draw = dict()

teams = list()

for i in range(n):
    # print("Start cycle number: {}".format(i))
    line = input().split(";")
    if int(line[1]) > int(line[3]):
        d_wins[line[0]] = d_wins.get(line[0], 0) + 1
        d_loss[line[2]] = d_loss.get(line[2], 0) + 1
    elif int(line[1]) < int(line[3]):
        d_wins[line[2]] = d_wins.get(line[2], 0) + 1
        d_loss[line[0]] = d_loss.get(line[0], 0) + 1
    else:
        d_draw[line[0]] = d_draw.get(line[0], 0) + 1
        d_draw[line[2]] = d_draw.get(line[2], 0) + 1

    # print(d_wins)
    # print(d_draw)
    # print(d_loss)

    if line[0] not in teams:
        teams.append(line[0])
    if line[2] not in teams:
        teams.append(line[2])

    # print(teams)
    # print("End of cycle number: {}".format(i))
    # print("-----------------------")

for team in teams:
    if team not in d_wins:
        # print("Adding team named {} to wins".format(team))
        d_wins[team] = 0
    if team not in d_loss:
        # print("Adding team named {} to loss".format(team))
        d_loss[team] = 0
    if team not in d_draw:
        # print("Adding team named {} to draw".format(team))
        d_draw[team] = 0

# print(teams)
for team in teams:
    total_scores = 0 + d_wins[team] * 3 + d_draw[team]
    total_games = d_wins[team] + d_draw[team] + d_loss[team]

    output = f"{team}:{total_games} {d_wins[team]} {d_draw[team]} {d_loss[team]} {total_scores}"
    print(output)
