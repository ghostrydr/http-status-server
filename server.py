import flask
from flask_cors import CORS
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/', defaults={'path': '200'})
@app.route('/<path:path>')
def home(path):
    params = {
        'errorCode': '%s' % path
    }
    return jsonify(**params), int(path)
app.run()
