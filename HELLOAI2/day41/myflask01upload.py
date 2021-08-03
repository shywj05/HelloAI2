import os
from flask import Flask,render_template, request, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/')
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']        
    filename = secure_filename(file.filename)
    file.save(os.path.join("D:/workspace_python/HELLOAI2/day41/static/upload", filename))    
    return render_template('upload.html')

@app.route('/download')
def download():
    file_name = f"static/upload/1_2.PNG"
    return send_file(file_name,
                     mimetype='image/png',
                     attachment_filename='1_2.PNG',
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)