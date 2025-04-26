from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'

    # Import and register routes
    from app.routes.auth import auth_bp
    from app.routes.post import post_bp
    from app.routes.search import search_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(search_bp)

    return app
