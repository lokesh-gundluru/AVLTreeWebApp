from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from avl_tree import AVLTree
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

avl = AVLTree()

@app.route('/')
def index():
    return render_template('index.html', tree=None)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        with open(filepath) as f:
            elements = [int(x.strip()) for x in f.readlines()]
        global avl
        avl = AVLTree()
        for element in elements:
            avl.root = avl.insert(avl.root, element)
        return render_template('index.html', tree=avl.get_preorder(avl.root))
    return "File upload failed", 400

@app.route('/insert', methods=['POST'])
def insert():
    value = int(request.form['value'])
    global avl
    avl.root = avl.insert(avl.root, value)
    return render_template('index.html', tree=avl.get_preorder(avl.root))

@app.route('/delete', methods=['POST'])
def delete():
    value = int(request.form['value'])
    global avl
    avl.root = avl.delete(avl.root, value)
    return render_template('index.html', tree=avl.get_preorder(avl.root))

@app.route('/download')
def download():
    filepath = os.path.join(app.config['OUTPUT_FOLDER'], 'avl_output.txt')
    with open(filepath, 'w') as f:
        for value in avl.get_preorder(avl.root):
            f.write(f"{value}\n")
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
