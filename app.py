from eve import Eve
from flask import render_template
from os import environ as env

## check eve docs:
## https://docs.python-eve.org/en/stable/features.html

settings = {
    'MONGO_HOST': env['MONGO_URL'] if env['MONGO_URL'] else 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'monker',
    'ALLOW_UNKNOWN' : True,
    'DOMAIN': {
        'meta'    : {},
        'state'   : {}, ## TODO change to state
        'buy'     : {},
        'sell'    : {},
        'logging' : {},
    }
}

app = Eve(settings=settings)

@app.route("/dash")
def index():
    return open('dash.html').read()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

