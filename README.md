# Russian Roulette Game

This is a simple, text-based Russian Roulette game implemented in Python. It's a turn-based game designed for two players.

## How to Play

### Prerequisites
- Python 3.x

### Running the Game
To start the game, run the following command in your terminal:
```bash
python RussianRouletteGame_v1.py
```

### Game Rules
1.  **Two Players**: The game is played in a Player-vs-Player (PvP) mode.
2.  **Health Points**: Each player starts with 5 health points. The game ends when a player's health reaches 0.
3.  **The Gun**: The gun has a chamber with 6 slots. Before each round, it's randomly loaded with blanks (0) and live bullets (1).
4.  **Your Turn**: On your turn, you have two choices:
    *   Shoot yourself.
    *   Shoot your opponent.
5.  **Outcomes**:
    *   **Shooting yourself with a blank**: You are safe, and you get to take another turn.
    *   **Shooting yourself with a live bullet**: You lose 1 health point, and your turn ends.
    *   **Shooting your opponent with a blank**: Nothing happens, and your turn ends.
    *   **Shooting your opponent with a live bullet**: Your opponent loses 1 health point, and your turn ends.

**Note**: The gun is reloaded after every shot, which is a known issue.

## Future Development
A Player-vs-Environment (PvE) mode is planned for a future release, where a player can compete against an AI.
