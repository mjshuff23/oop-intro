class Pokemon:
    def __init__(self, name, type, level, hp, attack, defense, special_attack, special_defense, speed):
        self.name = name
        self.type = type
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def __str__(self):
        return f'{self.name} is a {self.type} with level {self.level}'

    def __repr__(self):
        return f'{self.name} is a {self.type} with level {self.level}'

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type and self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level

    def __le__(self, other):
        return self.level <= other.level

    def __ge__(self, other):
        return self.level >= other.level

    def __ne__(self, other):
        return self.name != other.name or self.type != other.type or self.level != other.level

    def attack_enemy(self, other):
        other.hp -= self.attack
        print(f'{self.name} attacked {other.name} for {self.attack} damage')

    def defend(self, other):
        self.hp -= other.attack
        print(f'{other.name} attacked {self.name} for {other.attack} damage')

    def level_up(self):
        self.level += 1
        self.attack += 2
        self.defense += 2
        self.special_attack += 2
        self.special_defense += 2
        self.speed += 2
        print(f'{self.name} leveled up to level {self.level}')

    def evolve(self):
        if self.type == 'fire':
            self.type = 'water'
            print(f'{self.name} evolved into a {self.type} type')
        elif self.type == 'water':
            self.type = 'grass'
            print(f'{self.name} evolved into a {self.type} type')
        elif self.type == 'grass':
            self.type = 'electric'
            print(f'{self.name} evolved into a {self.type} type')
        elif self.type == 'electric':
            self.type = 'fire'
            print(f'{self.name} evolved into a {self.type} type')

pikachu = Pokemon('Pikachu', 'electric', 1, 100, 10, 10, 10, 10, 10)
bulbasaur = Pokemon('Bulbasaur', 'grass', 1, 100, 10, 10, 10, 10, 10)

pikachu.level_up()
pikachu.attack_enemy(bulbasaur)