import numpy as np

def clean_signal(signal):
    """
    Clean and normalize a 1D seismic signal.

    Steps:
    1. Convert to numpy array
    2. Apply simple moving average smoothing to reduce noise
    3. Normalize the values between 0 and 1
    """

    signal = np.array(signal)

    # Smooth signal using moving average
    window_size = 5
    smoothed = np.convolve(signal, np.ones(window_size) / window_size, mode="same")

    # Normalize values to 0–1 range
    min_val = smoothed.min()
    max_val = smoothed.max()
    normalized = (smoothed - min_val) / (max_val - min_val + 1e-8)

    return normalized
