import logging
import os

logger = logging.getLogger(__name__)


class DevelopmentConfig(object):
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
        os.getenv("POSTGRES_USER", "bc_challenge_user"),
        os.getenv("POSTGRES_PASSWORD", "lx2v4kw5nj12"),
        os.getenv("POSTGRES_HOST", "localhost"),
        os.getenv("POSTGRES_PORT", "5432"),
        os.getenv("POSTGRES_DB", "bc_challenge")
    )
    DEBUG = True
    HOST = "localhost"
    PORT = "5000"
    SECRET_KEY = "test"
    ENCRYPTION_KEY = "test"
