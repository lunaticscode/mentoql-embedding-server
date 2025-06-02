from pymilvus import Collection, CollectionSchema, FieldSchema, DataType, list_collections

COLLECTION_SCHEMAS = {
    "mento_seed_collection": {
        "fields": [
            FieldSchema(name="mento_seed_id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="mento_id", dtype=DataType.VARCHAR, max_length=100),
            FieldSchema(name="mento_seed_question", dtype=DataType.VARCHAR, max_length=300),
            FieldSchema(name="mento_question_vector", dtype=DataType.FLOAT_VECTOR, dim=384),
            FieldSchema(name="mento_seed_answer", dtype=DataType.VARCHAR, max_length=1000),
            FieldSchema(name="mento_answer_vector", dtype=DataType.FLOAT_VECTOR, dim=384),
        ],
        "description": "Mento seed embedding collection for Q&A"
    }
}

def create_collection_if_not_exists(name: str):
    if name in list_collections():
        return

    schema_data = COLLECTION_SCHEMAS.get(name)
    if not schema_data:
            raise ValueError(f"No schema defined for collection: {name}")

    target_schema = CollectionSchema(
        fields=schema_data['fields'],
        description= schema_data['description']
    )

    Collection(name=name, schema=target_schema)

def create_all_collections():
    for name in COLLECTION_SCHEMAS:
        create_collection_if_not_exists(name)