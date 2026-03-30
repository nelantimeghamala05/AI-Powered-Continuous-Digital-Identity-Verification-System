from deepface import DeepFace
import numpy as np
import cv2
import os

def get_embedding(frame):

    temp_path = "temp.jpg"
    cv2.imwrite(temp_path, frame)

    embedding = DeepFace.represent(
        img_path=temp_path,
        model_name="Facenet512",
        detector_backend="retinaface"
    )[0]["embedding"]

    os.remove(temp_path)

    return np.array(embedding)