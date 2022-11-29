import speech_recognition as sr


def recvoz():
    while True:
        rec = sr.Recognizer()
        with sr.Microphone() as fala:
            rec.adjust_for_ambient_noise(fala)
            print("ready")

            try:
                frase = rec.listen(fala)
                return rec.recognize_google(frase, language="pt").lower().split()

            except sr.UnknownValueError:
                return "erro"#retorna n oviu para repetir, n entra na lista e sim direto para o sintz


while True:
    result = recvoz()
    print(result)


"""
funcionalidade da google speech
https://github.com/Uberi/speech_recognition/blob/master/examples/special_recognizer_features.py
"""