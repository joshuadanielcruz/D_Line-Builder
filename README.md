🥎 Softball Lineup Builder

This Python script generates an automated defensive lineup for a co-ed softball team, enforcing specific team constraints and optimizing for player preferences.

📋 Features

Automatically builds valid defensive lineups for 8-inning softball games

Enforces rules:

6 males and 4 females on the field at all times

Minimum of 2 innings per player (unless otherwise specified)

Position eligibility based on each player's ranked preferences

At least 3 of the top 8 defenders in every inning

Ensures all female players rest for at least 1 inning

Allows player availability filtering and custom inning limits

Outputs:

Full inning-by-inning lineup with position assignments

Total innings played by each player

⚙️ Requirements

Python 3.7 or higher

No external libraries required (uses built-in collections and random)

🚀 Usage

Clone the repository:

git clone https://github.com/yourusername/softball-lineup-builder.git
cd softball-lineup-builder

Run the script:

python softball_lineup.py

👤 Player Configuration

Player preferences and other info are stored in the players dictionary inside softball_lineup.py.

Each player follows this structure:

"Player Name": {
    "gender": "M" or "F",
    "positions": ["Ranked", "Preferred", "Positions"],
    "fixed_innings": 2  # optional
}

🔧 Customization

To change player availability, comment out or remove entries from the players dictionary.

To limit a player's innings, add the "fixed_innings" key.

Modify the TOP_DEFENDERS set or other rules as needed in the config section.

📈 Example Output

Inning 1:
  C: Cat
  1B: Izzy
  2B: Carlos
  3B: Nick
  SS: Adam
  LF: Christian
  LR: Jenn
  CF: Isaac
  RR: Emily
  RF: Zach

... (more innings)

Inning Summary:
Adam: 3 innings
Izzy: 2 innings
...

🧠 Future Improvements

Smarter optimization (maximize preference satisfaction)

UI or web version for team managers

Substitution or injury overrides
