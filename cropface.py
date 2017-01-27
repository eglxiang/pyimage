import cv
import Image

def DetectFace(image, faceCascade):
    min_size = (20, 20)
    image_scale = 1
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0
    
    # Allocate the temporal images
    smallImages = cv.CreateImage((cv.Round(image.width / image_scale),
            cv.Round(image.height/ image_scale)), 8, 1)
    
    # Scale input image for faster processing
    cv.Resize()