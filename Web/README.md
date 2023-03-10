# Web Demo

This is a Web demo for Audio Text Localization Project.

## Installing Dependencies

```bash
sudo apt update && sudo apt install ffmpeg -y
python -m venv venv
source venv/bin/activate

pip install -r init/requirements.txt
pip install git+https://github.com/huggingface/datasets.git
pip install git+https://github.com/huggingface/transformers.git
```

## Running the Demo

```bash
python3 manage.py runserver
```
