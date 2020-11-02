class CaptainAmerica:

    def __init__(self):
        self.movement = [(8, "charge"), (7, "charge"), (7, "charge"), (6, "side??"), (6, "side??"), (5, "side??"),
                         (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.attack = [(11, "nothing"), (10, "nothing"), (10, "nothing"), (9, "nothing"), (9, "nothing"), (9, "nothing"),
                       (0, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing")]
        self.defense = [(17, "idk"), (17, "idk"), (17, "idk"), (16, "idk"), (16, "idk"), (17, "idk"),
                        (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.damageValue = [(3, "idk"), (3, "idk"), (3, "idk"), (2, "idk"), (2, "idk"), (2, "idk"),
                            (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.inPlay = True
        self.placeInDial = 0


class Thor:

    def __init__(self):
        self.movement = [(10, "charge"), (10, "charge"), (10, "charge"), (10, "running??"), (10, "running??"), (10, "running??"),
                         (9, "s"), (9, "s"), (9, "s"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.attack = [(11, "Super Strength"), (11, "Super Strength"), (11, "Super Strength"),
                       (10, "Energy Explosion?"), (10, "Energy Explosion?"), (10, "Energy Explosion?"),
                       (9, "Lightning Smash"), (9, "Lightning Smash"), (9, "Lightning Smash"),
                       (0, "ko"), (0, "ko"), (0, "ko")]
        self.defense = [(18, "idk"), (17, "idk"), (17, "idk"), (17, "Invulnerability"), (17, "Invulnerability"), (17, "Invulnerability"),
                        (17, "Wilpower"), (17, "Wilpower"), (16, "Wilpower"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.damageValue = [(4, "nothing"), (4, "nothing"), (3, "nothing"), (3, "nothing"), (3, "nothing"), (3, "nothing"),
                            (3, "nothing"), (3, "nothing"), (3, "nothing"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.inPlay = True
        self.placeInDial = 0


class IronMan:

    def __init__(self):
        self.movement = [(10, "Running?"), (10, "Running?"), (10, "Running?"), (9, "??"), (9, "??"), (8, "??"),
                         (8, "??"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.attack = [(10, "??"), (10, "??"), (10, "??"), (9, "nothing"), (9, "nothing"), (9, "nothing"),
                       (9, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing"), (0, "nothing")]
        self.defense = [(18, "Invulnerability"), (17, "Invulnerability"), (17, "Invulnerability"), (17, "idk"), (17, "idk"), (16, "idk"),
                        (16, "idk"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.damageValue = [(4, "nothing"), (3, "nothing"), (3, "idk"), (2, "Ranged"), (2, "Ranged"), (2, "Ranged"),
                            (2, "Ranged"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko"), (0, "ko")]
        self.inPlay = True
        self.placeInDial = 0

def main():

    temp = CaptainAmerica()
    print(temp.movement[0][1])

if __name__ == '__main__':
    main()
