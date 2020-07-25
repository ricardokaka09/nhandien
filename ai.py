import pyttsx3
import speech_recognition
from datetime import date,datetime
import wikipedia
import webbrowser
import time
import os 
# import predict
i=0
aispeak = pyttsx3.init()
aispeak.say(
"Hello" +'     '+
"can i help you somehow?")
aispeak.runAndWait()
def main():
	while i<5:
		hear = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as mic:
			print('...')
			audio = hear.listen(mic)
		try:
			you = hear.recognize_google(audio,language="vi-VN")
		except:
			you= ""
		if you=="":
			ai="I can't hear you"
			i=i+1
		elif "today" in you:
			today = date.today()
			ai = today.strftime("%B %d, %Y")
		elif "hi" in you:
			ai = 'Hello'
		elif "time" in you:
			now=datetime.now()
			ai=now.strftime("%H Hours %M Minutes %S Seconds")
		elif "chào" in you:
			ai = "Xin chào cậu chủ, chúc cậu chủ một ngày tốt đẹp nha"
		elif 'how are you' in you:
			ai="I'm Fine"
		elif 'how old are you' in you:
			ai="I'm zero year old"
		elif "thank" in you:
			ai='You are welcome'
		elif "chat" in you:
			predict.chat()
		elif "name" in you:
			ai="My name is Hung"
		elif 'sleep 5 second' in you:
			ai='Finish'
			time.sleep(5)
		elif 'sleep 10 second' in you:
			ai='Finish'
			time.sleep(10)
		elif 'sleep 1 minute' in you:
			ai='Finish'
			time.sleep(60)
		# elif 'shut down' in you:
		# 	os.system('shutdown -s')
		# elif 'restart' in you:
		# 	os.system('shutdown -r')
		elif "YouTube" in you:
			webbrowser.open('https://www.youtube.com',new=2)
			ai="Ok!Bye"
			print('Me:',you)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "Google" in you:
			webbrowser.open('https://www.google.com.vn/',new=2)
			ai="Ok!Bye"
			print('Me:',you)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "music" in you:
			webbrowser.open('https://www.youtube.com/results?search_query=music',new=2)
			ai="Ok!Bye"
			print('Me:',you)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "EDM" in you:
			webbrowser.open('https://www.youtube.com/watch?v=KjvM4WJcedA',new=2)
			ai="Ok!Bye"
			print('Me:',you)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "Facebook" in you:
			webbrowser.open('https://www.facebook.com/',new=2)
			ai="Ok!Bye"
			print('Me:',you)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "Gmail" in you:
			webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
			ai="Ok!Bye"
			print('Me:',you)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif "bye" in you:
			ai='GoodBye'
			print('Me:',you)
			print('AI:',ai)
			aispeak = pyttsx3.init()
			aispeak.say(ai)
			aispeak.runAndWait()
			break
		elif you=='Wikipedia':
			hear = speech_recognition.Recognizer()
			with speech_recognition.Microphone() as mic:
				print("Wikipedia: ...")
				audio = hear.listen(mic)
			try:
				wiki = hear.recognize_google(audio)
			except:
				wiki='Sorry'
			wikipedia.set_lang("vi")
			wiki=wikipedia.summary(wiki)
			print(wiki)
			ai='Finish ^.^'
			time.sleep(3)
		elif 'game' in you:
			os.system('python flappybird.py')
			ai='Finish'
		else: ai='Sorry!'	
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_VI-VN_ZIRA_11.0"
		aispeak.setProperty('voices',en_voice_id)

		# for voice in voices:
			# print("Voice:")
			# print(" - ID: %s" % voice.id)
			# print(" - Name: %s" % voice.name)
			# print(" - Languages: %s" % voice.languages)
			# print(" - Gender: %s" % voice.gender)
			# print(" - Age: %s" % voice.age)
		aispeak.setProperty('rate', 150) 
		aispeak.say(ai)
		aispeak.runAndWait()
def hello(name):
	aispeak = pyttsx3.init()
	en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_VI-VN_ZIRA_11.0"
	aispeak.setProperty('voices',en_voice_id)
	aispeak.setProperty('rate', 150) 
	aispeak.say("hello" + "    " + name + "I can help you")
	aispeak.runAndWait()

