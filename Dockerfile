FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install poppler-utils -y
ADD static /
ADD templates /
ADD app.py /
CMD ["waitress-serve", "--host", "127.0.0.1", "hello:app"]