"""Konstanta kelas dan preprocessing yang identik dengan notebook training."""

import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


IMAGE_SIZE = (224, 224)

# Urutan ini berasal dari CLASSES/label_idx pada Proyek_AI.ipynb.
CLASS_NAMES = ("daun_pepaya", "le_minerale", "roundup_b3")
DISPLAY_NAMES = {
    "daun_pepaya": "🌿 Organik",
    "le_minerale": "♻️ Anorganik",
    "roundup_b3": "⚠️ B3",
}


def prepare_image(image: Image.Image) -> np.ndarray:
    """RGB → resize 224x224 → NumPy → batch → MobileNetV2 preprocess_input."""
    rgb_image = image.convert("RGB")
    resized_image = rgb_image.resize(IMAGE_SIZE, Image.Resampling.BILINEAR)
    image_array = np.asarray(resized_image, dtype=np.float32)
    image_batch = np.expand_dims(image_array, axis=0)
    return preprocess_input(image_batch)
