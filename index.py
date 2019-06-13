from flask import Flask, Response, __version__, request
app = Flask(__name__)
source = 'https://github.com/zeit/now-examples/tree/master/python-flask'
css = '<link rel="stylesheet" href="/css/style.css" />'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    code = request.args.get("code")
    if code:
      return Response("%s<h1>Flask on Now 2.0</h1><p>You are viewing a Flask application written in Python running on Now 2.0.</p><p>Path: /%s</p><p>Code in Query String: %s</p>" % (css, path, request.args.get("code")), mimetype='text/html')
    return Response("%s<h1>Flask on Now 2.0</h1><p>You are viewing a Flask application written in Python running on Now 2.0.</p><p>Path: /%s</p><p>Query String (args): %s</p>" % (css, path, request.args), mimetype='text/html')
