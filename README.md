Random response generator.
Exposes 3 endpoints to test various responses:

* `/ok`: always returns a 200 status code with body 'ok'
* `/fail`: fails with a random code between `[400, 401, 404, 500]`
* `/fail/<code>`:  fails with <code> status code. Code can be one of `[400, 401, 404, 500]`
* `/random`: returns the `/ok` response 90% of times, fails with a random status code 10% of the times

# Installation

* `mkvirtualenv idt-webhook-test`
* `pip install -r requirements.txt`
* `python app.py`
