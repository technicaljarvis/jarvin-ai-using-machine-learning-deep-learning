import datetime
from Sence import Say
import pywhatkit
import serial
import webbrowser as web

#COM port for arduino
ser = serial.Serial("com3",9600)

#Non input task
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def LightOn():
    ser.write(b'l')
    Say("light on")

def LightOff():
    ser.write(b'Q')
    Say("light off")
 
def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()


#Home automation tasks
    elif "light on" in query:
        LightOn()

    elif "light off" in query:
        LightOff()
        
         
#input_task
def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","").replace("search","").replace("download","")
        pywhatkit.search(query)

    elif "youtube" in tag:
        result = str(query).replace("search","").replace("youtube","").replace("on","")
        result_1 = "https://www.youtube.com/results?search_query=" + result
        web.open(result_1)