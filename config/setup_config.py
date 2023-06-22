import os

from dotenv import load_dotenv

os.environ.setdefault('APP_ENV', 'dev')


def setup_config():

    app_env = os.environ.get("APP_ENV")

    if app_env == "dev":
        load_dotenv("../development.env")
    elif app_env == "prod":
        load_dotenv(".env")
    else:
        raise ValueError("unknow enviroment")


if __name__ == "__main__":
    setup_config()
