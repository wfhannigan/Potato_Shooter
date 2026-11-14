A turn-based command-line survival shooter written in Python. Battle against increasingly tough opponents, manage your cash, and upgrade your gear to survive as many rounds as possible.

Overview

In Potato Shooter, you start with $20, 20 HP, and a basic pistol dealing 5 damage. Each round, you face off against an opponent whose starting health increases by +5 HP every time you win. Defeating an opponent earns you $10 to spend on healing, shields, or weapon upgrades.

Features

• Turn-Based Combat: Choose between shooting, dodging, visiting the shop, or quitting each turn.
• Probability-Based Attacks: Both you and your opponent have an 80% chance to hit (4 in 5) when firing.
• In-Game Shop: Spend your winnings on survival items and upgrades—watch out, though; opening the shop leaves you open to an opponent's shot!
	• Health Potion ($10): Restores +10 HP.
	• Better Gun ($30): Increases weapon damage by +5 (also increases opponent gun stat).
	• Shield ($30): Grants +20 HP.
• Progressive Difficulty: Opponents scale in health each round (20 HP, 25 HP, 30 HP, etc.) until your health drops to zero.
• Custom Currency Protection: Uses a custom PositiveNumber dataclass with operator overloading (+=, -=, <, >) to format cash values and prevent spending money you don't have.

How to Run


Prerequisites

• Python 3.10+ (required for match/case structural pattern matching)

Launch the Game

1. Clone the repository:bash
git clone https://github.com
cd Potato_Shooter
Use code with caution.
2. Run the script:bash
python main.py
Use code with caution.

Controls

During each turn, type one of the following commands:
• shoot — Fire your weapon at the opponent while they fire back at you.
• dodge — Avoid the opponent's incoming bullet for the turn.
• buy — Open the shop menu to purchase potions, shields, or gun upgrades.
• quit — Exit the game.
