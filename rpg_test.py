import os
import random

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')


game_map = ['████████████████',
            '█    █$█  !  █ █',
            '██ $ █       ! █',
            '█$   ███  $  ███',
            '█    ! █     ! █',
            '█   ████     █ █',
            '█   █    p   █ █',
            '█   !        █$█',
            '████████████████', ]

game_map = [list(row) for row in game_map]

def show_map():
    for row in game_map:
        print(''.join(row))

game_w = len(game_map[0])
game_h = len(game_map)


HP   = 10
EXP  = 0
GOLD = 0

player_x = -1
player_y = -1

for y in range(game_h):
    for x in range(game_w):
        if game_map[y][x] == 'p':
            player_x = x
            player_y = y
            break



while True:
    show_map()

    instructiune = input()
    clean()
    instructiune = instructiune.split()

    if len(instructiune) > 0:

        if instructiune[0] in ["move", "m"]:

            in_combat = False

            if len(instructiune) > 1:

                new_x = player_x
                new_y = player_y

                if instructiune[1] in ["up", "u", "north", "n"]:
                    print("moving up")
                    if player_y > 0 and game_map[player_y-1][player_x] != '█':
                        new_y = player_y - 1

                elif instructiune[1] in ["down", "d", "south", "s"]:
                    print("moving down")
                    if player_y < game_h and game_map[player_y+1][player_x] != '█':
                        new_y = player_y + 1

                elif instructiune[1] in ["left", "l", "west", "w"]:
                    print("moving left")
                    if player_x > 0 and game_map[player_y][player_x-1] != '█':
                        new_x = player_x - 1

                elif instructiune[1] in ["right", "r", "east", "e"]:
                    print("moving right")
                    if player_x < game_w and game_map[player_y][player_x+1] != '█':
                        new_x = player_x + 1

                if new_x != player_x or new_y != player_y:
                    if game_map[new_y][new_x] == '$':
                        GOLD = GOLD + 1
                        print("You found gold! Gold amount:", GOLD)

                    elif game_map[new_y][new_x] == '!':
                        print("entering combat...")
                        in_combat = True
                    
                    game_map[player_y][player_x] = ' '
                    game_map[new_y][new_x] = 'p'
                    player_x = new_x
                    player_y = new_y


                    enemy_HP = 5
                    while(in_combat):
                        print("Enemy HP:", enemy_HP)
                        print("Your HP:", HP)
                        action = input("Choose action (attack, run): ").strip().lower()

                        if action == "attack":
                            enemy_HP -= random.randint(1, 3)
                            print("You attacked the enemy! Enemy HP is now", enemy_HP)

                            if enemy_HP <= 0:
                                print("You defeated the enemy!")
                                EXP += 5
                                GOLD += random.randint(1, 3)
                                in_combat = False
                            else:
                                HP -= 1
                                print("The enemy attacked you! Your HP is now", HP)

                                if HP <= 0:
                                    print("You have been defeated!")
                                    exit(0)

                        elif action == "run":
                            chance = random.randint(1, 10)
                            if chance > 3:
                                clean()
                                print("You successfully ran away!")
                                in_combat = False
                            else:
                                print("You failed to run away!")
                                HP -= 1
                                print("The enemy attacked you! Your HP is now", HP)

                                if HP <= 0:
                                    print("You have been defeated!")
                                    exit(0)


        elif instructiune[0] in ["check", "stats"]:
            print('HP:  ', HP)
            print('EXP: ', EXP)
            print('GOLD:', GOLD)





