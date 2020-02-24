DEBUG = True

SERVER_NAME = 'localhost:5000'
SECRET_KEY = 'watinemldkddjdjdeerfjf;ll;prirotitpprrie'

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

# Database Connection
#mysql://username:password@server/db
#db_uri = 'sqlite:////tmp/chat_db.db'
db_uri = 'mysql://root:@localhost/chat'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False





# Celery.
CELERY_BROKER_URL = 'redis://:localhost@redis:6379'
CELERY_RESULT_BACKEND = 'redis://:localhost@redis:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
