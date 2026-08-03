"""
Preprocessing Utility for Rice Leaf Disease Detection
Matches exact pipeline from Jupyter Notebook:
- Image Resizing to (224, 224)
- Conversion to RGB color space
- Normalization (pixel values / 255.0)
- Array Expansion to batch shape (1, 224, 224, 3)
"""

import cv2
import numpy as np
from PIL import Image
import io

IMAGE_SIZE = (224, 224)

def preprocess_pil_image(pil_img: Image.Image) -> tuple[np.ndarray, np.ndarray]:
    """
    Preprocesses a PIL Image object uploaded via Streamlit.
    Returns:
        display_img (np.ndarray): RGB numpy array (224, 224, 3) formatted for rendering.
        input_tensor (np.ndarray): Normalized float32 numpy array (1, 224, 224, 3).
    """
    # Ensure RGB
    if pil_img.mode != "RGB":
        pil_img = pil_img.convert("RGB")
    
    # Convert PIL Image to OpenCV / NumPy format
    img_array = np.array(pil_img)
    
    # Resize image to (224, 224) as defined in notebook
    resized_image = cv2.resize(img_array, IMAGE_SIZE)
    
    # Normalize image pixels to [0.0, 1.0]
    input_tensor = resized_image.astype("float32") / 255.0
    
    # Expand dims for batch prediction: (1, 224, 224, 3)
    input_tensor = np.expand_dims(input_tensor, axis=0)
    
    return resized_image, input_tensor


def preprocess_bytes(image_bytes: bytes) -> tuple[np.ndarray, np.ndarray]:
    """
    Preprocesses raw image bytes.
    """
    pil_img = Image.open(io.BytesIO(image_bytes))
    return preprocess_pil_image(pil_img)
