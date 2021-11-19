from flask import Flask

# blueprint import
from apps.adminweb.views import web

def create_app():
    app = Flask(__name__)
    # setup with the configuration provided
    #app.config.from_object('config.DevelopmentConfig')
    
    # register blueprint
    app.register_blueprint(web)
    
    return app

if __name__ == "__main__":
    create_app().run()