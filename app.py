import streamlit as st
from PIL import Image
import os

# Ensure folders exist
os.makedirs("demo_images", exist_ok=True)
os.makedirs("output_images", exist_ok=True)

st.title("CameraHMR: 3D Human Pose Estimation")
st.write("Upload an image to estimate 3D pose using CameraHMR")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Save to demo_images folder
    input_path = os.path.join("demo_images", uploaded_file.name)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.write("Running CameraHMR model...")

    # Run inference (adjust command if needed)
    output_image_path = os.path.join("output_images", uploaded_file.name)
    os.system(f"python demo.py --img_path {input_path} --output_path {output_image_path}")

    # Display result
    if os.path.exists(output_image_path):
        st.image(output_image_path, caption="Predicted Pose", use_column_width=True)
    else:
        st.error("Failed to generate output. Check demo.py for errors.")
