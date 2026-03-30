import numpy as np
from database.db import SessionLocal
from database.models import User, VerificationLog
from face.capture import capture_frame
from face.embedding import get_embedding
from face.compare import verify_embeddings
from services.email_service import send_alert_email
def verify_user(user_id):

    db = SessionLocal()

    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        print("User not found")
        db.close()
        return

    stored_emb = np.frombuffer(user.embedding, dtype=np.float32)

    print("Capturing face for verification...")
    frame = capture_frame()
    new_emb = get_embedding(frame)

    score, same = verify_embeddings(new_emb, stored_emb)

    print(f"Similarity Score: {score:.4f}")

    if same:
        print("Same User")
    else:
        print("Different User 🚨")
        send_alert_email(user.email, score)

    result = "Same User" if same else "Different User"

    log = VerificationLog(
    user_id=user_id,
    similarity=str(score),
    result=result
)
    db.add(log)
    db.commit()
    db.close()

    print(f"{result} | Similarity: {score:.4f}")