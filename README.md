# Text Localization in Audio
## Introduction
Text localization in audio involves the identification and localization of relevant segments of an audio stream. This task is crucial in efficiently identifying speech segments that correspond to the words in a query text, thereby enhancing the search process. Text localization finds application in several domains, including retrieving old voice messages stored on social platforms and searching for content in audio files such as tutorials or music.

This repository contains code for a system that performs text localization in audio, along with the necessary data processing pipeline. The system works for both English and Persian languages and can be used for a variety of applications. Moreover, all large materials such as datasets and models are in [this](https://drive.google.com/drive/folders/1QglqVqjF8WGh3tPwKhQ9dAjRNNEnUKzs) Google Drive link.

More details about the web-based demo can be found [here](https://github.com/aboots/text-localization-in-audio/tree/main/Web).

## Data processing pipeline
![Data processing pipeline](https://drive.google.com/uc?export=view&id=1ft-GsTHrkBvOG39RcIg4hK-2pXWXOwuo)

In order to perform the text localization task, it is necessary to have an appropriate dataset. As no such dataset is currently available, it is necessary to create one. This repository contains code for collecting audio files, segmenting them into smaller chunks, and extracting relevant keywords from them. Also, a Persian dataset containing 70 hours of audio is placed in the drive.


### Collecting audio files
For the English language, a portion of the [LibriSpeech](https://www.kaggle.com/datasets/benimaru069/librispeech-small-dataset) dataset was used. For the Persian language, a Farsi podcast ([Radio Marz](https://radiomarz.libsyn.com/)) in the form of an interview with multiple speakers was selected.

### Audio segmentation
In order to effectively localize a text within an input audio stream, it is necessary to first segment the audio into discrete sections. This segmentation enables the identification of those segments that are most relevant to the query text.
Also, given the large variance in the duration of audio files, ranging from a few minutes to hours, it is essential to segment them into smaller chunks for effective training of acoustic models. 
To this end, a segmentation technique that detects silences and generates segments of at least 10 seconds in length was applied.

![Audio segmentation](https://drive.google.com/uc?export=view&id=1o2FT3yQHxWj2A_AmhiiOigBPitw-G7Qs)


### Persian ASR
For English data, transcripts were already available in the LibriSpeech dataset. For the Persian language, transcripts for each chunk were extracted using an ASR model developed by ourselves.

### Keyword extraction

We use various methods such as PKE, BERT-based Language Model, YAKE algorithm, Multi-RAKE algorithm, and our fine-tuned Persian Summarizer to extract keywords.



## Model


### Baseline

In the baseline model, we take a text and an audio and then chunk the audio using rule-based methods. We the use ASR models to get the text of audio, and then, we calculate the similarity of the query text and the text extracted from audio. Finally, we retrieve the relevant chunks of audio based on this similarity.

![Baseline](https://drive.google.com/uc?export=view&id=1ye7W4t2E7qTBDRL7XJTKwFEUjPtZHJQG)

### Proposed Model

In our proposed model, we train them using Unsupervised Contrastive Learning paradim, where for batches of pairs of text and audio, the model will learn to encode audios and text to a shared embedding space and maximize the similarity between pairs and minimize the similarity between text and audio from different pairs. In the inference time, the model accepts a text query and chunks of audio and will return the similarity score between the text and the audio chunks.

Training Time:

![Proposed Model](https://drive.google.com/uc?export=view&id=1xALOA49j3QelgF8kpAfuT92gEl8x3FhQ)

Inference Time:

![Inference Model](https://drive.google.com/uc?export=view&id=1VSDwJ3E6YakYkqxbKV1AU28QhHzZP0sM)

## Conclusion
Text localization in audio is a critical problem with diverse applications. This repository provides a data processing pipeline and a system for performing text localization in audio for both English and Persian languages. By developing effective and efficient algorithms for this task, we can improve the accuracy and usability of ASR systems, generate more effective and engaging multimedia content, and augment the overall accessibility and discoverability of audio-based information.


## Colaborators
| Name                | Email                     |
| --- | --- |
| Mahdi Abootorabi    |mahdi.abootorabi@sharif.edu|
|Aryan Ahadiniya      |aryan.ahadinia@sharif.edu  |
|Arshan Dalili        |arshandalili@gmail.com     |
| Saeed Foroutan      |Foroutan@sharif.edu        |
| Parsa Haghighi      |Haghighi@sharif.edu        |
|Sina Rashidi         |sina_rashidi@outlook.com   |

