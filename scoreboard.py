from turtle import Turtle
from food import Food



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt", mode="r") as data:
                self.high_score = int(data.read())

        except (FileNotFoundError, ValueError):
            # If file doesn't exist or doesn't contain a valid number
            self.high_score = 0
            with open("data.txt", mode="w") as data:
                data.write("0")

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

      
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}, High Score:{self.high_score}", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:  
            self.high_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    