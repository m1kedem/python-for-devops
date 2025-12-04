FROM python:3.11-slim

#psutil
RUN pip install --no-cache-dir psutil

COPY week1/log_parser.py .
COPY week1/example.log .

CMD ["python", "log_parser.py"]