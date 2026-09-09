from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 28, "bold")
SCORE_Y = 325  # inside the header strip, above the play field
HIGH_SCORE_FILE = "high_score.txt"


class Scoreboard(Turtle):
    """Shows the current score, the all-time high score, and game-over text."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = self._load_high_score()
        self.update_scoreboard()

    def _load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def _save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.goto(0, SCORE_Y)
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -40)
        self.write("Press R to restart or Q to quit", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.score = 0
        self.update_scoreboard()