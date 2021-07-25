from collections import defaultdict
from itertools import cycle, product, combinations

global verbose
verbose = False

class Spell:
    def new(self, name):
        return {
            'Magic Missile': MagicMissile,
            'Drain': Drain,
            'Shield': Shield,
            'Poison': Poison,
            'Recharge': Recharge,
        }[name]()
    
class MagicMissile:
    def cast(self, a, d):
        a['Mana'] -= 53
        a['Spend'] += 53
        d['Hit Points'] -= 4
        if verbose: print(f"Player casts Magic Missile, dealing 4 damage.")

class Drain:
    def cast(self, a, d):
        a['Mana'] -= 73
        a['Spend'] += 73
        a['Hit Points'] += 2
        d['Hit Points'] -= 2
        if verbose: print(f"Player casts Drain, dealing 2 damage, and healing 2 hit points.")

class Effect:
    def worn_out(self):
        return self.timer == 0
    
class Shield(Effect):
    def cast(self, a, d):
        a['Mana'] -= 113
        a['Spend'] += 113        
        a['Armor'] += 7
        self.timer = 6
        if verbose: print(f"Player casts Shield, increasing armor by 7.")
    
    def apply(self, a, d):
        self.timer -= 1
        if verbose: print(f"Shield's timer is now {self.timer}.")
    
    def destroy(self, a, d):
        a['Armor'] -= 7
        if verbose: print(f"Shield wears off, decreasing armor by 7.")

class Poison(Effect):
    def cast(self, a, d):
        a['Mana'] -= 173
        a['Spend'] += 173
        self.timer = 6
        if verbose: print(f"Player casts Poison")
    
    def apply(self, a, d):
        d['Hit Points'] -= 3
        self.timer -= 1
        if verbose: print(f"Poison deals 3 damage; its timer is now {self.timer}.")

    def destroy(self, a, d):
        if verbose: print(f"Poison wears off.")

class Recharge(Effect):
    def cast(self, a, d):
        a['Mana'] -= 229
        a['Spend'] += 229
        if verbose: print(f"Player casts Recharge")
        self.timer = 5
    
    def apply(self, a, d):
        a['Mana'] += 101
        self.timer -= 1
        if verbose: print(f"Recharge provides 101 mana; its timer is now {self.timer}.")

    def destroy(self, a, d):
        if verbose: print(f"Recharge wears off.")

class Game:    
    def __init__(self, player, boss, hard = False):
        self.effects = {}
        self.player = player
        self.boss = boss
        self.hard = hard

    def cast(self, attacker, defender, name): 
        spell = Spell().new(name)
        spell.cast(attacker, defender)
        if issubclass(type(spell), Effect):
            self.effects[name] = spell
    
    # spells that can be afforded and not active (or just about to run out)
    def castable(self):
        costs = {'Magic Missile': 53, 'Drain': 73, 'Shield': 113, 'Poison': 173, 'Recharge': 229}
        valid = [k for k in costs.keys() if costs[k] <= self.player['Mana']]
        for k in self.effects:
            if self.effects[k].timer > 1 and k in valid: valid.remove(k)
        return valid
        
    def round(self, who, spell=None):        
        if verbose: 
            print(f"-- {who} turn --")
            print(f"- Player has {self.player['Hit Points']} hit points, {self.player['Armor']} armor, {self.player['Mana']} mana")
            print(f"- Boss has {self.boss['Hit Points']} hit points")

        attacker = getattr(self, who)
        other = {'player':'boss', 'boss':'player'}[who]
        defender = getattr(self, other)
        
        if self.hard and who == 'player':
            self.player['Hit Points'] -= 1
            if self.player['Hit Points'] <= 0: 
                if verbose: print("Boss kills the plyer, and the boss wins.")
                return [False, self.player['Spend']]

        to_delete = []
        for k in self.effects:
            self.effects[k].apply(self.player, self.boss)
            if self.effects[k].worn_out():
                self.effects[k].destroy(self.player, self.boss)
                to_delete += [k]
        for k in to_delete: del(self.effects[k])

        if self.boss['Hit Points'] <= 0: 
            if verbose: print("This kills the boss, and the player wins.")
            return [True, self.player['Spend']]
        
        if who == 'boss':
            damage = max(attacker['Damage'] - defender['Armor'], 1)
            defender['Hit Points'] -= damage
            if verbose: 
                print(f"Boss attacks for {damage} damage!")
            if self.player['Hit Points'] <= 0: 
                if verbose: print("Boss kills the plyer, and the boss wins.")
                return [False, self.player['Spend']]
        else:
            self.cast(attacker, defender, spell)
        
        if self.boss['Hit Points'] <= 0: 
            if verbose: print("This kills the boss, and the player wins.")
            return [True, self.player['Spend']]

        if verbose: print()
        return [None, self.player['Spend']]
