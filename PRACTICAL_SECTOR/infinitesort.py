from time import sleep as s
import random
from turtle import mode
def insert_by_min_distance(arr):
    # Must have at least 3 elements: two to compare, one to insert
    if len(arr) < 3:
        return arr
    
    new_value = arr[-1]
    base = arr[:-1]

    # Track best position
    best_index = 0
    best_distance = float('inf')

    # Compare new_value to every adjacent pair (base[i], base[i+1])
    for i in range(len(base) - 1):
        a, b = base[i], base[i+1]
        # Distance metric: sum of distances to both neighbours
        dist = abs(new_value - a) + abs(new_value - b)

        if dist < best_distance:
            best_distance = dist
            best_index = i + 1  # insert between a and b

    # Insert new_value at the best position
    return base[:best_index] + [new_value] + base[best_index:]
def custom_distance_sort(arr):
    if len(arr) <= 2:
        return arr[:]  # already "sorted" by definition

    sorted_arr = arr[:2]  # start with first two items

    # Insert each remaining item using the custom rule
    for value in arr[2:]:
        sorted_arr = insert_by_min_distance(sorted_arr, value)

    return sorted_arr
def physics_sort(arr):
    arr = arr[:]
    n = len(arr)

    # Momentum for each element
    momentum = [0] * n

    # Initialize momentum
    for i in range(n):
        left = arr[i-1] if i > 0 else arr[i]
        right = arr[i+1] if i < n-1 else arr[i]
        momentum[i] = abs(arr[i] - left) + abs(right - arr[i])

    changed = True
    while changed:
        changed = False

        for i in range(n):
            if momentum[i] <= 0:
                continue

            # Determine direction
            direction = 0
            if i > 0 and arr[i] < arr[i-1]:
                direction = -1
            elif i < n-1 and arr[i] > arr[i+1]:
                direction = +1

            # Compute friction
            left = arr[i-1] if i > 0 else arr[i]
            right = arr[i+1] if i < n-1 else arr[i]
            friction = (abs(arr[i] - left) + abs(right - arr[i])) / 2

            # Reduce momentum
            momentum[i] -= friction
            if momentum[i] <= 0:
                momentum[i] = 0
                continue

            # Move particle
            if direction == -1 and i > 0:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                momentum[i-1] += momentum[i] * 0.3
                changed = True

            elif direction == +1 and i < n-1:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                momentum[i+1] += momentum[i] * 0.3
                changed = True

    return arr
def headphone_sort(arr):
    arr = arr[:]

    while True:
        n = len(arr)
        if n <= 1:
            return arr

        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        top = []
        bottom = []

        # Pull values inward
        while left or right:
            if left:
                lv_first = left.pop(0)
                lv_last = left.pop(-1) if left else lv_first
            else:
                lv_first = lv_last = None

            if right:
                rv_first = right.pop(0)
                rv_last = right.pop(-1) if right else rv_first
            else:
                rv_first = rv_last = None

            # Compare firsts
            if lv_first is not None and rv_first is not None:
                if lv_first > rv_first:
                    top.append(lv_first)
                    bottom.append(rv_first)
                else:
                    top.append(rv_first)
                    bottom.append(lv_first)
            elif lv_first is not None:
                top.append(lv_first)
            elif rv_first is not None:
                top.append(rv_first)

            # Compare lasts
            if lv_last is not None and rv_last is not None:
                if lv_last > rv_last:
                    top.append(lv_last)
                    bottom.append(rv_last)
                else:
                    top.append(rv_last)
                    bottom.append(lv_last)
            elif lv_last is not None:
                bottom.append(lv_last)
            elif rv_last is not None:
                bottom.append(rv_last)

        # Merge top + bottom
        new_arr = bottom + top

        # If no change, sorted
        if new_arr == arr:
            return arr

        arr = new_arr
import random

