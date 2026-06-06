# Game by Bungsu

A simple object-dodging game built with Python and Pygame.

## Description

"Game Hindar Objek" is a fast-paced survival game where you control a blue square and must avoid falling red squares (enemies). The longer you survive, the higher your score! Be careful, as the enemies will fall faster as your score increases.

## Features

- **Simple Controls**: Use the Left and Right arrow keys to move.
- **Progressive Difficulty**: The falling speed of the enemies increases every 10 points.
- **Score Tracking**: Keep track of how many objects you've successfully dodged.

## Requirements

- Python 3.x
- Pygame

You can run the game easily with [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver. `uv run` will automatically install Pygame in an isolated environment and run the script:

```bash
uv run --with pygame game_by_bungsu.py
```

Alternatively, you can install Pygame manually using `pip` or `uv pip`:
```bash
pip install pygame
```

## How to Play

1. Run the game script:
   ```bash
   uv run --with pygame game_by_bungsu.py
   # OR if you already installed pygame manually:
   python game_by_bungsu.py
   ```
2. Use the **Left Arrow** and **Right Arrow** keys to move the blue square horizontally.
3. Dodge the falling red squares.
4. The game ends when a red square hits you ("KELARR").

Enjoy the game!