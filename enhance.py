import cv2
import numpy as np

def enhance_image(image):
    
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

   
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

   
    merged = cv2.merge((cl, a, b))

    
    enhanced_img = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    return enhanced_img
