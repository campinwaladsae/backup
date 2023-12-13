import streamlit as st
import cv2
import numpy as np
from PIL import Image

def load_image(file):
    # Convert the file to a byte array
    byte_data = file.read()
   
    # Use OpenCV to load the image from the byte array
    nparr = np.frombuffer(byte_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   
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
        # Define 'i' as 0
        i = 0
        
        # Display the image using Streamlit
        st.image(image, caption=f"Image {i + 1}", use_column_width=True)
