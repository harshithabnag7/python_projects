'''
@author : Harshitha Benakanahalli Nagaraj
 file : rescue_mission.py
'''


'''
This program is the main program from where simulation starts.
All the other python files are imported here.
'''
import os
import random
import sys
import enemy_base
import bunker
import chopper
import player
import role


# class where Rescue Mission happens
class Rescue_Mission:
    def __init__(self, seed: int, num_hostages: int, num_soldiers: int, num_guerrillas: int):
        self.seed = seed
        self.num_hostages = num_hostages
        self.num_soldiers = num_soldiers
        self.num_guerillas = num_guerrillas
        self.chopper_object = chopper.Chopper()
        self.bunker_object = bunker.Bunker(num_soldiers)
        self.predator = player.Player(1, role.Role.PREDATOR)
        random.seed(self.seed)
        self.enemy_object = enemy_base.EnemyBase(num_hostages, num_guerrillas, self.seed)
        print(self.seed, self.num_hostages, self.num_soldiers, self.num_guerillas)

    # simulation begins
    def run_simulation(self):
        print("Get to the choppa!")

        # loop runs till all the hostages die or soldiers die
        while self.enemy_object.get_num_hostages() != 0 and self.bunker_object.get_num_of_soldiers() != 0:
            print(
                "STATISTICS: {Hostages} hostage/a remain, {Soldier} soldier/s remain, {Guerillas} guerilla/s remain, {Rescued} rescued.".format(
                    Hostages=self.enemy_object.get_num_hostages(), Soldier=self.bunker_object.get_num_of_soldiers(),
                    Guerillas=self.enemy_object.get_num_guerillas(), Rescued=self.chopper_object.get_num_rescued()))

            send_soldier = self.bunker_object.deploy_next_soldier()
            hostage = self.enemy_object.rescue_hostage(send_soldier)

            if hostage is None:
                continue
            else:

                print("{Hostage} #{id} rescued from enemy base by soldier {soldier} #{id2}".format(
                    Hostage=hostage.role.name, id=hostage.id_player,
                    soldier=send_soldier.role.name, id2=send_soldier.id_player))
                # random.seed(self.seed)
                die_predator = random.randint(1, 100)
                print("{soldier} encounters the predator who rolls a #{die}".format(soldier=send_soldier.role.name,
                                                                                    die=die_predator))

                # if Soldier wins against Predator
                if die_predator > player.Player.PREDATOR_CHANCE_TO_BEAT_SOLDIER:
                    print(send_soldier.print_victory_message(self.predator))
                    self.chopper_object.board_passenger(hostage)
                    self.bunker_object.fortify_soldier(send_soldier)
                    continue
                # if Predator wins against Soldier.
                else:
                    print(self.predator.print_victory_message(send_soldier))
                    die_predator = random.randint(1, 100)
                    print("{Hostage} encounters the predator who rolls a #{die}".format(Hostage=hostage.role.name,
                                                                                        die=die_predator))
                    # if Hostage wins against Predator.
                    if die_predator > player.Player.PREDATOR_CHANCE_TO_BEAT_HOSTAGE:
                        print(hostage.print_victory_message(self.predator))
                        self.chopper_object.board_passenger(hostage)
                        continue
                    # if Predator wins against Hostage.
                    else:
                        print(self.predator.print_victory_message(hostage))
                        continue
        # to board soldiers into chopper if soldiers are remaining in bunker and all hostages are rescued.
        while not self.bunker_object.has_soldiers():
            self.chopper_object.board_passenger(self.bunker_object.deploy_next_soldier())
        # chopper flies if all soldiers are dead and hostages are remaining in chopper.
        if not self.chopper_object.is_empty():
            self.chopper_object.rescue_passengers()

        print(
            "STATISTICS: {Hostages} hostage/a remain, {Soldier} soldier/s remain, {Guerillas} guerilla/s remain, {Rescued} rescued.".format(
                Hostages=self.enemy_object.get_num_hostages(), Soldier=self.bunker_object.get_num_of_soldiers(),
                Guerillas=self.enemy_object.get_num_guerillas(), Rescued=self.chopper_object.get_num_rescued()))

        print('End of Rescue Mission!')
        return None


# main function
def main():
    n = len(sys.argv)
    if n == 5:
        seed = int(sys.argv[1])
        num_hostages = int(sys.argv[2])
        num_soldiers = int(sys.argv[3])
        num_guerillas = int(sys.argv[4])
        RescueTeja = Rescue_Mission(seed, num_hostages, num_soldiers, num_guerillas)
        RescueTeja.run_simulation()

    else:
        print('Usage: ' + os.path.basename(sys.argv[0] + " " + os.path.basename(sys.argv[-1])))
        sys.exit(1)


if __name__ == "__main__":
    main()
