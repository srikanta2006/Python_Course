#install external module and use it
#used to speak out sentences
import pyttsx3
engine = pyttsx3.init()
engine.say("hello world, i am srikanta")
engine.runAndWait()