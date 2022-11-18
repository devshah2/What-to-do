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
        to=datetime.datetime.strptime(timings[ind][1],'%I:%M%p').time()
        if(today in i and to>totime):
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
parser.add_argument("-i", "--interactive", help = "Set interactive on", action='store_true')
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

if not args.interactive:
    print(query(day,totime))
else:
    print("Interactive time")
    out=list(query(day,totime))
    chosen=[]
    ignore=[]
    while out!=[]:
        cls=out.pop(0)
        if(cls in ignore):
            continue
        print(cls)
        inp=input("Choose class y/n (exit to terminate): ")
        if(inp.lower()=="y"):
            chosen.append(cls)
            # Add functionality to recalculate out
            # Find end time of chosen class
            to=datetime.datetime.strptime(timings[classesTitles.index(cls[0])][1],'%I:%M%p').time()
            out=list(query(day,to))
        elif(inp.lower()=="exit"):
            break
        else:
            ignore.append(cls)

    out=chosen
    print()
    print()
    print("Classes for today: ")
    for x in chosen:
        print("{} at {} from {} to {}".format(x[0][x[0].find(':')+2:x[0].find('-')-1],x[1],timings[classesTitles.index(x[0])][0],timings[classesTitles.index(x[0])][1]))
    print()
    print()