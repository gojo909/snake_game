# Snake Game

The classic Snake game built with Python's built-in turtle module, organized into OOP classes with a main game loop and a scoreboard that also tracks the all-time high score.

## Files

- **main.py** - Game loop, screen setup, and collision checks
- **snake.py** - Snake class: movement, growth, direction control
- **food.py** - Food class: random food placement on a 20px grid
- **scoreboard.py** - Scoreboard class: score, high score, game-over screen

## Run

```bash
python main.py
```

## Controls

- **Move**: Arrow keys
- **Restart after game over**: R
- **Quit**: Q

## Window Layout

The window is 600x700: a 600x600 play field with a 50px header strip at the top. The scoreboard lives in that header, outside the playable area, separated by a divider line.

The high score is saved in `high_score.txt` next to main.py.