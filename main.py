from asgiref.wsgi import WsgiToAsgi
from flask import render_template
from src import create_app
import asyncio
from werkzeug.middleware.profiler import ProfilerMiddleware

# from src import app

app = create_app()
app.wsgi_app = ProfilerMiddleware(app.wsgi_app)

# asyncio.run(serve(application, Config()))

# asgi_app = WsgiToAsgi(application)
# @app.route('/home')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()
    