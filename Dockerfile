FROM protik77/python3-sensehat

COPY /control-sense-hat /control-sense-hat

WORKDIR /control-sense-hat

CMD ["python3", "main.py"]