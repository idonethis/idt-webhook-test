from flask import Flask, abort
import random
import os


app = Flask(__name__)


@app.route('/')
def index():
    return "<pre>{}</pre>".format(str(app.url_map).replace('<', '&lt;'))


@app.route('/ok')
def ok():
    return "ok"


@app.route('/fail')
@app.route('/fail/<int:code>')
def fail(code=None):
    codes = [400, 401, 404, 500]
    code = code if code and code in codes else random.choice(codes)
    abort(code)


@app.route('/random')
def random_response():
    if random.random() > 0.9:
        return random()
    else:
        return ok()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
