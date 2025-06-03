from typing import Literal
from sentence_transformers import SentenceTransformer

embedding_models: dict[Literal["ko", "en"], SentenceTransformer] = {
    # "ko": SentenceTransformer("jhgan/ko-sbert-nli"),
    "ko": SentenceTransformer("bespin-global/klue-sroberta-base-continue-learning-by-mnr"),
    "en": SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
}

def embedding_from_seed(question: str, answer: str, lang: Literal["ko", "en"] = "ko"):
    print("embedding_from_seed", question, answer, lang)
    if not question.strip():
        raise ValueError("`question` must not be empty.")
    if not answer.strip():
        raise ValueError("`answer` must not be empty.")
    model = embedding_models[lang]
    question_vector = model.encode(question).tolist()
    answer_vector = model.encode(answer).tolist()

    return question_vector, answer_vector