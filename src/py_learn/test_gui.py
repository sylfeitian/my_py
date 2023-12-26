#!/usr/bin/python3

import random
import tkinter as tk


class Snake:
    def __init__(self, canvas, food):
        self.canvas = canvas
        self.direction = (1, 0)
        self.segments = [(60, 60), (50, 60), (40, 60)]
        self.color = "green"
        self.food = food
        self.draw()

    def draw(self):
        self.canvas.delete("snake")
        for x, y in self.segments:
            self.canvas.create_rectangle(
                x, y, x + 10, y + 10, fill=self.color, tags="snake"
            )

    def move(self):
        dx, dy = self.direction
        x, y = self.segments[0]
        x += dx * 10
        y += dy * 10
        self.segments.insert(0, (x, y))
        if x < 0 or x > 290 or y < 0 or y > 190 or (x, y) in self.segments[1:]:
            raise Exception("Game Over")
        if (x, y) == self.food.position:
            self.food.eaten()
        else:
            self.segments.pop()
        self.draw()

    def set_direction(self, direction):
        dx, dy = self.direction
        dx_new, dy_new = direction
        if dx + dx_new != 0 or dy + dy_new != 0:
            self.direction = (dx_new, dy_new)


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.position = (0, 0)
        self.color = "red"
        self.draw()

    def draw(self):
        x, y = self.position
        self.canvas.create_oval(x, y, x + 10, y + 10, fill=self.color, tags="food")

    def eaten(self):
        self.canvas.delete("food")
        self.position = (random.randrange(0, 30) * 10, random.randrange(0, 20) * 10)
        self.draw()


class Game:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=500, height=700, bg="white")
        self.canvas.pack()
        self.food = Food(self.canvas)
        self.snake = Snake(self.canvas, self.food)
        self.master.bind("<Key>", self.key_pressed)
        self.master.after(100, self.animation)

    def key_pressed(self, event):
        if event.keysym == "Left":
            self.snake.set_direction((-1, 0))
        elif event.keysym == "Right":
            self.snake.set_direction((1, 0))
        elif event.keysym == "Up":
            self.snake.set_direction((0, -1))
        elif event.keysym == "Down":
            self.snake.set_direction((0, 1))

    def animation(self):
        try:
            self.snake.move()
        except Exception as e:
            self.master.destroy()
            print(e)
            return
        self.master.after(100, self.animation)


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
