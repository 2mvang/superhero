# superheroes.py

import random
## Ability
# 1) __init__: Parameters: name: String, max_damage: Integer
# 2) attack: No Parameters
class Ability:
    def __init__(self, name, attack_strength):
    #   '''Create Instance Variables:
    #       name:String
    #       max_damage: Integer
    #    '''
        self.name = name
        max_damage = 9001
        self.attack_strength = max_damage

       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
      print(random.randint(0, 9001))

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    # next line I edited so it would work because I am printing in line 25
    ability.attack()

## Armor
# 1) __init__: Parameters: name: String, max_block: Integer
# 2) block: Parameters: None



## Hero
# 1) __init__: Parameters: name:String, starting_health:Int (default value: 100)
# 2) add_ability: Parameters: ability:Ability Object
# 3) attack: No Parameters
# 4) defend: incoming_damage: Integer
# 5) take_damage: Parameters: damage
# 6) is_alive: No Parameters
# 7) fight: Parameters: opponent: Hero Class
