import random
team1 = [{"name": "Персонаж 1", "health": 50}, {"name": "Персонаж 2", "health": 50}]
team2 = [{"name": "Противник 1", "health": 50}, {"name": "Противник 2", "health": 50}]
while team1 and team2:
    attackiers1=team1[0]
    defender2=team2[0]
    damage=random.randint(5,15)
    defender2['health']-=damage
    print(attackiers1['name'], 'атакует', defender2['name'], 'и наносит', damage, 'урона')
    if defender2['health']<=0:
        print(defender2['name'], 'погиб')
        team2.pop(0)
    if not team2:
        print('Команда 1 победила')
        break
    attackiers2 = team2[0]
    defender1 = team1[0]
    damage = random.randint(5, 15)
    defender1['health'] -= damage
    print(attackiers2['name'], 'атакует', defender1['name'], 'и наносит', damage, 'урона')
    if defender1['health'] <= 0:
        print(defender1['name'], 'погиб')
        team1.pop(0)
    if not team1:
        print('Команда 2 победила')
        break

# test

