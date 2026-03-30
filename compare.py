import numpy as np

THRESHOLD = 0.55

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def verify_embeddings(new_emb, stored_emb):
    score = cosine_similarity(new_emb, stored_emb)
    return score, score >= THRESHOLD