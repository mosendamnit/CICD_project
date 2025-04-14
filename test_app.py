import os
import numpy as np
import tensorflow as tf

# Test file paths
DIGIT_MODEL_PATH = "digit_model.keras"
SYMBOL_MODEL_PATH = "symbol_model.h5"

def test_model_files_exist():
    assert os.path.exists(DIGIT_MODEL_PATH), "❌ digit_model.keras is missing"
    assert os.path.exists(SYMBOL_MODEL_PATH), "❌ symbol_model.h5 is missing"
    print("✅ Model files exist")

def test_models_can_load():
    try:
        tf.keras.models.load_model(DIGIT_MODEL_PATH, compile=False)
        tf.keras.models.load_model(SYMBOL_MODEL_PATH, compile=False)
        print("✅ Models loaded successfully")
    except Exception as e:
        raise AssertionError(f"❌ Failed to load model: {e}")

def test_digit_model_prediction():
    model = tf.keras.models.load_model(DIGIT_MODEL_PATH, compile=False)
    dummy_input = np.random.rand(1, 28, 28, 1).astype("float32")
    prediction = model.predict(dummy_input)
    assert prediction.shape == (1, 10), f"❌ Digit model prediction shape incorrect: {prediction.shape}"
    print("✅ Digit model predicts correctly")

def test_symbol_model_prediction():
    model = tf.keras.models.load_model(SYMBOL_MODEL_PATH, compile=False)
    dummy_input = np.random.rand(1, 28, 28, 1).astype("float32")
    prediction = model.predict(dummy_input)
    assert prediction.shape == (1, 4), f"❌ Symbol model prediction shape incorrect: {prediction.shape}"
    print("✅ Symbol model predicts correctly")

if __name__ == "__main__":
    test_model_files_exist()
    test_models_can_load()
    test_digit_model_prediction()
    test_symbol_model_prediction()
    print("🎉 All tests passed!")
