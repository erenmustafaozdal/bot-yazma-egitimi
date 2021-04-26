import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=5)
    print("Sesinizi Tanımlıyor…")
    text = r.recognize_google(data, language="tr")
    print(text)
