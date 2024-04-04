from flask import Flask, render_template, request, send_from_directory
import pdf2image
import io
import os

from base64 import b64encode

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/upload", methods = ['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    # Read bytes from the uploaded file
    #file_bytes = file.read()

    # You can now process the file bytes as needed
    # For example, you can save it to disk or perform other operations

    image_byte_arrays = []

    pil_images = pdf2image.convert_from_bytes(file.read(), fmt='png', size=(800, None), dpi=200)
    for image in pil_images:
        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format='PNG')
        img_byte_array = img_byte_array.getvalue()
        image_byte_arrays.append(b64encode(img_byte_array).decode('utf-8'))

    return render_template('render.html', images=image_byte_arrays)
    #return 'File received and processed successfully', 200
