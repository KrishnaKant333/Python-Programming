# virtualenv mega_env1
# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import subprocess

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

	if w.startswith("open") or w.startswith("launch") or w.startswith("fire"):
		name = w.split(" ")[1]
		if name in ["google" , "youtube" , "facebook" , "linkedin", "github"]:
			txt = f"Opening {name}.."
			printAndSpeak(txt)
			openSite(name)
			return

		if name == "notepad":
			subprocess.Popen(["notepad.exe"])
			printAndSpeak("Launching Notepad...")
			return
		elif name == "code":
			subprocess.Popen(["C:\\Users\\Krishna Kant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
			printAndSpeak("Launching Visual Studio Code...")
			return

		if name == "server":
			txt = "Launching Minecraft Server.."
			printAndSpeak(txt)
			webbrowser.open("https://aternos.org")
			return

		printAndSpeak("Sorry, I don't have the permission to open that.")

	elif w.startswith("play"):
		song = w.split(" ")[1]
		if song in musicLibrary.music:
			link = musicLibrary.music[song]
			txt = f"Playing {song.title()}.."
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
	r = sr.Recognizer()
	while True:
		# Listen for the wake word "Jarvis"
		# Obtain audio from microphone :

		print("Recognizing...")
		# Recognize speech :
		try:
			with sr.Microphone() as source:
				print("Listening..")
				audio = r.listen(source, timeout=3, phrase_time_limit=3)
			word = r.recognize_google(audio)
			if (isinstance(word, str) and word.lower() == "jarvis"):
				printAndSpeak("Yes!")
				# Listen for command :
				with sr.Microphone() as source:
					print("Jarvis is listening..")
					audio = r.listen(source, timeout=3, phrase_time_limit=3)
					command = r.recognize_google(audio)

					processCommand(command)
		except Exception as e:
			print("Error; {0}".format(e))
