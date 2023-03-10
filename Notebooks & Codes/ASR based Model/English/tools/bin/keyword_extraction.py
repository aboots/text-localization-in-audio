import yake
import json
from automatic_speech_recognition import transcribe_dataset


def extract_keywords_yake(transcription):

    # Specifying Parameters
    language = "en"
    max_ngram_size = 3
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = [x[0] for x in custom_kw_extractor.extract_keywords(transcription)]

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