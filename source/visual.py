import random
import time
import pygame
import cv2 as cv
import sys
import numpy as np
import os
import pyautogui as pg
from tkinter import *
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk, ImageDraw, ImageGrab, ImageEnhance

last_x, last_y = None, None
canvas = None
drawing = True
drawing_color = "orange"
user_drawings = []
drawing_mask = None

letter_to_audio = {
    'A' : 'A.mp3',
    'B' : 'B.mp3',
    'C' : 'C.mp3',
    'D' : 'D.mp3',
    'E' : 'E.mp3',
    'F' : 'F.mp3',
    'G' : 'G.mp3',
    'H' : 'H.mp3',
    'I' : 'I.mp3',
    'J' : 'J.mp3',
    'K' : 'K.mp3',
    'L' : 'L.mp3',
    'M' : 'M.mp3',
    'N' : 'N.mp3',
    'O' : 'O.mp3',
    'P' : 'P.mp3',
    'Q' : 'Q.mp3',
    'R' : 'R.mp3',
    'S' : 'S.mp3',
    'T' : 'T.mp3',
    'U' : 'U.mp3',
    'V' : 'V.mp3',
    'W' : 'W.mp3',
    'X' : 'X.mp3',
    'Y' : 'Y.mp3',
    'Z' : 'Z.mp3',
    '0' : '1.mp3',
    '1' : '1.mp3',
    '2' : '2.mp3',
    '3' : '3.mp3',
    '4' : '4.mp3',
    '5' : '5.mp3',
    '6' : '6.mp3',
    '7' : '7.mp3',
    '8' : '8.mp3',
    '9' : '9.mp3'
}

currently_displayed_letter = None

def toggle_draw_mode():
    global drawing
    drawing = not drawing
    if drawing:
        draw_button.config(text="Draw Mode", bg="red")
    else:
        draw_button.config(text="Draw Mode", bg="SystemButtonFace")

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y, canvas, drawing_color, erase_color
    x, y = event.x, event.y
    if last_x is not None and last_y is not None and canvas is not None:
        if drawing:
            line = canvas.create_line(last_x, last_y, x, y, fill=drawing_color, width=22)
            user_drawings.append(line)
    last_x, last_y = x, y

def erase_all():
    canvas.delete("all")

def erase_user_drawings():
    global user_drawings
    for drawing_item in user_drawings:
        canvas.delete(drawing_item)
    user_drawings = []

def create_drawing_mask():
    global drawing_mask
    drawing_mask = Image.new("L", (canvas.winfo_width(), canvas.winfo_height()))
    draw = ImageDraw.Draw(drawing_mask)

    for drawing_item in user_drawings:
        coords = canvas.coords(drawing_item)
        if coords and len(coords) == 4:
            x0, y0, x1, y1 = coords
            if x1 >= x0:
                draw.rectangle([x0, y0, x1, y1], fill=255)

def handle_key(event):
    if event.keysym == "e" or event.keysym == "E":
        erase_all()
    if event.keysym == 'l' or event.keysym == 'L':
        erase_user_drawings()

def load_image():
    global drawing_mask, currently_displayed_letter
    alphabet_selection = "/Users/maanitmalhan/Documents/Python/T.A.L.L/ref_pics" # Place to change files for background image (change as necessary)
    letter_images = [f for f in os.listdir(alphabet_selection) if f.endswith(".png")]

    chosen_letter = random.choice(letter_images)
    currently_displayed_letter = chosen_letter[0]
    letter_image = Image.open(os.path.join(alphabet_selection, chosen_letter))

    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    desired_width = 200 
    desired_height = 200

    letter_image = letter_image.resize((desired_width, desired_height))

    x_position = (canvas_width - desired_width) // 2
    y_position = (canvas_height - desired_height) // 2

    drawing_mask = Image.new("L", (canvas_width, canvas_height), 0)
    drawing_mask.paste(255, (x_position, y_position, x_position + desired_width, y_position + desired_height))

    brightness_level = 1
    enhancer = ImageEnhance.Brightness(letter_image)
    letter_image = enhancer.enhance(brightness_level)

    if letter_image.mode == "RGBA":
        alpha = 100
        r, g, b, a = letter_image.split()
        a = a.point(lambda p: p * alpha / 255)
        letter_image.putalpha(a)

    background_image = ImageTk.PhotoImage(letter_image)
    canvas.create_image(0, 0, anchor=NW, image=background_image)
    canvas.image = background_image

    play_corresponding_audio()

