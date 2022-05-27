@echo off
pip install --upgrade --user -r requirements.txt
python -m spacy download en_core_web_sm
pause