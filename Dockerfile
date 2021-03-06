FROM python:latest
WORKDIR Flask_App
COPY server.py __main__.py
RUN pip install flask
ENTRYPOINT ["python3", "__main__.py"]