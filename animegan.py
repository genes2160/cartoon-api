import numpy as np
import cv2

import os
import onnxruntime as ort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "paprika.onnx")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model not found at: {MODEL_PATH}")

session = ort.InferenceSession(MODEL_PATH, providers=["CPUExecutionProvider"])


def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (512, 512))
    img = img.astype(np.float32) / 127.5 - 1.0
    img = np.transpose(img, (2, 0, 1))
    return np.expand_dims(img, 0)


def postprocess(output):
    img = output[0]
    img = np.squeeze(img)
    img = np.transpose(img, (1, 2, 0))
    img = (img + 1.0) * 127.5
    img = np.clip(img, 0, 255).astype(np.uint8)
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


def cartoonize_image(input_path, output_path):
    img = cv2.imread(input_path)

    inp = preprocess(img)
    out = session.run(None, {"input": inp})[0]

    result = postprocess(out)
    cv2.imwrite(output_path, result)
