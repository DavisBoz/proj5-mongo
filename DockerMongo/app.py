import os
import flask
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import arrow
import acp_times
import config
import logging


app = Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

db.tododb.delete_many({})

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    
    km = request.args.get('km', 999, type=float)
    brevet_dist = request.args.get('brev_dis', 999, type=int)
    start_time = request.args.get('start_t', 999, type=str)
    start_date = request.args.get('start_d', 999, type=str)

    app.logger.debug("start time={}".format(start_time))
    app.logger.debug("start date={}".format(start_date))
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    
    time_str = "{}T{}".format(start_date, start_time)
    time = arrow.get(time_str)
    time = time.isoformat() 
    opening = acp_times.open_time(km, brevet_dist, time)
    closing = acp_times.close_time(km, brevet_dist, time)
    result = {"open": opening, "close": closing}
    return flask.jsonify(result=result)


@app.route('/display', methods=['POST'])
def display():
    _items = db.tododb.find()
    items = [item for item in _items]
    if items == []:
	    return redirect(url_for('none'))
    else:
        return render_template('acp.html',items=items) 


@app.route('/none')
def none():
	return render_template('none.html')


@app.route('/new', methods=['POST'])
def new():
    open_data = request.form.getlist("open")
    close_data = request.form.getlist("close")
    open_list = []
    close_list = []
    for item in open_data:
	    if str(item) != '':
		    open_list.append(str(item))
    for item in close_data:
        if str(item) != '':
            close_list.append(str(item))

    app.logger.debug("OPEN " + str(open_list))
    app.logger.debug("CLOSE " + str(close_list))

    for x in range(len(open_list)):	    
        item_doc = {
             'open_times': open_list[x],
		     'close_times': close_list[x]
        }
        db.tododb.insert_one(item_doc)
    _items = db.tododb.find() 
    items = [item for item in _items]
    
    app.logger.debug("Contents of db: " + str(items))
    
    if items == []:
	    return redirect(url_for('none'))
    else:
        return redirect(url_for('index')) 


app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
