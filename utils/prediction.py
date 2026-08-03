"""
Prediction Utility for Rice Leaf Disease Detection
Loads trained MobileNetV2 .keras model and performs inference.
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Exact Class Names matching notebook class indices
CLASS_NAMES = [
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Leaf Smut"
]

MODEL_PATH = os.path.join("model", "Best_RiceLeaf_Disease_Model.keras")

_cached_model = None

def get_model():
    """
    Lazy loads and returns cached model instance.
    """
    global _cached_model
    if _cached_model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        _cached_model = load_model(MODEL_PATH)
    return _cached_model


def predict_rice_disease(input_tensor: np.ndarray) -> dict:
    """
    Performs disease prediction on preprocessed image tensor (1, 224, 224, 3).
    Returns dictionary with:
    - predicted_class: str
    - confidence: float (0.0 to 100.0)
    - probabilities: dict mapping class name -> percentage float
    - class_index: int
    """
    model = get_model()
    
    # Run prediction
    raw_predictions = model.predict(input_tensor, verbose=0)[0]
    
    # Get index of highest probability
    predicted_idx = int(np.argmax(raw_predictions))
    predicted_class = CLASS_NAMES[predicted_idx]
    confidence_score = float(np.max(raw_predictions) * 100.0)
    
    # Create probability distribution dictionary
    prob_dict = {
        class_name: float(raw_predictions[i] * 100.0)
        for i, class_name in enumerate(CLASS_NAMES)
    }
    
    return {
        "predicted_class": predicted_class,
        "confidence": round(confidence_score, 2),
        "class_index": predicted_idx,
        "probabilities": prob_dict,
        "raw_probabilities": raw_predictions.tolist()
    }
