import cv2
import numpy as np
import streamlit as st
from PIL import Image
import pytesseract

# Ensure that you have tesseract installed on your system and pytesseract configured properly
# If you're on Windows, you may need to specify the tesseract executable path like this:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to detect text using Tesseract OCR
def detect_text(image):
    # Convert image to RGB (if not already in RGB format)
    if len(image.shape) == 3:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        image_rgb = image

    # Use Tesseract to perform text detection
    detected_text = pytesseract.image_to_string(image_rgb)

    # Draw bounding boxes around detected text (optional: using pytesseract's image_to_boxes)
    h, w, _ = image.shape
    boxes = pytesseract.image_to_boxes(image_rgb)

    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w_box, h_box = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(image_rgb, (x, h - y), (w_box, h - h_box), (0, 255, 0), 2)

    return image_rgb, detected_text

# Streamlit app layout
st.title('Live Text Detection using Tesseract OCR')

# Upload an image file
uploaded_file = st.file_uploader("Upload an image or capture a live image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    image = np.array(image)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Detect text in the image using Tesseract OCR
    output_image, detected_text = detect_text(image)

    # Display the image with bounding boxes (optional)
    st.image(output_image, caption="Processed Image with Detected Text", use_column_width=True)

    # Display the detected text
    st.write("Detected Text:")
    st.text(detected_text)

# Capture live image using the webcam
if st.button("Capture from Webcam"):
    cap = cv2.VideoCapture(0)  # Open the webcam

    if not cap.isOpened():
        st.error("Cannot access the webcam!")
    else:
        ret, frame = cap.read()
        if ret:
            # Detect text in the live image using Tesseract OCR
            output_image, detected_text = detect_text(frame)

            # Convert the image to RGB for displaying in Streamlit
            output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

            # Display the captured frame
            st.image(output_image, caption="Captured Frame with Detected Text", use_column_width=True)

            # Display the detected text
            st.write("Detected Text from Webcam:")
            st.text(detected_text)
        else:
            st.error("Failed to capture image from webcam!")
        cap.release()  # Release the webcam resource
