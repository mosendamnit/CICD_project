import os
import numpy as np
import tensorflow as tf
import pytest

DIGIT_MODEL_PATH = "digit_model.keras"
SYMBOL_MODEL_PATH = "symbol_model.h5"

@pytest.mark.skipif(not os.path.exists(DIGIT_MODEL_PATH), reason="Model file not found in CI")
def test_model_files_exist():
    assert os.path.exists(DIGIT_MODEL_PATH)
    assert os.path.exists(SYMBOL_MODEL_PATH)

@pytest.mark.skipif(not os.path.exists(DIGIT_MODEL_PATH), reason="Model file not found in CI")
def test_models_can_load():
    tf.keras.models.load_model(DIGIT_MODEL_PATH, compile=False)
    tf.keras.models.load_model(SYMBOL_MODEL_PATH, compile=False)

@pytest.mark.skipif(not os.path.exists(DIGIT_MODEL_PATH), reason="Model file not found in CI")
def test_digit_model_prediction():
    model = tf.keras.models.load_model(DIGIT_MODEL_PATH, compile=False)
    dummy_input = np.random.rand(1, 28, 28, 1).astype("float32")
    prediction = model.predict(dummy_input)
    assert prediction.shape == (1, 10)

@pytest.mark.skipif(not os.path.exists(SYMBOL_MODEL_PATH), reason="Model file not found in CI")
def test_symbol_model_prediction():
    model = tf.keras.models.load_model(SYMBOL_MODEL_PATH, compile=False)
    dummy_input = np.random.rand(1, 28, 28, 1).astype("float32")
    prediction = model.predict(dummy_input)
    assert prediction.shape == (1, 4)
