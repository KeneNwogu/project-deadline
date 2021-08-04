import json

from flask import request, Response, render_template

from app import app
from deadline.deadline import get_deadline


@app.route("/deadline")
@app.route("/")
def get_deadline_info():
    start_date = request.args.get('start-date')
    if start_date:
        start_date = request.args.get('start-date').replace('-', ' ')
    deadline = request.args.get('deadline')
    time_format = request.args.get('time-format')
    if start_date and deadline:
        deadline = int(deadline)
        if time_format:
            deadline_information = get_deadline(start_date, deadline, time_format)
            deadline_information_json = json.dumps(deadline_information)
            return Response(deadline_information_json)
        else:  # Use Default Time Format
            deadline_information = get_deadline(start_date, deadline)
            deadline_information_json = json.dumps(deadline_information)
            return Response(deadline_information_json)
    return render_template("index.html")
