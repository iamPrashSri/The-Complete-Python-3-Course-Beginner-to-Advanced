class Enemy:
    def __init__(self, hp, mp):
        self.max_hp = hp
        self.hp = hp
        self.map_mp = mp
        self.mp = mp

    def get_hp(self):
        return self.hp