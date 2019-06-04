import actors
import random
import time


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------')
    print('     WIZARD GAME APP')
    print('--------------------------')
    print()


def game_loop():

    creatures = [
        actors.SmallAnimal('Toad', 1),
        actors.Creature('Tiger', 12),
        actors.SmallAnimal('Bat', 3),
        actors.Dragon('Dragon', 50, scaliness = 75, breaths_fire = True),
        actors.Wizard('Evil Wizard', 1000)
    ]

    hero = actors.Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'.format(
            active_creature.name, active_creature.level
        ))
        print()

        cmd = input('Do you [a]ttack, [r]unaway or, [l]ook around? ')
        cmd = cmd.strip().lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")

        elif cmd == 'r':
            print('The wizard {} has become unsure of his power and flees!!!'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('OK, exiting game...bye!')
            break

        if not creatures:
            print("You've defeated all the creatures!")
            break

        print()


if __name__ == '__main__':
    main()