from .split_audio import split_audio
from .keyword_extraction import generate_dataset_keywords


def preprocess(input_file: str) -> str:
    dataset = split_audio(input_file, json_name=f'{input_file}.json')
    output_file = 'data/transcribed_' + f'{input_file}.json'
    dataset = generate_dataset_keywords(dataset, json_name=output_file)
    return output_file