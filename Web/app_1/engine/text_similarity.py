import json
import fasttext
from .keyword_extraction import extract_keywords_yake
from sentence_transformers import models, SentenceTransformer, util


def cosine_similarity(vec1, vec2):
    dot_product = sum([vec1[i] * vec2[i] for i in range(len(vec1))])
    norm1 = sum([vec1[i] ** 2 for i in range(len(vec1))]) ** 0.5
    norm2 = sum([vec2[i] ** 2 for i in range(len(vec2))]) ** 0.5
    return dot_product / (norm1 * norm2)


def load_st_model(model_name_or_path):
    word_embedding_model = models.Transformer(model_name_or_path)
    pooling_model = models.Pooling(
        word_embedding_model.get_word_embedding_dimension(),
        pooling_mode_mean_tokens=True,
        pooling_mode_cls_token=False,
        pooling_mode_max_tokens=False)
    
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    return model


def get_similar_parts(dataset_file, query, N):
    with open(dataset_file, 'r') as f:
        dataset = json.load(f)

    st_model = load_st_model('m3hrdadfi/bert-fa-base-uncased-wikitriplet-mean-tokens')

    query_embedding = st_model.encode(query)

    similarity_scores = []
    for utterance in dataset.keys():
        for chunk in dataset[utterance]:
            chunk_keywords = ' '.join(chunk['keywords'])
            chunk_embedding = st_model.encode(chunk_keywords)
            similarity_scores.append((utterance, chunk['start_time'], chunk['end_time'],
                                      chunk['transcription'], cosine_similarity(query_embedding, chunk_embedding)))
            
    # Sort similarity scores in descending order
    similarity_scores.sort(key=lambda x: x[4], reverse=True)

    # Get top N most similar records
    return similarity_scores[:N]