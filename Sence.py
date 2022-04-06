import pyttsx3
import speech_recognition as sr

def Say(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("     ")
    print(f"AI: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("     ")


def Listen():
    command = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source,0,2)

        try:
            print("Recognizing.....")
            query = command.recognize_goole(audio,language='en-in')
            print(f"You Said : {query}")

        except:
            return ""

        query = str(query)
        return query.lower()


