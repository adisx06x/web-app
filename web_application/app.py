from flask import Flask, request, abort
from datetime import date, datetime
import pytz


app = Flask(__name__)


def current_date():
    today = date.today()
    return today


def current_time():
    time_zone_NY = pytz.timezone("America/New_York")
    datetime_NY = datetime.now(time_zone_NY)
    return datetime_NY.strftime("%H:%M:%S")


@app.route('/')
def hello():
    if request.user_agent.string == "h4ck3r":
        return abort(403)
    else:
        return "Hello World! Today's date is {} and the current time is {}.".format(current_date(), current_time())


if __name__ == '__main__':
    app.run(ssl_context=("/etc/demo/ssl/blueapron.crt",
                         "/etc/demo/ssl/blueapron.key"), host='0.0.0.0')
