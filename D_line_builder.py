from collections import defaultdict
import random

# --- CONFIGURABLE PARAMETERS ---
TOTAL_INNINGS = 8
FIELD_POSITIONS = ["C", "1B", "2B", "3B", "SS", "LF", "LR", "CF", "RR", "RF"]
MIN_INNINGS_DEFAULT = 2
MAX_MALE_INNINGS = 5  # Add this line after your other configurable parameters
MAX_FEMALE_INNINGS = 7  # Add this line to set max innings for females
REQUIRED_MALES = 6
REQUIRED_FEMALES = 4
TOP_DEFENDERS = {"Adam", "Isaac", "Jaden", "Russell", "Nick", "Zach", "Carlos", "Christian"}

# --- PLAYER DATA ---
players = {
    # Males
    "Adam":        {"gender": "M", "positions": ["CF", "LF", "RF", "SS"]},
    "Carlos":      {"gender": "M", "positions": ["3B", "2B"]},
    "Christian":   {"gender": "M", "positions": ["LF", "CF", "RF", "SS", "2B", "3B"]},
    "Elliot":      {"gender": "M", "positions": ["LF", "RF", "LR", "RR"], "fixed_innings": 2},
    "Emile":       {"gender": "M", "positions": ["RF", "LF", "LR", "RR"]},
    "Isaac":       {"gender": "M", "positions": ["LF", "RF", "3B", "2B", "SS"]},
    "Jaden":       {"gender": "M", "positions": ["SS", "2B", "3B", "RF", "LF", "CF"]},
    "Jed":         {"gender": "M", "positions": ["RF", "LF", "RR", "LR"]},
    # "Keith":       {"gender": "M", "positions": ["LF", "RF", "CF"]},
    "Matthew":     {"gender": "M", "positions": ["RF", "LF", "RR", "LR"]},
    "Nick":        {"gender": "M", "positions": ["3B", "1B"]},
    "Russell":     {"gender": "M", "positions": ["SS", "CF", "RF", "LF"]},
    "Theodore":    {"gender": "M", "positions": ["LF", "RF", "LR", "RR"]},
    "Timothy":     {"gender": "M", "positions": ["RF", "LR", "RR", "LF"], "fixed_innings": 2},
    "Zachary":     {"gender": "M", "positions": ["CF", "RF", "LF", "SS", "3B"]},

    # Females
    "Cat":         {"gender": "F", "positions": ["C", "2B"]},
    # "Elina":       {"gender": "F", "positions": ["LR", "RR", "C"]},
    "Emily":       {"gender": "F", "positions": ["RR", "LR"]},
    # "Izzy":        {"gender": "F", "positions": ["1B", "2B"]},
    "Janice":      {"gender": "F", "positions": ["1B", "2B", "C"]},
    # "Rina":        {"gender": "F", "positions": ["C", "LR", "RR"]},
    # "Jenn":        {"gender": "F", "positions": ["LR", "RR", "C"]},
    "Priscilla":   {"gender": "F", "positions": ["C"], "fixed_innings": 4},
    "Tweety":      {"gender": "F", "positions": ["LR", "RR", "C"]}
}

# --- Utility Structures ---
class LineupBuilder:
    def __init__(self, players):
        self.players = players
        self.lineups = [{} for _ in range(TOTAL_INNINGS)]
        self.play_counts = defaultdict(int)
        self.female_rest_tracker = defaultdict(int)

    def is_valid_assignment(self, inning, assignments):
        males = sum(1 for p in assignments.values() if self.players[p]["gender"] == "M")
        females = sum(1 for p in assignments.values() if self.players[p]["gender"] == "F")
        top_defenders = sum(1 for p in assignments.values() if p in TOP_DEFENDERS)
        return males == REQUIRED_MALES and females == REQUIRED_FEMALES and top_defenders >= 3

    def assign_positions(self):
        available_players = list(self.players.keys())
        # Track how many innings each player has played
        for inning in range(TOTAL_INNINGS):
            success = False
            attempts = 0
            while not success and attempts < 10000:
                assigned = {}
                random.shuffle(available_players)
                used = set()

                for pos in FIELD_POSITIONS:
                    for p in available_players:
                        if p not in used and pos in self.players[p]["positions"]:
                            # Fixed innings check
                            max_innings = self.players[p].get("fixed_innings", TOTAL_INNINGS)
                            # Apply male/female innings limit
                            if self.players[p]["gender"] == "M":
                                max_innings = min(max_innings, MAX_MALE_INNINGS)
                            elif self.players[p]["gender"] == "F":
                                max_innings = min(max_innings, MAX_FEMALE_INNINGS)
                            if self.play_counts[p] >= max_innings:
                                continue
                            assigned[pos] = p
                            used.add(p)
                            break

                if len(assigned) == len(FIELD_POSITIONS) and self.is_valid_assignment(inning, assigned):
                    self.lineups[inning] = assigned
                    for p in assigned.values():
                        self.play_counts[p] += 1
                    success = True
                else:
                    attempts += 1

            if not success:
                raise Exception(f"Unable to create a valid lineup for inning {inning + 1} after {attempts} attempts")

        # Ensure every player has played at least MIN_INNINGS_DEFAULT innings
        for p in self.players:
            min_innings = self.players[p].get("fixed_innings", MIN_INNINGS_DEFAULT)
            if self.play_counts[p] < min_innings:
                raise Exception(f"Player {p} assigned only {self.play_counts[p]} innings, less than minimum required {min_innings}")

    def print_lineup(self):
        for i, inning in enumerate(self.lineups):
            print(f"\nInning {i + 1}:")
            for pos in FIELD_POSITIONS:
                player = inning.get(pos, "[unassigned]")
                print(f"  {pos}: {player}")
        print("\nInning Summary:")
        for player, count in sorted(self.play_counts.items()):
            print(f"{player}: {count} innings")

# --- Run Builder ---
builder = LineupBuilder(players)
builder.assign_positions()
builder.print_lineup()
