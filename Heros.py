#!/usr/bin/env python3


class CaptainAmerica:

    def __init__(self):
        self.movement = [(8, "charge"), (7, "charge"), (7, "charge"), (6, "sidestep"), (6, "sidestep"), (5, "sidestep"),
                         (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.attack = [(11, "nothing"), (10, "nothing"), (10, "nothing"), (9, "nothing"), (9, "nothing"),
                       (9, "nothing"),
                       (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.defense = [(17, "combat reflexes"), (17, "combat reflexes"), (17, "combat reflexes"), (16, "willpower"),
                        (16, "willpower"), (17, "willpower"),
                        (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.damageValue = [(3, "leadership"), (3, "leadership"), (3, "leadership"), (2, "close combat expert"),
                            (2, "close combat expert"), (2, "close combat expert"),
                            (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.location = "A1"
        self.inPlay = True
        self.placeInDial = 0
    def __str__(self):
        return "Captain America"


class Thor:

    def __init__(self):
        self.movement = [(10, "charge"), (10, "charge"), (10, "charge"), (10, "running shot"), (10, "running shot"),
                         (10, "running shot"),
                         (9, "sidestep"), (9, "sidestep"), (9, "sidestep"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.attack = [(11, "Super Strength"), (11, "Super Strength"), (11, "Super Strength"),
                       (10, "Energy Explosion"), (10, "Energy Explosion"), (10, "Energy Explosion"),
                       (9, "Lightning Smash"), (9, "Lightning Smash"), (9, "Lightning Smash"),
                       (0, "ko"), (0, "ko"), (0, "ko")]
        self.defense = [(18, "impervious"), (17, "impervious"), (17, "impervious"), (17, "Invulnerability"),
                        (17, "Invulnerability"),
                        (17, "Invulnerability"),
                        (17, "Willpower"), (17, "Willpower"), (16, "Willpower"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.damageValue = [(4, "nothing"), (4, "nothing"), (3, "nothing"), (3, "nothing"), (3, "nothing"),
                            (3, "nothing"),
                            (3, "nothing"), (3, "nothing"), (3, "nothing"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.location = "B1"
        self.inPlay = True
        self.placeInDial = 0

    def __str__(self):
        return "Thor"


class IronMan:

    def __init__(self):
        self.movement = [(10, "Running Shot"), (10, "Running Shot"), (10, "Running Shot"), (9, "Sidestep"),
                         (9, "Sidestep"), (8, "Sidestep"),
                         (8, "Sidestep"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.attack = [(10, "Energy Explosion"), (10, "Energy Explosion"), (10, "Energy Explosion"), (9, "nothing"),
                       (9, "nothing"), (9, "nothing"),
                       (9, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing")]
        self.defense = [(18, "Invulnerability"), (17, "Invulnerability"), (17, "Invulnerability"), (17, "Toughness"),
                        (17, "Toughness"), (16, "Toughness"),
                        (16, "Toughness"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.damageValue = [(4, "nothing"), (3, "nothing"), (3, "nothing"), (2, "Ranged Combat Expert"),
                            (2, "Ranged Combat Expert"), (2, "Ranged Combat Expert"),
                            (2, "Ranged Combat Expert"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.location = "C1"
        self.inPlay = True
        self.placeInDial = 0

    def __str__(self):
        return "Iron Man"


def main():
    temp = CaptainAmerica()
    print(temp.movement[0][1])


if __name__ == '__main__':
    main()
