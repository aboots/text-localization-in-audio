import torch
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torchaudio
import torchaudio.transforms as transforms


def get_transcript(waveform , chunk : dict):
    """
    This module takes a waveform and start & end time of
    a chunk of it and returns transcription of the chunk.

    inputs:
        - waveform: 
        - chunk: a dictionary with 2 keys: "start_time", "end_time"
    output:
        - transcripiton of that chunk
    """

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = Wav2Vec2Processor.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-persian")
    model = Wav2Vec2ForCTC.from_pretrained("m3hrdadfi/wav2vec2-large-xlsr-persian").eval().to(device)

    start_time = chunk["start_time"]
    end_time = chunk["end_time"]
    sample_rate = 16000
    
    start_sample = int(start_time * sample_rate)
    end_sample = int(end_time * sample_rate)
    audio_segment = waveform[start_sample:end_sample]

    input_values = processor(audio_segment, sampling_rate=sample_rate, return_tensors="pt").input_values
    input_values = input_values.to(device)

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = np.argmax(logits.cpu().detach().numpy(), axis=-1)
    transcription = processor.decode(predicted_ids[0])

    return transcription


def get_all_transcripts(audio_file_path : str, segments : list):

    """
    This module takes an audio file path and start & end time of
    all chunks and add another key for each chunk (transcription)

    inputs:
        - Audio_file_path 
        - segments: a list of dictionaries in the from of {"start_time":x, "end_time":y}
    output:
        - a list of dictionaries like {"start_time":x, "end_time":y , "transcription":z}
    """

    waveform, sr = torchaudio.load(audio_file_path)

    sample_rate = 16000
    resample_transform = transforms.Resample(sr,sample_rate)
    waveform = resample_transform(waveform).squeeze().numpy()
    
    for i, chunk in enumerate(segments):
        segments[i]["transcription"] = get_transcript(waveform , chunk)

    return segments