import librosa
import torch
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


def transcribe_dataset(dataset: dict) -> dict:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")
    model = Wav2Vec2ForCTC.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")
    if torch.cuda.is_available():
        model.cuda()    

    utterances = dataset.keys()
    for utterance in utterances:
        waveform, sample_rate = librosa.load(utterance, sr=16000)
        for chunk in dataset[utterance]:
            start_time = chunk["start_time"]
            end_time = chunk["end_time"]
            start_sample = int(start_time * sample_rate)
            end_sample = int(end_time * sample_rate)
            audio_segment = waveform[start_sample:end_sample]

            input_values = processor(audio_segment, sampling_rate=sample_rate, return_tensors="pt").input_values
            input_values = input_values.to(device)
            logits = model(input_values).logits
            predicted_ids = np.argmax(logits.cpu().detach().numpy(), axis=-1)
            transcription = processor.decode(predicted_ids[0])
            
            chunk["transcription"] = transcription

    return dataset


if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")
    model = Wav2Vec2ForCTC.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-english")
    if torch.cuda.is_available():
        model.cuda()
