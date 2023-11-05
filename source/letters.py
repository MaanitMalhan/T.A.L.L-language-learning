import cv2 as cv
import numpy as np
import pygame 

def audioButton():
    letter_image = "chosen_letter"
    if letter_image == "a":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/a.m4a")
        pygame.mixer.music.play()
    elif letter_image == "b":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/b.m4a")
        pygame.mixer.music.play()
    elif letter_image == "c":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/c.m4a")
        pygame.mixer.music.play()
    elif letter_image == "d":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/d.m4a")
        pygame.mixer.music.play()
    elif letter_image == "e":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/e.m4a")
        pygame.mixer.music.play()
    elif letter_image == "f":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/f.m4a")
        pygame.mixer.music.play()
    elif letter_image == "g":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/g.m4a")
        pygame.mixer.music.play()
    elif letter_image == "h":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/h.m4a")
        pygame.mixer.music.play()
    elif letter_image == "i":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/i.m4a")
        pygame.mixer.music.play()
    elif letter_image == "j":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/j.m4a")
        pygame.mixer.music.play()
    elif letter_image == "k":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/k.m4a")
        pygame.mixer.music.play()
    elif letter_image == "l":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/l.m4a")
        pygame.mixer.music.play()
    elif letter_image == "m":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/m.m4a")
        pygame.mixer.music.play()
    elif letter_image == "n":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/n.m4a")
        pygame.mixer.music.play()
    elif letter_image == "o":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/o.m4a")
        pygame.mixer.music.play()
    elif letter_image == "p":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/p.m4a")
        pygame.mixer.music.play()
    elif letter_image == "q":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/q.m4a")
        pygame.mixer.music.play()
    elif letter_image == "r":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/r.m4a")
        pygame.mixer.music.play()
    elif letter_image == "s":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/s.m4a")
        pygame.mixer.music.play()
    elif letter_image == "t":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/t.m4a")
        pygame.mixer.music.play()
    elif letter_image == "u":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/u.m4a")
        pygame.mixer.music.play()
    elif letter_image == "v":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/v.m4a")
        pygame.mixer.music.play()
    elif letter_image == "w":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/w.m4a")
        pygame.mixer.music.play()
    elif letter_image == "x":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/x.m4a")
        pygame.mixer.music.play()
    elif letter_image == "y":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/y.m4a")
        pygame.mixer.music.play()
    elif letter_image == "z":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/z.m4a")
        pygame.mixer.music.play()
    elif letter_image == "0":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/0.m4a")
        pygame.mixer.music.play()
    elif letter_image == "1":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/1.m4a")
        pygame.mixer.music.play()
    elif letter_image == "2":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/2.m4a")
        pygame.mixer.music.play()
    elif letter_image == "3":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/3.m4a")
        pygame.mixer.music.play()
    elif letter_image == "4":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/4.m4a")
        pygame.mixer.music.play()
    elif letter_image == "5":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/5.m4a")
        pygame.mixer.music.play()
    elif letter_image == "6":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/6.m4a")
        pygame.mixer.music.play()
    elif letter_image == "7":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/7.m4a")
        pygame.mixer.music.play()
    elif letter_image == "8":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/8.m4a")
        pygame.mixer.music.play()
    elif letter_image == "9":
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/9.m4a")
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load("/Users/maanitmalhan/Documents/Python/TraceLang/audio/blank.m4a")
        pygame.mixer.music.play()

def validateButton():
    letter_image = ""
    if letter_image =="a":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_A.png")
    elif letter_image =="b":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_B.png")
    elif letter_image =="c":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_C.png")
    elif letter_image =="d":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_D.png")
    elif letter_image =="e":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_E.png")
    elif letter_image =="f":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_F.png")
    elif letter_image =="g":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_G.png")
    elif letter_image =="h":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_H.png")
    elif letter_image =="i":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_I.png")
    elif letter_image =="j":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/Reference_Img_J.png")
    elif letter_image =="k":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_K.png")
    elif letter_image =="l":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_L.png")
    elif letter_image =="m":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_M.png")
    elif letter_image =="n":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_N.png")
    elif letter_image =="o":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_O.png")
    elif letter_image =="p":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_P.png")
    elif letter_image =="q":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_Q.png")
    elif letter_image =="r":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_R.png")
    elif letter_image =="s":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_S.png")
    elif letter_image =="t":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_T.png")
    elif letter_image =="u":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_U.png")
    elif letter_image =="v":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/Reference_Img_V.png")
    elif letter_image =="w":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/reference_Img_W.png")
    elif letter_image =="x":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/reference_Img_X.png")
    elif letter_image =="y":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/reference_Img_Y.png")
    elif letter_image =="z":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_image/reference_Img_Z.png")
    elif letter_image =="0":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_0.png")
    elif letter_image =="1":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_1.png")
    elif letter_image =="2":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_2.png")
    elif letter_image =="3":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_3.png")
    elif letter_image =="4":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_4.png")
    elif letter_image =="5":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_5.png")
    elif letter_image =="6":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_6.png")
    elif letter_image =="7":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_7.png")
    elif letter_image =="8":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_8.png")
    elif letter_image =="9":
        checkTrace("/Users/maanitmalhan/Documents/Python/TraceLang/traced.png", "/Users/maanitmalhan/Documents/Python/TraceLang/reference_images/reference_Img_9.png")


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

def checkTrace(traced_image_path, reference_image_path, threshold=0.9):
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

    cv.imwrite("/Users/maanitmalhan/Documents/Tra_Image.png", traced_image)
    cv.imwrite("/Users/maanitmalhan/Documents/Refece_Image.png", reference_image)
    # Get the difference between the traced image and the reference image

    result = cv.matchTemplate(traced_image, reference_image, cv.TM_CCOEFF_NORMED)

    # Get the best match location
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Determine if the traced image matches the reference
    if max_val >= threshold:
        return True
    else:
        return False
   
if __name__ == "__main__":
    traced_image_path = "/Users/maanitmalhan/Desktop/trace.png"  # Replace with your traced image path
    reference_image_path = "/Users/maanitmalhan/Desktop/refrence.png"  # Replace with your reference image path

    match = checkTrace(traced_image_path, reference_image_path)

    if match:
        print("The traced image matches the reference image.")
    else:
        print("The traced image does not match the reference image.")

