from collections import Counter

num_of_games = int(input('Введите количество сыгранных матчей: '))
scores, teams = [], []
d={}
win, draw, lose, pts = 0, 0, 0, 0
while len(scores) < num_of_games:
    match_result = input('Введите результаты матчей: ').split(';')
    scores.append(match_result)
    teams.append(match_result[0])
    teams.append(match_result[2])

teams_games = dict(Counter(teams))# Считаем количество матчей и делаем словарь
val = list(teams_games.values())
k = list(teams_games.keys())
for i in range(len(k)):
    d[k[i]] = [val[i], win, draw, lose, pts] # Заполняем словарь названиями команд и количеством матчей

for i in range(len(scores)): # Заполняем победы, ничьи и поражения
    if int(scores[i][1]) > int(scores[i][3]):
        d[scores[i][0]][1] += 1
        d[scores[i][2]] [3] += 1
    elif int(scores[i][1]) == int(scores[i][3]):
        d[scores[i][0]][2] += 1
        d[scores[i][2]] [2] += 1
    else:
        d[scores[i][0]][3] += 1
        d[scores[i][2]] [1] += 1

for i in range(len(k)):# Считаем количество очков
    d[k[i]][4] = d[k[i]][1] * 3 + d[k[i]][2]

for key, value in d.items():
    print(key + ':', *value)

