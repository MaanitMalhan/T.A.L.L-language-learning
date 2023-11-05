import time
import easyocr as ocr   # OCR library
import tensorflow as tf  # Tensorflow
import cv2 as cv       # OpenCV
import numpy as np     # Numpy
from PIL import Image  # Image
from PIL import ImageDraw # ImageDraw

imgFromCam = True # True if image is from camera, False if image is from file 
imge = "/Users/maanitmalhan/Desktop/output.png" # Image path
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

def checkImg():    
    reader = ocr.Reader(['en'],gpu=False, download_enabled=False) # English

    values = reader.readtext("/Users/maanitmalhan/Desktop/combined.png",rotation_info=[90, 180 ,270],decoder="beamsearch",allowlist="a") # Print text
    if len(values) > 0:
        confidence = values[-1][2]
        confidence = confidence * 100
        if confidence >= 30:
            print(values[-1][1])
        else:
            print(f"No text found. Clarity level at {confidence:.2f}% too low")
    
        ocrImg = Image.open("/Users/maanitmalhan/Desktop/combined.png")
        boundingBox = values[0][0][0]
        boundingBox = boundingBox + values[0][0][2]
    
        draw = ImageDraw.Draw(ocrImg)
        for box in boundingBox:
            x1, y1, x2, y2 = map(int, [boundingBox[0], boundingBox[1], boundingBox[2], boundingBox[3]])
            draw.rectangle([x1, y1,x2,y2], outline='red', width=2)

        ocrImg.save("/Users/maanitmalhan/Desktop/bound.png")
        ocrImg.close()
    else:
        print("No text found")
        
def preProcess():
    img = cv.imread(imge) # Read image
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Convert to grayscale
    #blur = cv.GaussianBlur(gray, (5,5), 0) # Blur image
    #ret, thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU) # Threshold image
    new_width = 200  # Adjust to your desired width
    new_height = 132  # Adjust to your desired height
    t_lower = 50  # Lower Threshold 
    t_upper = 150  
    aperture_size = 5 # Aperture size 
    L2Gradient = True # Boolean
    resized_image = cv.resize(img, (new_width, new_height))
    lab_image = cv.cvtColor(resized_image, cv.COLOR_BGR2Lab)

    result = cv.pyrMeanShiftFiltering(lab_image, sp=0, sr=0, maxLevel=1)

    result = cv.cvtColor(result, cv.COLOR_Lab2BGR)

    kernel_size = (15, 15)

    blurred_image = cv.GaussianBlur(img, kernel_size, sigmaX=0)
    
    background = cv.imread('/Users/maanitmalhan/Desktop/test.png')

    background = cv.resize(background, (new_width, new_height))
    blurred_image = cv.resize(blurred_image, (new_width, new_height))
    added_image = cv.addWeighted(background,0.65,blurred_image,0.70,0)
    gray_image = cv.cvtColor(added_image, cv.COLOR_BGR2GRAY)


    cv.imwrite("/Users/maanitmalhan/Desktop/combined.png", added_image) # Save image

if imgFromCam == True:
    preProcess()
    checkImg()


