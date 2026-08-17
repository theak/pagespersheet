import os
import io
from base64 import b64encode

import pdf2image
import bottle
from bottle import Bottle, request, response, static_file, template

app = Bottle()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
bottle.TEMPLATE_PATH.insert(0, os.path.join(BASE_DIR, 'templates'))
INDEX_HTML = open(os.path.join(BASE_DIR, 'templates', 'index.html')).read()


@app.route('/')
def index():
    return INDEX_HTML


@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root=STATIC_DIR)


@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root=STATIC_DIR, mimetype='image/vnd.microsoft.icon')


@app.route('/upload', method='POST')
def upload():
    f = request.files.get('file')
    if f is None or not f.raw_filename:
        response.status = 400
        return 'No selected file'

    images = []
    for image in pdf2image.convert_from_bytes(f.file.read(), fmt='png', size=(800, None), dpi=300):
        buf = io.BytesIO()
        image.save(buf, format='PNG')
        images.append(b64encode(buf.getvalue()).decode('utf-8'))

    return template('render.html', images=images)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, server='waitress')
