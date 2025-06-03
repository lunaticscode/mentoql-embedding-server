from utils.embedding import embedding_from_seed
from pymilvus import Collection
def get_answer_from_seed():
        return ""
def insert_seed_from_mento(question: str, answer: str, mento_id: str):
        if not mento_id.strip():
                raise ValueError("`mento_id` must not be empty.")
        if not question.strip():
                raise ValueError("`question` must not be empty.")
        if not answer.strip():
                raise ValueError("`answer` must not be empty.")
        question_vector, answer_vector = embedding_from_seed(question, answer)
        data = [
                {
                        "mento_id": mento_id,
                        "mento_seed_question": question,
                        "mento_question_vector": question_vector,
                        "mento_seed_answer": answer,
                        "mento_answer_vector": answer_vector,
                }
        ]

        collection = Collection("mento_seed_collection")
        collection.insert(data)

        return {"status": "success", "inserted_count": len(data)}
