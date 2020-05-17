import speech_recognition as sr
import pyautogui

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

    print("Text: " + r.recognize_google(audio_text))

except:
print("Sorry, I did not get that")

script = r.recognize_google(audio_text)
for x in script.split():
    pyautogui.write(x)
    pyautogui.press('enter')