# Text Localization in Audio
## Introduction
Text localization in audio involves the identification and localization of relevant segments of an audio stream. This task is crucial in efficiently identifying speech segments that correspond to the words in a query text, thereby enhancing the search process. Text localization finds application in several domains, including retrieving old voice messages stored on social platforms and searching for content in audio such as tutorials or music.

This repository contains code for a system that performs text localization in audio, along with the necessary data processing pipeline. The system works for both English and Persian languages and can be used for a variety of applications.

## Data processing pipeline
In order to perform the text localization task, it is necessary to have an appropriate dataset. As no such dataset is currently available, it is necessary to create one. This repository contains code for collecting audio files, segmenting them into smaller chunks, and extracting relevant keywords from them. Also, a Persian dataset containing 70 hours of audio is placed in the 'data/' directory.

### Collecting audio files
For the English language, a portion of the [LibriSpeech](https://www.kaggle.com/datasets/benimaru069/librispeech-small-dataset) dataset was used. For the Persian language, a Farsi podcast ([Radio Marz](https://radiomarz.libsyn.com/)) in the form of an interview with multiple speakers was selected.

### Audio segmentation
Given the large variance in the duration of audio files, ranging from a few minutes to hours, it is essential to segment them into smaller chunks for effective training of acoustic models. To this end, a segmentation technique that detects silences and generates segments of at least 10 seconds in length was applied.

### Persian ASR
For English data, transcripts were already available in the LibriSpeech dataset. For the Persian language, transcripts for each chunk were extracted using an ASR model developed by ourselves.

```python
detail about the ASR module (Must be written by Sina)
```

### Keyword extraction
```python
Must be written by Saeed
```


### Usage
To use the system for text localization in audio, follow these steps:
1. Clone the repository
2. Collect audio files and put them in the `data/` directory
3. Run the audio segmentation script: `python segment_audio.py`
4. Run the ASR and keyword extraction scripts for the desired language: `python extract_keywords_en.py` for English, and python `extract_keywords_fa.py` for Persian
5. Use the extracted keywords to perform text localization in audio


## Conclusion
Text localization in audio is a critical problem with diverse applications. This repository provides a data processing pipeline and a system for performing text localization in audio for both English and Persian languages. By developing effective and efficient algorithms for this task, we can improve the accuracy and usability of ASR systems, generate more effective and engaging multimedia content, and augment the overall accessibility and discoverability of audio-based information.
