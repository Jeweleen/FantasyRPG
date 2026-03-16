from create_player import Player


player_name = input("create player name, input:")
player_race = input("create player race, input")

new_player = Player(player_name, player_race)
new_player.printPlayer()
