from decouple import config 

class Config:
    SECRET_KEY = '|b2Jqw)h)35LHmKX'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='FS/5o3f71KbIPv@]'
    MYSQL_DB='tienda'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS = True
    MAIL_USERNAME='20213tn099@utez.edu.mx'
    MAIL_PASSWORD=config('MAIL_PASSWORD')
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
