import os
from .data_processing import preprocess
from .text_similarity import get_similar_parts


def usage(input_file: str, query: str, N: int):
    # input_file: input audio file (.wav)
    # query: input query (text)
    # N: number of required results
    if not os.path.isfile(os.getcwd() + 'transcribed_' + f'{input_file}.json'):
        print("Generating Input File Keywords...")
        preprocess(input_file)

    return get_similar_parts('transcribed_' + f'{input_file}.json', query, N)