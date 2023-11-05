import cv2 as cv
import numpy as np
import pygame 

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
    traced_image_path = "canvas_snapshot.png"  # Replace with your traced image path
    reference_image_path = "/Users/maanitmalhan/Desktop/refrence.png"  # Replace with your reference image path

    match = checkTrace(traced_image_path, reference_image_path)

    if match:
        print("The traced image matches the reference image.")
    else:
        print("The traced image does not match the reference image.")

