class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_admin_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev-secret-key'
