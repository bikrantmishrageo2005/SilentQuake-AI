import numpy as np
from model_training import load_model
from data_preprocessing import preprocess_signal
from utils_signal_processing import extract_features

def predict_sse(raw_signal):
    """
    Predict Silent Slip Events (SSE) using trained AI model.
    """

    # Step-1: Clean & normalize
    processed = preprocess_signal(raw_signal)

    # Step-2: Extract powerful features
    features = extract_features(processed)

    # Step-3: Load model
    model = load_model()

    # Step-4: Predict
    prediction = model.predict(np.array([features]))[0]

    if prediction > 0.5:
        return "⚠️ ALERT: Silent Slip Event detected — Earthquake Possibility High"
    else:
        return "✓ Stable: No underground stress detected"

if __name__ == "__main__":
    dummy = np.random.rand(200)
    print(predict_sse(dummy))
