FROM mattgleich/sense-hat

COPY ./control-sense-hat /control-sense-hat

WORKDIR /control-sense-hat

CMD ["python3", "main.py"]