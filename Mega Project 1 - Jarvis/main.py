# virtualenv mega_env1
# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
	engine.say(text)
	engine.runAndWait()

def openSite(c):
	webbrowser.open(f"https://{c}.com")

def processCommand(w):
	w = w.lower()
	if w.startswith("open"):
		site = w.split(" ")[1]
		if site in ["google" , "youtube" , "facebook" , "linkedin"]:
				openSite(site)
				return
		speak("Sorry, I don't have the permission to open that site.")

	if w.startswith("play"):
		song = w.split(" ")[1]
		if song in musicLibrary.music:
			link = musicLibrary.music[song]
			webbrowser.open(link)
		speak("Sorry, that song is not in my Library.")

	if w in ["bye", "quit", "end", "exit"]:
		speak("Goodbye, shutting down..")
		exit()

	else:
		speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
	speak("Initializing Jarvis...")
	while True:
		# Listen for the wake word "Jarvis"
		# Obtain audio from microphone :
		r = sr.Recognizer()

		print("Recognizing...")
		# Recognize speech :
		try:
			with sr.Microphone() as source:
				print("Listening..")
				audio = r.listen(source, timeout=5, phrase_time_limit=4)
			word = r.recognize_google(audio)
			if (isinstance(word, str) and word.lower() == "jarvis"):
				speak("Huh")
				# Listen for command :
				with sr.Microphone() as source:
					r.adjust_for_ambient_noise(source, duration=1)
					print("Jarvis is listening..")
					audio = r.listen(source)
					command = r.recognize_google(audio)

					processCommand(command)
		except Exception as e:
			print("Error; {0}".format(e))
