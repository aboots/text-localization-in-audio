sudo apt update && sudo apt install ffmpeg -y
python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r tools/requirements.txt
pip install git+https://github.com/huggingface/datasets.git
pip install git+https://github.com/huggingface/transformers.git
pip install -U sentence-transformers

mkdir -p tools/data
if [ ! -e tools/data/cc.fa.300.bin ]; then
    wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.fa.300.bin.gz -P tools/data
    gzip -d tools/data/cc.fa.300.bin.gz
fi

python tools/bin/automatic_speech_recognition.py