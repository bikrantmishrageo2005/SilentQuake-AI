import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

MODEL_PATH = "SilentQuake_AI_Model.pkl"


def generate_synthetic_seismic_data(samples=1200, length=200):
    X = np.random.rand(samples, length)
    y = np.random.randint(0, 2, samples)
    return X, y


def train_model():
    X, y = generate_synthetic_seismic_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    model = MLPClassifier(
        hidden_layer_sizes=(128, 64, 32),
        activation="relu",
        max_iter=900
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    print("Model Accuracy:", accuracy)

    joblib.dump(model, MODEL_PATH)
    print("Model saved as:", MODEL_PATH)


def load_model():
    return joblib.load(MODEL_PATH)


if __name__ == "__main__":
    train_model()
