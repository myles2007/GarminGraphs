class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = '/activities/'
    ALLOWED_EXTENSIONS = set([('gpx', 'pdf', 'png', 'jpg')])

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
