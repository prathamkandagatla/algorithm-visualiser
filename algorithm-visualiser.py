import random
import tkinter as tk

WIDTH = 800
HEIGHT = 400
NUM_BARS = 40
DELAY_MS = 20 #delay in steps to see sorting
data = []
sorting = None #holds the status of the sort generator

def generate_data():
    #Create a list of random bar heights
    return [random.randint(10, HEIGHT - 20 ) for i in range(NUM_BARS)]


def draw_bars(canvas, data, highlight=(), done=False):
    #Clear the canvas and draw one bar per value
    canvas.delete("all")
    bar_width = WIDTH / len(data)
    for i, value in enumerate(data):
        if done:
            colour = "seagreen"
        elif i in highlight:
            colour = "red"
        else:
            colour="steelblue"
        x0 = i * bar_width
        y0 = HEIGHT - value
        x1 = x0 + bar_width - 2
        canvas.create_rectangle(x0, y0, x1, HEIGHT, fill=colour, outline="")

def start_sort():
    global sorting
    if sorting is None:  # ignore clicks while already sorting
        sorting = bubble_sort(data)
        step()

def new_array():
    global data
    if sorting is None:  #Stops data from being randomised mid swap
        data = generate_data()
        draw_bars(canvas, data)
    
def bubble_sort(data):
    #Bubble sort that yields the pair of indices it just compared
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield (j, j + 1)
            
def step():
    #Advance the sort by one comparison, redraw, and schedule the next step
    global sorting#sets the sorting status
    try:
        highlight = next(sorting)
        draw_bars(canvas, data, highlight)
        root.after(DELAY_MS, step)
    except StopIteration:
        draw_bars(canvas, data, done=True)
        sorting = None


root = tk.Tk()
root.title("Algorithm Visualiser")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

controls = tk.Frame(root)
controls.pack(pady=10)
tk.Button(controls, text="New array", command=new_array).pack(side="left", padx=5)
tk.Button(controls, text="Bubble sort", command=start_sort).pack(side="left", padx=5)

data = generate_data()
draw_bars(canvas, data)

root.mainloop()
