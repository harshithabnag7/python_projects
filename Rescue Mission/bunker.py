"""
@author : Harshitha Benakanahalli Nagaraj
 file : bunker.py
"""

'''
This program is for the implementation of queue for a bunker.
'''

from queue import Queue

import player
import role


class Bunker:

    def __init__(self, num_soldiers: int):
        self.num_soldiers = num_soldiers
        self.bunker = Queue(maxsize=num_soldiers)
        for i in range(1, num_soldiers + 1):
            self.bunker.put(player.Player(i, role.Role.SOLDIER))
            # print("ID of the soldier is #", i)

    # method to send soldiers to enemy base.
    def deploy_next_soldier(self) -> player.Player:
        if not self.bunker.empty():
            return self.bunker.get()
        else:
            print("Empty Bunker")

    # method to add soldier back to queue.
    def fortify_soldier(self, soldier: player.Player) -> None:
        self.bunker.put(soldier)

    # method to return the size of queue.
    def get_num_of_soldiers(self) -> int:
        return self.bunker.qsize()

    # method to check whether queue is empty.
    def has_soldiers(self) -> bool:
        return self.bunker.empty()
