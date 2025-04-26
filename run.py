from app import create_app

app = create_app()

if __name__ == '__main__':
    from app.utils.db import init_db
    init_db()
    app.run(debug=True)
