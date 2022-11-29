def sintz(voice):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(voice)
    engine.runAndWait()
