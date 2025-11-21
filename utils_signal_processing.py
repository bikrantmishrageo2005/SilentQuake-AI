import numpy as np

def extract_seismic_features(signal):
    """
    Extracts numerical features from a cleaned seismic signal.

    Features:
    - Mean amplitude
    - Standard deviation
    - Signal energy
    - Maximum peak value
    - Frequency power (FFT-based)
    """

    signal = np.array(signal)

    mean_val = np.mean(signal)
    std_val = np.std(signal)
    energy = np.sum(signal ** 2)
    peak_val = np.max(signal)

    fft_values = np.abs(np.fft.fft(signal))[:40]
    freq_power = np.mean(fft_values)

    return [mean_val, std_val, energy, peak_val, freq_power]
