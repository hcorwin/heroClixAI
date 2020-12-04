#!/usr/bin/env python3

class CaptainAmerica:

    def __init__(self):
        self.movement = [(8, "Charge"), (7, "Charge"), (7, "Charge"), (6, "Sidestep"), (6, "Sidestep"), (5, "Sidestep"),
                         (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.attack = [(11, "Nothing"), (10, "Nothing"), (10, "Nothing"), (9, "Nothing"), (9, "Nothing"),
                       (9, "Nothing"),
                       (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.defense = [(17, "Combat Reflexes"), (17, "Combat Reflexes"), (17, "Combat Reflexes"), (16, "Willpower"),
                        (16, "Willpower"), (17, "Willpower"),
                        (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.damageValue = [(3, "Leadership"), (3, "Leadership"), (3, "Leadership"), (2, "Close Combat Expert"),
                            (2, "Close Combat Expert"), (2, "Close Combat Expert"),
                            (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.range = 5
        self.location = "A1"
        self.inPlay = True
        self.placeInDial = 0
        self.actionToken = 0
        self.name = "Captain America"
    def __str__(self):
        return "Captain America"


class Thor:

    def __init__(self):
        self.movement = [(10, "Charge"), (10, "Charge"), (10, "Charge"), (10, "Running Shot"), (10, "Running Shot"),
                         (10, "Running Shot"),
                         (9, "Sidestep"), (9, "Sidestep"), (9, "Sidestep"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.attack = [(11, "Super Strength"), (11, "Super Strength"), (11, "Super Strength"),
                       (10, "Energy Explosion"), (10, "Energy Explosion"), (10, "Energy Explosion"),
                       (9, "Lightning Smash"), (9, "Lightning Smash"), (9, "Lightning Smash"),
                       (0, "KO"), (0, "KO"), (0, "KO")]
        self.defense = [(18, "Impervious"), (17, "Impervious"), (17, "Impervious"), (17, "Invulnerability"),
                        (17, "Invulnerability"),
                        (17, "Invulnerability"),
                        (17, "Willpower"), (17, "Willpower"), (16, "Willpower"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.damageValue = [(4, "Nothing"), (4, "Nothing"), (3, "Nothing"), (3, "Nothing"), (3, "Nothing"),
                            (3, "Nothing"),
                            (3, "Nothing"), (3, "Nothing"), (3, "Nothing"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.range = 6
        self.location = "B1"
        self.inPlay = True
        self.placeInDial = 0
        self.actionToken = 0
        self.name = "Thor"

    def __str__(self):
        return "Thor"


class IronMan:

    def __init__(self):
        self.movement = [(10, "Running Shot"), (10, "Running Shot"), (10, "Running Shot"), (9, "Sidestep"),
                         (9, "Sidestep"), (8, "Sidestep"),
                         (8, "Sidestep"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.attack = [(10, "Energy Explosion"), (10, "Energy Explosion"), (10, "Energy Explosion"), (9, "Nothing"),
                       (9, "Nothing"), (9, "Nothing"),
                       (9, "Nothing"), (0, "Nothing"), (0, "Nothing"), (0, "Nothing"), (0, "Nothing"), (0, "Nothing")]
        self.defense = [(18, "Invulnerability"), (17, "Invulnerability"), (17, "Invulnerability"), (17, "Toughness"),
                        (17, "Toughness"), (16, "Toughness"),
                        (16, "Toughness"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.damageValue = [(4, "Nothing"), (3, "Nothing"), (3, "Nothing"), (2, "Ranged Combat Expert"),
                            (2, "Ranged Combat Expert"), (2, "Ranged Combat Expert"),
                            (2, "Ranged Combat Expert"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO"), (0, "KO")]
        self.range = 7
        self.location = "C1"
        self.inPlay = True
        self.placeInDial = 0
        self.actionToken = 0
        self.name = "Iron Man"

    def __str__(self):
        return "Iron Man"


def main():
    temp = CaptainAmerica()
    print(temp.movement[0][1])


if __name__ == '__main__':
    main()
