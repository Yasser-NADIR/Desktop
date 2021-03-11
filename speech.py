import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
	print("recording ..")
	audio=r.listen(source)
	order = r.recognize_google(audio, language="fr")

print("end of recording")

print(order)
"""
engine = pyttsx3.init()
engine.say(order)
engine.runAndWait()"""