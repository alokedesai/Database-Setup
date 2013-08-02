import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'leelelelelele'

UPLOAD_FOLDER= os.path.realpath('.') + '/app/static/'
ALLOWED_EXTENSIONS=set(['txt','pdf','doc','odt','docx'])

SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

DEFAULT_FILE_STORAGE = 'filesystem'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

