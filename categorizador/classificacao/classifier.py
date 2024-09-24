from scipy.spatial.distance import cosine
from .categories import category_embeddings
from .embeddings import generate_embedding

def classify_product(product_description):
    product_embedding = generate_embedding(product_description)
    similarities = {
        category: 1 - cosine(product_embedding, category_embedding)
        for category, category_embedding in category_embeddings.items()
    }
    return max(similarities, key=similarities.get)