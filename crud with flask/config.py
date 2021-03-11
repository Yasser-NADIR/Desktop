class Config(object):
	pass

class ProdConfig(Config):
	pass

class DevConfig(Config):
	Debug=True
	SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:azerty@localhost:5432/sqlalchemy"
	SQLACHEMY_ECHO = True