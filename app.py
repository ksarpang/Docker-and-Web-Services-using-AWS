from flask import request, Flask, render_template
from flask_restful import Resource, Api
from flask import jsonify
import csv, json
#from flask_cors import CORS, cross_origin
#from redis import Redis, RedisError
import datetime
import os
import shutil
from weather import Weather
weather = Weather()

#redis = Redis(host="redis" , db =0, scoket_connect_timeout =2, socket_timeout =2)
app = Flask(__name__)
api = Api(app)

@app.route('/')
def main():
    return render_template('forecast.html')

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
@app.route('/historical/', methods=['GET'])
def historical():
	with open('daily.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		list_date = []
		for row in reader:
			list_date.append({"DATE":row['DATE']})
	return json.dumps(list_date)
@app.route('/historical/<date>', methods=['GET'])
def historical_date(date):
	 with open('daily.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		data ={}
		for row in reader:
			if(row['DATE']==date):
				data = jsonify({"DATE":row['DATE'],"TMAX":row['TMAX'], "TMIN":row['TMIN']})
				return data
		return not_found()
@app.route('/historical/', methods=['POST'])
def historical_post():
	data = request.get_data();
	json_data = json.loads(data)
	Date = json_data['DATE']
	Tmax = json_data['TMAX']
	Tmin = json_data['TMIN']
	new= [Date, Tmax, Tmin]
	with open('daily.csv', 'a') as csvfile:
		newFileWriter = csv.writer(csvfile)
		jsonify(newFileWriter.writerow(new))
		resp=jsonify(json_data)
		resp.status_code=201
	return resp
@app.route('/forecast/<date>', methods=['GET'])
def forecast(date):
	tmp_date = date.replace("-","")
	forecast_list = []
	with open('daily.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		days=0
		for row in reader:
			if(row['DATE']==tmp_date or (days>0 and days<6)):
				forecast_list.append({"DATE":row['DATE'], "TMAX":row['TMAX'], "TMIN":row['TMIN']})
				days=days+1

	return json.dumps(forecast_list)
@app.route('/historical/<date_del>', methods=['DELETE'])
def historical_delete(date_del):
	fieldnames = ["DATE", "TMAX","TMIN"]
	with open('daily.csv', 'r') as csvfile, open('output.csv', 'w') as outputfile:
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)
		writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
	for row in reader:
		if not date_del == row['DATE']:
			writer.writerow({'DATE': row['DATE'], 'TMAX': row['TMAX'], 'TMIN': row['TMIN']})
		shutil.move('output.csv','daily.csv')
	return json.dumps(date_del)


@app.route('/API_forecast/<date>', methods=['GET'])
def apiforecast(date):
    temp_date = date.replace("-","")
    forecast_list = []
    lookup = weather.lookup(560743)
    location = weather.lookup_by_location('cincinnati')
    forecasts = location.forecast()
    days=0
    for forecast in forecasts:
        days=days+1
        if(days>5):
            break
        forecast_list.append({"DATE":str(forecast.date()), "TMAX":float(forecast.high()), "TMIN":float(forecast.low())})

    return json.dumps(forecast_list)

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=80)

