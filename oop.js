class Pokemon {
  constructor(name, type, hp, attack, defense, speed, ability, moves) {
    this.name = name;
    this.type = type;
    this.hp = hp;
    this.attack = attack;
    this.defense = defense;
    this.speed = speed;
    this.ability = ability;
    this.moves = moves;
  }
}

const pikachu = new Pokemon('Pikachu', 'electric', 100, 55, 40, 90, 'Static', [
  'Thunder Shock',
  'Quick Attack',
]);

console.log(pikachu);
