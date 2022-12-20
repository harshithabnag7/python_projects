"""
@author : Harshitha Benakanahalli Nagaraj
 file : enemy_base.py
"""

'''
This program is for the implementation of stack for hostages and queue for Guerillas.
'''
import random
from queue import LifoQueue
from queue import Queue

import player
import role


class EnemyBase:

    def __init__(self, num_hostages: int, num_guerillas: int, rnd: int):
        self.num_hostages = num_hostages
        self.num_guerillas = num_guerillas

        self.cave = LifoQueue(maxsize=num_hostages)
        self.guard_line = Queue(maxsize=num_guerillas)
        for x in range(1, num_hostages+1):
            self.cave.put(player.Player(x, role.Role.HOSTAGE))
        for x in range(1, num_guerillas+1):
            self.guard_line.put(player.Player(x, role.Role.GUERRILLA))

    # adding guerilla to queue.
    def add_guerilla(self, guerilla: player.Player):
        self.guard_line.put(guerilla)

    # adding hostage to stack.
    def add_hostage(self, hostage: player.Player):
        self.cave.put(hostage)

    # method to pop guerilla out to investigate soldier.
    def get_guerilla(self) -> player.Player:
        self.guard_line.get()

    # method to get hostage out of stack if soldier wins.
    def get_hostage(self) -> player.Player:
        self.cave.get()

    def get_num_guerillas(self):
        return self.guard_line.qsize()

    def get_num_hostages(self):
        return self.cave.qsize()

    # method to rescue hostage.
    def rescue_hostage(self, soldier: player.Player) -> player.Player:
        print("{soldier} #{id} enters the enemy base...".format(soldier=soldier.role.name,id=soldier.id_player))
        hostage_removed = self.cave.get()
        if self.guard_line.empty():
            return hostage_removed
        guerilla_removed = self.guard_line.get()
        die_guerilla = random.randint(1, 100)
        print("{soldier} #{id} battles {guerilla} #{id2} who rolls a die #{die}".format(soldier=soldier.role.name, guerilla=guerilla_removed.role.name,
                                                                           die=die_guerilla,id=soldier.id_player,id2=guerilla_removed.id_player))
        if die_guerilla > player.Player.GUERRILLA_CHANCE_TO_BEAT_SOLDIER:
            return hostage_removed
        else:
            self.add_hostage(hostage_removed)
            self.add_guerilla(guerilla_removed)
            return None
