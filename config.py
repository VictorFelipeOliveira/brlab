import os 
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'chave-secreta'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
	DEBUG = True

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
