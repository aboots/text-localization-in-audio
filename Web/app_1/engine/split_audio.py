import pandas as pd
import json
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_silence, detect_nonsilent


def split_audio(input_file: str, json_name=None) -> dict:
    audio_file = AudioSegment.from_file(input_file)

    #split on silent sections
    nonsilent_ranges = detect_nonsilent(audio_file, min_silence_len=900, silence_thresh=-25, seek_step=50)

    length = 0
    new_segments = []
    new_start = 0
    results = {}

    for start, end in nonsilent_ranges:

        # to have chuncks larger than 10 seconds
        if length > 10000:
            new_segments.append([new_start, new_end])
            new_start = start
            new_end   = end
        
        new_end   = end
        length = new_end - new_start
    
    time_segments = [{"start_time": start/1000, "end_time": end/1000} for start, end in new_segments]
    results[input_file] = time_segments 

    if json_name:
        with open(json_name, "w") as f:
            json.dump(results, f, indent=1)

    return results