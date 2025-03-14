from turtle import Turtle
from food import Food

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 260)  

    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("Game Over", align="center", font=("Poppins", 24, "bold"))
      
    def update_score(self):
        self.score += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
