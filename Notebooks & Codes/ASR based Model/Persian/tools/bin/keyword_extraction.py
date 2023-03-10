import hazm
import yake
import json
from multi_rake import Rake
from automatic_speech_recognition import transcribe_dataset


def extract_keywords_yake(transcription):
    # Tokenize the transcription using Hazm
    normalizer = hazm.Normalizer()
    tokenizer = hazm.WordTokenizer()
    tokens = tokenizer.tokenize(normalizer.normalize(transcription))
    tokens = [token for token in tokens if token not in hazm.stopwords_list()]

    # Extract keywords using YAKE
    extractor = yake.KeywordExtractor()
    keywords = extractor.extract_keywords(' '.join(tokens))
    keywords = [k[0] for k in keywords]
    keywords = list(map(lambda x: x.replace('\u200c', ''), keywords))

    return keywords


def extract_keywords_rake(transcription):
    # Extract keywords using multi_rake
    stopwords = hazm.stopwords_list()
    rake = Rake(
        min_chars=3,
        max_words=3,
        min_freq=1,
        language_code=None,  
        stopwords=None, 
        lang_detect_threshold=50,
        max_words_unknown_lang=2,
        generated_stopwords_percentile=80,
        generated_stopwords_max_len=3,
        generated_stopwords_min_freq=2,
    )
    keywords = rake.apply(transcription)
    keywords = [kw[0].replace('\u200c', '') for kw in keywords]

    return keywords


def generate_dataset_keywords(dataset_file, json_name=None) -> dict:
    if isinstance(dataset_file, str):
        with open(dataset_file, 'r') as f:
            dataset = json.load(f)  
    elif isinstance(dataset_file, dict):
        dataset = dataset_file
    else:
        raise NotImplementedError
    
    dataset = transcribe_dataset(dataset)
    utterances = dataset.keys()
    for utterance in utterances:
        for chunk in dataset[utterance]:
            chunk["keywords"] = extract_keywords_yake(chunk["transcription"])

    if json_name:
        with open(f'data/{json_name}', "w", encoding='utf-8') as f:
            json.dump(dataset, f, ensure_ascii=False)

    return dataset