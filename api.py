from flask import Flask
from config import Config, ConfigObject
from db import Redis

app = Flask(__name__)


@app.route("/")
def main():
    c = Config("./.env.json")
    return str(Config.config)


@app.route("/defaultconfig")
def default_config():
    return str(ConfigObject)


@app.route("/test")
def test():
    return "Flask successfully installed."


@app.route("/getall")
def get_all_data():
    Redis().get_every_list_count()


if __name__ == "__main__":
    app.run()
