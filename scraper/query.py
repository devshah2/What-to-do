# Attempting to load pickle
import pickle
import datetime

with open('classesLinks.pkl', 'rb') as f: classesLinks=pickle.load(f)
with open('classesTitles.pkl', 'rb') as f: classesTitles=pickle.load(f)
with open('locations.pkl', 'rb') as f: locations=pickle.load(f)
with open('days.pkl', 'rb') as f: days=pickle.load(f)
with open('timings.pkl', 'rb') as f: timings=pickle.load(f)

def query(today=datetime.datetime.today().weekday(), totime=datetime.datetime.today().time()):
    results=[]
    startTimes=[]
    for ind, i in enumerate(days):
        frm=datetime.datetime.strptime(timings[ind][0],'%I:%M%p').time()
        to=datetime.datetime.strptime(timings[ind][0],'%I:%M%p').time()
        if(today in i and to>=totime):
            startTimes.append(frm)
            results.append([classesTitles[ind],locations[ind]])
    i=[]
    for i in zip( *sorted( zip(startTimes, results) ) ):
        pass
    sortArr = i
    return sortArr



import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--day", help = "Set day (Mon, Tues, Wed, Thurs, Fri, etc)")
parser.add_argument("-t", "--time", help = "Set time (8:30AM, 12:00PM, etc)")
args = parser.parse_args()
 
day=datetime.datetime.today().weekday()
totime=datetime.datetime.today().time()
if args.day:
    inp=args.day
    dayKey={"mon":0,"tues":1,"wed":2,"thurs":3,"fri":4,"sat":5,"sun":6}
    if(inp.lower() in dayKey):
        day=dayKey[inp.lower()]
    else:
        print("Unable to parse entered day, going with current")

if args.time:
    inp=args.time
    try:
        totime=datetime.datetime.strptime(inp,'%I:%M%p').time()
    except Exception as e:
        print("Unable to parse entered time, going with current")

print(query(day,totime))