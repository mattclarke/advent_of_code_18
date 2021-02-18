import re

test_data = """
Immune System:
597 units each with 4458 hit points with an attack that does 73 slashing damage at initiative 6
4063 units each with 9727 hit points (weak to radiation) with an attack that does 18 radiation damage at initiative 9
2408 units each with 5825 hit points (weak to slashing; immune to fire, radiation) with an attack that does 17 slashing damage at initiative 2
5199 units each with 8624 hit points (immune to fire) with an attack that does 16 radiation damage at initiative 15
1044 units each with 4485 hit points (weak to bludgeoning) with an attack that does 41 radiation damage at initiative 3
4890 units each with 9477 hit points (immune to cold; weak to fire) with an attack that does 19 slashing damage at initiative 7
1280 units each with 10343 hit points with an attack that does 64 cold damage at initiative 19
609 units each with 6435 hit points with an attack that does 86 cold damage at initiative 17
480 units each with 2750 hit points (weak to cold) with an attack that does 57 fire damage at initiative 11
807 units each with 4560 hit points (immune to fire, slashing; weak to bludgeoning) with an attack that does 56 radiation damage at initiative 8

Infection:
1237 units each with 50749 hit points (weak to radiation; immune to cold, slashing, bludgeoning) with an attack that does 70 radiation damage at initiative 12
4686 units each with 25794 hit points (immune to cold, slashing; weak to bludgeoning) with an attack that does 10 bludgeoning damage at initiative 14
1518 units each with 38219 hit points (weak to slashing, fire) with an attack that does 42 radiation damage at initiative 16
4547 units each with 21147 hit points (weak to fire; immune to radiation) with an attack that does 7 slashing damage at initiative 4
1275 units each with 54326 hit points (immune to cold) with an attack that does 65 cold damage at initiative 20
436 units each with 36859 hit points (immune to fire, cold) with an attack that does 164 fire damage at initiative 18
728 units each with 53230 hit points (weak to radiation, bludgeoning) with an attack that does 117 fire damage at initiative 5
2116 units each with 21754 hit points with an attack that does 17 bludgeoning damage at initiative 10
2445 units each with 21224 hit points (immune to cold) with an attack that does 16 cold damage at initiative 13
3814 units each with 22467 hit points (weak to bludgeoning, radiation) with an attack that does 10 cold damage at initiative 1
"""

# test_data = """
# Immune System:
# 17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
# 989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3
#
# Infection:
# 801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
# 4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
# """


class Unit:
    def __init__(self, num, hp, attack, damage, initiative, weaknesses, immunities):
        self.num_units = num
        self.hp = hp
        self.attack = attack
        self.damage_type = damage
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.effective_power = self.num_units * self.attack
        self.name = ""
        self.target = None

    def calculate_damage(self, damage_type, power):
        if damage_type in self.immunities:
            return 0
        elif damage_type in self.weaknesses:
            return power * 2
        else:
            return power

    def take_hit(self, damage_type, power):
        damage = self.calculate_damage(damage_type, power)
        killed = damage // self.hp
        self.num_units -= killed
        if self.num_units < 0:
            self.num_units = 0
        self.calc_power()
        return killed

    def calc_power(self):
        self.effective_power = self.num_units * self.attack


def generate():
    is_immune = True

    all_units = []
    immune = []
    infection = []

    for line in test_data.splitlines():
        if not line:
            continue
        if line.startswith("Immune"):
            continue
        if line.startswith("Infection"):
            is_immune = False
            continue

        weaknesses = []
        immunities = []
        if "(" in line:
             m = re.match(r"(\d+) units each with (\d+) hit points \((.+)\) with an attack that does (\d+) (\w+) damage at initiative (\d+)", line)
             if m:
                 num = int(m.groups()[0])
                 hp = int(m.groups()[1])
                 attack = int(m.groups()[3])
                 damage = m.groups()[4]
                 initiative = int(m.groups()[5])
                 weak = re.match(r".*weak to (\w+)[,\s]*(\w+)*[,\s]*(\w+)*",
                                 m.groups()[2])
                 if weak:
                     for w in weak.groups():
                         if w:
                             weaknesses.append(w)
                 immun = re.match(r".*immune to (\w+)[,\s]*(\w+)*[,\s]*(\w+)*",
                                  m.groups()[2])
                 if immun:
                     for i in immun.groups():
                         if i:
                             immunities.append(i)
             else:
                 raise Exception("WTF!", line)

        else:
            m = re.match(
                r"(\d+) units each with (\d+) hit points with an attack that does (\d+) (\w+) damage at initiative (\d+)",
                line)

            if m:
                num = int(m.groups()[0])
                hp = int(m.groups()[1])
                attack = int(m.groups()[2])
                damage = m.groups()[3]
                initiative = int(m.groups()[4])
            else:
                raise Exception("WTF!", line)

        u = Unit(num, hp, attack, damage, initiative, weaknesses, immunities)
        all_units.append(u)
        if is_immune:
            immune.append(u)
            u.name = f"Immune System {len(immune)}"
        else:
            infection.append(u)
            u.name = f"Infection {len(infection)}"

    return all_units, immune, infection


