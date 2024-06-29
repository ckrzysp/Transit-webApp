import csv
from flask import Flask, render_template, jsonify, request
from routeStationTime import *

app = Flask(__name__)

# Function to read data from stations.csv
def read_stations():
    with open('stations.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        stations_data = list(reader)
    return stations_data

# Function to read data from routes.csv
def read_routes():
    with open('routes.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        routes_data = list(reader)
    return routes_data

# Define route to get station data
@app.route('/stations')
def get_stations():
    stations_data = read_stations()
    return jsonify(stations_data)


# Define route to get routes data
@app.route('/routes')
def get_sroutes():
    routes_data = read_routes()
    return jsonify(routes_data)


# Define route for the main page
@app.route('/')
def index():
    stations = read_stations()
    return render_template('index.html', stations=stations)


# route for getting station suggestions
@app.route('/get_station_suggestions/<partial_station>', methods=['GET'])
def get_station_suggestions(partial_station):
    suggestions = [station['name'] for station in read_stations() if partial_station.lower() in station['name'].lower()]
    return jsonify(suggestions)


@app.route('/process_stations', methods=['POST'])
def process_stations():
    current_station = request.json['current-station']
    destination_station = request.json['destination-station']
    train_line = request.json['train-line']
    direction = request.json['direction']

    print(current_station)
    print(destination_station)
    print(train_line)
    print(direction)

    # Using the search functionality here
    #current_station_code = getStationCode(current_station)
    #destination_station_code = getStationCode(destination_station)

    #our return value will contain two parts
    #ret_values[1] will contain a the calculating time
    #ret_value[2] will contain the future train times of the current station
    ret_values = []

    ret_values.append(showTimes(current_station, train_line, direction))


    #calculating time
    time = trip(current_station,destination_station,direction)
    ret_values.append(time)

    print(ret_values[0])
    print(ret_values[1])

    return jsonify(ret_values) 

    # Process the selected stations here
    return f"Current Station Code: {current_station_code}, Destination Station Code: {destination_station_code}"


if __name__ == '__main__': 
    app.run(debug=True)