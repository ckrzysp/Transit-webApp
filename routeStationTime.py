# Using csv package
import csv 

# Opening and storing data required to find stops
rows_stops = []
with open("stops.csv", 'r') as file1:
    csvreader = csv.reader(file1)
    header_stops = next(csvreader)

    for row in csvreader:
        rows_stops.append(row)

# Opening and storing data required to find time between stations
rows_stations = []
with open("stations.csv", 'r') as file2:
    csvreader = csv.reader(file2)
    header_stops = next(csvreader)

    for row in csvreader:
        rows_stations.append(row)

# Opening and storing data required to find time between stations
rows_stop_times = []
with open("stop_times.csv", 'r') as file2:
    csvreader = csv.reader(file2)
    header_stops = next(csvreader)

    for row in csvreader:
        rows_stop_times.append(row)

# // isStationCode Function \\
# param: str (targetStation we want to find for any given train line)
# return: str (Returns targetStation from dataset)
def getStationCode(targetStation):
    for i in range(len(rows_stations)):
        if rows_stations[i][2] == targetStation:
            return rows_stations[i][0]
         
# // stationsExistOnLine Function \\
# param: str (targetStart, targetEnd are the two station names as input)
# return: bool (Returns true if they are on the same line, false if not)
def stationsExistOnLine(targetStart, targetEnd):
    startLine = ""
    endLine = ""
    for i in range(len(rows_stations)):
        if rows_stations[i][2] == targetEnd:
            startLine = rows_stations[i][4]
        elif rows_stations[i][2] == targetStart:
            endLine = rows_stations[i][4]
    
    if startLine == endLine:
        return True
    else:
        return False

# // toMinutes \\
# param: str (time, is the time format for stop_times.csv)
# return: int (Returns minutes conversion from hour(s) and minutes)
def toMinutes(time):
    print(time)
    hour = ""
    minute = ""
    # Hour conversion
    if len(time) < 3:
        return 0

    if time[0] == "0":
        if time[1] == "0":
            hour = hour + time[1]
        hour = hour + time[1]
    else:
        hour = hour + time[0] 
        hour = hour + time[1]
    
    # Minute Conversion
    if time[3] == "0":
        minute = minute + time[3]
        if time[4] == "0":
            minute = minute + time[4]
        minute = minute + time[4]
    else:
        minute = minute + time[3] 
        minute = minute + time[4]
    
    total = int(hour) * 60
    total = total + int(minute)
    return total

# // trip Function \\
# param: str (targetStopStart is the stop we are using as comparison, 
#             targetStopEnd is the stop that the user wants to get to,
#             direction is either North or South bound, N or S)
# return: int (Returns the trip length, in minutes)
def trip(targetStopStart, targetStopEnd, direction):
    # timeTotal measured in minutes
    timeTotal = 0
    startStationFound = False
    startStationTime = ""
    endStationFound = False
    endStationTime = ""

    # Travel to where you already are
    if targetStopStart == targetStopEnd:
        return 0
    
    # Station Codes to work with stop_times.csv
    stationCodeStart = getStationCode(targetStopStart) + direction
    stationCodeEnd = getStationCode(targetStopEnd) + direction

    # Stop Check
    if stationsExistOnLine(targetStopStart, targetStopEnd):
        # Finding the scheduled time slots for each station
        for i in range(len(rows_stop_times)):
            # Once station time is found, we do not need to check it again
            if not(startStationFound) and (rows_stop_times[i][1] == stationCodeStart):
                startStationFound = True
                startStationTime = rows_stop_times[i][2]
            # Once station time is found, we do not need to check it again
            elif not(endStationFound) and (rows_stop_times[i][1] == stationCodeEnd):
                endStationFound = True
                endStationTime = rows_stop_times[i][2]

    timeTotal = abs(toMinutes(startStationTime) - toMinutes(endStationTime))

    print("It will be a {} minute trip.".format(timeTotal))

    return timeTotal

         