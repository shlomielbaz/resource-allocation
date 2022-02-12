FROM python:3.6.5-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV PATH="/app:$PATH"
ENV PYTHONPATH=.
CMD ["python", "app.py"]