import random
import tkinter as tk

WIDTH = 800
HEIGHT = 400
NUM_BARS = 40


def generate_data():
    #Create a list of random bar heights
    return [random.randint(10, HEIGHT ) for i in range(NUM_BARS)]


def draw_bars(canvas, data):
    #Clear the canvas and draw one bar per value
    canvas.delete("all")
    bar_width = WIDTH / len(data)
    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = HEIGHT - value
        x1 = x0 + bar_width - 2
        canvas.create_rectangle(x0, y0, x1, HEIGHT, fill="steelblue", outline="")


def new_array():
    global data
    data = generate_data()
    draw_bars(canvas, data)


root = tk.Tk()
root.title("Algorithm Visualiser")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

tk.Button(root, text="New array", command=new_array).pack(pady=10)

data = generate_data()
draw_bars(canvas, data)

root.mainloop()