class Fighter:
    def __init__(self, value, pos):
        self.value = value
        self.hp = 10
        self.shield = 3
        self.atk = max(1, value // 5)   # simple scaling
        self.defense = 1
        self.pos = pos

    def is_alive(self):
        return self.hp > 0

    def __repr__(self):
        return f"F({self.value},hp={self.hp},sh={self.shield},pos={self.pos})"


def rpg_sort(values):
    fighters = [Fighter(v, i) for i, v in enumerate(values)]

    def get_ordered():
        return sorted([f for f in fighters if f.is_alive()], key=lambda x: x.pos)

    def is_sorted():
        alive = [f.value for f in get_ordered()]
        return alive == sorted(alive)

    round_counter = 0

    while not is_sorted() and round_counter < 500:
        round_counter += 1
        fighters = get_ordered()

        for i, f in enumerate(fighters):
            if not f.is_alive():
                continue

            # Rebuild index mapping each round
            fighters = get_ordered()
            idx = fighters.index(f)

            # Neighbours
            above = fighters[idx - 1] if idx > 0 else None
            below = fighters[idx + 1] if idx < len(fighters) - 1 else None

            # Decide action
            action = decide_action(f, above, below)

            if action == "move_up" and above:
                try_move(f, above, fighters, direction=-1)
            elif action == "move_down" and below:
                try_move(f, below, fighters, direction=+1)
            elif action == "attack_up" and above:
                attack(f, above)
            elif action == "attack_down" and below:
                attack(f, below)
            elif action == "defend":
                defend(f)

        # Clean up dead fighters
        fighters = [f for f in fighters if f.is_alive()]

    # Final sorted values
    fighters = get_ordered()
    return [f.value for f in fighters]


def decide_action(f, above, below):
    # If already in correct local order, defend or idle
    if above and f.value >= above.value and below and f.value <= below.value:
        return random.choice(["defend", "defend", "attack_up", "attack_down"])

    # Prefer moving toward sorted position
    if above and f.value < above.value:
        # wants to move up
        if above.shield > 0:
            return "attack_up"
        return "move_up"

    if below and f.value > below.value:
        # wants to move down
        if below.shield > 0:
            return "attack_down"
        return "move_down"

    # If surrounded or low HP, defend
    if f.hp <= 3 or (above and below):
        return "defend"

    # Fallback: random poke
    return random.choice(["attack_up", "attack_down", "defend"])


def try_move(f, target, fighters, direction):
    # Blocked by shield → attack instead
    if target.shield > 0:
        attack(f, target)
        return

    # Swap positions
    old_pos = f.pos
    f.pos, target.pos = target.pos, old_pos


def attack(attacker, defender):
    # Damage shield first
    dmg = attacker.atk
    if defender.shield > 0:
        defender.shield -= dmg
        if defender.shield < 0:
            overflow = -defender.shield
            defender.shield = 0
            defender.hp -= max(1, overflow - defender.defense)
    else:
        defender.hp -= max(1, dmg - defender.defense)

    # Equal values → duel bonus
    if attacker.value == defender.value:
        defender.hp -= 1

    # Clamp
    if defender.hp < 0:
        defender.hp = 0


def defend(f):
    f.shield += 2
    f.hp = min(15, f.hp + 1)



class UndertaleProfile:
    def __init__(self):
        self.lv = 1          # Level of Violence
        self.mercy = 0
        self.karma = 0
        self.errors = 0

profile = UndertaleProfile()

def undertale_sort(arr):
    global profile

    # Error tracking
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        profile.errors += 1
        return arr

    swaps = 0
    chaos = 0

    # Violence or Mercy affects behaviour
    if profile.lv > profile.mercy:
        # Aggressive bubble sort
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1
                    chaos += abs(arr[j] - arr[j+1])
    else:
        # Gentle insertion sort
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
                swaps += 1
            arr[j+1] = key

    # Update profile
    profile.karma += chaos
    if swaps > len(arr):
        profile.lv += 1
    else:
        profile.mercy += 1

    return arr
def segregation_sort(arr, keep_separate=False):
    # Step 1: detect unsorted zones
    def split_into_clusters(lst):
        clusters = []
        current = [lst[0]]

        for i in range(1, len(lst)):
            if lst[i] >= lst[i-1]:
                current.append(lst[i])
            else:
                clusters.append(current)
                current = [lst[i]]

        clusters.append(current)
        return clusters

    # Step 2: recursively sort clusters
    def recursive_sort(cluster):
        if len(cluster) <= 1:
            return cluster

        subclusters = split_into_clusters(cluster)

        # If only one cluster, it's sorted
        if len(subclusters) == 1:
            return subclusters[0]

        # Otherwise sort each subcluster
        sorted_subs = [recursive_sort(sub) for sub in subclusters]

        if keep_separate:
            return sorted_subs  # keep as nested lists

        # Merge by boundaries
        merged = []
        for sub in sorted_subs:
            merged.extend(sub)
        return merged

    result = recursive_sort(arr)

    # Flatten if needed
    if keep_separate:
        return result
    else:
        return result
def heartbeat_sort(arr, beat_size=5):
    arr = sorted(arr)
    n = len(arr)

    # Split values into low, mid, high groups
    lows = arr[:n//3]
    mids = arr[n//3:2*n//3]
    highs = arr[2*n//3:]

    result = []
    i_low = i_mid = i_high = 0

    # Build heartbeat waveform
    while len(result) < n:
        # low → mid → high → mid → low
        if i_low < len(lows):
            result.append(lows[i_low]); i_low += 1
        if i_mid < len(mids):
            result.append(mids[i_mid]); i_mid += 1
        if i_high < len(highs):
            result.append(highs[i_high]); i_high += 1
        if i_mid < len(mids):
            result.append(mids[i_mid]); i_mid += 1
        if i_low < len(lows):
            result.append(lows[i_low]); i_low += 1

    return result[:n]
class Police:
    def __repr__(self):
        return "POLICE"

def police_sort(arr):
    arr = arr[:]  # copy
    police = Police()
    arr.insert(0, police)

    def is_criminal(i):
        if isinstance(arr[i], Police):
            return False
        # Criminal if out of sorted order
        return arr[i] != sorted([x for x in arr if not isinstance(x, Police)])[i-1]

    def find_criminal():
        for i in range(1, len(arr)):
            if is_criminal(i):
                return i
        return None

    while True:
        criminal_index = find_criminal()
        if criminal_index is None:
            break  # no criminals left

        police_index = arr.index(police)
        criminal_value = arr[criminal_index]

        # Criminal runs away from police
        while True:
            police_index = arr.index(police)
            criminal_index = arr.index(criminal_value)

            # Criminal direction: away from police
            if criminal_index < police_index:
                # criminal runs left
                if criminal_index == 0:
                    # cornered → arrested
                    arr.pop(criminal_index)
                    break
                # swap with left neighbour
                arr[criminal_index], arr[criminal_index-1] = arr[criminal_index-1], arr[criminal_index]
            else:
                # criminal runs right
                if criminal_index == len(arr)-1:
                    # cornered → arrested
                    arr.pop(criminal_index)
                    break
                arr[criminal_index], arr[criminal_index+1] = arr[criminal_index+1], arr[criminal_index]

            # Check if criminal fell into correct sorted position
            sorted_values = sorted([x for x in arr if not isinstance(x, Police)])
            correct_pos = sorted_values.index(criminal_value) + 1  # +1 because police is at index 0

            if criminal_index == correct_pos:
                # Criminal is safe
                break

            # Police moves one step toward criminal
            if police_index < criminal_index:
                arr[police_index], arr[police_index+1] = arr[police_index+1], arr[police_index]
            elif police_index > criminal_index:
                arr[police_index], arr[police_index-1] = arr[police_index-1], arr[police_index]

            # If police reaches criminal → arrest
            if arr.index(police) == arr.index(criminal_value):
                arr.pop(arr.index(criminal_value))
                break

    # Remove police
    arr.remove(police)
    return arr


class CorruptionSort:
    def __init__(self, corruption_rate=0.2):
        self.corruption_rate = corruption_rate
        self.rules = {
            "direction": 1,        # 1 = ascending, -1 = descending
            "frozen": set(),       # indices that never change
            "tolerance": 0,        # allowed violation margin
            "contradictions": []   # extra contradictory constraints
        }

    def valid(self, a, b):
        # Base rule: direction + tolerance
        if (a - b) * self.rules["direction"] > self.rules["tolerance"]:
            return False

        # Contradictory rules (rare)
        for rule in self.rules["contradictions"]:
            if not rule(a, b):
                return False

        return True

    def corrupt_rules(self, arr):
        roll = random.random()

        if roll < self.corruption_rate * 0.5:
            # Flip direction
            self.rules["direction"] *= -1
            print("⚠️ Corruption: Direction flipped")

        elif roll < self.corruption_rate * 0.8:
            # Freeze a random index
            idx = random.randint(0, len(arr) - 1)
            self.rules["frozen"].add(idx)
            print(f"⚠️ Corruption: Index {idx} frozen")

        elif roll < self.corruption_rate * 0.95:
            # Increase tolerance (allow violations)
            self.rules["tolerance"] += random.randint(1, 3)
            print(f"⚠️ Corruption: Tolerance increased to {self.rules['tolerance']}")

        else:
            # Add a contradictory rule
            def contradiction(a, b):
                return (a + b) % random.randint(2, 5) != 0

            self.rules["contradictions"].append(contradiction)
            print("⚠️ Corruption: Contradictory rule added")

    def sort(self, arr, max_cycles=50):
        arr = arr[:]  # copy so original isn't mutated

        for cycle in range(max_cycles):
            print(f"\n=== Cycle {cycle} ===")
            changed = False

            for i in range(len(arr) - 1):
                if i in self.rules["frozen"]:
                    continue

                # Randomize until valid under current rules
                while not self.valid(arr[i], arr[i+1]):
                    arr[i] = random.randint(0, 100)
                    changed = True

            # Corrupt rules after each cycle
            self.corrupt_rules(arr)

            # If nothing changed, we reached a "corrupted equilibrium"
            if not changed:
                print("✔️ Reached corrupted equilibrium")
                break

        return arr
import random

class ExplosiveSort:
    def __init__(self):
        self.blast_radius = 1
        self.damage = 1

    def explode(self, arr, index):
        # Apply damage to values within blast radius
        start = max(0, index - self.blast_radius)
        end = min(len(arr) - 1, index + self.blast_radius)

        for i in range(start, end + 1):
            arr[i] = max(0, arr[i] - self.damage)

        # 50% chance to increase blast radius
        if random.random() < 0.5:
            self.blast_radius += 1

        # 50% chance to increase damage
        if random.random() < 0.5:
            self.damage += 1

    def sort(self, arr):
        arr = arr[:]  # copy
        n = len(arr)

        # Bubble-sort style movement with explosions
        sorted_flag = False

        while not sorted_flag:
            sorted_flag = True

            for i in range(n - 1):
                # If out of order, attempt to swap
                if arr[i] > arr[i + 1]:
                    sorted_flag = False

                    # 50% chance to explode instead of swapping
                    if random.random() < 0.5:
                        self.explode(arr, i)
                    else:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]

        return arr


# Example usage
data = [40, 3, 18, 10, 20, 7]
es = ExplosiveSort()
result = es.sort(data)

print("Original:", data)
print("Explosive Sorted:", result)





def input_list():
    arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
    return arr

while True:
    print("""\nWelcome to Infinite Sort,where the ways to sort never end!
Current sorts avaivible:

1. Insert by min distance
2. Custom distance
3. Physics sort
4. Headphone sort
5. RPG sort
6. Undertale sort
7. Segregation sort
8. Heartbeat sort
9. Police sort
10. Corruption sort
11. Explosive sort""")
    sort = int(input("Please choose a sort:"))
    if sort == 1:
        arr = input_list()
        print("Sorting list by inserting each element at the position that minimizes the sum of distances to its neighbours...")
        s(2)
        print(f"Sorted list:{insert_by_min_distance(arr)}")
    elif sort == 2:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        print("Sorting list by minimizing the total distance to all other elements...")
        s(2)
        print(f"Sorted list:{custom_distance_sort(arr)}")
    elif sort == 3:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        print("Sorting list using physics-based simulation...")
        s(2)
        print(f"Sorted list:{physics_sort(arr)}")
    elif sort == 4:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        print("Sorting list using headphone-based sorting...")
        s(2)
        print(f"Sorted list:{headphone_sort(arr)}")
    elif sort == 5:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        print("Sorting list using RPG mechanics...")
        s(2)
        print(f"Sorted list:{rpg_sort(arr)}")
    elif sort == 6:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        print("Sorting list using Undertale mechanics...")
        s(2)
        print(f"Sorted list:{undertale_sort(arr)}")
    elif sort == 7:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        mode    = input("Do you want to keep clusters separate? (y/n, default n):").strip().lower() == 'y'
        print("Sorting list using Segregation mechanics...")
        s(2)
        print(f"Sorted list:{segregation_sort(arr, mode)}")
    elif sort == 8:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        heartbeat = int(input("Enter heartbeat size (default 5):") or 5)
        print("Sorting list using Heartbeat mechanics...")
        s(2)
        print(f"Sorted list:{heartbeat_sort(arr, heartbeat)}")
    elif sort == 9:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        print("Sorting list using Police mechanics...")
        s(2)
        print(f"Sorted list:{police_sort(arr)}")
    elif sort == 10:
        arr = list(map(int, input("Enter a list of numbers,seperated by a comma(,):").strip().split(",")))
        print("Sorting list using Corruption mechanics...")
        s(2)
        cs = CorruptionSort(corruption_rate=0.3)
        result = cs.sort(arr)
        print(f"Sorted list:{result}")
    elif sort == 11:
        arr = input_list()
        print("Sorting list using Explosive mechanics...")
        s(2)
        es = ExplosiveSort()
        result = es.sort(arr)
        print(f"Sorted list:{result}")
    else:
        print("Invalid sort")
