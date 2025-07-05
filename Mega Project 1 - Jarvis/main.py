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

def printAndSpeak(text):
	print(text)
	engine.say(text)
	engine.runAndWait()

def openSite(c):
	webbrowser.open(f"https://{c}.com")

def processCommand(w):
	w = w.lower()
	if w.startswith("open"):
		site = w.split(" ")[1]
		if site in ["google" , "youtube" , "facebook" , "linkedin"]:
			txt = f"Opening {site}.."
			printAndSpeak(txt)
			openSite(site)
			return
		if site == "minecraft":
			txt = "Opening Minecraft.."
			printAndSpeak(txt)
			webbrowser.open("https://aternos.org")
			return

		printAndSpeak("Sorry, I don't have the permission to open that site.")

	elif w.startswith("play"):
		song = w.split(" ")[1]
		if song in musicLibrary.music:
			link = musicLibrary.music[song]
			txt = f"Playing {link}.."
			printAndSpeak(txt)
			webbrowser.open(link)
			return
		printAndSpeak("Sorry, that song is not in my Library.")

	elif w in ["bye", "quit", "end", "exit"]:
		txt = "Goodbye, shutting down.."
		printAndSpeak(txt)
		exit()

	else:
		printAndSpeak("Sorry, I don't understand that command.")

if __name__ == "__main__":
	printAndSpeak("Initializing Jarvis...")
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
				printAndSpeak("Yes!")
				# Listen for command :
				with sr.Microphone() as source:
					print("Jarvis is listening..")
					audio = r.listen(source, timeout=5, phrase_time_limit=4)
					command = r.recognize_google(audio)

					processCommand(command)
		except Exception as e:
			print("Error; {0}".format(e))
