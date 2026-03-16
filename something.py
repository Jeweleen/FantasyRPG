from create_player import Player


player_name = input("create player name, input:")
#Updating so that a creater can only select from available races
races = ["human", "elf", "orc"]

player_race = input("Select race (human/elf/orc): ").lower()

while player_race not in races:
    player_race = input("Invalid race. Choose human, elf, or orc: ").lower()

new_player = Player(player_name, player_race)
new_player.printPlayer()