# Target selection phase
# Highest effective power goes first
# In a tie the higher initiative goes first
# Choose the target it will do most damage to
# In a tie chooses the group with largest effective power
# If cannot do any damage it does nothing
# Defending groups can only be chosen by one attacker

# Sort by effective power and initiative
def sort_attackers(all_units, immune, infection):
    total_killed = 0
    print("\nImmune System:")
    for i in immune:
        print(i.name, i.num_units)

    print("Infection:")
    for i in infection:
        print(i.name, i.num_units)

    all_units = sorted(all_units, key=lambda u: u.initiative, reverse=True)
    all_units = sorted(all_units, key=lambda u: u.effective_power, reverse=True)

    targeted = []

    for u in all_units:
        best_target = None
        best_damage = 0
        enemies = immune if u in infection else infection

        for i in enemies:
            if u.damage_type in i.immunities:
                continue

            d = i.calculate_damage(u.damage_type, u.effective_power)
            if d == 0:
                continue
            if i not in targeted and not best_target:
                best_target = i
                best_damage = d
                continue

            if i not in targeted and d > best_damage:
                best_damage = d
                best_target = i
            elif i not in targeted and d == best_damage:
                # Choose target with highest power
                if best_target.effective_power < i.effective_power:
                    best_damage = d
                    best_target = i
                elif best_target.effective_power == i.effective_power:
                    if i.initiative > best_target.initiative:
                        best_damage = d
                        best_target = i

        if best_target:
            targeted.append(best_target)
            u.target = best_target
            # print(best_damage)
        else:
            u.target = None

    for i, o in enumerate(infection):
        index = all_units.index(o)
        target = o.target
        if target:
            damage = target.calculate_damage(o.damage_type, o.effective_power)
            print(f"{o.name} would deal {target.name} {damage} damage")

    for i, o in enumerate(immune):
        index = all_units.index(o)
        target = o.target
        if target:
            damage = target.calculate_damage(o.damage_type, o.effective_power)
            print(f"{o.name} would deal {target.name} {damage} damage")

    # Do the attacking
    all_units = sorted(all_units, key=lambda u: u.initiative, reverse=True)

    for i, u in enumerate(all_units):
        target = u.target
        if target:
            killed = target.take_hit(u.damage_type, u.effective_power)
            print(f"{u.name} attacks {target.name}, killing {killed}")
            total_killed += killed

    for u in all_units:
        if u.num_units == 0:
            if u in immune:
                immune.remove(u)
            elif u in infection:
                infection.remove(u)

    if total_killed == 0:
        raise Exception("No kills")

    remaining_units = immune[:]
    remaining_units.extend(infection)
    return remaining_units


boost = 72
low = 0
old_low = 0
high = None

while True:
    try:
        all_units, immune, infection = generate()
        for i in immune:
            i.attack += boost
            i.calc_power()

        while infection:
            all_units = sort_attackers(all_units, immune, infection)
            if not immune:
                raise Exception("Failed to win")

        count = 0
        for u in all_units:
            count += u.num_units

        print(count)

        if not high:
            high = boost
        # Try binary search
        high = boost
        boost = low + (high - low)//2
    except:
        if not high:
            low = boost
            boost += 1000
        else:
            if low == old_low and abs(high-low) == 1:
                boost = high
                continue
            old_low = low
            low = boost
            boost = low + (high - low) // 2


