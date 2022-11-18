from bs4 import BeautifulSoup
import pickle
import requests

def scraper(urls):
    classesLinks=[]
    classesTitles=[]
    locations=[]
    days=[]
    timings=[]

    for url in urls:
        [classesLink,classesTitle,location,day,timing]=scrape(url)
        classesLinks+=classesLink
        classesTitles+=classesTitle
        locations+=location
        days+=day
        timings+=timing
    
    with open('classesLinks.pkl', 'wb') as f: pickle.dump(classesLinks, f)
    with open('classesTitles.pkl', 'wb') as f: pickle.dump(classesTitles, f)
    with open('locations.pkl', 'wb') as f: pickle.dump(locations, f)
    with open('days.pkl', 'wb') as f: pickle.dump(days, f)
    with open('timings.pkl', 'wb') as f: pickle.dump(timings, f)


def scrape(URL = "https://class-descriptions.northwestern.edu/4890/MEAS/COMP_SCI"):
    r = requests.get(URL)

    soup=BeautifulSoup(r.content)
    classes=soup.find('div',attrs={"class":"expander expander1"})

    classesLinks=[x.find('a')["href"] for x in classes.find_all('li')]
    classesTitles=[" ".join(x.text.strip().replace(" "," ").replace("\n","").split()) for x in classes.find_all('li')]

    def getInfo(c):
        c="/".join(URL.split("/")[:-1])+'/'+c
        c = requests.get(c)
        cSoup=BeautifulSoup(c.content)
        for x in cSoup.find_all('p'):
            if(":" in x.text and "-" in x.text):
                return x.text.replace("\n","").strip()
        return cSoup.find_all('p')[1].text.replace("\n","").strip()

    informations=[getInfo(x) for x in classesLinks]

    locations=[x[:x.index(":"):] for x in informations]

    dayKey={"Mon":0,"Tues":1,"Wed":2,"Thurs":3,"Fri":4,"Sat":5,"Sun":6}

    days=[x[x.index(":")+2:len(x)-x[::-1].index(",")-1] for x in informations]
    days=[cDays.replace(' ','').split(',') for cDays in days]
    days=[[dayKey[day] for day in cDays] for cDays in days]

    timings=[x[len(x)-x[::-1].index(","):].replace(" ","").split('-') for x in informations]

    return [classesLinks,classesTitles,locations,days,timings]
    # Output
if __name__=="__main__":
    scrape()