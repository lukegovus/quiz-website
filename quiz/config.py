import os

class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE.URL') or \
		#'sqlite:///' + os.path.join(basedir, 'app.db')	

	#SQLALCHEMY_TRACK_MODIFICATIONS = False
	