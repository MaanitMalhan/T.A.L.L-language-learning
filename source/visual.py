from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

last_x, last_y = None, None
canvas = None
drawing = True
background_image = None
drawing_color = "orange"
erase_color = "#ebe6d8"

def toggle_draw_mode():
    global drawing
    drawing = not drawing
    if drawing:
        draw_button.config(text="Draw Mode", bg="red")
        erase_button.config(text="Erase Mode", bg="SystemButtonFace")
    else:
        draw_button.config(text="Draw Mode", bg="SystemButtonFace")
        erase_button.config(text="Erase Mode", bg="red")

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y, canvas, drawing_color, erase_color
    x, y = event.x, event.y
    if last_x is not None and last_y is not None and canvas is not None:
        if drawing:
            canvas.create_line(last_x, last_y, x, y, fill=drawing_color, width=30)
        else:
            canvas.create_line(last_x, last_y, x, y, fill=erase_color, width=20)
    last_x, last_y = x, y

def erase_all():
    canvas.delete("all")

def handle_key(event):
    if event.keysym == "e" or event.keysym == "E":
        erase_all()

def load_image():
    global background_image
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        image = Image.open(file_path)
    alpha = 0.5
    enhancer = ImageEnhance.Brightness(image)
    background_image = ImageTk.PhotoImage(enhancer.enhance(alpha))
    canvas.create_image(0, 0, anchor=NW, image=background_image)

def submit():
    global user_drawings
    temp_image = Image.new("RGBA", (canvas.winfo_width(), canvas.winfo_height()))

    if background_image:
        temp_image.paste(background_image, (0,0))

    for drawing_item in user_drawings:
        canvas_item = canvas.itemcget(drawing_item, "image")
        if canvas_item:
            item_image = ImageTk.getimage(canvas_item)
            temp_image.paste(item_image, (0,0), item_image)

    temp_image.save("traced_drawings.png")
    print("Traced drawing saved as 'traced_drawings.png'")

root = Tk()
root.geometry("1200x800")
root.title("Visual")

canvas_frame = Frame(root, borderwidth=8, relief="solid")
canvas_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(canvas_frame, width=600, height=400, bg="#ebe6d8")
canvas.grid(row=0, column=0)

draw_button = Button(root, text="Draw Mode", bg="red", command=toggle_draw_mode)
draw_button.grid(row=1, column=0, padx=10, pady=10)

erase_button = Button(root, text="Erase Mode", bg="SystemButtonFace", command=toggle_draw_mode)
erase_button.grid(row=2, column=0, padx=10, pady=10)

load_button = Button(root, text="Load Image", command=load_image)
load_button.grid(row=3, column=0, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, padx=10, pady=10)

root.bind("<KeyPress>", handle_key)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()