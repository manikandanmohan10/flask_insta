# bind = "0.0.0.0:8000"
# workers = 4
# worker_class = "sync"
# timeout = 120
# chdir = "flask_insta"
# module = "app:app"

from src import create_app

if __name__ == '__main__':
    create_app = create_app()
    create_app.run()
else:
    gunicorn_app = create_app()