from database.db import SessionLocal
from database.models import User
from face.capture import capture_frame
from face.embedding import get_embedding
import numpy as np


def register_user(user_id, name, email):

    db = SessionLocal()

    existing = db.query(User).filter(User.user_id == user_id).first()
    if existing:
        print("User already exists.")
        db.close()
        return

    print("Capturing face for registration...")
    frame = capture_frame()
    embedding = get_embedding(frame)

    embedding_bytes = embedding.astype(np.float32).tobytes()

    user = User(
        user_id=user_id,
        name=name,
        email=email,
        embedding=embedding_bytes
    )

    db.add(user)
    db.commit()
    db.close()

    print("User registered successfully.")