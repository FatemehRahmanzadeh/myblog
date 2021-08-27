import os


class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = "thisIsSecretCODE"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  #current dir
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ='mh.sh7676@gmail.com'
    MAIL_PASSWORD = 'geszublyzamyegas'
