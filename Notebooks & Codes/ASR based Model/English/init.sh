sudo apt update && sudo apt install ffmpeg -y

pip install -r tools/requirements.txt
pip install git+https://github.com/huggingface/datasets.git
pip install git+https://github.com/huggingface/transformers.git
pip install -U sentence-transformers

python tools/bin/automatic_speech_recognition.py