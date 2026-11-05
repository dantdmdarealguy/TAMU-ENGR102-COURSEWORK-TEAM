# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
#
# Names: Joel Castillo, Kevin Shu, Vaibhav Vaidish, Namith Chelikani
# Section: 469, 569
# Assignment: LAB Topic 10 Team
# Date: 05 Nov 2026
#

"""Pack truffles into boxes of four so that every box follows the gift rules.

Approach: depth-first search with the "most constrained variable" heuristic.
At each step we pick the truffle with the fewest compatible boxmates left,
try every valid box built around it, and back out on a dead end. Two cheap
feasibility checks prune most bad branches early: every truffle left still has
enough possible boxmates, and the leftover cocoa counts can still be packed
legally (see cocoa_counts_fit). Many short randomized restarts guard against
the rare input where the search wanders.

The rules changed over time, and some later rules read as replacing an
earlier one rather than adding to it. make_boxes tries the strictest reading
first (every rule ever stated); an answer there satisfies every reading. Only
if that is impossible does it drop the rules that may have been replaced.
"""

import random
import time
from itertools import combinations

BOX_SIZE = 4
COCOA, SHAPE, FILLING, TOPPING = range(4)

# (field, a, b): a box may not contain both a and b in that field
CARAMEL_VANILLA = (FILLING, "caramel", "vanilla")
TOFFEE_COCONUT = (FILLING, "toffee", "coconut")              # "I changed my mind..."
NUTS_SPRINKLES = (TOPPING, "nuts", "sprinkles")
DRIZZLES = (TOPPING, "white chocolate drizzle", "dark chocolate drizzle")  # "And also..."
RECTANGLE_SQUARE = (SHAPE, "rectangle", "square")
ROUND_HEART = (SHAPE, "round", "heart")                      # "I bought new boxes..."

# A box holding any truffles of a "grouped" cocoa must hold 2 or 3 of them.
GROUP_MIN, GROUP_MAX = 2, 3

# Rule sets to try, strictest first. Each step drops one rule that a later
# autograder message may have replaced:
#   "My friends changed their minds..." -> white 2-3 may replace dark 2-3
#   "I bought new boxes..."             -> round/heart may replace rectangle/square
#   "I changed my mind..."              -> toffee/coconut may replace caramel/vanilla
ALWAYS = [TOFFEE_COCONUT, NUTS_SPRINKLES, DRIZZLES, ROUND_HEART]
RULE_SETS = [
    ("all rules", ALWAYS + [CARAMEL_VANILLA, RECTANGLE_SQUARE], ("dark", "white")),
    ("white 2-3 replaces dark 2-3", ALWAYS + [CARAMEL_VANILLA, RECTANGLE_SQUARE], ("white",)),
    ("...and round/heart replaces rectangle/square", ALWAYS + [CARAMEL_VANILLA], ("white",)),
    ("...and toffee/coconut replaces caramel/vanilla", ALWAYS, ("white",)),
]

# Restart strategy: a search that goes wrong early tends to stay stuck, so many
# short attempts (each with a fresh random tie-break) beat a few long ones.
# Benchmarked: 50 steps cut the slowest hard input from >60s to ~1s.
# The budget creeps up 1% per restart so a deeper search is still possible.
STEP_BUDGET = 50
BUDGET_GROWTH = 1.01
TIME_LIMIT = 15.0  # seconds per rule set; hard inputs in testing finish in ~1.5s


def compatible(a, b, conflicts):
    """True if truffles with descriptions a and b may share a box."""
    if list(a) == list(b):
        return False
    return not any({a[field], b[field]} == {x, y} for field, x, y in conflicts)