def play_corresponding_audio(): 
    global currently_displayed_letter
    if currently_displayed_letter:
        audio_file = letter_to_audio.get(currently_displayed_letter.upper()) 
        if audio_file:
            audio_file_path = os.path.join("/Users/maanitmalhan/Documents/Python/T.A.L.L/audio", audio_file)
            play_audio(audio_file_path)



def play_audio(audio_file_path):
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

def captureImg():
    cap = cv.VideoCapture(0) # Video Capture
    cap.set(cv.CAP_PROP_FRAME_WIDTH,800) # Width
    cap.set(cv.CAP_PROP_FRAME_HEIGHT,800)  # Height

    while True:
        success, img = cap.read() # Read image from camera
        cv.imshow("Result", img) # Show image
        if cv.waitKey(1) & 0xFF == ord('q'): # Press q to exit
            cv.imwrite("/Users/maanitmalhan/Desktop/tst.png", img) # Save image
            break
    
    imager = cv.imread("/Users/maanitmalhan/Desktop/tst.png") # Read image
    gray = cv.cvtColor(imager, cv.COLOR_BGR2GRAY)
    
    cv.imwrite("/Users/maanitmalhan/Desktop/tst.png", gray) # Save image
    cap.release() # Release camera
    cv.destroyAllWindows() # Destroy all windows    

def checkTrace(traced_image_path = "canvas_snapshot.png", reference_image_path= currently_displayed_letter, threshold=0.9):
    traced_image = cv.imread(traced_image_path, cv.IMREAD_GRAYSCALE)
    reference_image = cv.imread(reference_image_path, cv.IMREAD_GRAYSCALE)

    trace_edges = cv.Canny(traced_image, threshold1=50, threshold2=150)  
    ref_edges = cv.Canny(reference_image, threshold1=50, threshold2=150)  
    # Get the width and height of the reference image  
    imgWidth = 248
    imgHeight = 248

    # Resize the traced image to the same size as the reference image
    traced_image = cv.resize(trace_edges, (imgWidth, imgHeight))
    reference_image = cv.resize(ref_edges, (imgWidth, imgHeight))

    #cv.imwrite("/Users/maanitmalhan/Documents/Tra_Image.png", traced_image)
    #cv.imwrite("/Users/maanitmalhan/Documents/Refece_Image.png", reference_image)
    # Get the difference between the traced image and the reference image

    result = cv.matchTemplate(traced_image, reference_image, cv.TM_CCOEFF_NORMED)

    # Get the best match location
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Determine if the traced image matches the reference
    if max_val >= threshold:
        return True
    else:
        return False

def submit():
    global canvas
    x0 = canvas_frame.winfo_rootx()
    y0 = canvas_frame.winfo_rooty()
    x1 = x0 + canvas_frame.winfo_reqwidth() + 225
    y1 = y0 + canvas_frame.winfo_reqheight() + 165


    pg.screenshot("/Users/maanitmalhan/desktop")
    
    print("Canvas snapshot saved as 'canvas_snapshot.png'")

    #checkTrace()

pygame.mixer.init()


root = Tk()
root.geometry("800x600")
root.title("Visual")

style = ThemedStyle()
style.set_theme("plastik")

canvas_frame = Frame(root, width=400, height=400, borderwidth=8, relief="solid")
canvas_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(canvas_frame, bg="#ebe6d8")
canvas.grid(row=0, column=0)

draw_button = Button(root, text="Draw Mode", bg="red", command=toggle_draw_mode)
draw_button.grid(row=1, column=0, padx=10, pady=5)

audio_button = Button(root, text="Play Audio", command=play_corresponding_audio)
  # Path to audio file (specific audio file unlike background image file path)
audio_button.grid(row=3, column=1, padx=10, pady=10)

load_button = Button(root, text="Load Image", command=load_image)
load_button.grid(row=3, column=0, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, padx=10, pady=10)

root.bind("<KeyPress>", handle_key)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()
