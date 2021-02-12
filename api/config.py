
# more configuration options here http://flask.pocoo.org/docs/1.0/config/
class Config:
    """
    Base Configuration
    """

    # CHANGE SECRET_KEY!! I would use sha256 to generate one and set this as an environment variable
    # Exmaple to retrieve env variable `SECRET_KEY`: os.environ.get("SECRET_KEY")
    SECRET_KEY = "dev"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # LOG_FILE = "api.log"  # where logs are outputted to


class DevelopmentConfig(Config):
    """
    Development Configuration - default config
    This defaults the Database URL that can be created through the docker
    cmd in the setup instructions. You can change this to environment variable as well.
    """

    # url = (
    #     "postgresql://testusr:password@127.0.0.1:5432/testdb"
    # )  # set the URI to call get_pg_url() once you have `creds.ini` setup
    # SQLALCHEMY_DATABASE_URI = url
    DEBUG = True


# way to map the value of `FLASK_ENV` to a configuration
config = {"dev": DevelopmentConfig}
