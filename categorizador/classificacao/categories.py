from .embeddings import generate_embedding

category_descriptions = {
    "esporte": "Roupas confortáveis e respiráveis para atividades físicas. Itens adotados em práticas esportivas.",
    "formal": "Vestuário elegante para ocasiões formais e de negócios.",
    "casual": "Roupas confortáveis e descontraídas para o dia a dia.",
    "Frio": "Roupas quentes para invernos e dias frios, mantendo o corpo aquecido."
}

category_embeddings = {
    category: generate_embedding(description)
    for category, description in category_descriptions.items()
}