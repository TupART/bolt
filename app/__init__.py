from flask import Flask
from flask_cors import CORS

app = Flask(__name__, 
    static_folder='../static',
    template_folder='../templates'
)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'

from app.routes import main_routes
app.register_blueprint(main_routes)