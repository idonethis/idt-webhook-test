from flask import Flask, abort, request
import random
import os


app = Flask(__name__)


@app.before_request
def log_request():
    output = []
    # can contain partial names
    interesting_header_names = [
        "X-Idonethis",
        "X-Request-Id",
    ]
    for header, value in request.headers.items():
        for interesting_header_name in interesting_header_names:
            if interesting_header_name in header:
                output.append("{}:{}".format(header, value))
    output.append("body: {}".format(request.data))
    print ", ".join(output)


@app.route('/')
def index():
    return "<pre>{}</pre>".format(str(app.url_map).replace('<', '&lt;'))


@app.route('/ok', methods=['GET', 'POST'])
def ok():
    return "ok"


@app.route('/fail', methods=['GET', 'POST'])
@app.route('/fail/<int:code>', methods=['GET', 'POST'])
def fail(code=None):
    codes = [400, 401, 404, 500]
    code = code if code and code in codes else random.choice(codes)
    abort(code)


@app.route('/random', methods=['GET', 'POST'])
def random_response():
    if random.random() >= 0.9:
        return fail()
    else:
        return ok()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
