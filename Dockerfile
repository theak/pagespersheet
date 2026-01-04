FROM python:3.13-alpine
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN apk add --no-cache poppler-utils
RUN mkdir -p static
RUN mkdir -p templates
COPY static/ /static/
COPY templates/ /templates/
ADD app.py /
CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "5000", "app:app"]