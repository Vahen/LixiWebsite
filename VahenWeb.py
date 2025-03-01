from application import create_app
from application.configuration import DevelopmentConfig


def create_server():
    return create_app(DevelopmentConfig)


if __name__ == '__main__':
    app = create_server()
    app.run(host="0.0.0.0", port='80')
