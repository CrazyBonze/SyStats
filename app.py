from flask import Flask, render_template
from flask_cors import CORS

from api import api

app = Flask(__name__, static_url_path='', static_folder='web/bin', template_folder='web/bin')
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api.blueprint)
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300


@app.route("/")
@app.route("/index")
def index():
    """Return the Webpack generated index page as a template.
    """
    return render_template("index.html")

@app.after_request
def add_header(response):
    """Remove Cache Control from index and api calls.
    """
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
