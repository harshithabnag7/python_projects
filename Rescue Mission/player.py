"""
@author : Harshitha Benakanahalli Nagaraj
 file : player.py
"""

'''
This program is for the implementation of class Player.
'''
import role


class Player():
    # initialize the die rolls random.
    GUERRILLA_CHANCE_TO_BEAT_SOLDIER = 20
    PREDATOR_CHANCE_TO_BEAT_HOSTAGE = 50
    PREDATOR_CHANCE_TO_BEAT_SOLDIER = 75

    def __init__(self, id_player, role: role.Role):
        self.id_player = id_player
        self.role = role

    def __str__(self):
        return "{role} #{id_player}".format(role=self.role, id_player=self.id_player)

    # method to print who wins after rolling a die.
    def print_victory_message(self, opponent: 'Player'):
        return "{player} defeats {opponent}".format(player=self.role.name, opponent=opponent.role.name)
