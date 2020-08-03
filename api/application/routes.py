import json
from flask import current_app as app
from database import Url, session


@app.route('/')
def index():

    urls = session.query(Url).order_by(Url.id.desc()).all()

    return json.dumps(
        [
        {'url': model.url,
         'date': str(model.date),
         'duration': model.duration,
         'status': model.status} for model in urls
        ],
        indent=4
    )
