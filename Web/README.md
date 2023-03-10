# Web Demo

This is a Web demo for Audio Text Localization Project.

![Input](https://drive.google.com/uc?export=view&id=16x1mhRtClEj5ETCVf_iM4dCUc2v0nUXP)

![Output](https://drive.google.com/uc?export=view&id=1dg5z1D18cUxjkeUFMVOzVBpDHgxZitFd)

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
