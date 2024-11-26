from flask import Blueprint, request, render_template, send_file
from app.services.excel_processor import process_excel_data, process_step4_template
from app.utils.file_handler import save_uploaded_file
import os

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file_path = save_uploaded_file(file)
            data = process_excel_data(file_path)
            return render_template('index.html', data=data)
    
    return render_template('index.html')

@main_routes.route('/process_step4', methods=['POST'])
def process_step4():
    selected_rows = request.form.getlist('rows')
    output_file = process_step4_template(selected_rows)
    return send_file(output_file, as_attachment=True)