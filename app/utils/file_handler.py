import os
from werkzeug.utils import secure_filename

def save_uploaded_file(file):
    filename = secure_filename(file.filename)
    upload_folder = 'uploads'
    
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    return file_path