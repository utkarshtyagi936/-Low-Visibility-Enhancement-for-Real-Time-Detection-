import streamlit as st
import cv2
import numpy as np
from enhance import enhance_image

st.title("Low-Light Image Enhancer")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, caption="Original Image", channels="BGR")

    enhanced = enhance_image(image)

    st.image(enhanced, caption="Enhanced Image", channels="BGR")

    cv2.imwrite("output.jpg", enhanced)

    st.success("Image enhanced successfully!")
