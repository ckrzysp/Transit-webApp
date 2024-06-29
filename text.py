import csv, time, datetime

stops_list = []
with open ('stops.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            stops_list.append(row)

times_list = []
with open ('stop_times.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            times_list.append(row)

now = time.ctime()
day = now[0:3]
print(day)

compare_now = datetime.datetime.now();

if day == "Sun":
    day = "Sunday"
elif day == "Sat":
     day = "Saturday"
else:
     day = "Weekday"

time = now[11:20]
print(time)


user_station = input("Enter a station: ")
direction = input("Uptown or Downtown? (CASE SENSITIVE, MATCH INSTRUCTION) ")
line = input("Enter a train line (CASE SENSITIVE, CAPS/INT ONLY): ")
line += "."

for item in stops_list:
    if user_station == item['stop_name']:
        user_station = item['stop_id']
        break

if direction == "Uptown":
     user_station += "N"
else:
     user_station += "S"
    
print(user_station)

#create a temp time var for storing/comparing the time of the train at this section
temp_time = datetime.datetime.now()

for item in times_list: 
    if user_station != item['stop_id']:
        continue
    else:
        if day in item['trip_id']:
            if line in item['trip_id']:
                temp_time = temp_time.replace(hour=(int(item['arrival_time'][0:2]) % 23))
                temp_time = temp_time.replace(minute=int(item['arrival_time'][3:5]))
                temp_time = temp_time.replace(second=int(item['arrival_time'][6:8]))
                if (compare_now < temp_time ):
                    print(item['trip_id'] + ": " + item['arrival_time'])

