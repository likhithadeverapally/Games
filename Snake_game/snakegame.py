from tkinter import *
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#000000"
G_WIDTH = 700
G_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"


class Food:
    def __init__(self):
        # Correct calculation for food's x and y position
        x = random.randint(0, (G_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (G_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canva.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canva.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)


def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canva.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1

        score_label.config(text="Score:{}".format(score))

        canva.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canva.delete(snake.squares[-1])

        del snake.squares[-1]
    if(check_collisions(snake,square)):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake,square):
    x,y =snake.coordinates[0]

    if x<0 or x>=G_WIDTH:
        return True
    elif y<0 or y>=G_HEIGHT:
        return True
    for body_part in snake.squares[1:]:
        if square==body_part:
            return True
        
def game_over():
    canva.delete(ALL)
    canva.create_text(G_WIDTH // 2, G_HEIGHT // 2, font=('consolas', 70), text="Game Over", fill="red", tag="gameover")
    window.after(2000, window.quit)  # Delay for 2 seconds, then stop the game

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
score_label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
score_label.pack()
canva = Canvas(window, bg=BACKGROUND_COLOR, height=G_HEIGHT, width=G_WIDTH)
canva.pack()
window.update()

w_width = window.winfo_width()
w_height = window.winfo_height()
s_width = window.winfo_screenwidth()
s_height = window.winfo_screenheight()

x = int((s_width / 2) - (w_width / 2))
y = int((s_height / 2) - (w_height / 2))

window.geometry(f"{w_width}x{w_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
