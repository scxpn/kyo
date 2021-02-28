import speech_recognition as sr

#Inicialize a voice recognizer
r = sr.Recognizer()

#Open microphone
with sr.Microphone() as source:

    while True:
        audio = r.listen(source) #Microphone was defined like the main audio source
        print(r.recognize_google(audio, language = 'pt'))