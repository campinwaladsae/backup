import streamlit as st
import cv2
import numpy as np

def load_image(file):
    # Use OpenCV to load the image as a numpy array
    img = cv2.imread(file)
    
    # Check if the image was loaded correctly
    if img is None:
        st.error("Error loading image. Please make sure you're passing a valid image file.")
        return None
    
    # Convert the image from BGR to RGB format (since OpenCV uses BGR by default)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Convert the numpy array to a PIL image
    img = Image.fromarray(np.uint8(img))
    
    return img

# Assuming you're getting the file from a file uploader
file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])

if file is not None:
    # Load the image using OpenCV
    image = load_image(file)
    
    if image is not None:
        # Display the image using Streamlit
        st.image(image, caption=f"Image {i + 1}", use_column_width=True)
