"""
@author : Harshitha Benakanahalli Nagaraj
 file : chopper.py
"""

'''
This program is for the implementation of stack for a chopper.
'''
from queue import LifoQueue

import role

MAX_OCCUPANCY = 6


class Chopper:

    def __init__(self):
        self.chopper = LifoQueue(maxsize=MAX_OCCUPANCY)
        self.rescued = 0
        self.size = 0

    # method for boarding passenger into chopper
    def board_passenger(self, player) -> None:
        self.chopper.put(player)
        print("{passenger} #{id} boards the chopper!".format(passenger=player.role.name, id=player.id_player))
        # increment the number of passengers rescued iff the passenger is hostage.
        if player.role == role.Role.HOSTAGE:
            self.size += 1
        # chopper flies and rescues passengers when the chopper is full.
        if self.is_full():
            print("Chopper fly!")
            self.rescue_passengers()

    # returns the number of passengers rescued.
    def get_num_rescued(self) -> int:
        return self.size

    # to check whether chopper is empty.
    def is_empty(self) -> bool:
        return self.chopper.empty()

    # to check whether chopper is full.
    def is_full(self) -> bool:
        return self.chopper.full()

    # method to rescue passengers.
    def rescue_passengers(self) -> None:
        print("Chopper transported till  {passenger}  to safety!".format(passenger=self.chopper.get()))