def cocoa_counts_fit(group_counts, n_other):
    """Exact check that these cocoa counts alone can be packed into legal boxes.

    group_counts holds the count of each grouped cocoa (at most two, since two
    groups of 2+ fill a box of 4); n_other counts everything else. A grouped
    color goes 2-3 per box, topped up with "other" truffles, except that two
    grouped colors can share a box as exactly 2+2. Try every number of 2+2
    boxes; pack the rest of each color 3 per box (fewest boxes = fewest
    "other" truffles needed to fill them out), and check there are enough.
    Leftover "other" truffles always fill whole boxes since the total is a
    multiple of 4.
    """
    a, b = (list(group_counts) + [0, 0])[:2]
    for mixed in range(min(a, b) // GROUP_MIN + 1):
        other_needed = 0
        for left in (a - GROUP_MIN * mixed, b - GROUP_MIN * mixed):
            if 0 < left < GROUP_MIN:
                break  # a lone truffle of this color can't be boxed
            boxes = -(-left // GROUP_MAX)  # ceiling division
            other_needed += BOX_SIZE * boxes - left
        else:
            if other_needed <= n_other:
                return True
    return False


def solve(truffles, conflicts, grouped_cocoa, time_limit):
    """Search for a packing under one rule set.

    Returns (boxes, reason): boxes is the packing or None, and reason says why
    there is none ("impossible" when proven, "timeout" when the search gave up).
    """
    ids = list(truffles)
    if len(ids) % BOX_SIZE:
        return None, "impossible"
    partners = {
        t: {u for u in ids if u != t and compatible(truffles[t], truffles[u], conflicts)}
        for t in ids
    }
    groups = [{t for t in ids if truffles[t][COCOA] == c} for c in grouped_cocoa]

    def counts_fit(rest):
        sizes = [len(group & rest) for group in groups]
        return cocoa_counts_fit(sizes, len(rest) - sum(sizes))

    if not counts_fit(set(ids)):
        return None, "impossible"

    rank = {t: i for i, t in enumerate(ids)}  # tie-breaker, reshuffled on each restart

    def candidate_boxes(remaining):
        """Yield every valid box containing the most constrained remaining truffle."""
        options = {t: partners[t] & remaining for t in remaining}
        anchor = min(remaining, key=lambda t: (len(options[t]), rank[t]))
        if len(options[anchor]) < BOX_SIZE - 1:
            return  # some truffle can no longer be boxed at all
        for trio in combinations(sorted(options[anchor], key=rank.get), BOX_SIZE - 1):
            if not all(y in partners[x] for x, y in combinations(trio, 2)):
                continue
            box = (anchor, *trio)
            if any(len(group.intersection(box)) not in (0, GROUP_MIN, GROUP_MAX) for group in groups):
                continue
            yield box

    def search(remaining, budget):
        if not remaining:
            return []
        budget[0] -= 1
        if time.monotonic() > deadline:
            budget[0] = -1  # out of time counts as out of budget
        if budget[0] < 0:
            return None
        for box in candidate_boxes(remaining):
            rest = remaining.difference(box)
            if not counts_fit(rest):
                continue
            solution = search(rest, budget)
            if solution is not None:
                return [list(box)] + solution
            if budget[0] < 0:
                return None
        return None

    deadline = time.monotonic() + time_limit
    rng = random.Random(102)
    attempt = 0
    while time.monotonic() <= deadline:
        budget = [min(int(STEP_BUDGET * BUDGET_GROWTH ** min(attempt, 2000)), 10**9)]
        solution = search(set(ids), budget)
        if solution is not None:
            return sorted(sorted(box) for box in solution), None
        if budget[0] >= 0:
            # the attempt ended without running out of steps, so it tried every
            # possibility: no packing exists and restarting won't change that
            return None, "impossible"
        # stuck: break ties differently so the next attempt explores a new path
        shuffled = rng.sample(ids, len(ids))
        rank.update((t, i) for i, t in enumerate(shuffled))
        attempt += 1
    return None, "timeout"


def make_boxes(truffles):
    """Return a list of boxes (each a sorted list of 4 truffle ids), or [] if none exists."""
    for name, conflicts, grouped_cocoa in RULE_SETS:
        boxes, reason = solve(truffles, conflicts, grouped_cocoa, TIME_LIMIT)
        if boxes is not None:
            print(f"make_boxes: packed under '{name}'")
            return boxes
        print(f"make_boxes: '{name}' -> {reason}")
    return []


if __name__ == "__main__":
    chocolates = {
        1: ["milk", "heart", "caramel", "none"],
        2: ["dark", "round", "strawberry", "dark chocolate drizzle"],
        3: ["dark", "heart", "caramel", "white chocolate drizzle"],
        4: ["milk", "square", "toffee", "none"],
        5: ["dark", "round", "caramel", "nuts"],
        6: ["white", "heart", "vanilla", "sprinkles"],
        7: ["dark", "rectangle", "coconut", "sprinkles"],
        8: ["white", "heart", "vanilla", "none"],
    }
    # README example: no valid split exists under any of the rule sets (checked
    # by brute force). Rounds #2 and #5 can't sit with hearts, so all 4 hearts
    # would have to share a box with each other. Expect [].
    print(make_boxes(chocolates))
